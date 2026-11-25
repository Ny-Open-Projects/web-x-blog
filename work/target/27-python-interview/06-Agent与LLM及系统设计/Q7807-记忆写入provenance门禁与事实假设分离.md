---
title: "[Q7807] 记忆写入的 provenance 门禁：模型的猜测怎么变成了事实"
date: 2026-11-25
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7807 · 记忆写入的 provenance 门禁：模型的猜测怎么变成了事实

难度：P7 ｜ 标签：Agent 记忆、provenance、事实/假设、写入门禁、TTL

基线：库知识库外知识卡，用纯 Python 的记忆条目（来源/置信度/轮次）模拟"最新覆盖"与"来源门禁"两种写入/读取策略。

**问**：客服 Agent 有长期记忆。用户第一轮说"我在 ACME 做采购"，第五轮聊到竞品时 Agent 自己总结了一句"用户公司是 Beta Corp"，写进了记忆。两周后用户回来问报价，Agent 开口就说"为 Beta Corp 报价"，用户当场投诉。模型怎么会把自己的猜测写成事实？记忆系统该怎么区分"用户说的""工具查到的""模型推断的"？只加一个置信度够吗？

**答**：

- **结论**：记忆系统的写入路径如果只有"文本 + 向量"，就会把**所有来源**一视同仁：用户陈述、工具返回、模型推断都变成同一种"记忆条目"。读取时按相似度/时间取最新，模型的猜测就覆盖了用户的事实。必须引入 **provenance（来源）**：`user_stated` / `tool_observed` / `model_inferred`，并在**写入时**决定它能不能成为"事实"。只有前两类可以进事实库；推断类只能进"假设区"，带置信度、TTL、`needs_confirmation`，读取时默认不作为事实使用。
- **取舍**：① 只加置信度：不够，模型给猜测打 0.9 的置信度很常见，置信度是模型自评，不是证据；② 来源门禁：最有效，但需要把来源一路传进记忆写入 API，改造面大；③ 人工确认：最稳，但延迟高，只适合高价值事实；④ 推断也存但标灰：兼顾召回与安全，读取时按场景决定是否使用（如"猜你喜欢"可以用，报价不能用）。
- **实战**：① 记忆条目强制字段：`text/source/confidence/created_at/expires_at/derived_from`；② 写入 API 区分 `assert_fact()` 与 `add_hypothesis()`，后者不能覆盖前者；③ 冲突检测：同一主语出现两个事实来源时，不自动覆盖，标记 `conflict` 并回问用户；④ 读取时按用途分级：报价/合同/医疗等高风险场景只用 `user_stated/tool_observed`；⑤ 定期审计"假设被当成事实引用"的比例。

下面模拟：最新覆盖会把 Beta 当成事实，来源门禁 + 冲突标记会保留 ACME 并追问。

```python
# 记忆 provenance: 只有 user_stated/tool_observed 能进事实库
MEMORY = [
    {"text": "用户所在公司是 ACME", "source": "user_stated", "conf": 0.95,
     "turn": 1, "expires_at": None},
    {"text": "用户所在公司是 Beta Corp", "source": "model_inferred", "conf": 0.55,
     "turn": 5, "expires_at": 30},
]
FACT_SOURCES = {"user_stated", "tool_observed"}


def naive_answer(memory):
    # 最新一条胜出, 不看来源
    return max(memory, key=lambda m: m["turn"])["text"]


def gated_answer(memory):
    facts = [m for m in memory if m["source"] in FACT_SOURCES]
    if not facts:
        return "无事实依据, 需要追问"
    return max(facts, key=lambda m: m["conf"])["text"]


print(f"[1] 最新覆盖: {naive_answer(MEMORY)}")
print(f"[2] 来源门禁: {gated_answer(MEMORY)}")
assert "Beta" in naive_answer(MEMORY)
assert "ACME" in gated_answer(MEMORY)
print("    → 实测 只按时间取最新, 模型猜测会覆盖用户陈述; 来源门禁保住事实")

# 推断项进假设区: 带 TTL 与待确认标记, 不参与事实读取
def write_memory(memory, text, source, conf, turn):
    entry = {
        "text": text, "source": source, "conf": conf, "turn": turn,
        "expires_at": 30 if source == "model_inferred" else None,
        "needs_confirmation": source == "model_inferred",
    }
    memory.append(entry)
    return entry


mem = list(MEMORY)
entry = write_memory(mem, "用户偏好顺丰发货", "model_inferred", 0.7, 6)
print(f"[3] 写入推断: source={entry['source']}, needs_confirmation={entry['needs_confirmation']}, "
      f"TTL={entry['expires_at']}天")
assert entry["needs_confirmation"] is True

# 冲突检测: 两个事实来源指向不同公司 -> 不覆盖, 标记冲突
def detect_conflict(memory):
    facts = [m for m in memory if m["source"] in FACT_SOURCES]
    subjects = {m["text"].split("是")[-1].strip() for m in facts}
    return len(subjects) > 1, subjects


mem2 = list(MEMORY)
write_memory(mem2, "用户所在公司是 Gamma Inc", "tool_observed", 0.99, 7)
conflict, subjects = detect_conflict(mem2)
print(f"[4] 事实冲突={conflict}, 候选={sorted(subjects)}")
assert conflict is True
print("    → 实测 事实之间冲突不自动覆盖, 标记 conflict 并回问用户/查权威源")

# 高风险场景: 推断类一律不可用于报价
def answer_for(memory, risk):
    if risk == "high":
        facts = [m for m in memory if m["source"] in FACT_SOURCES]
        return facts[0]["text"] if facts else "需要用户确认"
    return gated_answer(memory)


print(f"[5] 高风险问答: {answer_for(MEMORY, 'high')}")
assert "ACME" in answer_for(MEMORY, "high")
print("    → 实测 provenance 是写入时就要打的标签, 读取时按用途分级, 不是事后补置信度")
```

**追问一**：来源是"用户说的"，就一定是事实吗？—— 不一定。用户可能说错、开玩笑、转述别人。`user_stated` 只表示"用户确实这么说过"，不表示"客观为真"。高风险场景仍要交叉验证（工具查询、二次确认）。provenance 解决的是"这句话是谁说的"，不是"这句话对不对"；两者要分开建模。

**追问二**：为什么不让模型自己判断"这条要不要记"？—— 模型判断本身也是 `model_inferred`，会受上下文暗示：它可能把"用户在比较竞品"推断成"用户公司是 Beta"，并自信地写入。写入门禁必须是**系统规则**（来源 + 用途 + 冲突检测），模型只能提议，不能自批。

## 背诵要点

- 记忆条目必须有 `source`（user_stated/tool_observed/model_inferred）、置信度、时间、TTL、derived_from。
- 只有前两类进事实库；推断类进假设区，带 `needs_confirmation` 与 TTL，高风险场景不参与回答。
- 事实冲突不自动覆盖，标记 `conflict` 回问；provenance 是写入时标签，不是事后补置信度。

## 复盘追问

- `tool_observed` 一定可信吗？工具返回过期/错误数据时，provenance 还缺哪一层？
- 假设区的记忆什么时候可以"转正"？转正需要哪些证据与审计留痕？
