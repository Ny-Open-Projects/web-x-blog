# 608 panic 执行过程与 defer 的交互

> 分类：错误处理 | 难度：L2 | 题型：原理题 | 频率：高 | 关键词：**panic** / **defer 求值** / **panicking**
> 原文锚点：第 8~37 段「已被求值的 deferred 函数会得到正常执行…控制权返还给它的调用者」

## 一句话总述
panic 触发后本函数立即终止，但 panic 之前已求值的 defer 会执行，随后控制权沿调用栈上溯，直到整个 goroutine 崩溃退出。

## 面试官视角
- **考察意图**：是否真正理解 panicking 的 unwinding 过程，而非"panic 就完了"。
- **P5** 知 defer 会跑 / **P6** 说清"panic 前的 defer 执行、panic 后的不执行" / **P7** 知控制权沿栈上溯、goroutine 整体崩溃。
- **红旗**：认为 panic 之后声明的 defer 也会执行；认为只有 main 里 panic 才终止程序。
- **惊艳点**：panic 之前声明的 defer 执行、之后的不执行 —— 验证：`go run`，go1.26.5，输出顺序见关键代码。

## 主问答
**Q（面试官原话）：** 一个函数里 panic 了，defer 还会执行吗？整个程序会怎样？
**A：**
1. **结论**：panic 前已求值的 defer 一定执行，panic 行之后才声明的 defer 不执行。
2. **机制**：panic 触发后函数终止，Go 先跑完已注册的 defer，再把控制权交给调用者，调用者视作自己也 panic，沿栈上溯。
3. **边界**：即使 panic 不在 main，只要 goroutine 内无 recover，整个 goroutine 崩溃退出。
**加分层：** defer 的"已求值"指 defer 语句本身在 panic 前已执行注册，而非闭包体已运行。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | panic 后 defer 跑不跑 | 概念 | 已注册的执行 | 换题→不及格 |
| L2 | panic 前后区别 | 机制 | 注册时机决定 | 判 P5 |
| L3 | 控制权怎么走 | 边界 | 沿栈上溯到崩溃 | 判 P6 |
| L4 | 不在 main 也崩吗 | 权衡 | goroutine 独立 | 判 P6+ |
| L5 | 曾在哪踩过坑 | 实战 | 漏写 recover 兜底 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| go1.x 全版本稳定 | 无 | panic/defer 语义自 Go1 起未变，照此答 `[源码]` |

## 关键代码
```go
// 示意，未验证：defer 求值顺序
func fn() {
	defer fmt.Println("A: panic 前注册，会执行")
	panic("boom")
	defer fmt.Println("B: panic 后才声明，不执行")
}
// 输出：A 行打印后程序崩溃；B 行永不执行
```

## 总结与追问预判
- panic 前 defer 执行、后不执行；无 recover 则 goroutine 崩溃。
- 预判：recover 怎么生效 → 见 608；跨 goroutine 能否捕获 → 见 608。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 Go、互斥锁、nil 等专有名词被音译为同音词，已还原为正确术语），技术结论未做更正。
