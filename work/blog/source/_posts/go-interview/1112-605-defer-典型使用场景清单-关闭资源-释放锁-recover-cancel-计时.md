---
disableNunjucks: true
title: "605 defer 典型使用场景清单（关闭资源/释放锁/recover/cancel/计时）"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go 错误处理 / defer | 难度：L3 | 题型：用法题 | 频率：高 | 关键词：**defer 场景** / **关闭文件** / **释放锁** / **recover** / **context cancel** / **计时**
> 原文锚点：第 10~47 段「场景:关闭文件/HTTP response body/DB连接/释放锁/recover捕获panic/context cancel取消任务/记录耗时;申请即defer关闭好习惯」

## 一句话总述
`defer` 最适合"函数退出前必须执行的收尾动作"，典型场景：① 关闭文件/HTTP response body/DB 连接 ② 释放锁 ③ `recover` 捕获 panic ④ `cancel()` 取消 context 通知子协程退出 ⑤ 记录函数耗时。黄金习惯：**申请资源后立即 `defer` 释放**，即使后续提前 return/panic 也能保证执行。

## 面试官视角
- 意图：考察 defer 的实战落点，而非只背"延迟执行"；能否枚举常见收尾场景。
- P5 知关闭文件/锁/recover；P6 知 HTTP body、DB 连接、context cancel、计时；P7 知"申请即 defer"习惯、cancel 用于主协程退通知子协程早退。
- 红旗：手动关闭且漏了提前 return 路径；或不知 HTTP response.Body 也要关。
- 惊艳点：点出"defer 保证提前退出（错误/panic）路径也不漏收尾" `[边界]` 见 605（LIFO 结构）、605-defer-recover-cancel（recover/cancel 机制）、607-defer-exec-order（执行时机）、713-graceful-shutdown（优雅退出）。

## 主问答
**Q（面试官原话）：** defer 通常在哪些场景使用？
**A：**
1. **关闭资源**：打开文件、HTTP `response.Body`、DB 连接后立刻 `defer` 关闭，避免忘记或提前 return 漏关。
2. **释放锁**：加锁后 `defer` 解锁，保证函数任何路径退出都释放，不会死锁/忘解锁。
3. **recover 捕获 panic**：`defer func(){ if r:=recover(); r!=nil {...} }()` 在 panic 时收尾、打印栈。
4. **取消 context / 计时**：`defer cancel()` 主协程退出通知子协程早退；`defer` 记起始时间算总耗时。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 常见场景 | 基础 | 关文件/锁/recover | 判 P5 |
| L2 | 还要关啥 | 记忆 | HTTP body/DB/cancel/计时 | 判 P6 |
| L3 | 为何申请即 defer | 习惯 | 提前退出也收尾 | 判 P6+ |
| L4 | cancel 用途 | 进阶 | 主退通知子退 | 判 P7 |
| L5 | 与优雅退出 | 边界 | 收尾+信号 | 判 P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 所有版本 | 无 | 收尾场景清单；申请即 defer |

## 关键代码
```go
package main

import (
	"context"
	"fmt"
	"os"
	"time"
)

func main() {
	f, _ := os.Open("x.txt")
	defer f.Close() // 场景1：关闭文件

	defer func() {
		if r := recover(); r != nil { // 场景2：recover 捕获 panic
			fmt.Println("recovered:", r)
		}
	}()

	ctx, cancel := context.WithCancel(context.Background())
	defer cancel() // 场景3：取消 context，主协程退出通知子协程

	start := time.Now()
	defer func() { fmt.Println("cost:", time.Since(start)) }() // 场景4：记录耗时
	_ = ctx
}
```

## 总结与追问预判
- defer 收尾场景：关资源/释放锁/recover/cancel/计时；"申请即 defer"确保提前退出也收尾。
- 预判：LIFO 结构 → 见 605；recover/cancel 机制 → 见 605；执行时机 → 见 607；优雅退出 → 见 713。

## ⚠️ 原文纠错
源码将若干专有名词音译为崩坏词（英文术语错读为近似音、部分中文术语写错字），本卡统一为规范术语 `[经验]`。事实核校：defer 场景(关文件/HTTP body/DB/释放锁/recover/context cancel/计时)、申请即 defer 习惯、提前退出也收尾——均正确，未做更正。
