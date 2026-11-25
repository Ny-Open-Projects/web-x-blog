---
title: "[Q7732] 批量 embedding 返回顺序不保证：文档和向量张冠李戴"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7732 · 批量 embedding 返回顺序不保证：文档和向量张冠李戴

难度：P6 ｜ 标签：embedding、批量接口、index 字段、向量入库

基线：Python 3.12；OpenAI 兼容 `/embeddings` 的 `data[].index`；纯 Python 模拟乱序返回与校验。

**问**：一次把 256 个 chunk 丢给 embedding 接口（`input=[...]`），拿到 `data` 数组后直接 `zip(chunks, data)` 写进向量库。上线后发现搜"退款政策"返回的是"配送时效"的段落，抽查确认向量和文本错位。接口不是按输入顺序返回吗？

**答**：
- **结论**：接口返回的每个元素带 `index` 字段，**协议上不保证数组顺序等于输入顺序**——批量大时网关可能并发分片、供应商内部可能重排、部分实现按完成顺序返回。直接把 `data` 当有序列表是常见事故。正确做法是建 `{index: embedding}` 映射或按 `index` 排序，再按输入顺序取，并校验 `len(data) == len(input)`、index 集合恰为 `0..n-1`。
- **取舍**：按 index 重排是 O(n)、必须做；额外校验（数量、连续性、维度一致）能在写入前抓到"少一条/重一条"，比事后排查便宜几个数量级。批量大省 RTT，但多数供应商对单次 `input` 有上限（条数 / 总 token），超了会报错或静默截断。
- **实战**：① 统一 `sorted(data, key=lambda d: d["index"])` 后再 zip；② 断言 index 集合完整无重复；③ 校验每条向量维度等于索引配置（换模型时维度会变）；④ 向量 id 用 `chunk_id`，检索结果能反查原文；⑤ 抽样回检：用 chunk 原文当 query，top1 应命中自己。

```python
"""批量 embedding 乱序返回：按 index 重排 + 三道校验。"""


def fake_embed_api(texts: list[str], shuffle: bool = True) -> list[dict]:
    """模拟供应商：返回带 index 的乱序数组。"""
    out = [{"index": i, "embedding": [round(len(t) / 10, 3), float(i)]}
           for i, t in enumerate(texts)]
    if shuffle:
        out = out[2:] + out[:2]          # 假设网关把前两条挪到最后
    return out


def pack(chunks: list[str], data: list[dict], dim: int = 2) -> list[tuple[str, list[float]]]:
    if len(data) != len(chunks):
        raise ValueError(f"返回 {len(data)} 条，输入 {len(chunks)} 条")
    ids = [d["index"] for d in data]
    if sorted(ids) != list(range(len(chunks))):
        raise ValueError(f"index 集合不完整或有重复: {sorted(ids)[:10]}")
    if any(len(d["embedding"]) != dim for d in data):
        raise ValueError(f"维度不一致，期望 {dim}")

    ordered = sorted(data, key=lambda d: d["index"])
    return [(chunk, d["embedding"]) for chunk, d in zip(chunks, ordered)]


if __name__ == "__main__":
    chunks = ["退款政策说明", "配送时效说明", "发票开具流程", "会员权益"]

    raw = fake_embed_api(chunks)
    print("接口返回顺序的 index:", [d["index"] for d in raw])

    naive = list(zip(chunks, raw))        # 错误：直接 zip
    print("直接 zip:", [(t, d["index"]) for t, d in naive])
    print("  -> 第 1 段拿到了第 3 段的向量")

    fixed = pack(chunks, raw)
    print("按 index 重排:", [(t, v[1]) for t, v in fixed], "-> 顺序对齐")

    # 少一条
    try:
        pack(chunks, raw[:-1])
    except ValueError as e:
        print("数量校验:", e)

    # 维度不对
    try:
        pack(chunks, raw, dim=3)
    except ValueError as e:
        print("维度校验:", e)

    # 回检：用文本长度做"相似度"，top1 应该是自己
    probe = "退款政策说明"
    scores = sorted(fixed, key=lambda kv: abs(len(kv[0]) - len(probe)))
    print("回检 top1:", scores[0][0], "-> 与 query 一致")

    print("结论：data 的顺序不可信，index 才是契约；数量/连续性/维度三校验缺一不可")
```

**追问一**：为什么用 `chunk_id` 当向量 id 能防错位？
→ 解析：错位的本质是"文本-向量配对关系"丢失。id 来自文本（内容哈希或业务主键）时，检索结果带回 id 就能反查原文，错位会在回检时立刻暴露；更强的是把 id 与文本片段一起写进向量库的 payload，检索后校验一致性。

**追问二**：批量接口部分失败（部分 input 被拒）会怎样？
→ 解析：有的实现整批 400，有的返回少于 n 条且 index 不连续。必须校验数量与 index 完整性，缺失的单独重试；不能假设"返回几条就是前几条"——那正是错位的来源。
