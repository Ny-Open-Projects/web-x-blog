# 1019 channel 误用导致 goroutine 泄漏

> 分类：并发模型 | 难度：L3 | 题型：事故题 | 频率：高 | 关键词：**goroutine leak** / **for-select** / **ticker Stop**
> 原文锚点：第 86~126 段「for-select 不判断 ok 读关闭 channel 会空转泄漏；缓冲不足致永久阻塞；ticker 不 Stop 泄漏」

## 一句话总述
channel 误用会让 goroutine 永久阻塞或空转：for-select 读已关闭 channel 不判 ok 会一直命中零值空转；发送方多于缓冲容量会永久阻塞；ticker 不 Stop 也泄漏。

## 面试官视角
- 意图：是否熟悉 goroutine 泄漏的几类典型形态与排查。
- P5 知泄漏概念 / P6 说清 ok 判断 + 缓冲 + ticker / P7 知用 ctx 取消、pprof 看 goroutine 数。
- 红旗：for-select 读 channel 不接第二个 bool；以为函数返回阻塞的 goroutine 就自动没了。
- 惊艳点：阻塞在无消费者 channel 上的 goroutine 不会自己结束，持续调用会累积到 for 循环次数级 `[经验]`。

## 主问答
**Q（面试官原话）：** 怎么我的 goroutine 数量一直涨？
**A：**
1. **结论**：泄漏常来自三类——for-select 不判 ok 空转、发送超缓冲永久阻塞、ticker 不 Stop。
2. **机制**：关闭的 channel 反复读得零值，case 永远选中空转占 CPU；缓冲 2 却 3 个发送方→必有一方永久阻塞；ticker 需手动 Stop 释放。
3. **边界**：**阻塞的 goroutine 不会因"调用它的函数返回"就消失**；是否会被 GC 回收取决于其阻塞对象是否仍可达，是运行时实现细节，不能依赖 `[经验]`。
**加分层：** 治理用 `context` 取消 + `defer ticker.Stop()`，线上用 pprof 的 goroutine profile 定位。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 现象 | 概念 | 数量涨 | 换题 |
| L2 | 三类 | 机制 | ok/缓冲/ticker | 判 P5 |
| L3 | 判定 | 边界 | 第二次返回值 | 判 P6 |
| L4 | 回收误区 | 演进 | 不会自动没 | 判 P6+ |
| L5 | 排查 | 实战 | pprof | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本稳定 | 无 | 泄漏形态与 GC 对不可达阻塞 goroutine 的处理长期如此 `[经验]` |

## 关键代码
```go
// 示意，未验证：for-select 必须判 ok，否则关闭后空转泄漏
package main

import "time"

func main() {
	ch := make(chan int)
	go func() {
		for {
			v, ok := <-ch
			if !ok {
				return // 关闭后必须退出，否则 case 空转泄漏
			}
			_ = v
		}
	}()
	time.Sleep(time.Second)
}
```

## 总结与追问预判
- 泄漏三类：空转/阻塞/ticker；阻塞 goroutine 不自动消失，需显式退出。
- 预判：channel 另一坑 → 见 1019-channel-close-panic。

## ⚠️ 原文纠错
原文称"函数返回之后这个 goroutine 就被回收掉了"，表述不严谨。纠正：goroutine 阻塞在 channel 上**不会**因为"调用它的外层函数返回"就自动结束；是否会被 GC 回收取决于其阻塞对象是否仍可达，这是运行时实现细节，不应作为可被依赖的退出机制。正确结论：生产上必须显式让 goroutine 退出（ctx 取消 / 关闭 channel / Stop ticker），不能依赖函数返回。
