# 1019 channel 读写未同时就绪致死锁

> 分类：并发模型 | 难度：L3 | 题型：事故题 | 频率：高 | 关键词：**deadlock** / **fatal error** / **go 参数估值**

> 原文锚点：第 67~86 段「读写没同时准备好就死锁且不可 recover；go 参数传 channel 时读取在 main 估值」

## 一句话总述
对 channel 只有读或只有写（且收发双方没在并发里准备好）会触发 `fatal error: all goroutines are asleep - deadlock`，**不可 recover**；把 channel 当参数传给 `go func` 会让读取在 main 里提前估值，造成"伪并发"死锁。一句话背法：**「channel 收发须同时就绪；只有单向且对方不在并发就绪→fatal error 不可 recover；go 参数在声明时即估值」**。

## 面试官视角
这道题考的是 channel 的"收发配对"模型和 go 语句的求值时序两个知识点叠加。考官想看你有没有真踩过这个坑。
- **P5**：知道读写要配对。
- **P6**：说清 fatal error 不可 recover + 参数估值陷阱。
- **P7**：知道用带缓冲 / select 防死锁。
- **红旗**：以为死锁能 recover；以为 `go f(ch)` 里的 ch 读取发生在子协程。
- **惊艳点**：`go f(ch)` 中 ch 作为参数在 **go 语句声明时即被求值**，读取实际发生在 main，并非子协程内 `[源码]` 语言规范。

## 主问答
**Q（面试官原话）：** 我往 channel 写、另一处读，怎么直接崩了还说 catch 不住？

**先铺垫（由浅入深第 1 层）**：channel 的发送和接收是"握手"动作——必须收发两端**同一时刻**都准备好才成交。一旦只有一端、另一端不在并发里就绪，程序就卡死。

1. **结论（第 2 层·机制）**：收发必须"同时就绪"；只有一个方向、且对方不在并发中准备好，就死锁并抛 fatal error，recover 抓不到 `[源码]`。
2. **机制（第 3 层）**：顺序执行的两行"先读后写"有先后，不算同时；`go f(ch)` 里 ch 是参数，go 声明时已估值，读取落在 main，与闭包内读取时序不同 `[源码]` 语言规范。
3. **边界（第 4 层）**：只有读无写、或只有写无读都会死锁；用带缓冲 channel 或把收发一方放进 goroutine 才安全 `[源码]`。
4. **不可恢复（第 5 层）**：fatal error 与 panic 不同，是运行时级错误，recover 对其无效 `[源码]` 运行时。
5. **防御（第 6 层）**：有超时/取消需求用 `select` + `context`；不确定就绪时机用带缓冲通道 `[经验]`。

## 追问链
| 档位 | 追问 | 答得到（背这句） | 答不出停在哪档 |
|------|------|------------------|----------------|
| L1 | 现象 | 直接崩溃 | — |
| L2 | 原因 | 收发未配对 | 停 L2：判 P5 |
| L3 | 不可恢复 | fatal error 非 panic | 停 L3：判 P6 |
| L4 | 估值陷阱 | go 参数声明即求值 | 停 L4：判 P6+ |
| L5 | 防死锁 | 缓冲 / select | 停 L5：判 P7 |

## 版本与兼容性
| 维度 | 说明 |
|------|------|
| Go 全版本稳定 | channel 死锁与 fatal error 行为长期不变 `[源码]` 运行时 |
| fatal error vs panic | 前者运行时级、recover 无效；后者可被 recover 捕获 |
| go 参数求值 | 实参在 go 语句"声明时"求值（非子协程内）`[源码]` 语言规范 |
| 防御手段 | 带缓冲通道 / 收发一方入 goroutine / select+context |

## 关键代码
```go
package main

import "fmt"

func main() {
	// ① 反例：只有接收无发送 -> fatal error: all goroutines are asleep - deadlock（recover 无效）
	// ch := make(chan int)
	// _ = <-ch // 取消注释会直接崩，且 recover 抓不到

	// ② 正解 A：把发送方放进 goroutine，收发同时就绪
	ch := make(chan int)
	go func() { ch <- 42 }() // 发送在并发里就绪
	fmt.Println("received:", <-ch)

	// ③ 正解 B：带缓冲通道，发送不阻塞（无需接收方即时就绪）
	buf := make(chan int, 1)
	buf <- 7 // 缓冲未满，发送立即返回
	fmt.Println("buffered:", <-buf)
}
```

## 总结与追问预判
**背这三句就够**：① **channel 收发须同时就绪，单向无配对即 fatal error**；② **fatal error 不可 recover**；③ **go f(ch) 的 ch 在声明时即估值，读取落在 main**。
**预判追问**：
- 「recover 能救吗？」→ 不能，fatal error 是运行时级错误。
- 「go 参数什么时候求值？」→ go 语句声明时（见关键代码①说明）。
- 「另一类 channel 坑？」→ 泄漏（不判 ok 空转 / 超缓冲阻塞 / ticker 不 Stop，见 1019 同号卡）。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 购入器/携程→goroutine、fateerrol→fatal error 等拼写还原），技术结论未做更正。
