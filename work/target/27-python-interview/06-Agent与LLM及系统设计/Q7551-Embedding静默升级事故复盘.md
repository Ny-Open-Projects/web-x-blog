---
title: [Q7551] Embedding 服务静默升级的事故复盘
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7551 · Embedding 服务静默升级的事故复盘

难度：P6 | 标签：RAG、Embedding、向量空间、事故复盘

**问**：某天上午 RAG 召回质量突然崩了——检索回来的文档全不对，但 embedding 接口全程 200 正常、无任何报错。供应商"静默升级"了向量模型意味着什么？这类事故怎么发现、怎么止损？

**答**：
- **结论**：embedding 模型换了，向量空间就换了——同一个文本的向量完全不同，跨空间的余弦相似度接近随机。事故形态是"索引还是旧模型向量、查询侧已经用新模型"，匹配全部失真，且没有任何报错信号。发现靠黄金集回归：固定一组"问题→期望命中文档"，每次查询侧配置变更后跑 top-1 召回率（本例从 0.88 跌到 0.12）。止损靠版本钉死：向量元数据里记录 model_version，查询侧校验不一致即拒绝服务并告警——宁可拒绝也不输出错误答案。
- **取舍**：召回质量监控有两个候选：线上用户行为信号（点击率）与离线黄金集。前者滞后且混入业务因素，后者能在接入层当天报警——两者都要，但黄金集是唯一的"分钟级发现"手段。版本钉死会牺牲供应商的"无缝升级"能力，换来的正是确定性：升级必须走双索引迁移预案（旧索引服务旧查询向量，新索引灰度验证后再切换）。
- **实战**：落地清单：① 向量库每条记录存 model_name+version；② 黄金集进 CI/定时巡检（每天一次，配置变更必跑）；③ embedding 客户端显式传 model 版本参数并禁止默认值；④ 供应商换模型走"双写-回填-灰度切换"迁移，和数据库换主键策略同等级的变更管理。

```python
"""Embedding 服务静默升级事故：召回突降的发现（黄金集回归）与止损（版本钉死）。"""
import hashlib
import math

def embed(text: str, salt: str = "v1", dim: int = 64) -> list[float]:
    """字符二元组哈希模拟 embedding；salt 变化 = 供应商换了模型（向量空间变了）。"""
    v = [0.0] * dim
    for i in range(len(text) - 1):
        h = int(hashlib.md5((salt + text[i:i + 2]).encode()).hexdigest(), 16)
        v[h % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]

def cos(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))

DOCS = {
    "doc_return": "七天无理由退货政策说明",
    "doc_invoice": "发票抬头与开票流程",
    "doc_ship": "物流配送范围与时效",
    "doc_account": "账号密码找回方法",
    "doc_pay": "支付方式与限额说明",
    "doc_refund": "退款到账周期说明",
    "doc_coupon": "优惠券使用规则",
    "doc_member": "会员等级权益表",
}
GOLDEN = [("退货政策", "doc_return"), ("开票流程", "doc_invoice"),
          ("配送时效", "doc_ship"), ("密码找回", "doc_account"),
          ("支付限额", "doc_pay"), ("退款到账", "doc_refund"),
          ("优惠券规则", "doc_coupon"), ("会员权益", "doc_member")]

def top1_recall(index: dict, embed_fn) -> float:
    hits = 0
    for q, expected in GOLDEN:
        qv = embed_fn(q)
        best = max(index, key=lambda d: cos(qv, index[d]))
        hits += best == expected
    return hits / len(GOLDEN)

# 索引用 v1 模型构建
index = {d: embed(text, "v1") for d, text in DOCS.items()}
print(f"黄金集 top-1 召回 = {top1_recall(index, lambda t: embed(t, 'v1')):.2f}（同空间，正常）")

# 供应商静默把模型换成 v2：索引还是 v1 向量，查询侧却产出 v2 向量
print(f"静默升级后 top-1 召回 = {top1_recall(index, lambda t: embed(t, 'v2')):.2f}"
      f"（跨空间匹配近似随机；接口 200 正常返回——只有黄金集回归能发现）")

# 止损：向量库记录 model_version，查询侧校验版本一致
vec_meta = {d: {"vec": embed(text, "v1"), "model": "emb-v1"} for d, text in DOCS.items()}
query_model = "emb-v2"
mismatch = any(m["model"] != query_model for m in vec_meta.values())
print(f"版本一致性校验：{'发现索引模型 emb-v1 != 查询模型 emb-v2，拒绝服务并告警' if mismatch else '一致'}")
print("纪律：embedding 模型名必须钉进向量元数据；换模型 = 重建索引的迁移预案，不是换参数")
```

**追问链**：
1. 追问一层：为什么"接口返回 200 且向量维度没变"让事故更隐蔽？——维度不变意味着下游解析不报错、链路指标全绿；坏的是语义不是结构。教训是"语义质量的监控不能依赖结构性校验"，黄金集这类行为断言才是语义层的探针。
2. 追问二层：双索引迁移期间，新写入的文档该进哪个索引？——双写（两个索引同时进），查询走旧索引（当前版本一致的那个）；新索引用新模型回填全量历史后，黄金集在新索引上验证通过再切查询侧，最后下线旧索引。顺序反了（先切查询再回填）就会出现本事故。

**背诵要点**：
1. 换 embedding 模型 = 换向量空间：跨空间相似度近似随机，无报错、全 200。
2. 发现靠黄金集回归（固定问题→期望文档的 top-1 召回），止损靠向量元数据版本校验。
3. 模型升级走双索引迁移：双写→回填→黄金集验证→切查询→下线旧索引。

**复盘追问**：
1. 事故当天怎么先恢复业务？（查询侧钉回旧模型版本——供应商保留旧模型 endpoint 的前提下，召回立即恢复；若供应商已下线旧模型，只能提示降级并加速重建索引）
2. 为什么黄金集要覆盖每个业务线的主要意图类别？（embedding 漂移对不同类别的影响不均匀；全集召回可能只跌 5%，但某类别从 0.9 跌到 0.2——分桶看召回才能定位爆炸半径）
