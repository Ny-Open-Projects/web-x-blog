---
disableNunjucks: true
title: "1025 扩展：CyclicBarrier 循环栅栏 vs WaitGroup"
date: 2026-10-10 11:16:27
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go 并发 | 难度：中 | 题型：对比 | 频率：中 | 关键词：**CyclicBarrier、循环栅栏、WaitGroup、可复用、await**

> 原文锚点：第 62~92 段「CyclicBarrier 可复用栅栏、New/WithAction、await/reset、与 WaitGroup 区别」

## 一句话总述
CyclicBarrier（循环栅栏）让一组 goroutine 彼此等待，全部到达同一执行点后才一起放行，且可重复使用。与 WaitGroup 区别：WaitGroup 通常是「主协程等一组子协程结束」；CyclicBarrier 是「多个对等 goroutine 互相等到齐」，并且可复用、可配置到达时的回调动作。一句话背法：**「WaitGroup 一对多等结束；CyclicBarrier 多对等到齐且可循环、可带回调」**。

## 面试官视角
这是 singleflight 章节的拓展题。考官看你能不能说清两者定位差异：WaitGroup 是「一对多等待结束」，CyclicBarrier 是「多对多等待到齐 + 可循环」。能举 `New(n)` / `NewWithAction(n, fn)` / `await()` 的 API 与「最后一个到达者触发回调」更佳。
- **P5**：说出两者语义区别。
- **P6**：知道 CyclicBarrier 可复用、多对等到齐。
- **P7**：知道 NewWithAction 回调时机、broken/reset 中断处理。

## 主问答
**Q（面试官原话）：** CyclicBarrier 和 WaitGroup 有什么区别？

**先铺垫（由浅入深第 1 层）**：两者都能"等"，但等的姿态不同。WaitGroup 是"一个班长等一队兵干完"；CyclicBarrier 是"一队兵互相等，大家都到齐了才一起冲"，而且冲完还能再来一轮。这个"互相等 + 可循环"就是栅栏的本质。

1. **WaitGroup（第 2 层）**：计数器等待，主协程 `Add/Wait`，子协程 `Done`；语义是「等一组任务结束」，通常一次性。
2. **CyclicBarrier（第 3 层）**：参与数 n 的栅栏，`await()` 表示「我已到达」；所有 n 个参与者都 await 后才一起放行，放行后可再次循环使用。
3. **回调动作（第 4 层）**：`NewWithAction(n, fn)` 在「最后一个参与者到达、其余尚未放行前」执行 fn，用于放行前的共享状态变更。
4. **错误处理（第 5 层）**：await 可被 context 中断返回 broken 错误；`IsBroken()` 判断栅栏是否处于中断态；`reset()` 可重置。
5. **误用风险（第 6 层）**：参与者数量必须凑齐 n 个才能放行，少一个就全员卡死；别把它当 WaitGroup 的"主等子"用，定位就错了。

## 追问链
| 档位 | 追问 | 答得到（背这句） | 答不出停在哪档 |
|------|------|------------------|----------------|
| L1 | 两者区别？ | WG 一对多等结束；CB 多对等到齐 | — |
| L2 | 可复用？ | CB 放行后可再循环 | 停 L2：当一次性 |
| L3 | 回调时机？ | 最后到达者触发 action | 停 L3：说不清 |
| L4 | 中断处理？ | broken/IsBroken/reset | 停 L4：不知中断 |
| L5 | 适用场景？ | 多 goroutine 必须到齐 | 停 L5：选错原语 |

## 版本与兼容性
| 维度 | 说明 |
|------|------|
| WaitGroup | 标准库 `sync.WaitGroup`，一对多等结束，通常一次性 |
| CyclicBarrier | 三方库（如 `github.com/marusama/cyclicbarrier`），多对等到齐 + 可循环 |
| API | `New(n)` / `NewWithAction(n, fn)` / `Await()` / `Reset()` / `IsBroken()` |
| 回调 | `NewWithAction` 的 fn 在最后到达者到达、他人未放行前执行 |
| 中断 | `Await()` 可被中断返回 broken；`reset()` 重置栅栏 |
| Go 版本 | 与 Go 版本无关，本项目实测 Go 1.26.5 |

## 关键代码
```go
package main

import (
	"fmt"
	"sync"
)

// 极简 CyclicBarrier 重实现：n 个 goroutine 互相等到齐，可循环复用
type Barrier struct {
	n    int
	gen  int
	mu   sync.Mutex
	cond *sync.Cond
	cur  int
}

func NewBarrier(n int) *Barrier {
	b := &Barrier{n: n}
	b.cond = sync.NewCond(&b.mu)
	return b
}

// Await：到达点；等齐 n 个后一起放行，并进入下一代（可循环）
func (b *Barrier) Await() {
	b.mu.Lock()
	b.cur++
	if b.cur == b.n {
		b.cur = 0
		b.gen++
		b.cond.Broadcast() // 最后到达者唤醒所有人
	} else {
		g := b.gen
		for b.gen == g {
			b.cond.Wait()
		}
	}
	b.mu.Unlock()
}

func main() {
	b := NewBarrier(3)
	var wg sync.WaitGroup
	for r := 0; r < 2; r++ { // 循环两轮
		for i := 0; i < 3; i++ {
			wg.Add(1)
			go func(id, round int) {
				defer wg.Done()
				// 各干各的活...
				b.Await() // 等 3 个到齐才继续
				fmt.Printf("round %d goroutine %d 放行\n", round, id)
			}(i, r)
		}
		wg.Wait()
	}
}
```

## 总结与追问预判
**背这三句就够**：① **WaitGroup 是一对多「主等子结束」，通常一次性**；② **CyclicBarrier 是多对多「互相等到齐」，放行后可循环复用**；③ **NewWithAction 在最后到达者处触发回调；await 可被中断返回 broken**。
**预判追问**：
- 「可复用怎么理解？」→ 一轮到齐放行后，栅栏自动进入下一代，下一轮同样等齐再用（见本卡第 3 层）。
- 「回调什么时候跑？」→ 最后一个到达者 await 时、其余尚未放行前（见本卡第 4 层）。
- 「singleflight 才是本节重点？」→ 是，栅栏只是拓展对比（见 1025 主卡）。

## ⚠️ 原文纠错
1. 事实核校：CyclicBarrier 可复用、多对等到齐、New/NewWithAction/await/reset/IsBroken、与 WaitGroup 语义差异——均正确，本卡为准。
2. 崩坏词归一：源码将 Go/goroutine/CyclicBarrier/WaitGroup 等音译为多组崩坏词；本卡统一为规范术语。
3. 补强：本卡将「单行 API 片段」升级为**完整可运行的极简栅栏重实现**（package main），实际运行可验证「3 个到齐才放行 + 循环两轮」，把对比结论落到可跑证据。
