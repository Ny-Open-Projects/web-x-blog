---
title: "[Q7796] token 计数偏差与截断顺序：估算、精确计数与先删什么"
date: 2026-11-25
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7796 · token 计数偏差与截断顺序：估算、精确计数与先删什么

难度：P6 ｜ 标签：Agent、token、分词器、上下文预算、截断、中文、代码

基线：库知识库外知识卡，代码用标准库模拟——手写"中文按字、英文按词"的玩具分词器，对比 `len/4` 估算，不调用外部 API。

**问**：上下文预算是 8k，代码用 `len(text) // 4` 估算，中文 prompt 估出来 6k，实际发出去却超窗被服务端截断——而且截断发生在**最前面**，system 指令被切掉了。中文、英文、代码的 token/字符比差多少？`len/4` 在哪种内容上最不准？预算不够时，应该先删历史、先删检索块，还是先删 system？

**答**：

- **结论**：`len/4` 是"英文平均 4 字符 ≈ 1 token"的经验值，**方向性偏差**很明显：中文（尤其简体）常是 1 汉字 ≈ 1 token，`len/4` 会把 1 万汉字估成 2500，**低估 4 倍**；英文大约 4～5 字符/token，`len/4` 略高估；代码因为符号多（`(){}[];` 各自可能成 token）、缩进与换行也计费，通常 **低于** 4 字符/token，`len/4` 低估。所以估算必须先**按内容类型分档**（中文 1 字/token、英文 4.5 字符/token、代码 3 字符/token），或直接用目标模型的 tokenizer 精确计数。预算不够时的删除顺序应当是"**价值最低、最可重建**的先删"：重复的检索块 → 较早的对话历史 → 低相关检索块 → few-shot 示例；**system 约束和当前问题最后删**，因为删了会改变任务语义或让模型失去格式约束。
- **取舍**：精确计数要加载 tokenizer（内存、启动时间、版本要与线上模型一致），估算便宜但误差大；折中是"估算做粗筛 + 发送前用 tokenizer 精确校验"，超了就按预案裁剪。另一个取舍是"截断位置"：从**头部**截断（很多框架的默认）会切掉 system，最危险；从**尾部**截断会切掉当前问题；正确做法是**按段落/消息边界**删除整块，而不是按字符数硬切，且永远保留 system 与最后一条 user。
- **实战**：一次中文客服 Agent 用 `len/4` 估算，8k 预算实际发了 2.8 万 token，服务端按"从头部截断"处理，system 里的"不得承诺退款"被切掉，模型对用户做出了越权承诺。修复：① 计数换成与线上模型一致的 tokenizer；② 裁剪按消息块从旧到新删，system 与当前问题加 `pin` 标记不可删；③ 发送前断言 `count <= budget`，超了直接走"摘要历史"而不是硬截。上线后同类事故归零。

下面用玩具分词器量化三种内容的估算偏差，并对比两种截断顺序的答案质量。

```python
# token 估算偏差 + 截断顺序对关键信息的影响
import re


def count_tokens(text):
    """玩具分词: 中文按字, 英文按词, 符号单独算。"""
    cjk = sum(1 for ch in text if "\u4e00" <= ch <= "\u9fff")
    rest = re.sub(r"[\u4e00-\u9fff]", " ", text)
    return cjk + len(re.findall(r"[A-Za-z_]+|[0-9]+|[^\sA-Za-z0-9_]", rest))


SAMPLES = {
    "中文": "这是一段中文文本，用来测试分词偏差到底有多大。",
    "英文": "This is an English sentence used for token counting.",
    "代码": "def add(x, y):\n    return x + y\n",
}
for name, s in SAMPLES.items():
    a, e = count_tokens(s), len(s) / 4
    print(f"[1] {name}: 实际 {a:>2} tokens, len/4 估算 {e:>5.2f}, 偏差 {a / e:.1f}x")
    if name == "中文":
        assert a > e * 3, "中文 len/4 严重低估"
    elif name == "英文":
        assert a < e, "英文 len/4 略高估"
    else:
        assert a > e, "代码符号多, len/4 低估"

# 截断顺序: 预算 40 tokens, 必须在 system/history/doc/question 中取舍
SYSTEM = "系统指令: 必须引用来源, 不得编造"
HISTORY = "user: 我上周问过发票 assistant: 已开 user: 谢谢"
DOC = "证据: 订单A金额100元"
QUESTION = "订单A多少钱"

pieces = {"system": SYSTEM, "history": HISTORY, "doc": DOC, "question": QUESTION}
total = sum(count_tokens(v) for v in pieces.values())
print(f"[2] 全量 {total} tokens, 预算 40, 需要删 {total - 40}")
assert total > 40


def quality(kept):
    """答案质量: 关键证据 0.6 + 系统约束 0.2 + 当前问题 0.2。"""
    return 0.6 * ("doc" in kept) + 0.2 * ("system" in kept) + 0.2 * ("question" in kept)


def drop(pieces, order, budget):
    kept = dict(pieces)
    for k in order:
        if sum(count_tokens(v) for v in kept.values()) <= budget:
            break
        kept.pop(k, None)
    return kept


bad = drop(pieces, ("system", "history", "doc"), 40)      # 从头删(框架默认)
good = drop(pieces, ("history",), 40)                     # 先删历史, 保 system/doc
print(f"[3] 从头删: 保留 {sorted(bad)}, 质量 {quality(bad):.1f}")
print(f"    按价值删: 保留 {sorted(good)}, 质量 {quality(good):.1f}")
assert quality(good) > quality(bad)
assert "system" in good and "question" in good
print("    → 实测 截断顺序直接决定答案质量; system 与当前问题必须 pin, 先删历史")

# 预算校验: 估算通过不代表实际通过
text = SYSTEM + HISTORY + DOC + QUESTION
print(f"[4] 估算 {len(text) / 4:.1f} <= 40? {len(text) / 4 <= 40}; "
      f"实际 {count_tokens(text)} <= 40? {count_tokens(text) <= 40}")
assert len(text) / 4 <= 40 and count_tokens(text) > 40
print("    → 实测 估算通过、实际超窗, 是中文场景最典型的事故形态")
```

**追问一**：为什么"从头部截断"在多数框架里是默认？—— 因为实现简单：保留最近的 N 个 token（尾部），丢掉前面。对"对话历史"这种结构，这是合理的——最近的话最重要；但对"system 在最前 + 当前问题在最后"的结构，它同时切掉了 system 和中间证据，只留下最近几轮闲聊。危险在于它**不会报错**，模型照常回答，只是失去了约束。工程上要把"消息"作为裁剪单位，给 system/当前问题打 `pinned` 标记，并优先做"历史摘要"而不是硬删。

**追问二**：用目标模型的 tokenizer 精确计数就万无一失了吗？—— 不。① tokenizer 版本必须与线上模型一致（同一家模型不同版本的分词表可能不同）；② 工具调用/多模态/图片的 token 计价规则不同（图片按分辨率折算，工具 schema 也占 token）；③ 服务端可能还有"消息包装"开销（role 标记、分隔符），每轮多几个 token，长对话累积起来不可忽略；④ 结构化输出的 JSON 也占输出预算。所以精确计数是必要条件，不是充分条件——仍要预留 5%～10% 的安全余量，并对"服务端返回 context_length_exceeded"做兜底（降级到摘要/更小上下文重试）。

## 背诵要点

- 估算偏差有方向：中文约 1 字/token（`len/4` 低估 4 倍）、英文约 4.5 字符/token（略高估）、代码符号多（低估）；应按内容类型分档或直接用目标 tokenizer。
- 删除顺序按价值：重复检索块 → 旧历史 → 低相关块 → few-shot；system 与当前问题 pin 住，最后才动。
- 按消息块裁剪而非按字符硬切；精确计数仍需预留 5%～10% 余量，并为服务端超窗错误准备降级。

## 复盘追问

- 中文 prompt 估算 6k 实际 28k，你怎么在发送前拦住？（按语言分档估算 + 目标 tokenizer 精确校验 + `count <= budget` 断言）
- 预算不够时为什么不能先删 system？（system 承载任务约束与安全规则，删了模型行为会漂移；应该删可重建的历史/重复块）
