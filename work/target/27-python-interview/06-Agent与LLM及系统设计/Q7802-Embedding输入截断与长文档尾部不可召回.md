---
title: "[Q7802] Embedding 输入截断：长文档的后半段为什么永远搜不到"
date: 2026-11-25
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7802 · Embedding 输入截断：长文档的后半段为什么永远搜不到

难度：P7 ｜ 标签：RAG、embedding、max_seq_len、截断、分块

基线：库知识库外知识卡，用"词袋向量 + 前缀截断"模拟 embedding 模型只编码前 N 个 token 的行为，对比整篇嵌入与分块嵌入的召回。

**问**：一份 30 页的产品手册，退款条款在第 22 页。用户问"退款窗口几天"，RAG 永远召回别的文档，把整篇手册的向量拿来比也不相关。排查发现 embedding 模型 `max_seq_len=512`，而手册有 1.8 万 token。模型不是有 32k 上下文吗？为什么 embedding 只吃 512？截断对召回的影响有多大？怎么切才能让后半段被搜到？

**答**：

- **结论**：embedding 模型的 `max_seq_len` 和生成模型的上下文窗口**不是一回事**：它由训练时的位置编码/注意力窗口决定，常见 512（如 BERT 类）或 8192（新一代）。超过的部分会被**静默截断**（有的库直接切，有的报 warning），后面的内容根本不参与向量计算。整篇 1.8 万 token 的手册只编码了前 512 token，第 22 页的退款条款在向量里"不存在"，任何 query 都不可能召回它。**整篇嵌入对长文档是错误做法**，必须分块。
- **取舍**：① 固定窗口分块（如 256/512 token + overlap）：简单、每块都能被编码，代价是块间语义割裂；② 语义/版式分块（按标题、段落、表格）：边界更自然，代价是要解析结构；③ 父子块（small-to-big）：小块召回、大块喂给 LLM，兼顾召回与上下文，代价是两次查询/存储；④ 长上下文 embedding 模型：减少切分，但 8192 仍装不下 1.8 万，而且长文本向量会"平均化"多个主题，检索精度下降。
- **实战**：① 入库前统计 token 长度分布，`P99 > max_seq_len` 的文档必须切；② 切块时保留标题/页码/章节路径，召回后能定位原文；③ 每块单独 embedding，不要用整篇向量"代表"文档；④ 评测集专门放"答案在文档尾部"的 query，验证截断是否被修复；⑤ 监控"文档 token 数 / 实际编码 token 数"的比值，>1 就是静默丢失。

下面模拟 905 token 的文档：整篇只编码前 512，尾部退款条款不可见；切成 256 的块后可召回。

```python
# embedding 截断: 只编码前 max_seq_len 个 token, 尾部内容对检索不可见
MAX_SEQ_LEN = 512
TAIL = ["refund", "window", "is", "14", "days"]
doc = ["intro"] * 900 + TAIL          # 905 token, 退款条款在最后
query = set(TAIL)


def embed(tokens):
    return set(tokens[:MAX_SEQ_LEN])   # 超长静默截断


def cosine(q, v):
    inter = len(q & v)
    return inter / (len(q) ** 0.5 * len(v) ** 0.5)


whole = embed(doc)
sim_whole = cosine(query, whole)
coverage = min(len(doc), MAX_SEQ_LEN) / len(doc)
print(f"[1] 整篇嵌入: 编码 {min(len(doc), MAX_SEQ_LEN)}/{len(doc)} token "
      f"({coverage:.0%}), 与 query 相似度={sim_whole:.2f}")
assert coverage < 0.6
assert sim_whole == 0.0

# 分块: 每块 300, 尾部条款正好落在最后一块
CHUNK = 300
chunks = [doc[i:i + CHUNK] for i in range(0, len(doc), CHUNK)]
chunk_sims = [cosine(query, embed(c)) for c in chunks]
best = max(chunk_sims)
print(f"[2] 分块后 {len(chunks)} 块, 各块相似度={[round(s, 2) for s in chunk_sims]}")
assert abs(best - 1.0) < 1e-9
assert chunk_sims.index(best) == len(chunks) - 1
print("    → 实测 整篇相似度 0, 分块后最后一块 1.0; 尾部内容重新可召回")

# 只按'开头'截断的另一种写法: 先摘要再嵌入, 同样会丢细节
def summarize_first(tokens, n=64):
    return tokens[:n]


summary_sim = cosine(query, embed(summarize_first(doc)))
print(f"[3] 只取开头 64 token 做摘要再嵌入: 相似度={summary_sim:.2f}")
assert summary_sim == 0.0

# 正确性检查: 所有 token 至少属于一个块
covered = set()
for idx, c in enumerate(chunks):
    covered.update(range(idx * CHUNK, idx * CHUNK + len(c)))
print(f"[4] token 覆盖率={len(covered)}/{len(doc)}")
assert len(covered) == len(doc)
print("    → 实测 分块要保证 100% token 覆盖; overlap 只解决边界语义, 不解决覆盖率")
```

**追问一**：`max_seq_len=512` 是 token 还是字符？—— 是 token。中文一个汉字约 1~2 token，英文一个词约 1~2 token，1.8 万 token 的手册可能只有 1 万多汉字。按字符数估算会低估截断风险，必须用模型对应的 tokenizer 实算，并在入库前记录 token 长度分布。

**追问二**：分块后每块都短，为什么还会召回不准？—— 块太短会丢上下文（代词、指代、表格列头），块太长又会平均化多主题。256~512 token + 10%~20% overlap 是常见起点，但要用评测集验证：答案被切断、指代缺失、表格跨块是三类典型 badcase。分块策略不是"切得越碎越好"，而是"每块自包含一个可回答的问题"。

## 背诵要点

- embedding 的 `max_seq_len` 由模型结构决定（常见 512），超长部分**静默截断**，不是生成模型的上下文窗口。
- 整篇长文档嵌入会让尾部内容在向量里"不存在"；必须分块，并保证 100% token 覆盖 + 适量 overlap。
- 入库前用 tokenizer 统计长度分布，`P99 > max_seq_len` 必须切；评测集放"答案在尾部"的 query 验证。

## 复盘追问

- 父子块（small-to-big）如何同时解决"块太大平均化"和"块太小丢上下文"？代价是什么？
- 如果 embedding 模型升级到 8192，是否就可以不分块了？长文本向量的"多主题平均"问题怎么解？
