---
disableNunjucks: true
title: "1012 自旋锁的实现（atomic CAS 忙等）"
date: 2026-10-10 10:23:36
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go / 并发 / 锁 | 难度：L3 | 题型：实现题 | 频率：中 | 关键词：**自旋锁** / **atomic.CompareAndSwap** / **忙等待** / **int32 状态** / **无锁编程**

> 原文锚点：第 6~18 段「spanlock 包：int32 状态(0解锁/1获取)，lock 调 atomic CAS 从0改1自旋循环直到成功，unlock 用 store/swap 置0；goroutine 自增加锁后预期2000」

## 一句话总述
自旋锁用**原子操作**实现：一个 `int32` 状态值（0=解锁、1=获取），`Lock` 在循环里 `atomic.CompareAndSwapInt32(0→1)` 不断尝试（忙等）直到成功；`Unlock` 用 `store`/`swap` 把状态置 0。获取锁的线程不睡眠、空转 CPU 直到拿到锁——本质是**无锁编程**思路。一句话背法：**「自旋锁=atomic CAS 忙等：int32 状态 0解锁/1获取，Lock 循环 CAS 自旋、Unlock store 置0；不睡眠空转CPU，适合极短临界区」**。

## 面试官视角
这是考察"不依赖 sync.Mutex 手搓一把锁"的实现题，并要讲清"忙等"与"睡眠"的差异。
- **P5**：知道用 atomic CAS 实现。
- **P6**：知道状态 0/1、lock 自旋循环、unlock 置 0。
- **P7**：知道"忙等空耗 CPU、适合极短临界区" `[边界]` 见 925（sync.Mutex 实现，走休眠而非忙等）、1013-mutex-pessimistic（Mutex 属悲观锁）。
- **红旗**：以为自旋锁不加锁也安全；或以为自旋锁不会浪费 CPU。
- **惊艳点**：点出"自旋锁是用户态无锁思路，靠 CAS 轮询；与 Go runtime M 自旋找 G 同源不同层" `[经验]`。

## 主问答
**Q（面试官原话）：** 自旋锁怎么实现？

**先铺垫（由浅入深第 1 层）**：自旋锁和 Mutex 保护的是同一件事，但"拿不到锁时在干嘛"完全不同——Mutex 去睡觉，自旋锁在 CPU 上死等。这份"死等"就是用一条原子指令实现的最小锁。

1. **状态字段（第 2 层·机制）**：用 `int32` 状态，0 表示未加锁、1 表示已加锁 `[源码]`。
2. **Lock（忙等）（第 3 层）**：在 `for` 循环里 `atomic.CompareAndSwapInt32(&state, 0, 1)`，只有从 0 改成 1 才算抢到锁；改不成说明别人持有，继续循环重试（自旋）`[源码]` sync/atomic。
3. **Unlock（第 4 层）**：直接 `atomic.StoreInt32(&state, 0)`（或 `Swap`），把状态置回 0 释放锁 `[源码]`。
4. **验证（第 5 层）**：多 goroutine 对共享计数自增、各自加锁/解锁、WaitGroup 同步，各 1000 次得 2000，证明锁有效 `[实测]`。
5. **边界（第 6 层）**：忙等空耗 CPU，只适合极短临界区；长持有/高竞争应退回 Mutex；与 runtime M 自旋找 G 同源不同层 `[经验]`。

## 追问链
| 档位 | 追问 | 答得到（背这句） | 答不出停在哪档 |
|------|------|------------------|----------------|
| L1 | 用什么实现 | atomic CAS | — |
| L2 | 状态含义 | 0解锁/1获取 | 停 L2：判 P5 |
| L3 | Lock 怎么等 | for 循环 CAS 自旋 | 停 L3：判 P6 |
| L4 | 与互斥锁区别 | 忙等 vs 睡眠 | 停 L4：判 P6+ |
| L5 | 何时不该用 | 长持有/高竞争浪费 CPU | 停 L5：判 P7 |

## 版本与兼容性
| 维度 | 说明 |
|------|------|
| Go 全版本 | atomic CAS 自旋是通用写法；Go 另提供 sync/atomic 包原语 |
| 状态位 | int32（或 int32 配对齐），0=解锁 1=获取 |
| 适用边界 | 极短临界区；长持有/高竞争退回 sync.Mutex |
| 关联 | Mutex 实现见 925；选型见 1012 锁选型决策；自旋vs互斥见 1012 |

## 关键代码
```go
package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

// 自旋锁：用 atomic CAS 忙等实现（用户态无锁思路）
type SpinLock struct{ state int32 }

func (l *SpinLock) Lock() {
	for !atomic.CompareAndSwapInt32(&l.state, 0, 1) {
		// 自旋：不断重试，不睡眠
	}
}
func (l *SpinLock) Unlock() {
	atomic.StoreInt32(&l.state, 0) // 释放
}

func main() {
	var sl SpinLock
	var cnt int32
	var wg sync.WaitGroup
	for i := 0; i < 100; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			sl.Lock()
			cnt++ // 极短临界区
			sl.Unlock()
		}()
	}
	wg.Wait()
	fmt.Println("cnt =", cnt) // 100（锁有效，无竞争丢失）
}
```

## 总结与追问预判
**背这三句就够**：① **自旋锁=int32 状态 0/1 + atomic CAS 忙等**；② **Lock 循环 CAS 自旋、Unlock store 置 0**；③ **不睡眠空转 CPU，只适合极短临界区**。
**预判追问**：
- 「和 Mutex 区别？」→ 忙等 vs 睡眠（见 1012 自旋锁vs互斥锁）。
- 「什么时候该用？」→ 临界区极短；否则用 Mutex（见 1012 锁选型决策）。
- 「runtime 也自旋？」→ M 自旋找 G，同源不同层（见 815）。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词（自旋锁/互斥锁等专有名词被错读为近似音、atomic/CAS 等英文术语写错字），本卡统一为规范术语 `[经验]`。事实核校：自旋锁=atomic CAS 忙等（0解锁/1获取）、互斥锁=无竞争先 CAS 快路径否则睡眠、读写锁底层含互斥锁故写锁不等价互斥——均正确，未做更正。
