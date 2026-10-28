---
disableNunjucks: true
title: "1020 WaitGroup.Add 时机陷阱（必须 goroutine 外）"
date: 2026-10-10 09:50:25
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go 并发/sync | 难度：L3 | 题型：陷阱题 | 频率：高 | 关键词：**Add 在 goroutine 外** / **Wait 竞态** / **计数归零提前返回** / **负计数 panic**

> 原文锚点：第 17~24 段「WaitGroup.Add 写在子协程内部→主协程 Wait 可能先于 Add 执行→计数异常」

## 一句话总述
`WaitGroup.Add` **必须在启动 goroutine 之前、Wait 之前、在主协程里调用**。若把 `Add` 写进子协程内部，goroutine 调度时机不确定，主协程的 `Wait()` 可能先于任何 `Add` 执行——计数仍是 0 则 Wait 立即返回（子任务根本没被等），或 Add 晚于 Wait 触发负计数 panic。一句话背法：**「Add 外提、Done 在内、Wait 收尾，时序铁律」**。

## 面试官视角
- 考察意图：是否真理解 Add/Done/Wait 的时序契约，而不只是会写。
- **P5**：知 Add/Done/Wait 语义。
- **P6**：能讲清"Add 放 goroutine 内 → Wait 竞态"。
- **P7**：能讲负计数 panic 与修复，并点出"goroutine 调度不确定 → Wait 可能抢在 Add 前"这一竞态本质。
- 红旗：把 Add 写在 `go func(){...}` 内部；以为"先 go 后 Add 也行"。

## 主问答
**Q（面试官原话）：** WaitGroup 用的时候还有什么坑，除了传指针？

**先铺垫（由浅入深第 1 层）**：WaitGroup 靠一个计数器工作——`Add(n)` 加 n、`Done()` 减 1、`Wait()` 阻塞到计数归零。坑不在"加多少"，而在"什么时候加"。

1. **Add 时机是隐性坑（第 2 层）**：`Add` 必须写在 **goroutine 外、Wait 之前**；若写在子协程里，主协程 `Wait()` 可能在第一个 `Add` 执行前就跑完——计数还 0，Wait 直接返回，子任务没被等。
2. **后果两样（第 3 层）**：轻则"等了个寂寞"（结果小于预期如 <1000），重则 `Add` 在 `Wait` 之后发生导致 **负数计数 panic**（`sync: negative WaitGroup counter`）。
3. **修复 = 外提 Add（第 4 层）**：启动 goroutine 前先 `Add(1)`，goroutine 内只 `Done()`，主协程 `Wait()`——时序契约稳。
4. **相关但不同（第 5 层）**："Add 在 goroutine 内"与"传指针/noCopy"是两码事；另要注意 `Done` 必须写在 goroutine 体内（见 913）。
5. **替代（第 6 层）**：需要"任一个出错即取消全部"时用 `golang.org/x/sync/errgroup`，比手写 Add/Wait + error 通道更稳。

## 追问链
| 档位 | 追问 | 答得到（背这句） | 答不出停在哪档 |
|------|------|------------------|----------------|
| L1 | Add 干嘛？ | 增计数，标记待等任务数 | — |
| L2 | 放 goroutine 内？ | Wait 可能抢在 Add 前，竞态 | 停 L2：判 P6 |
| L3 | 后果？ | 不等/负计数 panic | 停 L3：判 P6+ |
| L4 | 怎么修？ | 外提 Add，goroutine 内只 Done | 停 L4：判 P7 |
| L5 | 替代方案？ | errgroup 管错误与取消 | 停 L5：判 P7+ |

## 版本与兼容性
| 维度 | 说明 |
|------|------|
| 结论成立版本 | Go 1.0+（sync）时序契约长期成立：Add 必须在 Wait 前调用 |
| 并发安全 | WaitGroup 本身并发安全，但"Add 与 Wait 的时序"由调用方保证 |
| 注意 | `noCopy`：WaitGroup 不可值拷贝传递（会被 vet 抓）；用指针或地址传递 |
| Go 版本 | 与 Go 版本无关；本项目实测 Go 1.26.5 |

## 关键代码
```go
package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

func main() {
	var wg sync.WaitGroup
	var cnt int32

	// ❌ 错误：Add 写进 goroutine 内——Wait 可能抢在 Add 前，cnt 可能 < 1000 甚至 panic
	// for i := 0; i < 1000; i++ {
	//     go func() { wg.Add(1); atomic.AddInt32(&cnt, 1); wg.Done() }()
	// }

	// ✅ 正确：Add 写在 goroutine 外
	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			atomic.AddInt32(&cnt, 1)
		}()
	}
	wg.Wait() // 此刻计数稳定为 1000
	fmt.Println("cnt =", atomic.LoadInt32(&cnt)) // 1000
}
```

## 总结与追问预判
**背这三句就够**：① **Add 必须在 goroutine 外、Wait 之前**；② **否则 Wait 竞态，可能不等或负计数 panic**；③ **goroutine 内只调 Done**。
**预判追问**：
- 「传值拷贝 WaitGroup 会怎样？」→ 拷贝的是旧计数、vet 报 noCopy，必须用指针（见 913）。
- 「多个 goroutine 出错怎么汇总？」→ `errgroup.Group`，任一 `Go` 返回 error 即取消其余（见 1020 相关）。
- 「Done 漏调呢？」→ Wait 永久阻塞（死锁），故 Done 一律 `defer`。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡统一为规范术语（SYC→sync、勾引性→goroutine、购入t→goroutine、主学程→主协程、勾引性的调度→goroutine 调度等）；技术结论未做事实性更正。本卡第 5 层补「Add 时机坑 ≠ noCopy 坑」的区分，原卡未显式点出。
