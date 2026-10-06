# 1019 channel 读写未同时就绪致死锁

> 分类：并发模型 | 难度：L3 | 题型：事故题 | 频率：高 | 关键词：**deadlock** / **fatal error** / **go 参数估值**
> 原文锚点：第 67~86 段「读写没同时准备好就死锁且不可 recover；go 参数传 channel 时读取在 main 估值」

## 一句话总述
对 channel 只有读或只有写（且收发双方没在并发里准备好）会触发 `fatal error: all goroutines are asleep - deadlock`，**不可 recover**；把 channel 当参数传给 `go func` 会让读取在 main 里提前估值，造成"伪并发"死锁。

## 面试官视角
- 意图：是否真懂 channel 的收发配对模型，以及 go 语句参数求值的时序陷阱。
- P5 知读写要配对 / P6 说清 fatal error 不可 recover + 参数估值 / P7 知用带缓冲/select 防死锁。
- 红旗：以为死锁能 recover；以为 `go f(ch)` 里的 ch 读取发生在子协程。
- 惊艳点：`go f(ch)` 中 ch 作为参数在 **go 语句声明时即被求值**，读取实际发生在 main，并非子协程内 `[源码]` 语言规范。

## 主问答
**Q（面试官原话）：** 我往 channel 写、另一处读，怎么直接崩了还说 catch 不住？
**A：**
1. **结论**：收发必须"同时就绪"；只有一个方向、且对方不在并发中准备好，就死锁并抛 fatal error，recover 抓不到。
2. **机制**：顺序执行的两行"先读后写"有先后，不算同时；`go f(ch)` 里 ch 是参数，go 声明时已估值，读取落在 main，与闭包内读取时序不同。
3. **边界**：只有读无写、或只有写无读都会死锁；用带缓冲 channel 或把收发一方放进 goroutine 才安全 `[源码]`。
**加分层：** fatal error 与 panic 不同，是运行时级错误，recover 对其无效。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 现象 | 概念 | 崩溃 | 换题 |
| L2 | 原因 | 机制 | 未配对 | 判 P5 |
| L3 | 不可恢复 | 边界 | fatal error | 判 P6 |
| L4 | 估值陷阱 | 演进 | 参数先求 | 判 P6+ |
| L5 | 防死锁 | 实战 | 缓冲/select | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本稳定 | 无 | channel 死锁与 fatal error 行为长期不变 `[源码]` 运行时 |

## 关键代码
```go
// 示意，未验证：只有读无写 → fatal error 死锁，recover 无效
package main

func main() {
	ch := make(chan int)
	_ = <-ch // 只有接收，无发送 → all goroutines asleep
}
```

## 总结与追问预判
- 收发须同时就绪；go 参数会提前估值；fatal error 不可 recover。
- 预判：另一类 channel 坑 → 见 1019-channel-leak。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 购入器/携程→goroutine、fateerrol→fatal error 等拼写还原），技术结论未做更正。
