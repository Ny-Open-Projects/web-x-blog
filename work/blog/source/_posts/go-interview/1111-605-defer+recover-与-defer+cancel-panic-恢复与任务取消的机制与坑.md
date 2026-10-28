---
disableNunjucks: true
title: "605 defer+recover 与 defer+cancel：panic 恢复与任务取消的机制与坑"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go 错误处理 / defer | 难度：L3 | 题型：机制题 | 频率：高 | 关键词：**defer recover** / **recover 必须直接** / **context cancel** / **取消任务** / **主协程退通知子退**
> 原文锚点：第 29~43 段「defer recover捕获panic(打印栈);defer cancel()(context返回cancel,主协程退出通知子协程提前退避免浪费资源)」

## 一句话总述
`defer` 内嵌 `recover()` 可在 panic 时收尾（打印栈、避免进程崩）；`defer cancel()` 则在函数退出前取消 context，**主协程退出即通知依赖该 context 的子协程提前退出**，避免资源浪费。两个关键坑：① `recover` 必须**直接在 defer 函数体内**调用（包在嵌套函数无效）；② cancel 要及时，否则子协程泄漏。

## 面试官视角
- 意图：区分"recover 恢复"与"cancel 取消"两类 defer 收尾，并讲清各自坑点。
- P5 知 defer+recover 捕获 panic、defer cancel 取消；P6 知 recover 必须直接调用、cancel 防子协程泄漏；P7 知 recover 只在当前 goroutine 生效（不跨协程）、cancel 的 ctx 传播链。
- 红旗：把 recover 写在嵌套函数里以为能捕获；或忘了 defer cancel 导致子协程空转。
- 惊艳点：点出"recover 只恢复当前 goroutine 的 panic，跨协程需各自 recover" `[边界]` 见 605（场景清单）、605-defer-lifo-order（LIFO）、602-withvalue-timeout（context 取值/超时）、1022-goroutine-leak（协程泄漏）。

## 主问答
**Q（面试官原话）：** defer 里 recover 和 cancel 怎么用、有什么坑？
**A：**
1. **recover 直接调用**：`defer func(){ if r:=recover(); r!=nil {...} }()` 才能捕获 panic；若把 recover 包进嵌套函数再被 defer 调用，则捕获不到（recover 必须直接在 defer 函数体内）。
2. **recover 仅当前协程**：它只恢复**当前 goroutine** 的 panic，其他 goroutine 需各自 defer recover。
3. **defer cancel 取消任务**：`ctx, cancel := context.WithCancel(...); defer cancel()` 让函数退出前取消 ctx，依赖该 ctx 的子协程从 `ctx.Done()` 唤醒提前退出，避免空转浪费资源。
4. **cancel 要及时**：忘写 `defer cancel` 会导致子协程泄漏（一直阻塞在 ctx 上）。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | recover 怎么写 | 基础 | defer 函数内直接调用 | 判 P5 |
| L2 | 嵌套无效 | 陷阱 | recover 须直接 | 判 P6 |
| L3 | 跨协程 | 边界 | 仅当前 goroutine | 判 P6+ |
| L4 | cancel 作用 | 机制 | 主退通知子退 | 判 P7 |
| L5 | 忘了 cancel | 后果 | 子协程泄漏 | 判 P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 所有版本 | 无 | recover 直接调用；defer cancel 防泄漏 |

## 关键代码
```go
package main

import (
	"context"
	"fmt"
)

// recover 必须直接在 defer 函数体内
func safe() {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("捕获:", r)
		}
	}()
	panic("boom")
}

// context cancel：主协程退出前取消，通知子协程提前退出
func withCancel() {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel() // 忘写则子协程泄漏
	go func() {
		<-ctx.Done() // 被 cancel 唤醒，提前退出
	}()
}
```

## 总结与追问预判
- defer+recover 须直接调用、仅当前协程；defer cancel 主退通知子退、忘写则泄漏。
- 预判：场景清单 → 见 605；LIFO → 见 605；context 取值/超时 → 见 602；协程泄漏 → 见 1022。

## ⚠️ 原文纠错
源码将若干专有名词音译为崩坏词（英文术语错读为近似音、部分中文术语写错字），本卡统一为规范术语 `[经验]`。事实核校：defer recover 捕获 panic、recover 须直接调用且仅当前协程、defer cancel 取消 context 通知子协程退出、忘 cancel 泄漏——均正确，未做更正。
