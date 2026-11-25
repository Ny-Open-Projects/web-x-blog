---
title: [Q7616] pgvector 半精度（halfvec）与稀疏向量演进及迁移
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7616 · pgvector 0.7+ 的 halfvec/稀疏向量演进与存量迁移

难度：P7 ｜ 标签：版本演进 / pgvector / 向量库

**问**：知识库用 pgvector 0.5 的 `vector(1536)` + HNSW 跑了一年，库涨到 8000 万条，内存告警。pgvector 0.7 引入了 halfvec（半精度）与 sparsevec，升级能省多少？存量数据怎么迁？和直接换专用向量库（Qdrant/Milvus）比怎么决策？

**答**：
- **结论**：halfvec 用 fp16 存向量，**存储与 KV/索引内存直接减半**（HNSW 索引在内存里是主要开销，8000 万条 × 1536 维 fp32 ≈ 470GB 原始向量，索引+表常压垮实例），精度损失在检索场景通常可忽略（recall@10 掉 <1%，需实测对拍）；sparsevec 则为"稠密+稀疏混合检索"（BM25 式词权 + 向量语义）打开通路，0.7 还支持稀疏 HNSW 与迭代扫描。0.8/1.0 继续补齐迭代式扫描（解决过滤器过滤后无结果返回过少的问题，呼应 Q7588 的元数据过滤坑）。迁移路径关键约束：**类型变化是 schema 变更**——`vector → halfvec` 列要新列回填或重建表，HNSW 索引重建时长随库大小线性（千万级小时级），要走"新列 + 双写 + 回填 + 切读"的在线流程（呼应 Q6573/Q1410 套路）。
- **取舍**：决策矩阵：① **留在 PG**（halfvec）：检索规模 <亿级、过滤/事务/权限要与业务表强 join、团队只有 PG 运维能力——halfvec + 分区基本够用，成本最低；② **换专用向量库**：规模上亿 + QPS 高 + 需要丰富过滤 DSL/多租户原生隔离 + 向量是核心业务（而非业务的一个特性）——Qdrant/Milvus 的量化（标量/二值）、分片、副本是成熟件，代价是新运维栈与数据同步链路；③ **混合**：PG 存元数据与关系、专用库只做向量检索，ID 关联——工程上最常见但引入双写一致性。先做账：halfvec 升级的成本是"一次迁移 + 代码兼容"，专用库的成本是"常驻新基础设施 + 同步管道"，亿级以下前者几乎总是赢。
- **实战**：迁移剧本：① 升级扩展（`ALTER EXTENSION pgvector UPDATE`，检查 PG 版本兼容）并加 `halfvec` 新列；② 双写期：新写入同时填两列；③ 批量回填存量（按主键分段 UPDATE + 限速，防 WAL 峰值，见 Q6580）；④ 建 HNSW 索引（`halfvec_ops`，注意 m/ef_construction 与 fp16 的参数复测）；⑤ 召回对拍：同一评测集跑新旧列的 recall@k 与延迟，达标后切读、删旧列；⑥ 复盘项：索引内存水位重新计账（fp16 后应降 50%），监控迭代扫描是否启用。

```python
# halfvec 迁移收益账与在线迁移编排（标准库模拟）
# 基线：Python 3.9+；真实实现 pgvector 0.7+（psycopg3 + CREATE EXTENSION vector）

from dataclasses import dataclass


@dataclass
class VectorStore:
    rows: int
    dims: int
    dtype_bytes: int            # 4=fp32(vector), 2=fp16(halfvec)
    hnsw_overhead: float = 1.6  # HNSW 索引内存相对原始向量的倍数（实测口径）

    def memory_gb(self) -> float:
        raw = self.rows * self.dims * self.dtype_bytes
        return raw * self.hnsw_overhead / 1024**3


def migration_plan(rows: int, mem_budget_gb: float) -> dict[str, str]:
    fp32 = VectorStore(rows, 1536, 4)
    fp16 = VectorStore(rows, 1536, 2)
    plan = {
        "before_fp32_gb": f"{fp32.memory_gb():.0f}",
        "after_fp16_gb": f"{fp16.memory_gb():.0f}",
    }
    if fp16.memory_gb() <= mem_budget_gb < fp32.memory_gb():
        plan["decision"] = "halfvec 迁移即可达标，不换库"
    elif fp16.memory_gb() > mem_budget_gb:
        plan["decision"] = "halfvec 不够：分区拆实例或评估专用向量库"
    else:
        plan["decision"] = "内存本就达标，迁移非紧迫（按需）"
    return plan


def online_steps() -> list[str]:
    return ["加 halfvec 新列", "双写", "分段限速回填", "建 HNSW(halfvec_ops)",
            "召回对拍(recall@k/延迟)", "切读", "删旧列"]


def main() -> None:
    plan = migration_plan(rows=80_000_000, mem_budget_gb=500)
    print(f"fp32: {plan['before_fp32_gb']}GB → fp16: {plan['after_fp16_gb']}GB（减半）")
    assert float(plan["after_fp16_gb"]) < float(plan["before_fp32_gb"]) * 0.55
    assert plan["decision"] == "halfvec 迁移即可达标，不换库"
    steps = online_steps()
    assert steps.index("双写") < steps.index("切读"), "在线迁移必须先双写后切读"
    for s in steps:
        print("  -", s)
    print("OK: halfvec 内存减半的收益账 + 双写回填切读的在线迁移顺序")


if __name__ == "__main__":
    main()
```

**追问 1**：halfvec 的精度损失主要来自哪，怎么验证可接受？
→ 一句话提示：fp16 只影响数值精度（尾数位少）不影响指数动态范围，检索用距离排序对量化误差相对鲁棒；验证靠同一评测集的 recall@k 对拍 + 人工抽检 badcase，而不是只看平均召回。

**追问 2**：`vector(1536)` 固定维度类型在 Embedding 模型换型时为什么变成枷锁？
→ 一句话提示：维度写死在类型与索引里，换模型（维度变了）要整列重建（呼应 Q7599 空间不兼容）；halfvec 无固定维度用法（`halfvec` 无维度或运行期指定）给了缓冲，但语义对齐仍要重灌——选型时就把"未来换模型"写进容量与迁移预案。

## 背诵要点
- halfvec fp16 存储与 HNSW 内存减半，召回损失通常 <1% 但必须实测对拍；sparsevec 支撑稠密+稀疏混合检索。
- 迁移是 schema 变更：新列→双写→限速回填→halfvec_ops 索引重建→对拍→切读→删旧列；索引重建千万级是小时级任务。
- 决策账：亿级以下 halfvec 几乎必赢；上亿+高 QPS+多租户过滤需求才评估专用向量库，混合架构要背双写一致性。

## 复盘追问
- 为什么 HNSW 索引内存是主要开销而不是原始向量？提示：HNSW 每个节点要存多层邻居表（m 个邻居 × 层级指针），指针开销叠加使索引 ≈ 1.5-2× 原始向量；所以量化（fp16/标量量化）与降维（matryoshka embedding 截断）都是直接作用于索引内存的杠杆。
- 迭代扫描（iterative index scan）解决什么问题？提示：带过滤条件的 ANN 检索在过滤命中稀疏时会"取满 ef 个候选却大多被过滤掉"返回过少；迭代扫描继续深入索引直到凑够 k 条，是过滤场景正确性的关键演进（呼应 Q7588）。
