---
title: "[Q6758] binlog_row_image：FULL 与 MINIMAL 之间，闪回能力和带宽的账"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6758 · binlog_row_image：FULL 与 MINIMAL 之间，闪回能力和带宽的账

难度：P7 ｜ 标签：MySQL、binlog_row_image、row 事件、闪回前提、复制带宽

基线：Python 3.12；用行事件模型算 FULL/MINIMAL 的镜像字节数，并演示 MINIMAL 下 UPDATE 闪回失效。

**问**：宽表（40 列，其中一个大 text 字段）的高频更新把 binlog 带宽和订阅端（canal 类）压得很紧。有人建议 `binlog_row_image=MINIMAL` 只记主键和变更列，能省一半以上带宽。这个参数的代价是什么？为什么 DBA 常常宁可留着 FULL？

**答**：
- **结论**：`binlog_row_image` 决定 row 事件携带多少列：**FULL** 记录整行（UPDATE 带前后全量镜像，DELETE/INSERT 单镜像）；**MINIMAL** 只记主键/唯一键 + **发生变更的列**。省带宽的同时破坏了两个前提：① **闪回**——UPDATE 的反向 SQL 需要 before 镜像的全部旧值，MINIMAL 下没变更的旧列不在 binlog 里，闪回工具要么失败要么填 NULL（Q6754 的原理直接失效）；② **审计与订阅端兼容**——下游拿到的行不再完整，按"整行语义"消费的逻辑（缓存重建、ES 文档重建）必须改成增量合并逻辑，否则字段悄悄变成 NULL。
- **取舍**：① 宽表大字段高频更新的账：FULL 的每条 UPDATE 镜像 ≈ 整行字节 × 2，MINIMAL ≈ (主键 + 变更列) × 2，省的是行宽倍数；② 如果下游本来就做增量合并（只更新变更列），且**不做闪回/审计**，MINIMAL 是合理选项；③ 折中还有 NOBLOB：大 text/blob 未变更时跳过，普通列仍全量——兼顾重建完整性与大字段带宽；④ 参数是**会话级可调**的：全局 FULL，个别高吞吐通道会话级 MINIMAL，是更精细的姿势。
- **实战**：① 改参数前先问"我们是否依赖 binlog 闪回"（误删恢复预案里有没有 Q6754）；② 订阅端消费 MINIMAL 事件必须按主键先读当前行再合并，不能直接整行覆盖；③ 监控 binlog 流量（Q6587 的磁盘账）确认收益，MINIMAL 对窄表收益很小不值得动；④ 该参数主从各自设置，从库回放不受主库设置影响，但要保证两边一致避免镜像语义混乱。

```python
"""FULL vs MINIMAL：镜像字节数账 + UPDATE 闪回可行性演示。"""
import json


def row_bytes(row: dict[str, str]) -> int:
    return sum(len(v.encode()) for v in row.values())


def event_size(op: str, before: dict, after: dict, image: str) -> dict:
    if image == "FULL":
        if op == "UPDATE":
            return {"update镜像": row_bytes(before) + row_bytes(after)}
        mirror = before if op == "DELETE" else after
        return {"单镜像": row_bytes(mirror)}
    # MINIMAL：只保留主键与变更列
    if op == "UPDATE":
        changed = {k: before[k] for k in before if before[k] != after.get(k)}
        pk = {"id": before["id"]}
        return {"update镜像": row_bytes(pk) + row_bytes(changed)
                + row_bytes(pk) + row_bytes({k: after[k] for k in changed})}
    mirror = {k: before[k] for k in ("id",) + tuple(before if op == "DELETE" else after)}
    return {"单镜像": row_bytes(mirror)}


def flashback_update(before: dict, image: str) -> str | None:
    """UPDATE 的反向 SQL 需要 before 全量旧值。"""
    if image == "FULL":
        sets = ", ".join(f"{k}={json.dumps(v)}" for k, v in before.items() if k != "id")
        return f"UPDATE t SET {sets} WHERE id={before['id']}"
    return None                                   # MINIMAL：旧列缺失，闪回失败


if __name__ == "__main__":
    before = {"id": "1001", "name": "商品A" + "描述" * 200, "price": "99.0"}
    after = {**before, "price": "89.0"}
    for image in ("FULL", "MINIMAL"):
        s = event_size("UPDATE", before, after, image)
        print(f"{image:<8} UPDATE 镜像字节: {list(s.values())[0]:>6,}")
        print(f"         闪回反向 SQL: {flashback_update(before, image)}")
    print()
    fb = event_size("UPDATE", before, after, "MINIMAL")["update镜像"]
    fu = event_size("UPDATE", before, after, "FULL")["update镜像"]
    print(f"带宽账: MINIMAL 省 {1 - fb / fu:.0%}（本例大字段占绝对宽度）")
    print("结论：MINIMAL 是带宽优化，代价是闪回与整行语义消费；NOBLOB/会话级可作折中")
```

**追问一**：为什么 `binlog_row_image` 可以会话级设置，而 `binlog_format` 不行？

→ 解析：镜像大小只影响"这条事件里带哪些列"，不影响主从一致性的判定逻辑——从库按主键定位行后，只应用携带的列，语义自洽，所以允许按会话（某条导入通道）单独收紧。而 `binlog_format` 决定事件类型的重放语义（statement 要在从库重算，Q6751），主从两边格式不一致会直接造成数据分叉，所以它被限制为全局级且切换要断开复制链。可见粒度的设计跟着"是否影响复制正确性"走。

**追问二**：订阅端按"整行覆盖"写缓存，切到 MINIMAL 后会发生什么？

→ 解析：每条 UPDATE 事件只带来 {主键, 变更列}，覆盖逻辑会把没带的列写成默认值/NULL——缓存里的商品描述悄悄被清空，且不报错。这类事故的隐蔽点在于**延迟显现**：只有"改价格"这种部分列更新触发后，字段才开始烂，监控上看不到错误、只有缓存命中率或业务正确性下降。对策是消费端改为"按主键回读+合并"或改订阅 FULL；同理，ES 文档重建、宽表同步都有这个坑，参数变更前必须盘点所有 binlog 消费方的消费语义。
