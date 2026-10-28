---
disableNunjucks: true
title: "805 newproc 与 mstart：创建 main 协程并启动调度"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：运行时 | 难度：L3 | 题型：原理题 | 频率：中 | 关键词：**newproc** / **mstart** / **runtime.main 协程**
> 原文锚点：第 88~92 段「调用 newproc 创建新 g 放入队列…g 执行 runtime.main…再 mstart 启动调度」

## 一句话总述
`schedinit` 之后，runtime 用 `newproc` 创建出一个专跑 `runtime.main` 的 goroutine 放进运行队列，再调 `mstart` 启动调度器，由调度器把这个 g 捞出来执行——用户 `main` 还远没轮到。

## 面试官视角
- 意图：是否理清"创建 g"与"启动调度"是两件事，且此时跑的是 runtime.main 而非用户 main。
- P5 知 newproc 建 g、mstart 起调度 / P6 能说 g 跑的是 runtime.main / P7 知 newproc 与 go 语句创建 g 同源。
- 红旗：以为 mstart 后就直接跑用户 main；混淆 runtime.main 与用户 main。
- 惊艳点：`go f()` 和启动建 runtime.main 都走 `newproc` —— 验证 `runtime.newproc` `[源码]`。

## 主问答
**Q（面试官原话）：** 调度器是怎么被启动的？一开始执行的是哪个函数？
**A：**
1. **结论**：`schedinit` 后用 `newproc` 创建执行 `runtime.main` 的 g 入队，再 `mstart` 启动调度器。
2. **机制**：`newproc` 是 Go 创建 goroutine 的统一入口（用户 `go` 语句也走它）；调度器从可运行队列取出该 g 执行 `runtime.main`。
3. **边界**：此时跑的是 `runtime.main`（里面才去调 init 与用户 main），不是用户 `main` 函数本身。
**加分层：** 把"启动调度"与"跑 runtime.main"分清，是分清 Go 启动模型的关键一步。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 谁启调度 | 概念 | mstart | 换题 |
| L2 | newproc 干啥 | 机制 | 建 runtime.main g | 判 P5 |
| L3 | 跑的是谁 | 边界 | runtime.main | 判 P6 |
| L4 | 与 go 同源 | 权衡 | newproc 统一 | 判 P6+ |
| L5 | 队列调度 | 实战 | 可运行队列 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本稳定 `[源码]` | 无 | newproc 建 g + mstart 启调度时序稳定 |

## 关键代码
```go
// 示意，未验证：启动期创建 runtime.main 的 g（概念，非完整源码）
// g := newproc(runtime.main)   // 创建执行 runtime.main 的 goroutine
// g 入可运行队列
// mstart()                     // 启动调度器，开始调度
```

## 总结与追问预判
- newproc 建 runtime.main 的 g 入队，mstart 启调度；此时仍非用户 main。
- 预判：runtime.main 流程 → 见 805；g0/m0 → 见 805。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对 newproc/mstart 职责与版本相关行为；仅做了机翻解码（如 勾浪→Go、魅影→main、勾入t→goroutine、六PROC→newproc、mstar→mstart 等拼写还原），技术结论未做更正。
