# 1024 signal.Notify 让主协程优雅阻塞（常驻进程推荐做法）

> 分类：Go 并发 / 信号 | 难度：L3 | 题型：技巧题 | 频率：中 | 关键词：**signal.Notify** / **os.Signal** / **SIGINT** / **优雅退出** / **recover**
> 原文锚点：第 26~46 段「signal.Notify 监听信号阻塞 main，可捕获 interrupt/terminate/kill 退出方式；业务协程需 recover 防 panic 退出」

## 一句话总述
生产最推荐的做法是用 `signal.Notify` 把 `os.Signal` channel 注册到指定信号（如 `SIGINT`/`SIGTERM`），主协程 `<-ch` 阻塞等待；收到信号时还能读到**具体退出方式**。配合 `recover` 捕获业务协程 panic，可避免单个 goroutine panic 拖垮整个常驻进程。

## 面试官视角
- 意图：考察生产级常驻进程写法，以及"优雅退出 + 容错"的成熟度。
- P5 知 signal.Notify 阻塞 main、能捕获信号；P6 知可监听多种信号、读到退出方式；P7 知配合 recover 防 panic、信号法相比纯阻塞的优势。
- 红旗：只写 `for {}` 当作生产方案；或常驻进程不处理 panic/recover。
- 惊艳点：点出"信号法既阻塞又能拿到退出原因、可接优雅关停钩子" `[边界]` 见 713、713-graceful-shutdown（优雅退出）、909-empty-select-block（对照空 select）。

## 主问答
**Q（面试官原话）：** 常驻进程主协程最推荐怎么写？怎么拿到退出原因？
**A：**
1. **注册信号阻塞 main**：`signal.Notify(ch, sigs...)` 把目标信号转发到 channel，主协程 `<-ch` 阻塞；未收到信号前一直常驻。
2. **可读退出方式**：从 channel 读出具体 `os.Signal`（如 `interrupt`=Ctrl+C、`terminated`=SIGTERM、`kill`=SIGKILL），据此打印/记录退出来源。
3. **多信号可枚举**：把要监听的信号（SIGINT/SIGTERM/…）作为变参传入，运行时枚举出全部可捕获信号，按需挑选。
4. **配 recover 防 panic**：业务协程里 `defer recover()`，否则任一 goroutine panic 会让整个进程随 main 退出而终止。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 怎么阻塞 main | 基础 | signal.Notify + <-ch | 判 P5 |
| L2 | 能读退出方式吗 | 细节 | 读出 os.Signal | 判 P6 |
| L3 | 监听哪些信号 | 记忆 | SIGINT/SIGTERM/... | 判 P6+ |
| L4 | 还应注意什么 | 边界 | recover 防 panic | 判 P7 |
| L5 | 与优雅退出关系 | 进阶 | 接 shutdown 钩子 | 判 P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 所有版本 | 无 | signal.Notify 阻塞 main、读退出方式；配合 recover |

## 关键代码
```go
package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

func main() {
	// 业务协程：recover 防 panic 拖垮进程
	go func() {
		defer func() {
			if r := recover(); r != nil {
				fmt.Println("recovered:", r)
			}
		}()
		// 常驻业务逻辑...
	}()

	sig := make(chan os.Signal, 1)
	signal.Notify(sig, syscall.SIGINT, syscall.SIGTERM)
	s := <-sig // 阻塞直到收到信号
	fmt.Println("exit by:", s) // 打印具体退出方式
}
```

## 总结与追问预判
- signal.Notify 是常驻进程最推荐写法：阻塞 main + 捕获退出方式 + 可接优雅关停；务必配 recover。
- 预判：信号捕获与优雅退出 → 见 713、713-graceful-shutdown；空 select 对照 → 见 909；panic/recover → 见 defer/recover 相关卡。

## ⚠️ 原文纠错
源码将若干专有名词音译为崩坏词（英文术语错读为近似音、部分中文术语写错字），本卡统一为规范术语 `[经验]`。事实核校：signal.Notify 监听信号、可捕获 SIGINT/SIGTERM/SIGKILL、读到具体退出方式、业务协程需 recover 防 panic——均正确，未做更正。
