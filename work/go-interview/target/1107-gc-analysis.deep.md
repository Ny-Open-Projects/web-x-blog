## 思路与架构
```text
分析 Go GC 的三层模型：
1. 定性层（gctrace）：不改代码，运行期流式输出，回答"GC 发生了几次、占多少 CPU、堆怎么变"。
2. 定量层（ReadMemStats）：在代码关键点采样做差，回答"这段逻辑 GC 次数/暂停具体多少"。
3. 定位层（pprof + trace）：heap 找分配热点，trace 看 GC 与调度的时序交叠，回答"谁在制造 GC 压力"。

决策流：先 gctrace 看 % 是否异常 -> 是则用 ReadMemStats 量化关键路径 -> 仍要到热点则用 pprof 下钻。
```

## 方案取舍
```text
- gctrace vs ReadMemStats：前者零侵入、只概览；后者需埋点、可精确断言。线上先用 gctrace，单测用 ReadMemStats。
- ReadMemStats vs pprof：前者轻量、只看计数；后者重、能定位函数级分配。定位阶段才上 pprof。
- 调参（GOGC）vs 改业务：优先改业务减少分配（治本），参数调优易掩盖真问题（治标）。仅当分配不可避免才调 GOGC。
- forced GC：runtime.GC() 强制同步回收，仅用于测试/基准，生产慎用（造成人为 STW 尖刺）。
```

## 答题技巧
```text
- 口译 gctrace 行：按"编号 -> 占比 -> clock -> cpu -> heap 三段 -> goal -> P -> forced"顺序背，配一张示例行。
- 被问"GC 慢怎么办"：先反问"你确认瓶颈在 GC 吗？"——展示整体性能观，避免盲目调参。
- 强调 ReadMemStats 必须做差、PauseTotalNs 是累计纳秒，别把绝对值当单次。
- 收尾落到"减少分配"：预分配 make([]T,0,n)、sync.Pool 复用、值类型替代指针。
```

## 细节与核心 API

```go
// 1) 运行时打印 GC 日志
//    GODEBUG=gctrace=1 ./app
//    gc 1 @0.12s 2%: 0.01+0.30+0.01 ms clock, ... 4->5->3 MB, 5 MB goal
//    含义：第1次GC；wall clock；标记/暂停；堆 存活->标记中->标记后；goal
// 2) 程序内读指标
var ms runtime.MemStats
runtime.ReadMemStats(&ms)
fmt.Println(ms.HeapAlloc, ms.NumGC, ms.PauseNs[(ms.NumGC+255)%256])
// 3) pprof 堆采样
//    go tool pprof http://localhost:6060/debug/pprof/heap
// 4) 手动触发：debug.FreeOSMemory() 把内存还给 OS（谨慎）
```
