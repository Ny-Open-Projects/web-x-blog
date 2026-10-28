---
disableNunjucks: true
title: "1015 channel 锁的四道坑：不可重入、无 TryLock、panic 与误用"
date: 2026-10-10 10:00:07
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：并发模型 | 难度：L3 | 题型：陷阱题 | 频率：中高 | 关键词：**不可重入、TryLock、defer 解锁、死锁、通信共享内存**

> 原文锚点：第 31~36 段「推荐使用 channel 并不是因为 channel 的性能有多高，主要是它符合不要通过共享内存来通信，而是通过通信来共享内存的设计哲学」

## 一句话总述
推崇 channel 是因为它契合**用通信共享内存**的设计哲学，不代表性能更高；当锁用它时会踩到**不可重入、无原生 TryLock、漏解锁即死锁**三道坑。一句话背法：**「channel 锁是通信哲学下的玩具——不可重入、无 TryLock、漏解锁即死锁，正经互斥优先标准库 Mutex」**。

## 面试官视角
singleflight 是 Go 并发高频题的邻位考点。考官想看你有没有被"官方推荐 channel"这句话带偏。能区分「推荐的是通信模型」与「拿通道当锁用」是关键。
- **P5**：说出"官方推荐用 channel"这句话。
- **P6**：讲清通道锁的三道坑（不可重入 / 无 TryLock / 漏解锁死锁）。
- **P7**：纠正为**推荐的是通信模型，不是把通道当锁用**；能指出同一 goroutine 二次加锁会永久阻塞，且标准库 `Mutex` 有 `TryLock` 而通道锁没有。

## 主问答
**Q（面试官原话）：** 既然官方推崇 channel，是不是该处处用它替代锁？

**先铺垫（由浅入深第 1 层）**："用 channel"这句话的出处是 Go 设计哲学——**不要通过共享内存来通信，而要通过通信来共享内存**。它的本意是"用数据流表达协作"，不是"把 `chan struct{}` 当 `Mutex` 使"。把二者混为一谈，就会在互斥场景踩坑。

1. **定位（第 2 层·机制）**：选择通道是因为它符合"通过通信共享内存"的设计哲学，能更简单解决复杂协作问题；**并不代表它比锁快** `[源码]`。
2. **对比（第 3 层）**：在"互斥保护一段临界区"这个场景上，标准库 `sync.Mutex` **既简单又快**，通道实现的锁没有性能优势 `[实测]`。
3. **不可重入（第 4 层）**：用「写入=加锁、读出=解锁」的带缓冲通道模拟锁时，同一 goroutine 连续加锁两次会阻塞在第二次写入上；实测 200ms 仍未返回，等价于自锁 `[实测]`。
4. **无原生 TryLock（第 5 层）**：标准库 `Mutex` 提供 `TryLock` 尝试加锁；通道锁要自己用 `select` + `default` 模拟，且语义不完全一致（拿不到锁时行为靠自己定义）`[经验]`。
5. **漏解锁即死锁（第 6 层）**：解锁动作是"从通道读出"，一旦临界区 `panic` 或提前 `return` 而没读出，后续所有加锁方永久阻塞；**必须 `defer` 解锁** `[源码]`。

## 追问链
| 档位 | 追问 | 答得到（背这句） | 答不出停在哪档 |
|------|------|------------------|----------------|
| L1 | 推崇 channel 的真实理由？ | 推荐的是通信模型，不是性能 | — |
| L2 | 处处替代锁对吗？ | 互斥场景 Mutex 更简单更快 | 停 L2：说不出不合适 |
| L3 | 能重入吗？ | 通道锁不可重入，二次加锁自锁 | 停 L3：答不出不可重入 |
| L4 | 有 TryLock 吗？ | 无原生支持，需 select+default 模拟 | 停 L4：说不出没有 TryLock |
| L5 | 临界区 panic 会怎样？ | 漏解锁则后续全部永久阻塞 | 停 L5：答不出必须 defer |

## 版本与兼容性
| 维度 | 说明 |
|------|------|
| Go 1.0 起 | 通道语义稳定，重入必阻塞（写入已满通道） |
| Go 1.18 起 | `sync.Mutex` 新增 `TryLock`；通道锁仍无等价能力 |
| 任意版本 | 设计哲学未变：保护共享状态优先用 `sync.Mutex` |
| 性能实测 | 通道锁在互斥场景无优势，且多一次 channel 收发开销 `[实测]` |
| 并发安全 | 通道锁本身靠 channel 串行化，但"漏解锁"是逻辑死锁，非数据竞争 |

## 关键代码
```go
package main

import (
	"fmt"
	"time"
)

// ChLock 用带缓冲通道实现的互斥锁：写入=加锁，读出=解锁
type ChLock struct {
	ch chan struct{}
}

func NewChLock() *ChLock { return &ChLock{ch: make(chan struct{}, 1)} }
func (m *ChLock) Lock()  { m.ch <- struct{}{} }
func (m *ChLock) Unlock() { <-m.ch }

// TryLock 模拟：select + default 非阻塞；标准库 Mutex 原生就有，通道锁需手写
func (m *ChLock) TryLock() bool {
	select {
	case m.ch <- struct{}{}:
		return true
	default:
		return false
	}
}

func main() {
	m := NewChLock()

	// ① 正常加锁/解锁
	m.Lock()
	fmt.Println("locked ok")
	m.Unlock()

	// ② TryLock 模拟：主协程占着锁时，另一 TryLock 返回 false 且不阻塞
	m.Lock()
	if m.TryLock() {
		fmt.Println("should not happen")
		m.Unlock()
	} else {
		fmt.Println("trylock failed, no block") // 输出这句
	}
	m.Unlock()

	// ③ 不可重入：同一 goroutine 连续 Lock 两次会永久阻塞（用超时演示，不真死等）
	done := make(chan struct{})
	go func() {
		m.Lock()
		fmt.Println("first lock ok")
		m.Lock() // 第二次写入：通道已满，永久阻塞
		fmt.Println("second lock ok (never reached)")
		close(done)
	}()
	select {
	case <-done:
	case <-time.After(200 * time.Millisecond):
		fmt.Println("200ms 未返回 -> 确认不可重入自锁")
	}
}
```

## 总结与追问预判
**背这三句就够**：① **推荐 channel 是通信模型，不是性能**；② **通道锁不可重入、无原生 TryLock、漏解锁即死锁**；③ **互斥场景优先 `sync.Mutex`**。
**预判追问**：
- 「通道真正擅长什么？」→ 表达所有权流转/信号量/任务编排，见同批信号量卡。
- 「那什么时候该用 channel？」→ 多 goroutine 协作、数据流传递、需要超时/取消的场景。
- 「TryLock 在通道锁里怎么写？」→ `select` + `default` 非阻塞写入（见关键代码②）。

## ⚠️ 原文纠错
1. 事实核校：原文"推荐 channel 不是因为性能"准确；补充——这也是**通道锁性能更差却不推荐替换互斥锁**的完整理由，两句要连起来答 `[经验]`。
2. 补充：原文未提重入与异常路径风险；通道锁与互斥锁同样**不可重入**，且必须 `defer` 解锁，否则一次 panic 就会拖垮全部等待方 `[源码]`。
3. 崩坏词归一：源码将 channel、goroutine、互斥锁、共享内存等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
