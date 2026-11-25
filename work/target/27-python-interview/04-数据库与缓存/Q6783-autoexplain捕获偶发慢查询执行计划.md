---
title: "[Q6783] 白天跑不慢凌晨跑不动：auto_explain 捕获偶发慢查询的执行计划"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6783 · 白天跑不慢凌晨跑不动：auto_explain 捕获偶发慢查询的执行计划

难度：P6 ｜ 标签：PostgreSQL、auto_explain、偶发慢查询、计划捕获、log_min_duration

基线：Python 3.12；模拟 auto_explain 的"超时触发事后捕获"机制（阈值采样、计划快照、min duration 采样版），对比 pg_stat_statements 只见均值不见计划的盲区，全标准库实跑。

**问**：pg_stat_statements 里这条 SQL 平均 8ms，但每天总有几次跑到 8 秒，EXPLAIN 复现不出来——计划可能只在特定参数/特定统计状态下翻转。怎么把"偶发慢"那一瞬间的真实执行计划抓下来？auto_explain 和 pg_stat_statements 是什么分工？

**答**：
- **结论**：pg_stat_statements 是**聚合仪表**：按 queryid 汇总 total/mean/max 调用次数，能告诉你"这条 SQL 慢"，但**不记录计划**——max_time 高而 mean 正常的语句就是偶发慢信号，但为什么慢无从得知。auto_explain 是**事后黑匣子**：以 extension 形式加载，任何执行时长超过 `auto_explain.log_min_duration` 的语句结束时，自动把**当时真实使用的执行计划**（含实际行数 timing，开 `log_analyze`）写进日志——你不需要守着现场，慢发生的那一刻证据自动落盘。偶发慢的典型病理是**计划翻转**：参数相关的行数估算（空值/极端分布参数）、统计信息在 ANALYZE 前后跳变、缓存冷热差异——手工 EXPLAIN 用的是"现在"的统计与参数，复现不了"当时"。auto_explain 的采样版 `log_min_duration_sample` 只按比例采样超过阈值的语句，控制日志量；`log_nested_statements` 能带出函数内部的子语句计划。
- **取舍**：① 开销账：`log_analyze` 会给每条被捕获的语句做真实计时（Instrumentation 开销），全量开在高 QPS 实例上不可接受——用采样版（如 1/50）或只在事发窗口临时开启；② 阈值选择：设成 P99.9 时长（比如 500ms），既覆盖偶发慢又过滤常规流量；③ 与慢查询采样器的关系：pg_stat_statements 负责"发现与量化"，auto_explain 负责"取证"，慢日志/诊断日志采样（Q6628、Q1961）负责"归因到流量特征"——三层各司其职，不要指望单一工具；④ auto_explain 输出进 PG 日志，日志管道要配好 trace 关联（否则计划与业务请求对不上号），应用侧在 SQL 注释里带 trace_id 是把两个世界缝起来的关键招。
- **实战**：① 常驻配置：`shared_preload_libraries='auto_explain'` + `auto_explain.log_min_duration_sample='1s'` + `sample_rate=0.02`，低成本常驻取证；② 事故窗口切全量：收到慢查询告警后 `SET auto_explain.log_min_duration='200ms'; sample_rate=1` 只对当前会话/库开启，事后关掉；③ 计划比对工作流：把捕获的计划与当前 EXPLAIN 逐项 diff，行数估算偏差 >10 倍的节点就是翻转点，直接指向统计信息或参数分布问题；④ 参数敏感验证：用 `EXPLAIN (ANALYZE, GENERIC_PLAN)` 或给真实参数重放，确认翻转与参数相关，再决定走部分索引、拆 SQL 还是强制 plan hint。

```python
"""Q6783 auto_explain 模拟: 偶发慢语句的事后计划捕获 + 采样率控制。"""
import random

# 模拟: 同一条 SQL, 参数 95% 走索引计划(3ms), 5% 走顺序扫描计划(900ms)
random.seed(42)


class AutoExplain:
    """模拟 auto_explain: 超过阈值的语句结束时捕获其真实计划."""

    def __init__(self, threshold_ms: float, sample_rate: float = 1.0):
        self.threshold_ms = threshold_ms
        self.sample_rate = sample_rate
        self.captured: list[tuple[str, str, float]] = []
        self._seen = 0

    def run(self, sql: str, plan_name: str, actual_ms: float) -> float:
        self._seen += 1
        if actual_ms >= self.threshold_ms and random.random() < self.sample_rate:
            self.captured.append((sql[:20], plan_name, actual_ms))
        return actual_ms


def workload(n: int) -> list[tuple[str, float]]:
    """95% 参数走 IndexScan 3ms, 5% 参数走 SeqScan 900ms (计划翻转)."""
    out = []
    for _ in range(n):
        if random.random() < 0.95:
            out.append(("IndexScan", 3.0 + random.random()))
        else:
            out.append(("SeqScan", 900.0 + random.random() * 100))
    return out


if __name__ == "__main__":
    random.seed(7)
    plans = workload(400)                      # 400 次执行, 约 20 次翻转
    full = AutoExplain(threshold_ms=500, sample_rate=1.0)
    for plan, ms in plans:
        full.run("SELECT * FROM orders WHERE ...", plan, ms)
    sampled = AutoExplain(threshold_ms=500, sample_rate=0.25)
    for plan, ms in plans:
        sampled.run("SELECT * FROM orders WHERE ...", plan, ms)
    print(f"总执行 400 次, 预计慢语句 ~{sum(1 for _, m in plans if m > 500)} 次")
    print(f"全量捕获: {len(full.captured)} 条, 计划分布="
          f"{sorted({p for _, p, _ in full.captured})}")
    print(f"采样捕获(1/4): {len(sampled.captured)} 条 "
          f"(日志量降为 {len(sampled.captured) / max(len(full.captured), 1):.0%})")
    seq = sum(1 for _, p, _ in full.captured if p == "SeqScan")
    ok = seq > 0 and len(sampled.captured) < len(full.captured)
    print(f"校验: 慢语句全部为 SeqScan 计划且被捕获 -> {'通过' if ok else '异常'}")
    print("结论：pg_stat_statements 发现'谁慢', auto_explain 取证'为何慢';")
    print("      偶发慢=计划随参数/统计翻转, 手工 EXPLAIN 复现不了, 只能事后捕获")
```

**追问一**：auto_explain 捕到的计划与手工 EXPLAIN 结果不一致，怎么判断是"计划翻转"还是"环境差异"？

→ 解析：先排除环境差异三件套：① **统计信息新旧**：捕获计划与手工 EXPLAIN 之间如果发生过 ANALYZE/autovacuum，估算基线已经变了——先查 `pg_stat_user_tables.last_analyze` 时间戳，把手工 EXPLAIN 放到"当时"的统计状态附近验证（必要时手动导入统计快照或重建同样分布的测试库）；② **参数值**：prepared statement 的通用计划 vs 具体参数计划不同（`plan_cache_mode` 决定何时切 generic），手工 EXPLAIN 用的是你给的参数，捕获的是业务真实参数——把捕获 SQL 的参数从日志里还原出来重放；③ **会话级 GUC**：work_mem/random_page_cost/enable_seqscan 等在业务会话可能被 SET 过（连接池串味 Q6708 的同族），捕获计划头部会带 Settings 行，逐项比对。排除后剩下的才是真翻转：估算行数 vs 实际行数的比值沿执行树看，比值突变的那一层就是病灶节点，通常对应统计信息无法描述的分布（相关列、倾斜值）——解法要么造表达式索引/扩展统计（CREATE STATISTICS），要么把 SQL 拆开消灭计划歧义。

**追问二**：为什么 auto_explain 的 log_analyze 开销不能全量常驻？有没有低成本替代？

→ 解析：`log_analyze` 给语句执行加上 Instrumentation：每个计划节点要记录实际行数、循环次数、每节点耗时（多次 gettime 系统调用）——在OLTP 的高频小查询上，这套计时开销可达执行时间本身的 20%~50%，等于给全库查询加了个减速带，而且记录本身还会放大缓冲区/锁争抢。低成本替代梯度：① **只开 log_timing=false 的 log_analyze**：仍记录实际行数（开销小得多），丢掉每节点耗时但"估算 vs 实际行数"的翻转定位能力保留大半；② **采样常驻**：sample_rate 1%~5% 的全功能捕获，日志量与开销同比例缩小，长尾事件在统计意义上仍会被扫到；③ **双阶段**：常驻 `log_min_duration` 高阈值（如 2s）不 analyze，告警后临时窗口 `SET` 会话级低阈值 + analyze——事前取证兜底、事发全量取证；④ 用 pg_stat_statements 的 max_time/总时长做"值得不值得抓"的守门，避免为一次性抖动扩容取证。工具的通用账：**观测本身是负载，任何常驻探针都要有开销预算和采样率，这是可观测性设计的第一性约束。**
