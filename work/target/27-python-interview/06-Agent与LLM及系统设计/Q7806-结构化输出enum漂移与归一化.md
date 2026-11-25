---
title: "[Q7806] 结构化输出的枚举漂移：in-progress 为什么过不了校验"
date: 2026-11-25
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7806 · 结构化输出的枚举漂移：in-progress 为什么过不了校验

难度：P7 ｜ 标签：结构化输出、enum、归一化、闭集校验、LLM

基线：库知识库外知识卡，用纯 Python 模拟 JSON Schema `enum` 的严格校验、别名归一与未知值分流。

**问**：工单分类接口要求返回 `{"status": "IN_PROGRESS"}`，schema 里 `enum` 写死三个值。上线后 38% 的响应校验失败，日志里是 `in-progress`、`进行中`、`IN PROGRESS`、`In_Progress`；重试三次仍有 12% 失败。模型明明"理解"了状态，为什么就是不肯输出枚举原值？把 `enum` 去掉改成自由字符串行不行？归一化会不会把 `canceled` 和 `cancelled` 之外的错误也"洗白"？

**答**：

- **结论**：LLM 对枚举的"语义"理解正确，但对**字面量**没有强约束：它会把 `IN_PROGRESS` 写成 `in-progress`、中文、空格分隔，甚至在 `temperature>0` 时自造变体。JSON Schema 的 `enum` 是**闭集精确匹配**，一个字符不同就失败；重试只是在同一分布里再采样，不能保证收敛。正确做法是三层：① 生成侧用**约束解码/严格 schema**（如 JSON mode、GBNF、`strict: true`）把候选 token 限制在枚举内；② 校验侧做**显式别名归一**（大小写、连字符、下划线、中文同义词），归一后再做闭集判断；③ 未知值不猜，进人工/降级队列。
- **取舍**：① 去掉 `enum` 改自由字符串：校验通过率上去了，但下游状态机拿到 `"进行中"` 仍然无法分支，问题从"校验失败"变成"运行时 KeyError"；② 约束解码：最硬，但依赖模型/网关支持，且枚举多时首 token 分布被强行裁剪，可能影响语义质量；③ 别名归一：兼容性好，但映射表要版本化，新增同义词需要评审，不能"看到像就归"；④ 未知值默认成某个合法值：最危险，会把"模型没听懂"伪装成"正常结果"。
- **实战**：① 枚举值用 `UPPER_SNAKE_CASE` 并在 prompt 里给出"允许值 + 每个值的一句话定义 + 反例"；② 归一化只做**形式变换**（大小写/分隔符/全半角），语义同义词必须走显式映射表；③ 归一后仍不在闭集的，记录原始值 + 上下文，进 `needs_review`，不要静默 fallback；④ 监控"原始值 → 归一值"的映射命中率，新变体突增说明 prompt 或模型版本变了。

下面模拟 8 条原始输出：严格校验只过 1 条，归一化后过 7 条，未知值仍被拒绝。

```python
# enum 漂移: 严格闭集只认原值; 形式归一 + 显式别名表提升通过率
ALLOWED = {"IN_PROGRESS", "DONE", "CANCELLED"}
ALIASES = {
    "in_progress": "IN_PROGRESS",
    "进行中": "IN_PROGRESS",
    "done": "DONE",
    "已完成": "DONE",
    "cancelled": "CANCELLED",
    "canceled": "CANCELLED",
}


def canon(raw):
    # 只做形式归一: 去空白、转小写、连字符/空格转下划线
    key = raw.strip().lower().replace("-", "_").replace(" ", "_")
    return ALIASES.get(key, raw.strip().upper())


raw_values = ["in-progress", "进行中", "IN_PROGRESS", "done", "已完成", "cancelled", "CANCELED", "foo"]
strict_ok = [v for v in raw_values if v in ALLOWED]
normalized = [(v, canon(v)) for v in raw_values]
norm_ok = [(v, c) for v, c in normalized if c in ALLOWED]
rejected = [(v, c) for v, c in normalized if c not in ALLOWED]

print(f"[1] 严格校验通过 {len(strict_ok)}/{len(raw_values)}: {strict_ok}")
print(f"[2] 归一后通过 {len(norm_ok)}/{len(raw_values)}: {[c for _, c in norm_ok]}")
print(f"[3] 仍被拒绝: {rejected}")
assert len(strict_ok) == 1
assert len(norm_ok) == 7
assert rejected == [("foo", "FOO")]

# 语义同义词必须显式映射, 不能靠'像不像'
def unsafe_fuzzy(value):
    for allowed in ALLOWED:
        if allowed.startswith(value[:3].upper()):
            return allowed
    return None


print(f"[4] 模糊前缀 'CAN' -> {unsafe_fuzzy('CAN')}, 'DON' -> {unsafe_fuzzy('DON')}")
assert unsafe_fuzzy("CAN") == "CANCELLED"
assert unsafe_fuzzy("DON") == "DONE"
print("    → 实测 模糊匹配会把拼写错误的未知值洗白; 只允许显式别名表")

# 未知值分流: 不猜, 进 review, 保留原始值
def classify(raw):
    c = canon(raw)
    if c in ALLOWED:
        return "accepted", c
    return "needs_review", raw


print(f"[5] 'foo' -> {classify('foo')}, 'in-progress' -> {classify('in-progress')}")
assert classify("foo") == ("needs_review", "foo")
assert classify("in-progress") == ("accepted", "IN_PROGRESS")
print("    → 实测 归一化只处理形式, 未知值显式分流; 不要把'没听懂'伪装成合法状态")
```

**追问一**：约束解码能 100% 保证枚举合法吗？—— 在 tokenizer/文法层面能保证"输出落在枚举集合内"，但保证不了"语义选对"：模型可能被强行裁剪到 `DONE`，而实际应该是 `CANCELLED`。约束解码解决的是**格式合法性**，不是**语义正确性**。仍需要业务校验（状态机是否允许该跃迁）与抽检。

**追问二**：为什么重试对枚举漂移效果有限？—— 重试是同一模型、同一 prompt、同一温度下再采样：如果模型对字面量的偏好是稳定的（`temperature=0` 时几乎必然复现），重试只是重复失败；`temperature>0` 时随机性可能碰对，但成本高且不可控。正确顺序是"约束解码 > 归一化 > 重试"，重试放最后。

## 背诵要点

- `enum` 是闭集精确匹配，LLM 的语义理解不等于字面量遵循；`in-progress`/`进行中` 都会校验失败。
- 三层治理：约束解码/严格 schema → 形式归一（大小写/分隔符/全半角）+ 显式别名表 → 未知值进 review。
- 不要模糊匹配"洗白"未知值，也不要默认 fallback 到合法值；重试放最后，temperature=0 时重试常无效。

## 复盘追问

- 别名表应该由谁维护、怎么版本化？模型升级后新增变体如何进入评审流程？
- 约束解码把候选裁到枚举内，为什么仍可能"格式对、语义错"？业务侧还要加什么校验？
