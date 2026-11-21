---
title: [Q7599] embedding 模型升级向量空间不兼容事故复盘
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7599 · embedding 模型升级后向量空间不兼容事故复盘

难度：P7 ｜ 标签：RAG / embedding / 事故复盘 / 版本演进

**问**：为了提升检索质量，团队把 embedding 模型从 text-embedding-ada-002 换成新一代模型，只重刷了部分数据的向量（灰度几天），之后检索质量大幅回退、还有命中文本驴唇不对马嘴的案例。为什么会这样？正确的升级姿势是什么？

**答**：
- **结论**：不同模型（甚至同模型不同版本）的向量空间互不兼容——维度可以不同（1536 vs 3072），维度相同语义也完全不同。库里新旧向量混存时，查询向量（新模型）与旧向量计算余弦相似度是"两套坐标系的点积"，结果数值上仍能算、排序却无意义，检索退化成近似随机。更隐蔽的是降维后维度恰好相同时，系统不报错、质量静默劣化，等用户投诉才发现。唯一安全规则：**一次模型升级 = 一次全量重建**，库中同一时刻只允许存在一个向量空间；并存过渡期靠"双集合/双索引"而不是混写。
- **取舍**：全量重建的成本与策略：千万级向量重建 = embedding 计算费 + 索引构建时长 + 切换窗口。策略选择：① 双索引影子期——新索引全量建好、用固定评测集对比召回指标，达标后流量一刀切（简单、双份存储成本）；② 按 partition 逐批切换——复杂且过渡期跨 partition 检索依然不兼容，只在业务能按分区隔离查询时可行。评测先行：没有固定的检索评测集（query + 期望命中）就不要做模型升级，"感觉更好"不是验收标准。
- **实战**：事故剧本：① 判定事故：评测集对新旧库分别打分，混存库分数显著低于两者纯库；② 恢复：切回旧模型查询路径（旧向量仍在库里但被新向量污染——若混写只能按写入时间过滤或重建旧索引），新模型走全新集合；③ 规范化：给每条向量记录 `embedding_model` 元数据 + collection 级强制单模型校验，写入侧拒绝与集合模型不符的向量；④ 复盘项：把"模型升级 checklist"（评测集基线 → 全量重建 → 影子对比 → 一刀切 → 旧索引保留 2 周可回滚）固化为流程。

```python
# 向量空间兼容性校验与双集合切换模拟（纯标准库）
# 基线：Python 3.9+

import math


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb)


class VectorStore:
    """collection 级单模型校验：写入即拒绝跨空间向量"""

    def __init__(self, name: str, model: str) -> None:
        self.name, self.model = name, model
        self.items: list[tuple[str, tuple[float, ...]]] = []

    def upsert(self, model: str, key: str, vec: tuple[float, ...]) -> None:
        if model != self.model:
            raise ValueError(
                f"collection '{self.name}' 绑定 {self.model}，"
                f"拒绝写入 {model} 向量（维度也不校验混淆）"
            )
        self.items.append((key, vec))

    def search(self, model: str, q: tuple[float, ...], k: int = 1) -> list[str]:
        assert model == self.model
        ranked = sorted(self.items,
                        key=lambda kv: -cosine(q, kv[1]))
        return [key for key, _ in ranked[:k]]


def main() -> None:
    old = VectorStore("docs", "ada-002")
    new = VectorStore("docs_v2", "new-emb")
    # 旧空间向量
    v_old = (1.0, 0.0, 0.0)
    old.upsert("ada-002", "doc1", v_old)
    # 新空间向量：语义上 doc2 应最相似于查询，但坐标完全独立
    v_new_doc1, v_new_doc2, q_new = (0.0, 1.0, 0.0), (0.9, 0.1, 0.0), (1.0, 0.05, 0.0)
    new.upsert("new-emb", "doc1", v_new_doc1)
    new.upsert("new-emb", "doc2", v_new_doc2)
    assert new.search("new-emb", q_new) == ["doc2"]
    # 混写被拒绝：事故根因被封死
    try:
        old.upsert("new-emb", "doc2", v_new_doc2)
        raise AssertionError("should reject")
    except ValueError as e:
        print("拒绝混写:", e)
    # 跨空间相似度数值上可算但语义无意义（演示数值）
    print("跨空间余弦(无意义):", round(cosine(q_new, v_old), 3))
    print("OK")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么"维度相同"反而是更危险的情况？
→ 一句话提示：维度不同时向量库直接报错，逼你处理；维度相同时（如多个模型都用 1536）混存静默通过，相似度计算全部执行但语义崩坏，劣化要靠评测集才能发现。

**追问 2**：embedding 模型升级后要不要重训下游（reranker/分类器）？
→ 一句话提示：要——以 embedding 为输入的下游模型学到的是旧坐标系的几何关系，向量空间换了它们同样失效；升级 checklist 必须枚举所有 embedding 消费者，不只是向量库。

## 背诵要点
- 不同模型的向量空间互不兼容，余弦数值可算但语义无意义；一次升级 = 一次全量重建，库内单模型强制校验。
- 安全姿势：双集合影子期 + 固定评测集对比 + 达标后一刀切 + 旧索引保留 2 周可回滚；无评测集不做升级。
- 向量元数据记录 embedding_model；升级 checklist 要枚举全部 embedding 消费者（reranker/分类器同样失效）。

## 复盘追问
- 为什么"灰度几天、只重刷部分数据"注定失败？提示：灰度切的是查询模型而不是向量空间，新旧向量在同一库里被同一查询比较，灰度比例越大污染越均匀、劣化越隐蔽；灰度只能发生在双集合层。
- 增量写入在重建期怎么处理？提示：重建窗口内新数据要双写（新旧模型各算一次向量），否则切换瞬间有数据缺口；双写成本要计入升级预算。
