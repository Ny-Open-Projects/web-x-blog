# 1105 执行追踪 vs 采样剖析（trace vs pprof）

> 分类：Go/性能 | 难度：L3 | 题型：对比题 | 频率：中 | 关键词：**trace** / **pprof** / **时序阻塞** / **CPU 百分比**
> 原文锚点：第 68~72 段「trace 有性能开销,分析完别无意义采集;go tool pprof 看函数CPU百分比(总体开销);go tool trace 看一段时间在做什么(时序/阻塞);定位慢函数用pprof,看goroutine阻塞/调度用trace」

## 一句话总述
**pprof 是采样剖析**——告诉你"每个函数花了多少 CPU 百分比"（总体开销在哪）；**执行追踪（trace）是事件记录**——告诉你"某段时间里程序在做什么、goroutine 阻塞/调度在哪"。定位慢函数用 pprof，看 goroutine 阻塞与调度延迟用 trace；二者互补，trace 还有运行时开销、采完即停。

## 面试官视角
- 意图：考察两种性能工具的选择能力，避免"只会 pprof"。
- P5 知道两者都能查性能；P6 能说清 pprof=CPU 百分比、trace=时序/阻塞；P7 能讲清"何时用哪个"并提 trace 开销。
- 红旗：以为 trace 能替代 pprof；用 trace 找慢函数（不如 pprof 直观）。
- 惊艳点：点出"pprof 适合找总体开销/热点函数，trace 适合找 goroutine 阻塞、调度延迟、GC 停顿时序"的分工。

## 主问答
**Q（面试官原话）：** trace 和 pprof 怎么选？
**A：**
1. **结论**：**pprof** 是采样剖析，输出"每个函数的 CPU 时间百分比 / 内存分配"，适合找**热点函数、总体开销**；**trace** 是执行追踪，记录 goroutine 生命周期事件，适合看**时序、阻塞点、调度延迟、GC 停顿分布**——"一段时间里程序在做什么"。
2. **机制（分工）**：要定位"哪个函数最慢/最耗 CPU"→ pprof（直观）；要定位"goroutine 卡在哪、等了多久、被调度打断几次"→ trace（pprof 采样看不出）。源中百万 goroutine 案例正是靠 trace 的时间分解发现瓶颈在 GC 暂停。
3. **边界（开销）**：trace 有**运行时开销**，且录制期间会拖慢程序，分析完应停止无意义采集；pprof 采样开销相对小。二者不是替代关系而是互补 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 两者区别 | 基础 | 采样 vs 事件 | 判 P5 |
| L2 | 各看什么 | 分工 | CPU百分比 / 时序阻塞 | 判 P6 |
| L3 | 何时用 trace | 取舍 | 阻塞/调度/GC时序 | 判 P6+ |
| L4 | 开销 | 边界 | trace 有运行时开销 | 判 P7 |
| L5 | 互补定位 | 综合 | 慢函数pprof/阻塞trace | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 工具链长期稳定 | 无 | pprof 与 execution tracer 分工恒定；trace 开销需注意，采完即停 `[经验]` |

## 关键代码
```go
// 找"热点函数/总体 CPU 开销" → pprof（采样）
// go tool pprof http://host:port/debug/pprof/profile  → 看每个函数 CPU%

// 找"goroutine 阻塞/调度延迟/GC 时序" → trace（事件记录）
// go tool trace t.trace  → 看 Goroutine 时间分解（执行/同步阻塞/GC暂停...）

// 选择口诀：慢函数/总体开销用 pprof；卡哪了/等了多久用 trace
```

## 总结与预判
- pprof 看总体 CPU%/热点；trace 看时序/阻塞/调度；互补，trace 有开销。
- 预判：trace 采集 → 见 1105-trace-collect；trace UI → 见 1105-trace-ui；pprof 全解见 1114-pprof-*。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读并重点核对"pprof 看函数 CPU 百分比(总体开销)、trace 看一段时间在做什么(时序/阻塞)、trace 有运行时开销采完即停、定位慢函数用 pprof/看 goroutine 阻塞调度用 trace"的描述，与 Go 性能工具定位一致。源码将术语音译为崩坏词（勾入进→goroutine、PPROF→pprof、gototrice→go tool trace、whenyoutruice→可视化链接 等），本卡统一为规范术语，技术结论未做更正。与 1114-pprof-*（采样剖析全解）互补——本卡聚焦"执行追踪与 pprof 的分工"，不重复 pprof 用法 `[经验]`。
