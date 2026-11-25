---
title: "[Q7735] 阈值写在反方向：cosine distance 越小越像，你却筛 > 0.8"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7735 · 阈值写在反方向：cosine distance 越小越像，你却筛 > 0.8

难度：P6 ｜ 标签：向量检索、cosine distance、metric、阈值标定

基线：Python 3.12；pgvector `<=>`（cosine distance）、`<#>`（负内积）；FAISS `IndexFlatIP`。

**问**：换了一个向量库。之前用 cosine similarity（越大越像）设 `score_threshold=0.8`，新库返回的是 cosine **distance**（越小越像），代码照抄 `if score > 0.8`，召回几乎为空；改成 `< 0.8` 后又把不相关的都放进来了。distance 和 similarity 到底怎么换算？

**答**：
- **结论**：cosine similarity ∈ [-1, 1]，越大越像；cosine distance = `1 - similarity` ∈ [0, 2]，越小越像。similarity 0.8 对应 distance 0.2，直接互换会差一个量级。不同库默认度量不同：pgvector `<=>` 是 cosine distance、`<#>` 是负内积；Milvus/Qdrant 用 `metric_type` 显式声明；FAISS `IndexFlatIP` 返回内积（越大越像）。**换库必须重标阈值**，不能平移。
- **取舍**：distance 与 ANN 索引的"升序取前 k"天然一致；similarity 更符合人的直觉。工程上统一在应用层转成 similarity（`sim = 1 - dist`）再判断，避免两套方向混用；向量归一化后内积等价 cosine，可省一次除法。
- **实战**：① 适配层暴露统一的 `similarity()`，内部按库的 metric 转换；② 阈值用固定标注集重标（正/负样本分布），不要拍脑袋；③ 单测断言"同一对向量在不同适配器上 similarity 相同"；④ 日志同时记录原始 score 与换算后的 similarity；⑤ 归一化入库，减少模长干扰。

```python
"""cosine similarity / distance 的换算与阈值方向事故。"""
import math


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


def cosine_distance(a: list[float], b: list[float]) -> float:
    return 1.0 - cosine_similarity(a, b)


class SimStore:
    """similarity 语义：越大越像，筛 >= threshold。"""

    def __init__(self, vectors: dict[str, list[float]]) -> None:
        self.vectors = vectors

    def search(self, q: list[float], threshold: float) -> list[tuple[str, float]]:
        scored = [(k, cosine_similarity(q, v)) for k, v in self.vectors.items()]
        return sorted([(k, s) for k, s in scored if s >= threshold],
                      key=lambda kv: -kv[1])


class DistStore:
    """distance 语义：越小越像，筛 <= threshold。"""

    def __init__(self, vectors: dict[str, list[float]]) -> None:
        self.vectors = vectors

    def search(self, q: list[float], threshold: float) -> list[tuple[str, float]]:
        scored = [(k, cosine_distance(q, v)) for k, v in self.vectors.items()]
        return sorted([(k, d) for k, d in scored if d <= threshold], key=lambda kv: kv[1])


if __name__ == "__main__":
    vectors = {
        "退款政策": [1.0, 0.0, 0.0],
        "退款时效": [0.9, 0.1, 0.0],
        "配送说明": [0.4, 0.9, 0.0],
        "发票流程": [-1.0, 0.0, 0.0],
    }
    q = [1.0, 0.0, 0.0]

    sim = SimStore(vectors)
    print("similarity >= 0.8:", sim.search(q, 0.8))

    dist = DistStore(vectors)
    print("distance <= 0.2 (正确):", dist.search(q, 0.2))

    # 事故：照抄 similarity 的 0.8 当 distance 阈值
    print("distance <= 0.8 (放宽):", dist.search(q, 0.8), "-> 不相关的也进来了")

    # 事故：方向写反
    wrong = [(k, cosine_distance(q, v)) for k, v in vectors.items()]
    print("distance > 0.8:", [kv for kv in wrong if kv[1] > 0.8], "-> 只剩最不相关的")

    # 阈值换算表
    for s in (0.9, 0.8, 0.7, 0.5):
        print(f"similarity {s} <-> distance {1 - s:.1f}")

    # 归一化后内积 = cosine
    def normalize(v: list[float]) -> list[float]:
        n = math.sqrt(sum(x * x for x in v))
        return [x / n for x in v]

    ip = sum(x * y for x, y in zip(normalize(q), normalize(vectors["退款时效"])))
    print("归一化内积:", round(ip, 6),
          "| cosine:", round(cosine_similarity(q, vectors["退款时效"]), 6))

    print("结论：换库必重标阈值；应用层统一用 similarity，别让两个方向共存")
```

**追问一**：为什么归一化之后内积等于 cosine？
→ 解析：`cos = (a·b) / (|a||b|)`，若 `|a| = |b| = 1` 则 `cos = a·b`。所以 embedding 先 L2 归一化再用内积索引，结果与 cosine 完全一致，还能省掉每次查询的除法；FAISS 的 `IndexFlatIP` + 归一化就是常用组合。

**追问二**：欧氏距离和 cosine 排序一定一致吗？
→ 解析：归一化向量下 `||a-b||² = 2 - 2·a·b`，与 cosine 单调对应，排序一致；**未归一化**时不一致——模长大的向量欧氏距离大，但方向可能高度相同。混用两个指标会出现"同一份数据两种 top-k"，排障时先确认向量是否归一化。
