---
title: [Q7504] rerank 成本分层与降级矩阵
date: 2026-11-18
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7504 · 混合检索后的 rerank 成本分层与降级矩阵

> 难度:★★★ | 标签:RAG, rerank, 成本

**问**：混合检索（BM25+向量+RRF 融合）后接 rerank，QPS 高时 rerank 模型费用和延迟都顶不住了。rerank 的成本怎么分层控制？哪些查询可以不 rerank？高峰降级的优先级怎么定？

**答**：结论：rerank 是"精度换钱"的最后一层，成本分层的本质是**按 query 难度和流量分桶，给不同桶配不同的 rerank 深度（候选数）与模型档位**。不是所有查询都需要 rerank：RRF 融合后 top-1 领先巨大（向量与 BM25 一致）的高置信查询跳过 rerank 直接透传；模糊/多意图/零结果查询才进重 rerank。降级优先级从轻到重：缩候选数（50→20）→ 换轻量 reranker → 跳过 rerank 仅保留融合排序 → 只走向量单路。

分层设计与实战：
- 分桶判据（在线可算的廉价信号）：融合分数 margin（top1 与 top2 差）、query 长度与意图分类、历史零点击率。margin > 0.3 的查询约占 40% 流量，跳 rerank 后端到端质量几乎无损——这是最大的省钱点。
- 成本结构：rerank 费用 ∝ 候选数 × query 数；候选从 50 砍到 20，费用降 60% 而 recall@5 通常只掉 1~2 个点，这条曲线必须实测自家数据，别抄别人的。
- 事故复盘：大促流量峰值 reranker 排队 2 秒，P99 爆炸。修复：按并发水位自动降档（水位 > 70% 缩候选，> 85% 轻量模型，> 95% 跳 rerank），并给 rerank 调用加 300ms 预算超时——超时即走融合排序兜底。峰值 P99 从 2.1s 回到 450ms，答案质量抽样 diff < 3%。

```python
# 基线:Python 3.9+ 标准库;rerank 分层决策器 + 水位降级(可运行)
def need_rerank(margin: float, q_len: int, zero_click_rate: float) -> tuple[bool, str]:
    """按置信信号决定是否 rerank 与档位。"""
    if margin > 0.3:
        return False, "skip"                 # 高置信:跳过 rerank
    if zero_click_rate > 0.4 or q_len > 40:
        return True, "heavy"                 # 难查询:重 rerank
    return True, "light"

def pick_depth(tier: str, water_level: float) -> int:
    """按服务水位缩候选数:降级矩阵。"""
    base = {"skip": 0, "light": 20, "heavy": 50}[tier]
    if water_level > 0.95:
        return 0                             # 最终兜底:跳 rerank
    if water_level > 0.85:
        return base // 2 or 0
    if water_level > 0.70:
        return max(base // 2, 10)
    return base

if __name__ == "__main__":
    tier, _ = need_rerank(margin=0.05, q_len=12, zero_click_rate=0.1)
    print(tier, pick_depth(tier, 0.5), pick_depth(tier, 0.9))
```

**追问**：
- 一层追问：RRF 融合的权重（k=60）需要调吗？——RRF 本身对分数尺度不敏感（用排名不用分值），k 影响头部排名的平滑度，一般不动；要调的是"各路召回的条数配比"（向量 30 条 + BM25 30 条）与"是否按路加权"，这些靠离线 eval 网格搜索。
- 二层追问：rerank 超时兜底用什么排序？——RRF 融合分数直接排序（已有、零成本），绝不用原始向量分数兜底（两路分数量纲不同）；兜底命中要打点统计占比，占比持续 > 5% 说明容量规划有问题。
- 三层追问：怎么验证"跳 rerank"没有伤质量？——分流实验：跳过组与 rerank 组按 query 分桶对比答案正确率与用户反馈；注意分桶要按难度分层（简单题跳过无感、难题跳过掉分），整体均值会掩盖局部退化。
