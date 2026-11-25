---
title: "[Q7755] 流到一半的表格：流式 Markdown 半截语法的前端渲染兜底"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7755 · 流到一半的表格：流式 Markdown 半截语法的前端渲染兜底

难度：P6 ｜ 标签：流式输出、Markdown 渲染、语法状态机、SSE、前端兜底

基线：Python 3.12；模拟分块到达的 Markdown，对比"逐块渲染"与"语法状态机缓冲渲染"的输出稳定性。

**问**：流式输出的回复里带 Markdown（代码块、表格、列表），前端逐 chunk 渲染时用户会看到"半截表格""未闭合的代码围栏闪一下""列表符号孤零零挂着"，块闭合的瞬间内容还会跳变。逐块渲染为什么必然出现破损？怎么让流式渲染既保持打字机效果，又不在语法结构中间露怯？

**答**：
- **结论**：逐块渲染把每个 chunk 当独立文本喂给渲染器，而 Markdown 语法是**跨 chunk 的状态**：代码围栏（三反引号）开与闭可能相隔几十个 chunk、表格行间的分隔行、列表的缩进层级都要向后看。破损不可避免，解法是给渲染层加一个**语法状态机**：维护当前是否处于未闭合的代码块/表格/多行结构中，处于"结构内部"的 chunk 先缓冲不渲染，等闭合标记到达（或流结束的 fallback）后整块渲染——打字机效果对普通文本段落保留，对结构块变成"块级出现"，视觉从"闪变"变成"稳定出现"。关键点：状态机要能处理"围栏标记本身被 chunk 切开"（第一块结尾是两个反引号、下一块开头是一个）。
- **取舍**：① 缓冲粒度按语法块而不是按 chunk：块大时（长代码段）等待时间久，可折中"代码块内部按行渐进渲染但明确标注未完成态"；② 状态机实现要在前端做还是后端做？后端打标（每个 chunk 附 `in_code_block` 状态）把复杂度收在服务端，前端 dumb 渲染，多端一致；③ 流中断时（Q2592 的断流恢复）状态机的未闭合块要能按"未完成"降级渲染，而不是永远空白；④ 渲染器升级（换 markdown 库）时状态机语义要跟着回归测试。
- **实战**：① 服务端在 SSE 帧上附加语法状态标记，前端不做自己的状态推断；② 测试集覆盖"围栏被切在任意位置"的分块序列（属性测试思路）；③ 与内容审查联动：审查器（Q2322 跨块正则）与渲染状态机共享同一个缓冲窗口，避免两套缓冲不一致；④ 跳变问题除缓冲外，可对块级出现加淡入动画，减少"内容突然出现"的突兀感。

```python
"""流式 Markdown 渲染状态机：未闭合结构缓冲, 闭合后整块渲染。"""
FENCE = chr(96) * 3

CHUNKS = [
    "查询结果如下：\n",
    "| 商品 | 价格 |\n|---|---|\n",
    "| A | 99 |\n| B | 199 |\n\n用法：\n",
    FENCE + "python\n",                       # 围栏被单独切成一块
    "print('hello')\n",
    "print('world')\n" + FENCE + "\n",        # 闭合
    "以上即为全部结果。",
]


def render_naive(chunks: list[str]) -> list[str]:
    """反例：逐 chunk 直接渲染。"""
    return [c for c in chunks]


def render_buffered(chunks: list[str]) -> list[str]:
    """状态机：未闭合的围栏/表格缓冲, 闭合即整块渲染。"""
    out, buf, in_fence = [], [], False
    pending_tail = ""                          # 围栏标记被切断的残段
    for c in chunks:
        text = pending_tail + c
        pending_tail = ""
        # 残段检测: 末尾有 1-2 个反引号, 可能是切开的围栏
        stripped = text.rstrip("\n")
        if stripped.endswith(chr(96)) and not in_fence:
            n = len(stripped) - len(stripped.rstrip(chr(96)))
            if 1 <= n < 3:
                pending_tail = stripped[len(stripped) - n:]
                text = text[:len(text) - n]
        for line in text.split("\n"):
            line += "\n"
            if line.strip().startswith(FENCE):
                if in_fence:                   # 闭合 -> 整块渲染
                    buf.append(line)
                    out.append("".join(buf))
                    buf, in_fence = [], False
                else:                          # 开启 -> 进入缓冲
                    buf.append(line)
                    in_fence = True
            elif in_fence:
                buf.append(line)
            else:
                out.append(line)               # 普通文本直接渲染
    if buf:                                    # 流结束仍未闭合 -> 降级渲染
        out.append("".join(buf) + "[输出未完成]")
    return out


if __name__ == "__main__":
    naive = render_naive(CHUNKS)
    print("逐块渲染(反例): 第 4 帧用户看到孤立的围栏标记:",
          repr(naive[3][:12]), "<-- 闪变源")
    print("\n状态机渲染:")
    for i, frame in enumerate(render_buffered(CHUNKS), 1):
        head = frame.replace("\n", " ")[:48]
        print(f"  帧{i}: {head}")
    print("\n结论：Markdown 是跨 chunk 的语法状态；结构块缓冲到闭合再渲染,")
    print("      残段(围栏被切开)要拼接回传；流结束未闭合按'未完成'降级")
```

**追问一**：为什么不在前端用完整的 Markdown 解析器做增量重渲染？

→ 解析：可以，但有三个代价：① 每帧全量重解析，长回复高频 chunk 下 CPU 开销显著，低端设备掉帧；② 增量重渲染无法避免"半截语法"的中间态——解析器自己也只能输出"未闭合结构"的某种解释，视觉跳变只是被换了个形式；③ 前后端各一套解析逻辑，审查、计费、录制回放（Q1762）都要对齐同一份内容切分。服务端统一状态机 + 帧上打标的方案，把渲染正确性收敛到一处，前端只做展示，是更可维护的分层。

**追问二**：状态机需要覆盖哪些语法块？优先级怎么定？

→ 解析：按"破损视觉冲击 × 出现频率"排：① 围栏代码块（最高频且切开概率大，必须缓冲）；② 表格（分隔行跨块，必须缓冲到出现至少表头+分隔行）；③ HTML 原生标签（LLM 输出里少见但一旦半截最危险，直接整块缓冲并转义）；④ 多级列表/引用块（向后看最多一行，可用"行级缓冲"轻量处理）。不追求一次覆盖全部语法——把最常见的两类做稳，配合流结束的降级渲染，90% 的破损场景就能消掉；剩余长尾靠"渲染快照回归测试"逐步纳入状态机，而不是一开始造一个过度复杂的状态机。
