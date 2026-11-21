---
disableNunjucks: true
title: "822 调度延迟抽样与 /sched/latencies 深挖"
date: 2026-11-17 23:53:06
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：并发模型 / runtime | 难度：L3 | 题型：深挖 | 频率：低 | 关键词：**casgstatus 寄生统计**/**HDR 直方图桶公式**/**标量 vs 直方图**/**墙钟非 CPU 时间**
> 原文锚点：第 145~165 段「trackingSeq/runnableTime 字段」
> 主卡见 822-调度延迟抽样与sched-latencies。

## 思路与架构

四个字段各司其职，但**它们只为一件极小的事服务**：在状态机转换的**尾巴上**挂一个 1/8 抽样的计时器。流程（`proc.go`）：

```text
casgstatus（离开 Grunning 等）
  └─ trackingSeq 除 8 余 0?（或 casgstatusAlwaysTrack）
       ├─ 否 → trackingSeq 加 1 直接返回
       └─ 是 → tracking 置 true
            └─ 进 Grunnable → 记 trackingStamp
                 └─ 进 Grunning → runnableTime 累加 → timeToRun.record → 清零 → tracking 置 false
```

1. 入口是 `casgstatus`——**统计逻辑寄生在状态转换函数里**，这是它「零额外结构」的原因。
2. 抽样判据是 `trackingSeq % gTrackingPeriod == 0`，**`trackingSeq` 每次转换都自增**，所以是「每 8 次转换抽 1 次」。
3. 计时窗口只覆盖 `_Grunnable` 段：进 runnable 记时间戳，进 running 结算并清零。
4. **`tracking` 是「本轮是否在跟踪」**，`trackingSeq` 才是「抽样计数器」——两者语义完全不同，原文把它们混成一个开关。

## 方案取舍

| 维度 | 方案 | 代价 | Go 选谁 |
|---|---|---|---|
| 采样率 | 全量记录 | `casgstatus` 是**全局最热的状态转换函数**，每次多 2~3 次写内存 | 否 |
| 采样率 | **1/8 抽样** | 统计有偏（但无偏估计，读数时乘回周期） | **是** |
| 采样时机 | 定时器采样 | 需 per-P 定时器 + 扫描 | 否 |
| 采样时机 | **状态转换时顺带抽** | 零额外结构 | **是** |
| 记录内容 | goroutine 端到端延迟 | 需挂 prologue/defer，改动用户代码 | 否 |
| 记录内容 | **runnable 段** | 覆盖不到「被唤醒后的排队」之外的东西 | **是** |
| 锁等待估计 | 记录原始值 | 抽样后偏小 8 倍，误导 | 否 |
| 锁等待估计 | **乘 `gTrackingPeriod` 修正** | 仍有方差 | **是** |

选型结论：Go 选「**寄生在 `casgstatus` + 1/8 抽样 + 乘回周期**」，本质是**用统计精度换热路径开销**。**不适用边界**：这个指标**只回答「可运行队列里等了多久」**，不回答「从提交到完成」——后者要靠 pprof、`runtime/trace` 或业务埋点。

## 细节与核心 API

- `gTrackingPeriod = 8` 是 `runtime2.go` 的常量，注释「the number of transitions out of _Grunning between latency tracking runs」。
- `isMutexWait()`（`runtime2.go:1333-1337`）**只认三个** `waitReason`：`SyncMutexLock` / `SyncRWMutexRLock` / `SyncRWMutexLock`。`SyncCondWait`、`SyncWaitGroupWait`（`isSyncWait` 覆盖的）**都不算**。
- `sched.totalMutexWaitTime` 喂给 **`/sync/mutex/wait/total:seconds`**，它是**标量（KindUint64）不是直方图**——**最容易读错的地方**。
- `sched.timeToRun` 喂给 **`/sched/latencies:seconds`**，是**直方图（KindFloat64Histogram）**。
- `newproc1` 里 `newg.trackingSeq = uint8(cheaprand())`（`proc.go:5376`）——**用随机数初始化**而非 0，意味着新 g 的第一次转换是否被抽中也是随机的。
- `casgstatusAlwaysTrack`（`proc.go:1269`）默认 `false`，注释说是 debug flag；打开后所有 g 全量跟踪。
- `_Gsyscall ↔ _Grunning` 的转换**不计入**（`proc.go:1323` 注释：两个状态太相似，不跟踪）。

## 性能量级与实测数据

**直方图桶的精确公式**（`runtime/histogram.go:66-72、174-198`）：

```text
timeHistMinBucketBits    = 9      // 最小桶 2^8 = 256 ns 量级
timeHistMaxBucketBits    = 48     // 最高桶 2^47 ns ≈ 1.4 天
timeHistSubBucketBits    = 2      // 每桶 4 个子桶
timeHistNumBuckets       = 48 - 9 + 1 = 40
timeHistTotalBuckets     = 40 * 4 + 2 = 162   // +1 下溢 +1 上溢
```

桶边界 `b[i]` 由 `uint64(1) << (i-1)` 位运算生成——**所以是 2 的幂乘 1/4**，前几个实测为 `0`、`6.4e-8`、`1.28e-7`、`1.92e-7`（`6.4e-8 = 2^8 / 4`）。`metrics.Read` 拿到的 `Buckets` 长度 163（多 1 是 `-Inf`）。

实测（go1.26.5 darwin/amd64，3000 个 goroutine）[实测]：

```text
桶数 = 163  计数数 = 162
样本总数 = 699
前 8 个桶边界: -Inf 0.000e+00 6.400e-08 1.280e-07 1.920e-07 2.560e-07 3.200e-07
非零计数的桶: [2.560e-07]=1 [1.024e-06]=2 ... [8.192e-06]=113 [1.024e-05]=77 ... [2.048e-05]=2
```

三个可引用的结论：

1. **样本数 699 ≫ 3000/8 = 375**——因为 runtime 自身的 g（GC worker、sysmon 等）也在被统计，且 1 次 `go` 会产生多次状态转换 [实测]。
2. **峰值在 `8.192e-06`（8.2 µs）附近**，三次实测形状一致（峰值区间 3~8 µs），**长尾 20 µs 后基本消失** [实测]。
3. **桶边界完全确定，计数随机**——引用时**只给桶边界，不给计数**；说「约 3~8 µs」是安全的，说「p50 = 5.1 µs」是危险的。

## 答题技巧

```text
30 秒版：内置 /sched/latencies:seconds，靠 g 上四个字段在 casgstatus 里做 1/8 抽样
        统计 runnable 等待时间。

3 分钟版：先讲指标名与直方图形态（163 桶 HDR），再讲四个字段的分工
         （trackingSeq 抽样计数器 / tracking 本轮标志 / trackingStamp 时间戳 /
         runnableTime 累加器），最后讲两个边界（1/8 抽样、只含 Mutex）。

白板版：写出 if casgstatusAlwaysTrack || gp.trackingSeq%gTrackingPeriod == 0 这一行，
       再写状态迁移入口做对比——一个在 casgstatus 尾部做统计，头部做状态迁移。

话术模板：「这题的重点不是『有这个指标』，而是『它是抽样的，且只统计可运行段和
         Mutex 等待』——不说清这两点，数字就没法解读。」

不会怎么接：被问「怎么拿到端到端延迟」——诚实收尾：runtime 不提供；要么在业务层埋点，
          要么用 runtime/trace 看完整时间线（代价是 trace 的开销）。
```

## 广度与深度延伸

- 横向：Java Flight Recorder 有 `ThreadPark` 事件、有「调度延迟」；但它们**默认全量或采样率可配**，Go 的 1/8 是硬编码的——**这是 Go「几乎零观测开销」取向的代价**。
- 纵向：`runtime/metrics` 是 Go 官方的结构化指标出口，`histogram.go` 是它唯一的 HDR 实现。
- 规范：`/sched/latencies:seconds` 的**桶边界是 API 契约的一部分**，但**计数不是**。

## 补充纠错（deep 级）

| 原文说 | 实际是 | 依据 |
|---|---|---|
| 「tracking 字段用来表示是否正在跟踪这个 goroutine 调度延迟统计信息」 | `tracking` 只是**本轮是否在跟踪**的 `bool`；**抽样计数器是 `trackingSeq uint8`**，判据在 `casgstatus` 里 | `runtime2.go:542-545`；`proc.go:1325` |
| 「没有跟踪的 goroutine，tracking 字段可能是零值表示不跟踪」 | 方向对但**因果倒置**：`tracking` 初值是 `false`，但「不被跟踪」是 `trackingSeq % 8 != 0` 的**结果**而非原因；且 `newg.trackingSeq = uint8(cheaprand())` 是**随机**初始化 | `proc.go:5376-5379` |
| 「这个字段是用来记录 CPU 时间戳的」（对 `trackingStamp`） | 是 **nanotime 墙钟时间**，**不是 CPU 时间**；用途是算「进入 runnable 到进入 running」的**墙钟差值** | `proc.go:1345/1358/1378` 均调 `nanotime()` |
| 「runnableTime 在启用跟踪时才会使用」 | 对，但漏了归零时机：进入 `_Grunning` 时 `sched.timeToRun.record(gp.runnableTime); gp.runnableTime = 0`——**每次结算后立即清** | `proc.go:1380-1381` |
