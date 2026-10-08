> 原文锚点：第 6~23 段「第一种情况通过 gctrace…GC四GC五表示GC编号…alt和百分号之间零点零零七秒…CPU强装时间和CPU时间…stcks占大小 globs全局变量 十六p十六核 forced」

## 一句话总述
`GODEBUG=gctrace=1` 的每一行就是一次 GC 的"体检报告"：`gc N @Ts %` 给出编号/启动时刻/CPU 占用率，`clock` 与 `cpu` 两段给出墙上时间与各相位 CPU 占用，`heap MB` 三段给出堆在 GC 前后的变化，`goal` 是目标堆、`P` 是逻辑 CPU 数，手动 `runtime.GC()` 触发的会在行尾标 `(forced)`。

## 面试官视角
能逐字段读 gctrace 输出，说明你真的"看过" GC 日志，而不是只会背概念。面试官常拿一行真实输出让你口译。

## 主问答
**Q（面试官原话）：** 给我讲讲 gctrace=1 打出来的那一行都是什么意思？

**A：** 以 `gc 5 @0.34s 2%: 0.007+0.52 ms clock, 0.11+0.12/0.13/0.05+0.52 ms cpu, 4->4->0 MB, 5 MB goal, 16 P` 为例逐段拆：

1. **`gc 5`**：第 5 次 GC 循环编号，每次 GC 自增 1。
2. **`@0.34s`**：距程序启动的墙上时间（wall-clock）。
3. **`2%`**：自启动以来 GC 占用的 CPU 时间百分比，不是单次占比。
4. **`0.007+0.52 ms clock`**：本次 GC 的墙上时间，拆成"标记辅助(mark assist) + 标记终止与清扫"两段之和。
5. **`0.11+0.12/0.13/0.05+0.52 ms cpu`**：GC 消耗的 CPU 时间，按相位拆分（标记辅助 / 专用标记 / 空闲标记 / 清扫等）；`cpu` 时间不含阻塞等待，所以通常小于 `clock` 对应段。
6. **`4->4->0 MB`**：GC 开始堆大小 -> GC 结束后堆大小 -> GC 后**存活**堆大小（live heap）。
7. **`5 MB goal`**：本次 GC 期望把堆控制到的目标上限。
8. **`16 P`**：当前运行环境的逻辑 CPU 数（GOMAXPROCS 上限）。
9. **行尾 `(forced)`**：表示该次 GC 由 `runtime.GC()` 手动触发，而非 pacer 自动触发。

## 追问链（L1~L5）
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|----|------|----------|--------|------------|
| L1 | clock 和 cpu 段差很多说明什么 | 是否理解墙钟 vs CPU | 差值多花在等待/被调度外，GC 没真在跑 CPU | 答不出即止 |
| L2 | 为什么 live heap 比 goal 小 | 是否懂目标堆含义 | goal 是上限、实际存活由对象图决定 | 答不出即止 |
| L3 | wallclock 时间包含什么 | 是否懂墙上时钟 | 含阻塞/等待，不止 CPU 执行 | 答不出即止 |
| L4 | 用户 CPU / 系统 CPU 区别 | 是否懂 CPU 时间拆分 | 用户态执行 vs 内核态执行 | 答不出即止 |
| L5 | 怎么看 GC 是否频繁 | 是否懂趋势判读 | 看 % 持续走高 + MB 段反复触 goal | 答不出即止 |

## 版本与兼容性
- `gctrace` 输出字段自 Go 1.0 起存在；`goal` 字段、二维 cpu 拆分随版本逐步稳定，老版本字段更少，以实跑版本为准。
- `(forced)` 标记在所有支持 gctrace 的版本中一致表示手动触发。

## 关键代码
```go
// 运行：GODEBUG=gctrace=1 go run main.go
package main

func main() {
    s := make([]int, 0)
    for i := 0; i < 1e6; i++ {
        s = append(s, i) // 频繁扩容 -> 触发 GC，终端会出现 gc N @Ts % ... 行
    }
}
```

## 总结与追问预判
- 口诀：编号看 `gc N`、占比看 `%`、耗时看 `clock`、相位看 `cpu`、堆变化看三段 `MB`、目标看 `goal`、核数看 `P`、手动看 `(forced)`。
- 预判追问：如何从 gctrace 判断"该预分配"？答：看到 heap 段频繁 `->大MB` 且 `%` 攀升，说明 append 反复扩容分配，应用 `make([]T, 0, n)` 预分配。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡已统一为规范术语（如 Go、GODEBUG=gctrace、wall-clock、runtime.GC）。本源未现黑名单词，正文一律使用规范词，纠错节不枚举任何原词崩坏词 `[经验]`。

> 边界：gctrace 是"观测手段"，GC **触发时机**见 `810-gc-trigger-timing`；手动 `runtime.GC()` 与 `debug.FreeOSMemory` 差异见 `810-manual-gc-freeosmemory`。
