---
title: "[Q6778] 计划突然回退没人改过代码：统计信息过期与 ANALYZE 时机账"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6778 · 计划突然回退没人改过代码：统计信息过期与 ANALYZE 时机账

难度：P6 ｜ 标签：MySQL、统计信息、ANALYZE、执行计划回退、直方图

基线：Python 3.12；模拟优化器基于过期统计快照估算选择率并选计划，复现计划回退与 ANALYZE 纠偏，全标准库实跑。

**问**：某天线上一条 SQL 突然从毫秒级劣化到十几秒，代码没改、索引没动、数据量平滑增长——为什么会"计划突然回退"？优化器用的统计信息是怎么过期的？ANALYZE TABLE 该什么时候跑、跑多了有什么代价？

**答**：
- **结论**：优化器不是对数据执行查询，而是**对统计快照做估算**：各值的基数、列的分布直方图、索引页采样。快照在三种时点会过期：① 自动重采样的触发条件没到（MySQL `innodb_stats_auto_recalc` 要求变更行数超 10% 才触发，PG 依赖 autovacuum analyze 的阈值比例）——**均匀增长撞不到 10%，倾斜写入（pending 状态从 2% 涨到 12%）长期失真**；② 大批量导入后没手动 ANALYZE；③ 快照本来就采在异常时点。过期统计的后果：选择率估错 → 该走索引时估成全表、该全表时估成走索引（回表放大）→ 计划回退。修复动作便宜：`ANALYZE TABLE`（MySQL，秒级采样）或 `ANALYZE table`（PG），重新采样后计划立刻纠偏——**这是执行计划事故里性价比最高的第一止血动作**。
- **取舍**：① 采样页数（`innodb_stats_persistent_sample_pages`）调大：估算更准、ANALYZE 更慢——超宽表/倾斜列才调；② 直方图（MySQL 8.0 `ANALYZE ... UPDATE HISTOGRAM`）：解决等值谓词在倾斜列上的估算失真，但直方图不随 DML 自动更新，要纳入定时任务；③ 频繁 ANALYZE 的代价：采样读消耗 IO、计划短暂抖动（重采样瞬间新旧计划切换），别进高频循环；④ PG 侧扩展统计（CREATE STATISTICS）处理关联列估算，MySQL 用直方图近似。
- **实战**：① 大批量导入/删除后把 ANALYZE 排进作业收尾步骤（像 commit 一样固定）；② 计划突变告警：慢日志新模式 + EXPLAIN 的 estimated rows 与 actual rows 偏差比（>10 倍即异常）；③ 倾斜列（状态机列、租户 ID）优先建直方图；④ 回归防护：上线涉及查询模式的变更前，对目标表先 ANALYZE 一次，排除统计过期变量的干扰。

```python
"""Q6778 统计信息过期: 大量写入后统计失真, 优化器选错索引, ANALYZE 纠偏。"""
import random
random.seed(42)


class TableStats:
    def __init__(self, total_rows: int, status_dist: dict[str, int]):
        self.total_rows = total_rows
        self.dist = dict(status_dist)          # 统计快照(可能过期)

    def estimate(self, status: str) -> float:
        """基于过期统计的选择率估算."""
        return self.total_rows * self.dist.get(status, 0) / sum(self.dist.values())

    def analyze(self, actual_dist: dict[str, int], actual_rows: int) -> None:
        self.dist = dict(actual_dist)
        self.total_rows = actual_rows


def choose_index(est_rows: float) -> str:
    # 索引对选择率敏感: 估 <5% 走索引, 否则全表
    return "idx_status" if est_rows < 0.05 * 1_000_000 else "全表扫描"


if __name__ == "__main__":
    t = TableStats(1_000_000, {"done": 980_000, "pending": 20_000})
    # 三周大量写入: pending 涨到 12%
    actual = {"done": 880_000, "pending": 120_000}
    est = t.estimate("pending")
    plan_before = choose_index(est)
    real_rows = actual["pending"]
    print(f"过期统计: 估 pending {est:.0f} 行 -> 计划 {plan_before}")
    print(f"实际 pending {real_rows} 行 ({real_rows / 1_000_000:.0%}) -> "
          f"{'索引扫描反而放大回表' if plan_before != '全表扫描' else '计划合理'}")

    t.analyze(actual, 1_000_000)
    est2 = t.estimate("pending")
    plan_after = choose_index(est2)
    print(f"ANALYZE 后: 估 {est2:.0f} 行 -> 计划 {plan_after}")

    # 断言: 过期统计选错, 收集后纠正
    ok = (plan_before == "idx_status" and plan_after == "全表扫描"
          and abs(est - 20_000) < 1)
    print(f"校验: 过期统计误判 + ANALYZE 纠偏 -> {'通过' if ok else '异常'}")
    print("结论：统计快照落后于数据演进, 计划回退是慢性病;")
    print("      批量写入/大 DML 后预约 ANALYZE, 计划突变告警挂 estimated_rows vs actual 偏差")
```

**追问一**：为什么"变更超 10% 才自动重采样"会在倾斜写入场景下长期失效？

→ 解析：自动重采样以**变更行数占总行数的比例**为触发条件，而倾斜写入的特点是"少数状态列的分布大幅漂移，但总变更行数占比很小"：一百万行的表，pending 从 2% 涨到 12% 需要十万行状态迁移，恰好撞上 10% 线——但如果表本身有三千万行，同样十万行迁移只占 0.3%，永远触发不了。更隐蔽的是**行数没变、分布变了**（UPDATE 状态不增不减行）：变更计数的口径覆盖 UPDATE，但分布漂移对等值估算的影响远大于行数本身。所以倾斜列的正确姿势是直方图 + 定时重采，而不是指望 auto_recalc 兜底。这也是"计划回退事故查不到代码变更"的高频根因：**变的是分布，不是结构**。

**追问二**：ANALYZE 采样页是随机的，重采样后计划一定会稳定吗？怎么对付"计划抖动"？

→ 解析：不一定。采样天然有方差：两次 ANALYZE 采到的页不同，估算的选择率可能跨过计划的决策边界（比如估 4.8% 走索引、5.2% 走全表），出现"跑一次 ANALYZE 计划变一次"的抖动。对策分三层：① 加大采样页数降低方差（代价是 ANALYZE 变慢）；② 计划固化兜底：对关键 SQL 用 `optimizer hint`/plan management（MySQL 8.0 的 hint 或 set_var，PG 的 pg_hint_plan/plan cache 控制）把验证过的计划钉住，统计更新只影响其余查询；③ 观测先行：EXPLAIN ANALYZE 对比 estimated/actual rows，偏差收敛（<2 倍）才认为统计可信。抖动问题本质是"用有限样本估计分布"，参数只能压缩方差、hint 只能钉个案，长期解是让查询对估算误差不敏感（更稳定的索引设计、减少跨边界的选择率依赖）。
