---
title: [Q6621] CREATE INDEX CONCURRENTLY 失败留下 INVALID 索引事故复盘
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6621 · CREATE INDEX CONCURRENTLY 失败留下 INVALID 索引事故复盘

难度：P6 ｜ 标签：事故复盘 / PostgreSQL / 索引

**问**：线上给一张 3 亿行的表加索引，用了 `CREATE INDEX CONCURRENTLY` 避免锁表，中途因为复制冲突失败了一次，重跑成功。几天后写入变慢、计划里出现这个索引却"该走不走"。问题出在哪？为什么 CIC 失败不会自动清理？

**答**：
- **结论**：`CREATE INDEX CONCURRENTLY` 失败（死锁、唯一冲突、取消、复制冲突）不会回滚已建的索引，而是留下一个 `pg_index.indisvalid = false` 的 INVALID 索引。INVALID 索引**仍然会被写入维护**（每次 INSERT/UPDATE 都要维护它，写放大照付），但**规划器不会用它做查询**——于是出现"白白多付一份写成本、却没有读收益"的中间态。事后查询变慢/写入退化正是这个原因。修复方式：`DROP INDEX` 掉 INVALID 索引再重建；唯一索引的 INVALID 状态更隐蔽——它建了一半但**没生效约束**，误以为唯一性已受保护是二次事故来源。CIC 之所以不自动清理：它与普通事务的原子回滚不同，需要多轮全表扫+等待快照收敛，中断点可能在任意阶段，回滚代价高于留下待清理产物。
- **取舍**：发现 INVALID 后是"立即重建"还是"挂起观察"？看表写入速率：高写入表留着 INVALID 每小时白烧一份写放大，立即重建；低写入表可以排到低峰。监控上把 `indisvalid=false` 当告警项（pg_index 一条 SQL 的事），而不是等写入退化才查——这类事故最贵的部分不是重建本身，而是"带病运行几周没被发现"。Alembic/迁移工具里手写 DDL 的场景要显式加失败处理：CIC 失败 → 查 INVALID → DROP → 重试。
- **实战**：① 上线前查：`SELECT indexrelid::regclass FROM pg_index WHERE NOT indisvalid;` 应为空；② 迁移脚本幂等化：先 DROP IF EXISTS 再 CIC；③ 长事务/备份窗口期间不要跑 CIC（冲突高发），选择低峰且停备份；④ 把 `indisvalid` 纳入巡检 SQL 与 Alembic 迁移完成后的断言。

```python
# INVALID 索引判定与修复决策: 写放大白付但查询不受益
# 基线: Python 3.9+ 标准库; 真实场景对接 pg_index 查询
from dataclasses import dataclass


@dataclass
class IndexState:
    name: str
    indisvalid: bool
    write_rps: float          # 表写入速率
    maintain_cost_per_write: float  # 每次写维护该索引的成本


def wasted_writes_per_hour(idx: IndexState) -> float:
    """INVALID 索引每小时的纯浪费(写放大没有任何读收益)。"""
    return idx.write_rps * idx.maintain_cost_per_write * 3600


def repair_plan(idx: IndexState, threshold: float = 1e6) -> str:
    if idx.indisvalid:
        return "healthy: no action"
    if wasted_writes_per_hour(idx) > threshold:
        return "DROP invalid index NOW, rebuild CIC at low peak"
    return "DROP invalid index, schedule rebuild this week"


def main() -> None:
    hot = IndexState("idx_orders_ext_id", False, 5000, 0.4)
    cold = IndexState("idx_archive_tag", False, 2, 0.3)
    # 5000 rps * 0.4 * 3600 = 7.2M/h 白烧 -> 立即重建
    assert wasted_writes_per_hour(hot) > 1e6
    assert repair_plan(hot).startswith("DROP invalid index NOW")
    assert repair_plan(cold).startswith("DROP invalid index, schedule")
    # 唯一索引 INVALID = 约束未生效, 不能当防线
    print(f"hot: {wasted_writes_per_hour(hot):.0f} cost/h wasted -> rebuild now")
    print("OK: indisvalid=false 必须进巡检; 唯一INVALID不提供约束保护")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么 CIC 需要两次全表扫描、中间要等待所有事务快照收敛？
→ 一句话提示：第一轮建主结构并增量补差，第二轮补第一轮期间的写入差异；中间必须等所有旧事务结束（等所有能"看见旧快照"的事务退出）才能保证任何并发事务对索引完整性有一致视图，这就是它怕长事务和复制冲突的原因。

**追问 2**：唯一索引 CIC 失败留下的 INVALID 索引为什么比普通索引更危险？
→ 一句话提示：应用以为唯一约束已生效，实际 INSERT 检查跳过 INVALID 唯一索引，重复键照样写入；发现后除了重建还要对已写入数据做判重回补，这是"约束失效期"的数据修复问题而不仅是索引问题。

## 背诵要点
- CIC 失败不回滚，留下 `indisvalid=false` 索引：写放大照付、查询不走、唯一约束不生效，是"三重带病运行"。
- 修复 = DROP INVALID 再重建；决策看表写入速率（浪费 = write_rps × 单次维护成本 × 3600）。
- `indisvalid=false` 必须进巡检/迁移后断言；CIC 挑低峰并避开长事务与备份窗口。

## 复盘追问
- 为什么"写入退化但查询没变慢"的组合症状能直接指向 INVALID 索引？提示：写路径要维护所有索引（含 INVALID），读路径只走 valid 索引，两者不对称是判别签名。
- 迁移工具（Alembic）里怎么把 CIC 幂等化？提示：先查 pg_index 清 INVALID + DROP IF EXISTS 再建，迁移完成断言 indisvalid 全真。
