---
title: [Q7684] embedding 模型升级向量维度不兼容事故复盘
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7684 · 换个 embedding 模型检索全废：维度不兼容事故复盘

难度：P6 ｜ 标签：事故复盘、embedding、向量库迁移
基线：text-embedding-3-small/large（1536/3072 维，支持 dimensions 参数）；pgvector / Qdrant。

**问**：为了省成本把 embedding 从 ada-002（1536 维）换成 text-embedding-3-small，同事以为维度相同直接切——上线后检索质量崩了：相似度分数全在 0.7-0.9 的"假高分"区间，top-k 全是错文档。同样的维度为什么不兼容？这次迁移正确的剧本是什么？

**答**：**结论**：向量的兼容性不是维度相等，而是**同一嵌入空间**：两个模型的向量语义坐标系完全不同——新模型的向量对旧向量算余弦相似度没有语义意义，会出现"什么都像"的假高分。而且不同模型的相似度分布（分数标定）也不同：旧模型 top1 通常 0.85，新模型 top1 可能只有 0.55，**阈值过滤的老配置直接误杀**。正确迁移剧本：① **双空间并行**——新集合/表另建（向量库支持多 collection 或加 namespace 列），双写两套向量；② **回填脚本**——按主键分批重嵌入全量文档（N 文档 × 单价 × 时长的容量账），回填期间新旧索引共存；③ **评测门禁**——检索评估集（命中率/MRR）跑分对比，新空间分数超过旧空间才切读；④ **切读+观察期**——读流量灰度切新空间，观察期后下线旧向量。

**取舍**：dimensions 截断参数（text-embedding-3 支持自定义维度）与换模型的取舍：截断省存储但 MRR 有损（实测约降 1-3%），适合规模巨大且精度余量足的场景。双写期间的成本是**双份 embedding 费用 + 双份存储**（pgvector 每空间 1536 维 ×4B×N 行），回填账要在评审时算清：千万级文档 × 单次 0.02 厘就是数千元与数小时墙钟。

**实战**：迁移账与假高分检测（标准库）：

```python
# embedding 换模型的迁移账：假高分检测 + 回填成本
import math, random

def cos(a, b):
    return sum(x*y for x, y in zip(a, b)) / (
        math.sqrt(sum(x*x for x in a)) * math.sqrt(sum(x*x for x in b)))

random.seed(42)
old_vec = [random.gauss(0, 1) for _ in range(8)]           # 旧模型向量(示意)
new_vecs = [[random.gauss(0, 1) for _ in range(8)]
            for _ in range(3)]                             # 新模型向量: 无关文档

scores = [cos(old_vec, v) for v in new_vecs]
print(f"旧向量 × 新模型向量 余弦: {[f'{s:.2f}' for s in scores]}")
print("跨空间相似度无语义 —— '假高分'来源\n")

# 分数标定差异：阈值必须随模型重标
calib = {"ada-002": {"top1_mean": 0.85, "threshold": 0.75},
         "te3-small": {"top1_mean": 0.55, "threshold": 0.40}}
print(f"ada-002 top1 均值 {calib['ada-002']['top1_mean']}，老阈值 0.75")
print(f"te3-small top1 均值 {calib['te3-small']['top1_mean']} -> "
      f"老阈值 0.75 会滤掉 {(1-calib['te3-small']['top1_mean']/0.85)*100:.0f}% 的正确结果\n")

# 回填账
DOCS, cost_per_doc, rate = 10_000_000, 0.00002, 3000   # 千万文档, 元/篇, 篇/分钟
backfill_yuan = DOCS * cost_per_doc
backfill_h = DOCS / rate / 60
dual_store_gb = DOCS * 1536 * 4 / 1e9
print(f"回填: {backfill_yuan:,.0f} 元 + {backfill_h:.0f}h 墙钟")
print(f"双空间存储峰值: {dual_store_gb:.0f} GB ×2 副本 -> 切换后释放一半")

# 切读门禁：评测集命中率对比
eval_hit = {"old": 0.91, "new": 0.93}
print("切读决策:", "放行" if eval_hit["new"] >= eval_hit["old"] else "回滚，继续回填")
```

**追问 1**：为什么余弦相似度对不同模型没有可比性？分数阈值重标的正确方法是什么？
提示：相似度分布由模型的训练目标决定（温度标定不同），正确做法是拿标注评测集跑新模型分数分布，按 P95 噪声/有效召回重定阈值，而不是沿用经验值。

**追问 2**：向量库层面的迁移（pgvector 单表 vs 多 collection）怎么选？
提示：加 namespace/version 列 + 查询过滤适合单库小规模；独立 collection（Qdrant）隔离更干净，切换与回滚都是指针操作——回滚成本是选型第一权重。

**追问 3**：回填过程中业务在写入新文档，怎么保证双空间最终一致？
提示：双写（应用层写两个索引）+ 回填队列处理存量 + 尾部对账（对比两边向量 count 与最新文档向量哈希）；期间新增 embedding 调用双份计费要计入迁移预算。

## 背诵要点
1. 向量兼容 = 同一嵌入空间，维度相等不代表兼容；跨空间余弦相似度无语义，产生"假高分"。
2. 迁移剧本：双空间并行 → 分批回填（千万文档≈数千元+数小时）→ 评测集门禁（命中率/MRR）→ 灰度切读 → 释放旧空间。
3. 分数阈值必须随模型重标：不同模型相似度标定不同（top1 均值 0.85 vs 0.55），老阈值直接误杀正确结果。

## 复盘追问
1. "以为维度相同就能直接切"这个假设为什么没有在评审时被挑战？embedding 模型变更现在有没有强制评测门禁？
2. 双写期间两边成本和一致性对账是怎么做的？切换观察期里有没有出现检索质量分区域劣化的情况？
