# 805 schedinit：调度器/内存分配器/GC 参数初始化

> 分类：运行时 | 难度：L3 | 题型：原理题 | 频率：中 | 关键词：**schedinit** / **创建 P** / **GC 参数初始化**
> 原文锚点：第 82~87 段「执行 schedinit 进行栈/内存分配器/调度器初始化…创建 P…GC 参数初始化不启动 GC」

## 一句话总述
`schedinit` 是运行时早期的总装车间：初始化栈、内存分配器、调度器，按 CPU 核数（受 GOMAXPROCS 约束）创建 P，并只初始化 GC 的参数——此时 GC 还没启动，要等到 `runtime.main`。

## 面试官视角
- 意图：是否清楚启动期各组件初始化的时序，尤其"GC 参数先设、GC 后启"。
- P5 知 schedinit 做初始化 / P6 能说 P 数量来源与 GC 分两步 / P7 知为何 GC 不在 schedinit 启动。
- 红旗：以为 schedinit 就启动了 GC；以为 P 数量固定等于核数不看 GOMAXPROCS。
- 惊艳点：P 数量 = min(CPU 核数, GOMAXPROCS)，GC 到 runtime.main 才 enable —— 验证 `GOMAXPROCS` 与 `gcenable` `[源码]`。

## 主问答
**Q（面试官原话）：** 启动阶段 `schedinit` 都干了什么？GC 这时候起来了吗？
**A：**
1. **结论**：`schedinit` 初始化栈、内存分配器、调度器，并创建 P；它只设 GC 参数，不启动 GC。
2. **机制**：P 的数量由 CPU 核数与 `GOMAXPROCS` 共同决定（受后者上限约束）；GC 的并发回收在 `runtime.main` 里经 `gcenable` 才真正开启。
3. **边界**：`schedinit` 阶段还没用户代码、调度未正式开始，故 GC 只需把参数摆好，启动留到更后面。
**加分层：** 把"GC 参数初始化"和"GC 启动"分成两个阶段，能体现对启动时序的精确掌握。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | schedinit 干啥 | 概念 | 总装初始化 | 换题 |
| L2 | P 数量 | 机制 | 核数/GOMAXPROCS | 判 P5 |
| L3 | GC 启了吗 | 边界 | 只设参数 | 判 P6 |
| L4 | 为何分两步 | 权衡 | 时序 | 判 P6+ |
| L5 | ncpu 读取 | 实战 | schedinit 内 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本稳定 `[源码]` | 早期 mcache 随 M，后随 P | 讲"创建 P + GC 参数初始化不启动"时序 |

## 关键代码
```go
// 示意，未验证：schedinit 关键动作（概念，非完整源码）
// schedinit() {
//   procs := ncpu; if n := GOMAXPROCS; n > 0 { procs = min(procs, n) }
//   for i := 0; i < procs; i++ { 创建 p }
//   gcinit()        // 仅初始化 GC 参数
// }
```

## 总结与追问预判
- schedinit 总装：栈/分配器/调度器 + 创建 P（核数受 GOMAXPROCS 限）+ GC 参数初设不启。
- 预判：newproc/mstart → 见 805；runtime.main → 见 805。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对 schedinit 职责与 GC 启动时序及版本相关行为；仅做了机翻解码（如 勾浪→Go、魅影→main、勾入t→goroutine、sky的NIP→schedinit 等拼写还原），技术结论未做更正。
