---
title: [Q6520] Redis 持久化选型与恢复演练
date: 2026-11-19
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6520 · Redis 持久化选型与恢复演练

> 难度:★★☆ | 标签:Redis, 持久化, RDB, AOF

**问**：RDB 与 AOF 各自的恢复口径是什么——「RDB 快照每小时一次」意味着最多丢多少数据？AOF 的三种 fsync 策略（always/everysec/no）分别对应什么丢失窗口与性能？混合持久化（4.0+）解决什么，恢复演练为什么必须做？

**答**：① **RDB**：定时 fork 全量快照——fork 瞬间 COW（写时复制），内存翻倍风险（大实例 + 写入高峰同时发生 = OOM 经典事故）；丢失窗口 = 快照间隔（每小时 = 最多丢 1 小时）。② **AOF**：追加写命令日志，fsync 三档：`always`（每命令刷盘，丢≈0，吞吐掉一个量级）、`everysec`（每秒刷，最多丢 1s，**默认与主流选择**）、`no`（交给 OS，丢 30s 级，最快）。③ **混合持久化**（4.0+ `aof-use-rdb-preamble`）：重写时 RDB 头 + 增量 AOF 尾——恢复快（RDB 部分直接载入）+ 丢失窗口小，**生产默认选它**。④ AOF 重写也是 fork + COW，大实例同样要注意。⑤ 恢复演练：备份文件「看着在」不等于「能恢复」——RDB 损坏（fork 中断）、AOF 半截命令（kill -9 后）、版本不兼容，都是恢复现场才暴露；演练 = 定期把备份在新实例 load 并比对 key 数与校验和，用演练结果倒逼备份策略。

```python
# demo 用纯 Python 模拟 RDB fork-COW 内存翻倍风险与 AOF fsync 丢失窗口（口径实测）
import os, time, random

def rdb_fork_cow_cost(used_gb: float, write_bps_pct: float, snapshot_min: float = 60) -> dict:
    """fork 瞬间：页表复制 + COW 增量内存 ≈ 期间写入量。"""
    cow_gb = write_bps_pct / 100 * used_gb * (snapshot_min * 60 / 10)  # 10s 内写增量近似
    return {"page_table_extra": "fork 瞬间页表复制（实例越大越久，主线程卡顿）",
            "cow_extra_gb": round(cow_gb, 2),
            "oom_risk": cow_gb > used_gb * 0.3}
print("RDB fork COW（10GB 实例、20% 写入率）：", rdb_fork_cow_cost(10, 20))

def aof_loss_window(mode: str) -> dict:
    return {
        "always":    {"loss": "≈0（每命令 fsync）", "throughput": "低（磁盘上限）"},
        "everysec":  {"loss": "≤1s（后台线程每秒刷）", "throughput": "高"},
        "no":        {"loss": "≤30s（OS flush 周期）", "throughput": "最高"},
    }[mode]

def recovery_drill(rdb_path_ok: bool, aof_tail_valid: bool) -> bool:
    """恢复演练：load 备份并校验（demo 模拟两类常见损坏）。"""
    if not rdb_path_ok:
        print("演练发现：RDB 文件 CRC 损坏 —— 依赖 AOF 尾部恢复")
    if not aof_tail_valid:
        print("演练发现：AOF 半截命令 —— redis-check-aof --fix 截断修复（丢尾）")
    return rdb_path_ok or aof_tail_valid

if __name__ == "__main__":
    for m in ("always", "everysec", "no"):
        print(m, aof_loss_window(m))
    print("混合持久化：RDB 头（恢复快）+ AOF 尾（丢失窗口小）→ 生产默认")
    assert recovery_drill(rdb_path_ok=False, aof_tail_valid=True), "至少一条恢复路径可用"
    print("恢复演练通过（有一条可用路径即合格；双损坏 = 备份策略不合格）")
    # 口径速记：生产默认 = RDB（每小时）+ AOF everysec + 混合重写；
    # fork 前看内存余量（maxmemory 留 30% headroom 给 COW），大实例避免整点集中重写。
```

**追问**：1) 为什么 fork 瞬间主线程会卡？——复制页表（10GB 实例页表几百 MB，拷贝百毫秒级）；实例越大卡越久，这也是「Redis 单实例别超 10GB」口径的来源之一。2) 主从架构下持久化可以省吗？——主关持久化 + 从持久化（读写分离架构的常见省钱做法）有个坑：主重启空库后从全量同步，期间主是空的——**主重启后必须先从从库同步完成才接写**，或干脆两边都开。3) AOF 文件膨胀怎么治？——重写（fork 生成精简版）；重写期间新命令写进 aof_buf + 重写缓冲双份，重写完成原子替换——监控 `aof_rewrite_in_progress`。

## 背诵要点
1. RDB = fork 快照：丢失窗口 = 间隔；fork 卡顿 + COW 内存翻倍是大实例 OOM 经典事故。
2. AOF fsync 三档：always 丢≈0 吞吐低 / everysec 丢≤1s（默认）/ no 丢 30s 级；生产默认混合持久化（RDB 头 + AOF 尾）。
3. 恢复演练 = 定期新实例 load 备份并校验；RDB 损坏/AOF 半截都是现场才暴露的坑。

## 复盘追问
1. 为什么「每小时 RDB」在大实例上要错峰？（提示：整点快照与业务高峰重合 → fork COW OOM；错峰 + maxmemory 留 30% 余量）
2. 缓存实例（可全丢）和队列实例（不可丢）的持久化策略怎么分？（提示：缓存可只 RDB 甚至不持久化；队列 everysec+everysec 目录盘 SSD——分实例分策略，参考 Q6518）
