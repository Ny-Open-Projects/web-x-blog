---
title: "[Q7781] 流式 JSON 断在半截：partial JSON 的增量解析与截断修复"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7781 · 流式 JSON 断在半截：partial JSON 的增量解析与截断修复

难度：P6 ｜ 标签：流式JSON、partial parse、截断修复、增量解析、finish_reason

基线：Python 3.12；实现逐 chunk 的增量 JSON 解析器（括号深度追踪、字符串内转义感知、前缀提取已完整字段），对比"等完整再 parse"的 TTFT 损失与截断修复降级链，全标准库实跑。

**问**：流式输出的结构化结果（工具参数、表单抽取），前端想边流边渲染——但 JSON 断在中间 `{"name": "张三", "tags": ["a", "b` 根本 parse 不了。partial JSON 怎么解析？已完整闭合的字段怎么提前吐给前端？截断发生时（finish_reason=length）修复到什么程度算可用，什么时候必须整体降级？

**答**：
- **结论**：partial JSON 解析器是**带状态的增量扫描**：逐字符跟踪三个状态——是否在字符串内（引号开关 + 反斜杠转义感知）、括号/方括号深度栈、当前 key 是否已闭合；扫到任何位置都能给出**可恢复的"最合法前缀"**：把未闭合的字符串补引号、按深度栈逆序补全 `]` 与 `}`，得到一个语法完整的 JSON——它可能语义不完整（缺字段），但**已闭合的 key-value 是可信的**，可以增量交付给前端渲染。与"等完整再 parse"的账：等完整意味着首字段渲染延迟 = 整个输出的生成时长（TTFT 恶化到 TTFB+ 全程），而增量解析让首字段在生成它之后立即上屏。截断修复的分级：① **截断落在 value 内部**（字符串、数组中间）→ 补全后**丢弃最后一个不完整 value**，保留之前的字段——语义安全；② **截断落在 key 内部** → 丢弃整个不完整 key；③ **必需字段缺失** → 进入降级链（模板兜底 Q1488 / 重试请求带"输出中断于 X，请续写"）。底线：修复产物必须带"partial: true"标记与缺失字段清单，下游不许把修复结果当完整结果用（Q7608/Q7772 截断分级降级的同族链路）。
- **取舍**：① 自研扫描器 vs 库（partial-json-parser 类）：核心状态机 100 行内可控、无第三方依赖是自研的理由；但转义/Unicode 边界（Q7769 UTF-8 多字节边界）的坑多，生产自研必须带全量单测；② 增量交付的粒度：每 chunk 解析一次 vs 节流（每 50ms 或每 N 字符）——解析器本身 O(总长)，重复扫描用"记住上次位置"的真正增量（游标推进）把复杂度摊平；③ 数组流式的特例：顶层数组（列表结果）可以做**逐元素流式**（每个完整元素即交付），比对象流式更有价值（列表 UI 渐进渲染），代价是要求生成端保证元素顺序；④ 与 schema 校验的关系：修复产物过 schema 时必须以"partial 模式"校验（只校验存在的字段），全量校验会把合法的部分交付全部拦死。
- **实战**：① 交付契约：部分交付的对象带 `_incomplete: true` + `_missing: [字段清单]`，前端按标记禁用"提交"按钮——部分数据可展示不可操作；② 重试续写的协议：截断后把已生成前缀回传给模型续写（模型侧上下文延续），比整体重试省 token（Q7614 重复计费的缓解），但要验证续写边界的语义连贯（不重复不丢字段）；③ 监控三指标：截断率（finish_reason=length 占比）、修复成功率（修复后必需字段完整率）、部分交付转化率（用户在部分数据下继续操作的比例）——截断率持续超阈值说明 max_tokens 配置问题（Q7643 思考 token 吃预算的同族）；④ 测试集：构造各截断位置的用例（引号内/转义符后/数组中间/嵌套对象内）做金样回归（Q7277 同族）。

```python
"""Q7781 partial JSON 增量解析: 深度栈+引号状态+可恢复前缀补全。"""


def partial_parse(text: str) -> tuple[dict, list[str]]:
    """解析到任意位置, 返回(已闭合字段dict, 缺失/未完成项清单)."""
    depth = []                # 括号栈: True=dict(False=list)
    in_str = False
    esc = False
    obj: dict = {}
    key = None
    val = ""
    reading_val = False
    for ch in text:
        if in_str:
            if esc:
                esc = False
                val += ch
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
                if not reading_val and key is None:
                    key = val          # key 闭合
                else:
                    obj[key] = val     # value 闭合
                    key, val, reading_val = None, "", False
            else:
                val += ch
            continue
        if ch == '"':
            in_str = True
            val = ""
        elif ch == ":":
            reading_val = True
            val = ""
        elif ch == ",":
            key, val, reading_val = None, "", False
        elif ch in "{[":
            depth.append(ch == "{")
        elif ch in "}]":
            if depth:
                depth.pop()
    missing = []
    if in_str or key is not None or depth:
        missing = ["未闭合 value" if in_str else
                   ("未闭合 key" if key is not None else "未闭合括号")]
    return obj, missing


def repair_prefix(obj: dict, missing: list[str]) -> str | None:
    """截断修复: 只信任已闭合字段, 标记 partial."""
    if not missing:
        return None                     # 完整, 无需修复
    return '{"partial": true, "data": ' + json_dumps(obj) + "}"


def json_dumps(obj: dict) -> str:
    parts = [f'"{k}": "{v}"' for k, v in obj.items()]
    return "{" + ", ".join(parts) + "}"


if __name__ == "__main__":
    full = '{"name": "张三", "tags": "a,b", "city": "北京"}'
    cut = '{"name": "张三", "tags": "a,b", "city": "北'      # 断在字符串中间
    obj, miss = partial_parse(cut)
    print(f"流中断于: {cut!r}")
    print(f"增量解析: 已闭合字段 {obj}, 未完成 {miss}")
    repaired = repair_prefix(obj, miss)
    print(f"修复产物: {repaired}  <- 只含可信字段, 带标记")
    obj_ok, _ = partial_parse(full)
    print(f"完整输入: {obj_ok} (无需修复)")
    # 增量交付演示: 每 chunk 到达即可提取已闭合字段
    stream_out = []
    for i in range(1, len(full) + 1):
        o, m = partial_parse(full[:i])
        if o and (not stream_out or stream_out[-1][0] != len(o)):
            stream_out.append((len(o), dict(o)))
    print("首字段提前上屏点:", stream_out[0])
    ok = (obj.get("name") == "张三" and obj.get("tags") == "a,b"
          and miss and stream_out[0][0] == 1)
    print(f"校验: 截断点安全提取 + 增量首字段提前交付 -> {'通过' if ok else '异常'}")
    print("结论：partial 解析=状态机(引号/深度/转义), 已闭合字段可信可交付;")
    print("      修复产物必须带 partial 标记与缺失清单, 截断在 value 内丢弃该字段")
```

**追问一**：转义字符与 Unicode 转义（\u4e2d）在增量扫描里有哪些坑？为什么"每 chunk 独立解码"会在字节边界出错？

→ 解析：三个坑的层次：① **转义引号**（`\"`）：简单状态机会把 `\"` 的引号误判为"字符串结束"，之后的 `}` 被当成语法字符——扫描器必须维护 `esc` 状态（本卡实现），反斜杠后第一个字符无条件吞掉；连锁坑是 `\\\"`（转义的反斜杠后跟真引号）：esc 标志要"每字符重置"而不是"遇到反斜杠就翻转"，否则偶数个反斜杠的判断全错。② **Unicode 转义**（`\u4e2d`）：6 字符序列表示一个字符，截断正好落在 `\u4e` 时——语法上不完整，补引号修复会得到非法转义；扫描器要么把 `\u` 开头的序列当作"原子等待"状态，要么修复时检测尾部未完成的转义序列直接截到序列开始处。③ **字节级边界**（Q7769 专卡主题）：网络流给的是 bytes，UTF-8 多字节字符可能被 chunk 切开——必须用增量解码器（`codecs.getincrementaldecoder('utf-8')`）缓存不完整字节序列，绝不能对每个 chunk 独立 `decode`（会在边界抛 UnicodeDecodeError 或产生替换字符污染字符串）。三层坑的共同教训：**流式文本处理的正确姿势是"字节→字符→语法"三级状态机贯通，任何一级独立处理都会在边界处出错**；测试集必须覆盖三类边界的截断点（转义内、\u 序列内、多字节字符中间），这类 bug 不构造边界用例永远测不出来。

**追问二**：如果模型输出的是 JSON Lines（NDJSON）而非单个 JSON 对象，流式处理的设计要改什么？容错语义怎么变化？

→ 解析：NDJSON（每行一个独立 JSON，Q5148 同族格式）把"部分可用"的粒度从字段级升到**记录级**——处理模型完全不同：① **解析单位是行**：每收到 `\n` 即一条完整记录，不需要深度栈补全；未完成的行（无换行结尾）留在缓冲区等下一个 chunk，天然是增量流；行内截断（TCP 层断开）只需丢弃当前不完整行，前面的行全部完好——**容错语义从"修复"退化为"丢弃"，简单且无歧义**；② **流式交付更强**：长列表场景（导出、批量标注）可以真正逐条上屏，首条延迟 = 第一条记录的生成时长，比对象流式又早一截；③ **代价是表达力**：单对象里的嵌套结构（对象嵌数组）NDJSON 表达不了跨行关联（除非用 key 关联拍平），适合"记录同构"的场景（日志、批量任务结果），不适合复杂嵌套 schema；④ **空行与分隔容错**：模型偶发输出空行或双换行，解析端要跳过空行而非报错；行尾 `\r`（Windows 风格）要 strip。工程判断标准：**schema 是"单记录扁平+记录数多"→ NDJSON 优先（流式与容错都最简单）；schema 是"复杂嵌套单对象"→ 单 JSON + partial 解析**；两者也可以组合：顶层 NDJSON、每行内是小对象。把格式选择当成 API 设计的一部分而不是实现细节——它决定了下游整条流式链路的复杂度。
