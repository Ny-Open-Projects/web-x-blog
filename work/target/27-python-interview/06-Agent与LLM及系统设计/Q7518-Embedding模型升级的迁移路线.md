---
title: [Q7518] Embedding 模型升级的迁移路线：双写-回填-切换
date: 2026-11-19
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7518 · Embedding 模型升级迁移

> 难度:★★★ | 标签:向量库, Embedding, 迁移

**问**：向量库里的 embedding 要从模型 A 换到模型 B（维度都不同，768→1024）——为什么「原地更新」不可行？双集合（新旧并存）迁移怎么走，切换时的「召回对比验证」（A/B 回放查询对比）怎么设计，回填期间新写入的文档走哪套？

**答**：① 原地不可行的三个原因：不同模型的向量**不在同一语义空间**（A 的查询向量 vs B 的文档向量余弦全是噪声）、维度不同物理上混存不了、回填百万级文档期间「一部分 A 一部分 B」的库检索结果混乱——**必须新旧两集合并存**。② 迁移四步：建新集合（B 模型，1024 维）→ **双写**（新文档同时写 A/B 两集合，保证切换时无缺口）→ **回填**（历史文档批量重 embed，按 id 分片 + 水位断点，Q6515/Q7017 同构）→ **对比验证后切换**。③ 召回对比：用真实查询回放集（生产采样 100-500 条查询 + 人工标注相关文档集），分别在新旧集合检索，对比 Recall@10 与 MRR——**B 必须显著不劣于 A 才切换**（模型升级不是想当然）。④ 切换方式：应用层路由开关（灰度：10% 查询走 B → 对比在线指标 → 全量），旧集合保留一个观察期（回滚用）后清理。

```python
# 全部标准库；demo 模拟双集合回填 + 召回对比（Recall@10 计算）
import hashlib, random

def fake_embed(model: str, text: str) -> list[float]:
    """确定性伪 embedding：同模型同文本同向量（哈希派生，演示用）。"""
    dim = 768 if model == "A" else 1024
    h = hashlib.sha256(f"{model}:{text}".encode()).digest()
    return [b / 255 for b in (h * ((dim // 32) + 1))[:dim]]

def cosine(a, b) -> float:
    return sum(x * y for x, y in zip(a, b)) / (
        (sum(x * x for x in a) ** 0.5) * (sum(y * y for y in b) ** 0.5) or 1)

class VectorStore:
    def __init__(self, model: str):
        self.model, self.vecs = model, {}
    def upsert(self, doc_id: str, text: str):
        self.vecs[doc_id] = fake_embed(self.model, text)
    def search(self, query: str, k: int = 10) -> list[str]:
        q = fake_embed(self.model, query)
        scored = [(cosine(q, v), d) for d, v in self.vecs.items()]
        return [d for _, d in sorted(scored, reverse=True)[:k]]

def dual_write(old: VectorStore, new: VectorStore, doc_id: str, text: str):
    old.upsert(doc_id, text); new.upsert(doc_id, text)      # 双写：切换期无缺口

def recall_at_k(retrieved: list[str], relevant: set[str], k: int = 10) -> float:
    return len(set(retrieved[:k]) & relevant) / len(relevant)

def compare(models: tuple[VectorStore, VectorStore], queries: list[tuple[str, set[str]]]) -> dict:
    """A/B 回放对比：B 不显著劣于 A 才切换。"""
    r = {}
    for name, store in zip(("old", "new"), models):
        r[name] = sum(recall_at_k(store.search(q), rel) for q, rel in queries) / len(queries)
    return r | {"verdict": "GO" if r["new"] >= r["old"] else "NO-GO"}

if __name__ == "__main__":
    random.seed(1)
    old, new = VectorStore("A"), VectorStore("B")
    docs = [f"doc-{i}: python {'gil' if i % 3 else 'asyncio'} 深度解析" for i in range(50)]
    for i, d in enumerate(docs):                # 阶段1：双写新文档
        dual_write(old, new, f"d{i}", d)
    # 阶段2：历史回填（直接 upsert 到 new；生产按 id 分片+水位断点）
    assert len(new.vecs) == len(old.vecs) == 50
    queries = [(f"python gil 原理", {"d0", "d3", "d6"}),
               ("asyncio 并发", {"d1", "d4"})]
    result = compare((old, new), queries)
    print({k: (round(v, 3) if isinstance(v, float) else v) for k, v in result.items()})
    # 灰度切换：应用路由 10% 查询走 new → 在线指标（点击率/人工反馈）无回退 → 全量 →
    # 旧集合保留观察期（回滚保险）后清理；回填失败分片重试（幂等 upsert）。
```

**追问**：1) 回填的embedding成本怎么算与控速？——百万文档 × 单价/延迟（批量 API 通常 5-10× 折扣）；限速按上游 API 配额（Q5518 三闸门），分片水位断点（中断续跑），重复跑幂等（同文本同向量）。2) 为什么要「双写」而不只是「切换后补写」？——切换时刻起的新文档如果只写新集合，观察期内回滚到 A 就丢这些文档的向量——双写保证任意时刻回滚都不缺数据。3) 维度相同也不混存？——是：即使 768→768，语义空间不同（几何方向意义不同），混存检索是垃圾结果；集合按「模型版本」命名（`docs_a_v1`/`docs_b_v2`）是运维纪律。

## 背诵要点
1. 换 embedding 模型必须双集合并存：语义空间不兼容、维度可能不同、回填期混存不可检索。
2. 迁移四步：双写（无缺口可回滚）→ 分片回填（水位断点+限速）→ 召回对比（Recall@10 回放集）→ 灰度切换。
3. 对比验证「B ≥ A 才 GO」；旧集合留观察期后清理；回填幂等（同文本同向量）。

## 复盘追问
1. 回放集的「相关文档标注」从哪来？（提示：生产点击/引用日志（隐式反馈）+ 人工抽样标注子集；没有标注就先做「查询分布回放对比 top-k 重合度」作为弱信号）
2. 上线后发现 B 在某类长尾查询上明显劣于 A，但整体 Recall 更高，切不切？（提示：分切片段化路由（长尾类走 A、主类走 B）成本高；先看该类查询占比与业务价值——数据说话，必要时按类灰度）
