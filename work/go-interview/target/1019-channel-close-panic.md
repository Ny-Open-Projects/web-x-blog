# 1019 channel 重复关闭与向已关闭写

> 分类：并发模型 | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**close** / **panic** / **单次关闭**
> 原文锚点：第 125~126 段「同一 channel 只能 close 一次，重复 close 或向已关闭 channel 写都会 panic」

## 一句话总述
channel 只能 `close` 一次；对同一 channel 重复 `close`、或向已关闭的 channel 发送数据，都会直接 `panic`——关闭责任要唯一，通常交给发送方。

## 面试官视角
- 意图：是否掌握 channel 关闭的正确归属与禁忌操作。
- P5 知不能重复关 / P6 说清向已关 channel 写也 panic + 关闭方约定 / P7 知用 ok 判断 + 单一关闭责任。
- 红旗：多个 goroutine 都去 close 同一 channel；以为读已关闭 channel 会 panic（其实读是安全的，得零值）。
- 惊艳点：向已关闭 channel **写** panic，但**读**已关闭 channel 不会 panic，只是反复得零值 `[源码]` 语言规范。

## 主问答
**Q（面试官原话）：** channel 关了还能写吗？关两次呢？
**A：**
1. **结论**：同一 channel 只能关闭一次；重复 close、或向已关闭 channel 发送，都会 panic。
2. **机制**：close 把 channel 置为关闭态，再 close 或再 send 都触发 runtime panic；接收端读已关闭 channel 安全，只是拿到零值。
3. **边界**：关闭责任应唯一，惯例由**发送方**关闭，接收方不关；多发送方可用额外 signal channel + 一次关闭统筹 `[源码]`。
**加分层：** 接收端用 `v, ok := <-ch` 判断关闭，不要自己调 close。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 能不能写 | 概念 | 会panic | 换题 |
| L2 | 读呢 | 机制 | 安全得零 | 判 P5 |
| L3 | 谁关 | 边界 | 发送方 | 判 P6 |
| L4 | 多发送方 | 演进 | 统筹关闭 | 判 P6+ |
| L5 | 排查 | 实战 | 复现panic | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本稳定 | 无 | close 语义与 panic 行为长期不变 `[源码]` 语言规范 |

## 关键代码
```go
// 示意，未验证：重复关闭 / 向已关写都会 panic
package main

func main() {
	ch := make(chan int)
	close(ch)
	// close(ch) // 重复关闭 → panic
	// ch <- 1   // 向已关闭 channel 写 → panic
	_ = ch
}
```

## 总结与追问预判
- close 仅一次，写已关 panic、读已关安全；关闭责任归发送方。
- 预判：channel 全貌 → 见 1019-concurrency-pitfalls.deep。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 购入器/携程→goroutine、clocloclose→close、panick→panic 等拼写还原），技术结论未做更正。
