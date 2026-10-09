# 1023 无缓冲 channel 同步 vs 信号量：等待退出与限并发的边界

> 分类：Go 并发 / 同步 | 难度：L3 | 题型：技巧题 | 频率：中 | 关键词：**无缓冲 channel 同步** / **semaphore** / **P/V 操作** / **限并发** / **资源池**
> 原文锚点：第 25~47 段「无缓冲channel同步(子末行写主读全部);信号量(semaphore包,P/V)此场景不推荐,本职限并发数;本质是资源池防过度使用」

## 一句话总述
除 WaitGroup 外，也可用**无缓冲 channel** 同步主协程（子协程末行写、主依次读全部值），但多协程必须读满全部值；**信号量**（`semaphore` 包，P 获取/V 释放）也能"等全释放"，只是它的本职是**限制并发数、保护资源池**，并非"等待退出"的合适原语，此场景不推荐。

## 面试官视角
- 意图：厘清"等待退出"与"限并发"两类不同诉求对应的原语，避免误用信号量。
- P5 知 channel 同步与信号量 P/V；P6 知多协程 channel 需读满、信号量限并发；P7 知信号量是资源池语义、与 WaitGroup 职责边界。
- 红旗：用信号量去"等 N 个协程退出"（语义错位）；或 channel 同步只读了一次导致漏等。
- 惊艳点：点出"信号量本质是资源池（P 减/V 增），保证资源不被过度使用，不是完成计数" `[边界]` 见 1023（选型）、1015-channel-semaphore（信号量限并发实现）、609-channel-send-recv（无缓冲阻塞）。

## 主问答
**Q（面试官原话）：** 除了 WaitGroup，channel 和信号量怎么用来等协程？
**A：**
1. **无缓冲 channel 同步**：子协程把"写 channel"放最后一行，主协程依次读出全部值即代表全完成；多协程必须读满 N 个，否则漏等。
2. **信号量 P/V**：启动前 `Acquire`（P 减），完成后 `Release`（V 增），主协程获取全部即表示全释放——但这是"资源池"语义。
3. **信号量本职限并发**：它的设计目标是限制同时执行的协程数、确保资源池不被过度使用，并非"等待退出"的原语，本场景应优先 WaitGroup。
4. **对比结论**：等待退出用 WaitGroup/无缓冲 channel；限制并发用信号量——二者诉求不同，选错即语义错位。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | channel 怎么同步 | 基础 | 末行写主读全 | 判 P5 |
| L2 | 信号量 P/V | 记忆 | Acquire/Release | 判 P6 |
| L3 | 为何不推荐信号量 | 选型 | 本职限并发 | 判 P6+ |
| L4 | 漏等陷阱 | 机制 | 读满全部值 | 判 P7 |
| L5 | 资源池语义 | 本质 | P减V增防过度 | 判 P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 所有版本 | 无 | channel 同步 + 信号量限并发；等待退出优先 WaitGroup |

## 关键代码
```go
package main

import (
	"context"
	"sync"

	"golang.org/x/sync/semaphore"
)

// 无缓冲 channel 同步：主读全部值即全完成
func withChannel(n int) {
	done := make(chan struct{})
	var wg sync.WaitGroup
	for i := 0; i < n; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			done <- struct{}{} // 末行写，主读全部即表示完成
		}()
	}
	go func() { wg.Wait(); close(done) }()
	for range done { /* 读满全部 */ }
}

// 信号量：本职是限并发数，不是等待退出
func withSem(n int) {
	sem := semaphore.NewWeighted(int64(n))
	ctx := context.Background()
	for i := 0; i < n; i++ {
		_ = sem.Acquire(ctx, 1) // P
		go func() {
			defer sem.Release(1) // V
		}()
	}
}
```

## 总结与追问预判
- channel 同步可读但需读满；信号量限并发非等待原语；等待退出优先 WaitGroup。
- 预判：等待选型 → 见 1023；广播 → 见 1023；信号量限并发 → 见 1015；无缓冲阻塞 → 见 609、1024-keep-main-alive。

## ⚠️ 原文纠错
源码将若干专有名词音译为崩坏词（英文术语错读为近似音、部分中文术语写错字），本卡统一为规范术语 `[经验]`。事实核校：无缓冲 channel 末行写主读全部、信号量 P/V 且本职限并发、多协程需读满避免漏等——均正确，未做更正。
