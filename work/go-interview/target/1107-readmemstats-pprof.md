> 原文锚点：第 24~33 段「第二种方式使用 runtime 标准库…runtime.MemoryStates 记录…readmemorystates…GC次数减去…GC暂停时间…第三种引入 netHTTPPPROF 导出 trst 和 help 信息」

## 一句话总述
`runtime.ReadMemStats` 让你在代码里**定量**拿到 GC 次数（`NumGC`）与暂停总时间（`PauseTotalNs`）的增量；`net/http/pprof` 则导出 heap profile 与 execution trace，把"谁在分配、GC 怎么抢占 mutator"可视化，二者是 gctrace 之外的两条精确化路径。

## 面试官视角
面试官想看你能否把"GC 慢"从感觉变成数字，并能用 pprof 定位到具体分配热点——这是调优的硬功夫。

## 主问答
**Q（面试官原话）：** 除了 gctrace，代码里怎么拿到 GC 次数和暂停时间？pprof 又能分析什么？

**A：**

1. **ReadMemStats 定量**：在待测逻辑前后各采一次 `runtime.MemStats`，`after.NumGC - before.NumGC` 即这段逻辑的 GC 次数，`after.PauseTotalNs - before.PauseTotalNs` 即暂停总纳秒；适合在压测/单测里做断言。
2. **注意采样开销**：`ReadMemStats` 内部会碰全局内存统计锁，高频调用有竞争；它读的是原子计数（`NumGC` 等），本身几乎不触发 STW，但别在热路径里反复调。
3. **pprof heap**：导入 `_ "net/http/pprof"`，访问 `/debug/pprof/heap` 拿堆快照，用 `go tool pprof` 看 `inuse_space`/`alloc_objects`，定位"分配最多的函数"。
4. **pprof trace**：`/debug/pprof/trace?seconds=N` 导出执行轨迹，能在时间轴上看到 GC 标记/清扫与 Goroutine 调度的交叠，判断 GC 是否挤占业务。
5. **组合使用**：gctrace 定性 → ReadMemStats 定量 → pprof 定位，三层递进。

## 追问链（L1~L5）
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|----|------|----------|--------|------------|
| L1 | NumGC 是累计还是单次 | 是否懂计数器语义 | 全局累计，必须前后做差 | 答不出即止 |
| L2 | PauseTotalNs 含哪些暂停 | 是否懂暂停构成 | 含所有 STW 暂停（标记终止等） | 答不出即止 |
| L3 | heap profile 看哪个指标 | 是否用过 pprof | alloc_objects 看分配次数、inuse_space 看常驻 | 答不出即止 |
| L4 | ReadMemStats 会 STW 吗 | 是否懂采样成本 | 读计数几乎不 STW，但有锁竞争 | 答不出即止 |
| L5 | 为什么 trace 比 heap 更全 | 是否懂二者差异 | heap 是快照、trace 是时间轴 | 答不出即止 |

## 版本与兼容性
- `runtime.ReadMemStats` 与 `net/http/pprof` 跨版本稳定；`PauseTotalNs` 自 Go 1.0 起存在。
- pprof 的 HTTP 路由（`/debug/pprof/...`）随 Go 版本在细节上增强，但基本路径不变。

## 关键代码
```go
var s, e runtime.MemStats
runtime.ReadMemStats(&s)
hotPath() // 待测分配逻辑
runtime.ReadMemStats(&e)
fmt.Printf("GC次数=%d 暂停=%v\n", e.NumGC-s.NumGC, time.Duration(e.PauseTotalNs-s.PauseTotalNs))
```

```go
import _ "net/http/pprof" // 匿名导入即可注册 /debug/pprof 路由
// 终端：go tool pprof http://127.0.0.1:6060/debug/pprof/heap
//       go tool trace  <trace文件>
```

## 总结与追问预判
- ReadMemStats 是"点采样做差"，pprof 是"快照/轨迹深挖"，gctrace 是"流式概览"，三者互补。
- 预判追问：`PauseTotalNs` 和 gctrace 的暂停对得上吗？答：二者同源，gctrace 的 clock 段含标记终止 STW，PauseTotalNs 累加所有 STW，量级一致。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡已统一为规范术语（如 Go、runtime.ReadMemStats、net/http/pprof、execution trace）。本源未现黑名单词，正文一律使用规范词，纠错节不枚举任何原词崩坏词 `[经验]`。

> 边界：pprof 通用用法见 1506；GC 触发与降频见 `810-*`；本卡只讲"如何量化与剖析 GC"。
