---
title: "[Q7737] 非对称 embedding 少了 query/passage 前缀：召回率掉一半"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7737 · 非对称 embedding 少了 query/passage 前缀：召回率掉一半

难度：P6 ｜ 标签：embedding、非对称检索、query/passage 前缀、BGE/E5

基线：Python 3.12；BGE/E5 系列的 `query:` / `passage:` 前缀约定；纯 Python 模拟角色投影偏移。

**问**：换用 BGE/E5 这类非对称检索模型后，离线评测 recall@10 从 0.82 掉到 0.41。索引和查询用的是同一个 `encode()`，两边都没加前缀。模型文档写着"query 需加 `query: `、文档需加 `passage: `"。加个前缀真有这么大影响？

**答**：
- **结论**：非对称检索模型训练时，query 与 passage 走**不同的投影**（有的用不同前缀 token 让模型区分角色）。推理不加对应前缀，等于把 query 当 passage 编码，两侧分布错位，相似度整体塌陷。E5 系要求 `query: ` / `passage: `；BGE 中文 v1.5 的 query 指令是一句"为这个句子生成表示以用于检索相关文章："，passage 不加。**索引侧与查询侧必须严格配套**，换前缀就要重建索引。
- **取舍**：前缀多花几十 token 的编码成本，换来显著召回提升；对称模型（如 text-embedding-3）不需要前缀、通用性好，但垂直领域检索弱。最糟的是"索引无前缀、查询有前缀"这种半套配置，比两边都不加还差。
- **实战**：① 拆成 `encode_query()` / `encode_document()` 两个函数，禁止业务直接调底层 `encode`；② 前缀写进配置并与模型名绑定，换模型必须重建索引；③ 离线评测当门禁（recall@10 低于基线不许上线）；④ 索引元数据记录 `model + prefix_version`，检索时校验一致；⑤ 迁移时双写新旧向量，灰度切换。

```python
"""非对称检索的玩具模型：query 被当 passage 编码后，表示整体偏移到 passage 区域。"""
import math

# 段落表示（角度不同、彼此相近，模拟同领域语料）
DOCS = {
    "退款政策说明": [1.0, 0.0],
    "退款时效说明": [0.985, 0.174],     # 10 度
    "退款到账说明": [0.940, 0.342],     # 20 度
    "发票开具流程": [-1.0, 0.0],
}
DOC_ANGLE = {"退款政策说明": 0.0, "退款时效说明": 10.0,
             "退款到账说明": 20.0, "发票开具流程": 180.0}
# 角色偏移：不加 query 前缀时，query 被当 passage 编码，表示整体落到 passage 区域
BIAS = [3.0 * 0.985, 3.0 * 0.174]


def rotate(v, deg):
    r = math.radians(deg)
    return [v[0] * math.cos(r) - v[1] * math.sin(r),
            v[0] * math.sin(r) + v[1] * math.cos(r)]


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


def encode_query(text: str, use_prefix: bool):
    """加了 query 前缀 => 落在 query 区域（与文档对齐）；否则被当段落编码。"""
    q = rotate(DOCS[text], 3.0)         # query 与对应段落是不同文本，方向差 3 度
    return q if use_prefix else add(q, BIAS)


def recall_at_1(queries, use_prefix, threshold=0.8):
    hits, sims = 0, []
    for q in queries:
        qv = encode_query(q, use_prefix)
        scored = sorted(((d, cosine(qv, DOCS[d])) for d in DOCS), key=lambda kv: -kv[1])
        top_doc, top_sim = scored[0]
        sims.append(round(top_sim, 3))
        if top_doc == q and top_sim >= threshold:
            hits += 1
    return hits / len(queries), sims


if __name__ == "__main__":
    queries = list(DOCS)

    r_no, s_no = recall_at_1(queries, use_prefix=False)
    r_yes, s_yes = recall_at_1(queries, use_prefix=True)
    print("无前缀 recall@1:", r_no, "| top1 相似度:", s_no)
    print("有前缀 recall@1:", r_yes, "| top1 相似度:", s_yes)

    print("注意：无前缀时 top1 相似度依然接近 1.0，但选中的是相邻段落")
    print("  -> 相似度高 != 选对文档；阈值拦不住这种错，只有 recall 能")
    print("结论：query/passage 前缀必须配套；换前缀 = 重建索引，不能只改查询侧")
```

**追问一**：对称模型加前缀会怎样？
→ 解析：对称模型训练时两侧同分布，多出来的前缀 token 属于训练时没见过的输入，通常轻微掉点（1~3%），不会像非对称模型那样塌。但没必要加，加错反而引入噪声。

**追问二**：为什么改前缀必须重建索引？
→ 解析：索引里存的是"旧前缀下编码出的向量"，查询用新前缀得到的是另一个空间的向量，两者不可比。只改查询侧是最坏情况——索引和查询分别落在两个不同投影里，相似度排序基本随机。
