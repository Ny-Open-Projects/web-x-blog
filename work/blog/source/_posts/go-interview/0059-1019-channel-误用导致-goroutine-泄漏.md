---
disableNunjucks: true
title: "1019 channel 误用导致 goroutine 泄漏"
date: 2026-10-10 10:03:27
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：并发模型 | 难度：L3 | 题型：事故题 | 频率：高 | 关键词：**goroutine leak** / **for-select** / **ticker Stop**

> 原文锚点：第 86~126 段「for-select 不判断 ok 读关闭 channel 会空转泄漏；缓冲不足致永久阻塞；ticker 不 Stop 泄漏」

## 一句话总述
channel 误用会让 goroutine 永久阻塞或空转：for-select 读已关闭 channel 不判 ok 会一直命中零值空转；发送方多于缓冲容量会永久阻塞；ticker 不 Stop 也泄漏。一句话背法：**「channel 泄漏三类：for-select 不判 ok 空转 / 发送超缓冲永久阻塞 / ticker 不 Stop；阻塞 goroutine 不随函数返回消失，必须显式退出」**。

## 面试官视角
这是 goroutine 泄漏的"形态学"题。考官要你不仅知道泄漏概念，还能枚举典型形态并说出排查手段。
- **P5**：知道泄漏概念。
- **P6**：说清 ok 判断 + 缓冲 + ticker 三类。
- **P7**：知道用 `context` 取消、`defer ticker.Stop()`，线上用 pprof 的 goroutine profile 定位。
- **红旗**：for-select 读 channel 不接第二个 bool；以为函数返回阻塞的 goroutine 就自动没了。
- **惊艳点**：阻塞在无消费者 channel 上的 goroutine 不会自己结束，持续调用会累积到 for 循环次数级 `[经验]`。

## 主问答
**Q（面试官原话）：** 怎么我的 goroutine 数量一直涨？

**先铺垫（由浅入深第 1 层）**：goroutine 轻量但非零成本。一旦它被永久阻塞在 channel 操作上，它就再也不会被调度走，也不会被 GC 当垃圾收掉——每次触发都多一个"僵尸"，数量就一路涨。

1. **结论（第 2 层·机制）**：泄漏常来自三类——for-select 不判 ok 空转、发送超缓冲永久阻塞、ticker 不 Stop `[经验]`。
2. **机制（第 3 层）**：关闭的 channel 反复读得零值，case 永远选中空转占 CPU；缓冲 2 却 3 个发送方→必有一方永久阻塞；ticker 需手动 Stop 释放 `[源码]`。
3. **边界（第 4 层）**：**阻塞的 goroutine 不会因"调用它的函数返回"就消失**；是否会被 GC 回收取决于其阻塞对象是否仍可达，是运行时实现细节，不能依赖 `[经验]`。
4. **治理（第 5 层·实战）**：用 `context` 取消驱动退出，ticker 一律 `defer Stop()`；线上用 pprof 的 goroutine profile 看数量与栈 `[源码]`。
5. **验证（第 6 层·工具）**：`runtime.NumGoroutine()` 打点观察、或压测后取 pprof，定位泄漏点 `[经验]`。

## 追问链
| 档位 | 追问 | 答得到（背这句） | 答不出停在哪档 |
|------|------|------------------|----------------|
| L1 | 现象 | goroutine 数量涨 | — |
| L2 | 三类 | ok 判断 / 缓冲 / ticker | 停 L2：判 P5 |
| L3 | 判定 | 读关闭 channel 要判第二个 bool | 停 L3：判 P6 |
| L4 | 回收误区 | 不会随函数返回自动消失 | 停 L4：判 P6+ |
| L5 | 排查 | pprof goroutine profile 定位 | 停 L5：判 P7 |

## 版本与兼容性
| 维度 | 说明 |
|------|------|
| Go 全版本稳定 | 泄漏形态与 GC 对不可达阻塞 goroutine 的处理长期如此 `[经验]` |
| for-select 读关闭 channel | 必须判第二个 bool（ok），否则零值空转 |
| 缓冲通道 | 发送方数 > 容量且无接收方 → 永久阻塞 |
| ticker | `NewTicker` 后必须 `Stop()`，否则底层 goroutine 泄漏 |
| 排查工具 | `runtime.NumGoroutine()` / `pprof` 的 goroutine profile |

## 关键代码
```go
package main

import (
	"fmt"
	"time"
)

func main() {
	// ① 反例说明：for-select 必须判 ok，否则关闭后空转泄漏
	ch := make(chan int)
	go func() {
		for {
			v, ok := <-ch
			if !ok {
				return // 正确：判 ok 即退出；不判则 v 恒为 0、case 永远选中 -> CPU 空转
			}
			_ = v
		}
	}()
	close(ch)
	time.Sleep(50 * time.Millisecond)
	fmt.Println("channel drained without leak")

	// ② ticker 必须 Stop，否则底层 goroutine 永久驻留
	t := time.NewTicker(time.Second)
	defer t.Stop() // 漏掉这一行 -> ticker goroutine 泄漏
	<-t.C
	fmt.Println("ticker fired once, stopped cleanly")
}
```

## 总结与追问预判
**背这三句就够**：① **channel 泄漏三类：不判 ok 空转 / 超缓冲阻塞 / ticker 不 Stop**；② **阻塞的 goroutine 不随函数返回自动消失**；③ **治理靠 ctx 取消 + defer Stop + pprof 定位**。
**预判追问**：
- 「不判 ok 会怎样？」→ 关闭后读得零值、case 永远命中，CPU 空转而不是退出。
- 「函数返回后 goroutine 还在吗？」→ 不会自动消失；是否回收取决于阻塞对象是否可达，不可依赖。
- 「线上怎么查？」→ `runtime.NumGoroutine()` 打点 + pprof goroutine profile（见 1019 同号卡）。

## ⚠️ 原文纠错
原文称"函数返回之后这个 goroutine 就被回收掉了"，表述不严谨。纠正：goroutine 阻塞在 channel 上**不会**因为"调用它的外层函数返回"就自动结束；是否会被 GC 回收取决于其阻塞对象是否仍可达，这是运行时实现细节，不应作为可被依赖的退出机制。正确结论：生产上必须显式让 goroutine 退出（ctx 取消 / 关闭 channel / Stop ticker），不能依赖函数返回。
