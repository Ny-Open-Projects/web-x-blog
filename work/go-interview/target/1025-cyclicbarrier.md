# 1025 扩展：CyclicBarrier 循环栅栏 vs WaitGroup

> 分类：Go 并发 | 难度：中 | 题型：对比 | 频率：中 | 关键词：**CyclicBarrier、循环栅栏、WaitGroup、可复用、await**

> 原文锚点：第 62~92 段「CyclicBarrier 可复用栅栏、New/WithAction、await/reset、与 WaitGroup 区别」

## 一句话总述
CyclicBarrier（循环栅栏）让一组 goroutine 彼此等待，全部到达同一执行点后才一起放行，且可重复使用。与 WaitGroup 区别：WaitGroup 通常是「主协程等一组子协程结束」；CyclicBarrier 是「多个对等 goroutine 互相等到齐」，并且可复用、可配置到达时的回调动作。

## 面试官视角
这是 singleflight 章节的拓展题。考官看你能不能说清两者定位差异：WaitGroup 是「一对多等待结束」，CyclicBarrier 是「多对多等待到齐 + 可循环」。能举 `New(n)` / `NewWithAction(n, fn)` / `await()` 的 API 与「最后一个到达者触发回调」更佳。

## 主问答
**Q（面试官原话）：** CyclicBarrier 和 WaitGroup 有什么区别？

1. **WaitGroup**：计数器等待，主协程 `Add/Wait`，子协程 `Done`；语义是「等一组任务结束」，通常一次性。
2. **CyclicBarrier**：参与数 n 的栅栏，`await()` 表示「我已到达」；所有 n 个参与者都 await 后才一起放行，放行后可再次循环使用。
3. **回调动作**：`NewWithAction(n, fn)` 在「最后一个参与者到达、其余尚未放行前」执行 fn，用于放行前的共享状态变更。
4. **错误处理**：await 可被 context 中断返回 broken 错误；`IsBroken()` 判断栅栏是否处于中断态；`reset()` 可重置。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 两者区别？ | 说不清等待语义 |
| L2 | 可复用？ | 说不清循环栅栏 |
| L3 | 回调时机？ | 说不清最后到达触发 |
| L4 | 中断处理？ | 说不清 broken/reset |
| L5 | 适用场景？ | 说不清多 goroutine 到齐 |

## 版本与兼容性
| 原语 | 语义 |
|------|------|
| WaitGroup | 等一组结束（一对多） |
| CyclicBarrier | 多对等到齐+可循环 |

## 关键代码
```go
b := cyclicbarrier.New(3)        // 3 个参与者
go func() { /* 工作 */; b.Await() }()  // 等三者到齐才继续
```

## 总结与追问预判
核心：**WaitGroup 一对多等结束；CyclicBarrier 多对等到齐且可循环、可带回调**。追问常回「singleflight 才是本节重点」（见 1025-overview）。

## ⚠️ 原文纠错
1. 事实核校： [经验] CyclicBarrier 可复用、多对等到齐、New/NewWithAction/await/reset/IsBroken、与 WaitGroup 语义差异——均正确，本卡为准。
2. 崩坏词归一：源码将 Go/goroutine/CyclicBarrier/WaitGroup 等音译为多组崩坏词；本卡统一为规范术语。
