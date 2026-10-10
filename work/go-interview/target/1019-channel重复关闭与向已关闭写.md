# 1019 channel 重复关闭与向已关闭写

> 分类：并发模型 | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**close** / **panic** / **单次关闭**

> 原文锚点：第 125~126 段「同一 channel 只能 close 一次，重复 close 或向已关闭 channel 写都会 panic」

## 一句话总述
channel 只能 `close` 一次；对同一 channel 重复 `close`、或向已关闭的 channel 发送数据，都会直接 `panic`——关闭责任要唯一，通常交给发送方。一句话背法：**「channel 只能 close 一次；重复 close / 向已关闭写都 panic；读已关闭安全得零值；关闭责任归发送方」**。

## 面试官视角
这是 channel 关闭归属的基础题，常和"谁负责关""读关闭 channel 安不安全"一起考。
- **P5**：知道不能重复关。
- **P6**：说清向已关闭 channel 写也 panic + 关闭方约定。
- **P7**：知道用 ok 判断 + 单一关闭责任，多发送方如何统筹。
- **红旗**：多个 goroutine 都去 close 同一 channel；以为读已关闭 channel 会 panic（其实读安全，得零值）。
- **惊艳点**：向已关闭 channel **写** panic，但**读**已关闭 channel 不会 panic，只是反复得零值 `[源码]` 语言规范。

## 主问答
**Q（面试官原话）：** channel 关了还能写吗？关两次呢？

**先铺垫（由浅入深第 1 层）**：channel 的 `close` 是"宣告不再有发送方"的单向操作，运行时对它的状态校验很严——一旦关闭态成立，再关或再写都会被当成程序错误直接 panic。

1. **结论（第 2 层·机制）**：同一 channel 只能关闭一次；重复 close、或向已关闭 channel 发送，都会 panic `[源码]` 语言规范。
2. **机制（第 3 层）**：close 把 channel 置为关闭态，再 close 或再 send 都触发 runtime panic；接收端读已关闭 channel 安全，只是拿到零值 `[源码]`。
3. **边界（第 4 层）**：关闭责任应唯一，惯例由**发送方**关闭，接收方不关；多发送方可用额外 signal channel + 一次关闭统筹 `[源码]`。
4. **读关闭（第 5 层）**：接收端 `v, ok := <-ch`，ok 为 false 表示已关闭且无更多值；不要自己调 close `[经验]`。
5. **统筹（第 6 层）**：多发送方场景用 `sync.Once` 或"最后一个发送方关闭"约定，避免重复关闭 panic `[经验]`。

## 追问链
| 档位 | 追问 | 答得到（背这句） | 答不出停在哪档 |
|------|------|------------------|----------------|
| L1 | 能不能写 | 向已关写会 panic | — |
| L2 | 读呢 | 读已关安全得零值 | 停 L2：判 P5 |
| L3 | 谁关 | 发送方负责关闭 | 停 L3：判 P6 |
| L4 | 多发送方 | 统筹单一关闭责任 | 停 L4：判 P6+ |
| L5 | 排查 | 复现 panic 调用栈 | 停 L5：判 P7 |

## 版本与兼容性
| 维度 | 说明 |
|------|------|
| Go 全版本稳定 | close 语义与 panic 行为长期不变 `[源码]` 语言规范 |
| 读已关闭 | 安全，返回零值 + ok=false，不 panic |
| 写/重复关 | panic: send on closed channel / close of closed channel |
| 推荐约定 | 发送方关闭；多发送方用 Once 或最后发送方关闭 |

## 关键代码
```go
package main

import "fmt"

func main() {
	ch := make(chan int, 1)
	ch <- 1
	close(ch) // 发送方负责关闭，仅一次

	// 读已关闭 channel 是安全的，得零值 + ok=false
	v, ok := <-ch
	fmt.Println("read:", v, "open:", ok) // 1 true
	v, ok = <-ch
	fmt.Println("read:", v, "open:", ok) // 0 false（已关闭，安全得零值）

	// 以下二者都会 panic（仅作说明，不执行）：
	// close(ch) // 重复关闭 → panic: close of closed channel
	// ch <- 2   // 向已关闭 channel 写 → panic: send on closed channel
}
```

## 总结与追问预判
**背这三句就够**：① **channel 只能 close 一次**；② **重复 close / 向已关闭写都 panic，读已关闭安全得零值**；③ **关闭责任归发送方**。
**预判追问**：
- 「读关闭 channel 会 panic 吗？」→ 不会，得零值 + ok=false。
- 「多发送方怎么关？」→ Once 或最后发送方关闭，避免重复关（见 1021 多发送者关闭方案）。
- 「关闭后还泄漏？」→ 见 1019 channel 泄漏（不判 ok 空转 / 不 Stop ticker）。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 购入器/携程→goroutine、clocloclose→close、panick→panic 等拼写还原），技术结论未做更正。
