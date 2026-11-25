---
title: "[Q7726] 批量 upsert 部分失败：200 响应里藏着 3 条错误"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7726 · 批量 upsert 部分失败：200 响应里藏着 3 条错误

难度：P6 ｜ 标签：向量库、批量写入、部分失败、幂等

基线：Python 3.12；Milvus/Qdrant/pgvector 批量 upsert；纯 Python 模拟逐条校验。

**问**：每晚把 10 万条 chunk 批量 upsert 到向量库，接口返回 HTTP 200，任务显示成功。第二天检索发现少了一批文档，回查响应体里有个 `errors` 数组，37 条因维度不一致被拒。为什么 200 还会有失败？重试整批会不会把已成功的写重？怎么做才能既补齐又不重复？

**答**：
- **结论**：批量写接口常是**部分成功**语义：服务端逐条/逐分片处理，成功的已落库，失败的收集到 `errors` 返回，HTTP 仍是 200（请求本身被接受）。只判状态码会把"部分失败"当成功。向量库通常按主键 upsert，**同一 id 重复写是幂等的**（覆盖），所以重试整批不会产生重复行，但会重复计算/计费、放大写入压力，且如果主键不是业务 id（而是自动生成），重试就会插重复。
- **取舍**：整批重试简单，依赖 upsert 幂等；逐条重试精准但 RPC 次数多。更好的做法是：客户端预校验（维度、类型、主键非空）把大部分错误挡在发送前；发送后解析 `errors`，只重试失败项；主键用**业务唯一 id**，保证重试幂等。对"部分成功"不要用事务思维要求全有全无，向量库很少提供跨分片事务。
- **实战**：① 响应必须解析 `errors`/`failed` 字段，按条记录失败原因；② 主键用确定性 id（如 `doc_id#chunk_no`），不要用随机 uuid；③ 重试前做指数退避，超过 N 次进死信队列人工处理；④ 写完做一次 `count` + 抽样 `retrieve` 对账，别只看接口返回。

```python
"""批量 upsert 的部分失败、幂等重试与对账。"""
from dataclasses import dataclass


@dataclass
class Item:
    id: str
    vector: list[float]


class VectorStore:
    def __init__(self, dim: int) -> None:
        self.dim = dim
        self.data: dict[str, list[float]] = {}

    def upsert_batch(self, items: list[Item]) -> dict:
        ok, errors = 0, []
        for it in items:
            if len(it.vector) != self.dim:
                errors.append({"id": it.id,
                               "reason": f"dim {len(it.vector)} != {self.dim}"})
                continue
            self.data[it.id] = it.vector      # 按 id 覆盖 = 幂等
            ok += 1
        return {"status": 200, "ok": ok, "errors": errors}


if __name__ == "__main__":
    store = VectorStore(dim=3)
    batch = [Item(f"doc{i}", [0.1, 0.2, 0.3]) for i in range(10)]
    batch[3] = Item("doc3", [0.1, 0.2])        # 维度错
    batch[7] = Item("doc7", [0.1, 0.2, 0.3, 0.4])

    resp = store.upsert_batch(batch)
    print("第一次:", resp["status"], "成功", resp["ok"], "错误", resp["errors"])
    print("库里条数:", len(store.data), "-> 200 不代表全成功")

    # 只重试失败项（修正后）
    retry = [Item("doc3", [0.1, 0.2, 0.3]), Item("doc7", [0.1, 0.2, 0.3])]
    print("重试:", store.upsert_batch(retry))
    print("重试后条数:", len(store.data))

    # 整批重试也不会重复（按 id 覆盖）
    store.upsert_batch(batch[:3])
    print("整批重试后条数:", len(store.data), "-> 主键幂等")
```

**追问一**：为什么向量库很难提供"整批原子成功/失败"？
→ 解析：数据按分片/分区分布在多个节点，批量写会并行落到不同分片，跨分片两阶段提交代价高、可用性差；索引构建还是异步的（写入成功 ≠ 可检索）。所以多数系统选择"逐条尽力 + 返回错误列表 + 最终一致"，把补偿交给客户端。

**追问二**：写入返回成功，但立刻检索不到，是什么原因？
→ 解析：向量索引通常是**异步构建/刷新**的：写入先落到段/日志，后台再建索引，期间查询走旧索引。要看系统的 refresh/consistency 参数（如 Milvus 的 consistency level、Qdrant 的 wait 参数）。对"写完立即查"的场景要显式等待刷新，或接受短暂不可见并在业务上做补偿。

**追问三（可选）**：如何设计对账任务判断"少了一批文档"？
→ 解析：按业务主键做集合对账：源端导出 id 集合，目标端用 `count` + 分页/scroll 拉取 id 集合，求差集；不要只比总数（部分失败 + 部分重复可能总数刚好相等）。对差集按 id 重放 upsert，并记录每次对账的差集大小作为数据质量指标。
