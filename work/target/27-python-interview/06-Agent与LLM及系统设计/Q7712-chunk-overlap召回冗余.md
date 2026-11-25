---
title: "[Q7712] chunk overlap 的召回冗余：同一段话挤掉三个名额"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7712 · chunk overlap 的召回冗余：同一段话挤掉三个名额

难度：P6 ｜ 标签：RAG、分块、overlap、召回冗余

基线：Python 3.12；纯 Python 模拟分块重叠与 top-k 去重。

**问**：RAG 分块用了 20% overlap，top-k=5。用户问"退款到账时间"，召回结果里有 4 条都来自同一份文档的相邻块，内容大段重复，真正讲"跨境退款"的另一篇文档被挤到第 6 名没进 prompt。overlap 不是为了不切断语义吗，怎么反而降低了召回质量？

**答**：
- **结论**：overlap 让相邻块共享一段文本，作用是避免关键句被切在边界。但它同时制造了**高度相似的块**：同一文档的相邻块在向量空间里非常接近，检索时容易一起命中，把 top-k 名额占满。结果不是"召回更多信息"，而是"同一信息重复 N 次"，prompt token 浪费、覆盖度下降，还会让模型过度相信重复出现的片段。
- **取舍**：overlap 要小到能保护边界、大到不制造冗余，常见 10%-20%；更有效的治理是**检索后去重/多样性控制**：按文档 ID 或父子块聚合（同一父块只保留得分最高的子块）、MMR（最大边际相关性）在相关性与多样性间折中、按来源配额限制单文档占比。代价是可能丢掉同文档内另一段真正有用的细节。
- **实战**：① 记录每次召回的 `doc_id/parent_id`，统计单文档占比与重复率；② 用父子块索引：子块检索、父块入 prompt，天然去重；③ top-k 扩大后再重排+去重，比直接 top-5 更稳；④ 评估指标除了命中率，加"唯一信息来源数"和"prompt 冗余率"。

```python
def chunk_tokens(tokens: list[str], size: int, overlap: int) -> list[list[str]]:
    step = size - overlap
    return [tokens[i:i + size] for i in range(0, len(tokens) - overlap, step)]


def retrieve(chunks: list[dict], query: str, k: int) -> list[dict]:
    scored = sorted(chunks, key=lambda c: -sum(w == query for w in c["tokens"]))
    return scored[:k]


if __name__ == "__main__":
    doc = "退款 到账 时间 取决于 支付 渠道 跨境 退款 通常 七 个 工作日".split()
    chunks = [{"id": f"d1#{i}", "doc": "d1", "tokens": t}
              for i, t in enumerate(chunk_tokens(doc, 6, 2))]
    chunks += [{"id": "d2#0", "doc": "d2", "tokens": ["跨境", "退款", "需要", "额外", "审核"]}]
    top = retrieve(chunks, "跨境", 3)
    print("top3:", [c["id"] for c in top])
    print("唯一文档数:", len({c["doc"] for c in top}))
    # 按文档去重，保留每篇最高分块
    seen, diverse = set(), []
    for c in sorted(chunks, key=lambda c: -sum(w == "跨境" for w in c["tokens"])):
        if c["doc"] not in seen:
            seen.add(c["doc"])
            diverse.append(c["id"])
    print("按文档去重后:", diverse[:3])
```

**追问一**：为什么"扩大 top-k 再去重"比"直接减小 overlap"更有效？
→ 解析：减小 overlap 会削弱边界保护，可能把关键句切断；扩大候选集再按文档去重，既保留了 overlap 的边界收益，又保证最终 prompt 覆盖多个来源。代价是检索与重排成本上升，需要候选集大小与延迟的平衡。

**追问二**：MMR 去重和按文档去重有什么区别？
→ 解析：按文档去重是硬规则（同一文档只留一条），简单但可能丢掉同文档的另一段关键信息；MMR 按"与已选结果的相似度"做软惩罚，允许同文档多条但降低重复，粒度更细、计算更贵。选择取决于文档内信息密度与延迟预算。
