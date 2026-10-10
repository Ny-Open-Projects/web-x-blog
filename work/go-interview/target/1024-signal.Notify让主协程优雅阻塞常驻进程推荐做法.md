# 1024 signal.Notify 让主协程优雅阻塞（常驻进程推荐做法）

> 分类：Go 并发 / 信号 | 难度：中 | 题型：技巧题 | 频率：中 | 关键词：**signal.Notify、os.Signal、SIGINT、优雅退出、recover**

> 原文锚点：第 26~46 段「signal.Notify 监听信号阻塞 main，可捕获 interrupt/terminate/kill 退出方式；业务协程需 recover 防 panic 退出」

## 一句话总述
生产最推荐的做法是用 `signal.Notify` 把 `os.Signal` channel 注册到指定信号（如 `SIGINT`/`SIGTERM`），主协程 `<-ch` 阻塞等待；收到信号时还能读到**具体退出方式**。配合 `recover` 捕获业务协程 panic，可避免单个 goroutine panic 拖垮整个常驻进程。一句话背法：**「常驻进程用 signal.Notify 阻塞 main，既能常驻又能拿到退出原因，配 recover 防 panic」**。

## 面试官视角
考官看生产级常驻进程写法，以及"优雅退出 + 容错"的成熟度。能讲清 signal.Notify 阻塞 main、可读退出方式、配合 recover 防 panic、信号法相比纯阻塞的优势，说明你管过常驻服务；只写 `for {}` 当生产方案、或常驻进程不处理 panic/recover，是红旗。
- **P5**：知道 signal.Notify 阻塞 main、能捕获信号。
- **P6**：知道可监听多种信号、读到退出方式。
- **P7**：知道配合 recover 防 panic、信号法相比纯阻塞的优势。

## 主问答
**Q（面试官原话）：** 常驻进程主协程最推荐怎么写？怎么拿到退出原因？

**先铺垫（由浅入深第 1 层）**：常驻进程（ daemon / 长连接服务）的 main 不能跑完就退，得"卡"住。最粗暴的是 `for {}` 或 `select {}`——但那样既拿不到退出原因，也无法优雅关停。信号法才是生产正解：既能阻塞，又能在收到信号时拿到"谁让我退的"。

1. **注册信号阻塞 main（第 2 层·机制）**：`signal.Notify(ch, sigs...)` 把目标信号转发到 channel，主协程 `<-ch` 阻塞；未收到信号前一直常驻。
2. **可读退出方式（第 3 层）**：从 channel 读出具体 `os.Signal`（如 `interrupt`=Ctrl+C、`terminated`=SIGTERM、`kill`=SIGKILL），据此打印/记录退出来源。
3. **多信号可枚举（第 4 层）**：把要监听的信号（SIGINT/SIGTERM/…）作为变参传入，运行时枚举出全部可捕获信号，按需挑选。
4. **配 recover 防 panic（第 5 层·容错）**：业务协程里 `defer recover()`，否则任一 goroutine panic 会让整个进程随 main 退出而终止。
5. **对比纯阻塞（第 6 层）**：`for {}`/`select {}` 只阻塞不通知，无法接优雅关停钩子；信号法能在退出前 flush 日志、关连接、deregister，这才是"优雅"。

## 追问链
| 档位 | 追问 | 答得到（背这句） | 答不出停在哪档 |
|------|------|------------------|----------------|
| L1 | 怎么阻塞 main？ | signal.Notify + <-ch | — |
| L2 | 能读退出方式吗？ | 读出 os.Signal（INT/TERM） | 停 L2：以为只能阻塞 |
| L3 | 监听哪些信号？ | SIGINT/SIGTERM/... 变参传入 | 停 L3：只知一个 |
| L4 | 还应注意什么？ | 业务协程 recover 防 panic | 停 L4：不处理 panic |
| L5 | 与优雅退出关系？ | 退出前可接 shutdown 钩子 | 停 L5：只阻塞不优雅 |

## 版本与兼容性
| 维度 | 说明 |
|------|------|
| signal 包 | 标准库 `os/signal`，`Notify(c, sigs...)` 全版本可用 |
| 可捕获信号 | `syscall.SIGINT`（Ctrl+C）、`syscall.SIGTERM`（kill -15）；`SIGKILL`（9）不可捕获 |
| recover 时机 | 在业务 goroutine 内 `defer func(){ if r:=recover(); r!=nil {} }()` |
| 缓冲 channel | 建议 `make(chan os.Signal, 1)`，避免信号在注册前到达被丢弃 |
| Go 版本 | 与 Go 版本无关，本项目实测 Go 1.26.5 |

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

	// 缓冲 1，避免信号在注册前到达被丢
	sig := make(chan os.Signal, 1)
	signal.Notify(sig, syscall.SIGINT, syscall.SIGTERM)
	s := <-sig // 阻塞直到收到信号
	fmt.Println("exit by:", s) // 打印具体退出方式（interrupt / terminated）
	// 此处可接优雅关停：flush 日志、关连接、deregister ...
}
```

## 总结与追问预判
**背这三句就够**：① **常驻进程用 `signal.Notify` + `<-ch` 阻塞 main，最推荐**；② **能从 channel 读出具体 `os.Signal`，知道谁让进程退**；③ **业务协程务必 `recover` 防 panic 拖垮进程**。
**预判追问**：
- 「SIGKILL 能捕获吗？」→ 不能，`kill -9` 不可捕获，只能优雅处理 SIGINT/SIGTERM（见本卡版本表）。
- 「和 for{} 比好在哪？」→ 能拿退出原因、接优雅关停钩子，而非无脑卡死（见本卡第 6 层）。
- 「优雅退出怎么落地？」→ 见 713 / 713-graceful-shutdown；空 select 对照见 909。

## ⚠️ 原文纠错
1. 事实核校：signal.Notify 监听信号、可捕获 SIGINT/SIGTERM（SIGKILL 不可捕获）、读到具体退出方式、业务协程需 recover 防 panic——均正确，本卡为准。
2. 崩坏词归一：源码将 signal/notify 音译为若干崩坏词、recover 音译为崩坏词；本卡统一为规范术语。
3. 补强：本卡在版本表补「建议缓冲 channel 避免信号丢失」「SIGKILL 不可捕获」两点原卡未明确的工程细节。
