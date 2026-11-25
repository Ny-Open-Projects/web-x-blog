---
title: [Q7138] 长跑 worker 内存泄漏的 RSS 增长容量账与重启策略
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7138 · 长跑 worker 内存泄漏的 RSS 增长容量账与重启策略

难度：P6 ｜ 标签：容量规划 / 内存 / 工程化

**问**：常驻数据处理 worker 跑三天后 RSS 从 300MB 涨到 4GB 被 OOM 杀掉。怎么给这类长跑进程建"内存泄漏容量账"：泄漏速率怎么测、容器内存上限怎么定、优雅重启策略怎么设计让 OOM 永远轮不到触发？

**答**：
- **结论**：泄漏容量账四个参数：① **泄漏速率**：RSS 对请求数/任务数回归斜率（线性泄漏 vs 与任务量成正比），用 `resource.getrusage().ru_maxrss`（峰值）或 cgroup `memory.current` 按小时采样；② **安全上限**：容器 limit 设为"基线 + 泄漏余量 × 计划重启间隔内的总泄漏 + 30% 安全系数"，上限不是防泄漏而是给重启策略留时间窗；③ **重启阈值**：在"预测到达上限前 N 小时"的 RSS 处主动优雅退出（跑完当前任务、关连接、交还任务），由编排器拉起新进程——**主动重启永远优于被动 OOM**（OOM 是任务中断 + 可能丢状态 + 全量冷启动）；④ **归因前置**：重启只是止血，泄漏根因要靠 tracemalloc 快照 diff / objgraph 找（常见：全局 list 缓存无界、闭包引用、C 扩展不释放、日志 handler 累积）。
- **取舍**：重启间隔拉长（少重启）省冷启动成本但压缩余量；限流式方案（任务计数重启，如 Celery `max_tasks_per_child`）最简单可靠，按字节数重启更精细但需要监控管道。另一个方向是泄漏"修复优先级"：若泄漏速率 × 重启成本 < 修复人日成本，短期接受泄漏 + 自动重启是理性决策——泄漏不一定都要立刻修。
- **实战**：① 采样口径统一用 cgroup memory.current（容器内 RSS 会低估共享页与缓存）；② 重启脚本必须"任务边界"退出（处理完当前消息再退），粗暴 kill 等于把 OOM 挪个位置；③ 把 RSS-任务数回归斜率做成周报指标，斜率突变（新版本引入泄漏）立即告警——斜率监控比绝对值更早发现问题。

```python
# 泄漏容量账: 采样回归斜率 -> 预测触顶时间 -> 主动重启阈值
# 基线: Python 3.9+ 标准库; 容器内采 cgroup memory.current
from dataclasses import dataclass


@dataclass
class LeakAccount:
    baseline_mb: float            # 干净基线 RSS
    limit_mb: float               # 容器内存上限
    leak_mb_per_1k_tasks: float   # 每 1000 任务泄漏量
    restart_buffer_hours: float   # 提前重启的预测缓冲

    def tasks_until_limit(self, current_mb: float) -> int:
        headroom = self.limit_mb * 0.9 - current_mb   # 90% 之上留给安全系数
        return max(0, int(headroom / self.leak_mb_per_1k_tasks * 1000))

    def restart_at_mb(self, tasks_per_hour: float) -> float:
        """在触顶前预留 restart_buffer_hours 的任务量对应的水位。"""
        pre_reserve = tasks_per_hour * self.restart_buffer_hours \
            * self.leak_mb_per_1k_tasks / 1000
        return self.limit_mb * 0.9 - pre_reserve


def main() -> None:
    acct = LeakAccount(baseline_mb=300, limit_mb=4096,
                       leak_mb_per_1k_tasks=50,
                       restart_buffer_hours=2.0)    # 每 1k 任务泄漏 50MB
    fresh = acct.tasks_until_limit(acct.baseline_mb)
    # (4096*0.9 - 300)/50*1000 ≈ 67728
    assert 67_000 < fresh < 68_500, fresh
    # 三天后: 300 + 50*72/1 ≈ 3900MB (每 1k 任务/天) -> 已近上限
    day3 = acct.baseline_mb + acct.leak_mb_per_1k_tasks * 72
    assert acct.tasks_until_limit(day3) < 3_600
    # 主动重启水位: 1000任务/小时, 提前 2 小时 -> 4000*0.9-100 = 3586
    restart_mb = acct.restart_at_mb(tasks_per_hour=1000)
    assert restart_mb == 4096 * 0.9 - 100
    assert restart_mb < day3                        # 现状三日内必触发
    print(f"新进程可跑 {fresh} 任务; 主动重启水位 {restart_mb:.0f}MB "
          f"(第3天 RSS {day3:.0f}MB 必触)")
    print("OK: 容器上限给泄漏余量; 按任务边界主动重启, OOM 永不触发")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么容器内存上限不能直接设成"预期峰值"？
→ 一句话提示：上限只决定"何时被杀"，不阻止增长；必须给重启策略留时间窗（提前 N 小时的水位），否则限值一到就是被动 OOM。

**追问 2**：RSS 采样为什么在容器里会低估或高估？
→ 一句话提示：RSS 不含可回收页缓存、共享库被多进程重复计数——容器账要用 cgroup memory.current（含缓存）对齐 limit 口径，否则账对不上。

## 背诵要点
- 容量账参数：泄漏斜率（RSS/任务数回归）+ 容器上限（基线+余量×重启间隔+30% 系数）+ 主动重启水位（触顶前预留缓冲）。
- 主动重启（任务边界优雅退出）优于被动 OOM（任务中断+冷启动）；Celery `max_tasks_per_child` 是最简实现。
- 根因排查 tracemalloc diff/objgraph；斜率周报比绝对值监控更早发现新版本引入的泄漏；泄漏速率×重启成本 < 修复成本时可接受泄漏。

## 复盘追问
- 如何区分"真泄漏"与"缓存合理增长"？提示：缓存有界（命中率稳定、增长封顶）而泄漏线性不封顶；给缓存加上限配置后回归斜率归零即是缓存，否则是真泄漏。
- 重启瞬间的服务连续性怎么保证？提示：任务边界退出 + 编排器就绪探针控制流量切入（Q1111 健康检查思路）+ 新进程预热（模型/连接）再放量。
