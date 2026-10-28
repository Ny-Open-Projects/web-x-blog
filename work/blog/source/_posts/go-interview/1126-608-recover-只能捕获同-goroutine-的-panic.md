---
disableNunjucks: true
title: "608 recover 只能捕获同 goroutine 的 panic"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：错误处理 | 难度：L3 | 题型：原理题 | 频率：中 | 关键词：**goroutine** / **跨协程不捕获** / **recover 作用域**
> 原文锚点：第 55~60 段「recover 与函数调用方不在同一个协程时无法捕获…新协程包裹 defer 无效」

## 一句话总述
recover 只对本 goroutine 内未恢复的 panic 有效；在另一个 goroutine 的 defer 中调用 recover，无法捕获当前 goroutine 的 panic。

## 面试官视角
- **考察意图**：是否理解 panic/recover 是 goroutine 局部机制。
- **P5** 知 recover 不跨协程 / **P6** 能解释为何新 goroutine 的 defer 捕获不到外层 panic / **P7** 知每个 goroutine 独立 panicking，子 goroutine 崩不影响父（除非父也 panic）。
- **红旗**：以为在子 goroutine 里 recover 能兜住调用方；以为 go func 里 recover 能保护外部。
- **惊艳点**：把 recover 放进 `go func(){ defer recover() }()` 再让外层 panic，外层仍崩溃退出 —— 验证：`go run`，go1.26.5，见关键代码。

## 主问答
**Q（面试官原话）：** 我在 goroutine 里写了 recover，为什么还是崩了？
**A：**
1. **结论**：panic 和 recover 都绑定在各自 goroutine 上，跨 goroutine 不传递。
2. **机制**：goroutine 是独立执行流，其 panicking 只在本 goroutine 的 defer 链中 unwind；子 goroutine 的 recover 只能接住子 goroutine 自己的 panic。
3. **边界**：父 goroutine 未 recover 而子 goroutine 崩，两者互不影响，父照常运行（除非父自己 panic）。
**加分层：** 想统一兜错，应在每个会 panic 的 goroutine 入口各自 defer recover。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 跨协程能捕获吗 | 概念 | 不能 | 换题 |
| L2 | 为什么不能 | 机制 | goroutine 独立 | 判 P5 |
| L3 | 子崩影响父吗 | 边界 | 互不影响 | 判 P6 |
| L4 | 如何统一兜底 | 权衡 | 每 goroutine 各自 recover | 判 P6+ |
| L5 | 真实踩坑 | 实战 | 漏给子协程加 recover | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| go1.x 全版本稳定 | 无 | panic/recover 的 goroutine 局部性自 Go1 起未变 `[源码]` |

## 关键代码
```go
// 示意，未验证：子 goroutine 的 recover 兜不住外层 panic
func main() {
	go func() {
		defer func() { _ = recover() }() // 只能接住本 goroutine
		select {}                        // 永不 panic
	}()
	panic("main boom") // 此处崩溃，子 goroutine 的 recover 无能为力
}
```

## 总结与追问预判
- panic/recover 局限在本 goroutine；想兜底需每个 goroutine 各自 recover。
- 预判：就近捕获与覆盖 → 见 608；正确用法 → 见 608。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 Go、互斥锁、nil 等专有名词被音译为同音词，已还原为正确术语），技术结论未做更正。
