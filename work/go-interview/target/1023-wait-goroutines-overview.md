# 1023 主协程如何等待其他协程退出（同步方式总览与选型）

> 分类：Go 并发 / 同步 | 难度：L3 | 题型：方法论题 | 频率：中 | 关键词：**WaitGroup** / **无缓冲 channel** / **信号量** / **主协程等待** / **选型**
> 原文锚点：第 1~50 段「主协程等子协程退出:WaitGroup(Add/Done/Wait,最推荐)/WaitGroup广播通知/无缓冲channel同步/信号量(此场景不推荐,本职限并发)」

## 一句话总述
主协程等待子协程退出有几种同步手段：**WaitGroup（`Add`/`Done`/`Wait`）最推荐、可读性最好**；也可用**无缓冲 channel**（子协程末行写、主读全部值）同步；还能用**信号量**，但信号量本职是**限制并发数**，此"等待退出"场景并不推荐。

## 面试官视角
- 意图：考察对 goroutine 同步手段的体系化认知与正确选型，而非只会一种。
- P5 知 WaitGroup 三件套与 channel 同步；P6 知 WaitGroup 最推荐、Done 等价 Add(-1)、多协程需读全 channel 值；P7 知信号量在此场景不推荐、其本职是限并发、广播通知模式。
- 红旗：用信号量去"等退出"（误用）；或不知 WaitGroup 比 channel 可读性更好。
- 惊艳点：点出"WaitGroup 是等待原语、信号量是资源池/限并发原语，二者职责不同" `[边界]` 见 913-waitgroup-usage（Add/Done/Wait 用法与坑）、1024-keep-main-alive（无缓冲 channel 阻塞 main）、1015-channel-semaphore（信号量限并发）。

## 主问答
**Q（面试官原话）：** 主协程怎么等其他协程都退出？
**A：**
1. **WaitGroup 最推荐**：启动前 `Add(1)`，协程内 `defer Done()`（等价于 `Add(-1)`），主协程 `Wait()` 阻塞到全部完成；代码简洁、可读性最佳。
2. **无缓冲 channel 同步**：子协程把"写 channel"放最后一行，主协程依次读出全部值即表示全完成；多协程需读满全部，否则会漏等。
3. **信号量不推荐**：信号量（`semaphore` 包，P/V 操作）本职是限制同时执行的协程数、保护资源池，并非"等待退出"的合适原语，此场景应优先 WaitGroup。
4. **广播通知**：当协程需等"其他协程准备好数据"再继续，可用第二个 WaitGroup 做通知（详见 1023-waitgroup-broadcast）。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 最推荐哪种 | 基础 | WaitGroup | 判 P5 |
| L2 | Done 等价 | 细节 | Add(-1) | 判 P6 |
| L3 | channel 同步坑 | 机制 | 读满全部值 | 判 P6+ |
| L4 | 信号量为何不推荐 | 选型 | 本职限并发 | 判 P7 |
| L5 | 广播通知 | 进阶 | 双 WG 通知 | 判 P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 所有版本 | 无 | WaitGroup 首选；信号量限并发非等待 |

## 关键代码
```go
package main

import (
	"sync"
	"time"
)

// WaitGroup：最推荐的主协程等待方式
func main() {
	var wg sync.WaitGroup
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done() // 等价 wg.Add(-1)
			time.Sleep(time.Millisecond)
		}()
	}
	wg.Wait() // 阻塞直到所有 Done
}
```

## 总结与追问预判
- 等待退出首选 WaitGroup；channel 同步可读但繁琐；信号量限并发非等待原语。
- 预判：WaitGroup 用法与坑 → 见 913-waitgroup-usage；无缓冲 channel 阻塞 → 见 1024-keep-main-alive；信号量限并发 → 见 1015-channel-semaphore；广播模式 → 见 1023-waitgroup-broadcast。

## ⚠️ 原文纠错
源码将若干专有名词音译为崩坏词（英文术语错读为近似音、部分中文术语写错字），本卡统一为规范术语 `[经验]`。事实核校：WaitGroup 三件套、Done 等价 Add(-1)、无缓冲 channel 末行写主读全部、信号量本职限并发此场景不推荐——均正确，未做更正。
