# 713 信号捕获与优雅退出触发

> 分类：Go 工程 / 系统编程 | 难度：L3 | 题型：原理题 | 频率：中 | 关键词：**signal.Notify**/**os.Signal channel**/**SIGHUP=1**/**SIGINT=2**/**SIGTERM=15**/**SIGQUIT=3**/**SIGKILL=9 不可捕获**

> 原文锚点：第 4~22 段「监听退出信号 / signal.Notify / 信号清单」

## 一句话总述
优雅关闭的第一步是**捕获 OS 退出信号**：用 `signal.Notify(ch, sigs...)` 把指定信号转发到 `chan os.Signal`，主 goroutine 阻塞 `<-ch` 直到收到信号再执行收尾。常用信号：**SIGHUP=1**（终端挂断）、**SIGINT=2**（Ctrl+C）、**SIGTERM=15**（可捕获终止，生产主流）、**SIGQUIT=3**（Ctrl+\，含 core dump）；**SIGKILL=9** 不可捕获/不可忽略，故不监听。

## 面试官视角
信号是优雅关闭的入口，但很多人只知 `signal.Notify` 而不清各信号含义与为何不监听 SIGKILL。能报出常见信号的值与语义、点出 SIGKILL 无法拦截，就是合格；结合 http.Server.Shutdown 讲成完整链路更佳。

## 主问答
**Q（面试官原话）：** 怎么让程序感知到要退出了？

1. **signal.Notify 转发**：`signal.Notify(ch, syscall.SIGINT, syscall.SIGTERM)` 把信号写入 channel；不传第二个参数则转发**全部**信号（含 SIGHUP/SIGQUIT），一般不推荐全转。
2. **阻塞等待**：主 goroutine `sig := <-ch` 阻塞，直到收到信号才继续——这就是「拦截信号、提前做收尾」的机制。
3. **信号语义清单**：SIGHUP=1 终端挂断；SIGINT=2 用户 Ctrl+C 强制结束；SIGTERM=15 可被捕获/阻塞/忽略的程序终止（生产 `kill` 默认发它）；SIGQUIT=3 用户 Ctrl+\，通常伴随 core dump。
4. **SIGKILL=9 不监听**：`kill -9` 无条件终止进程，**内核级不可捕获、不可忽略**，应用层无法在其前做收尾，所以优雅关闭只监听可捕获信号。
5. **channel 要带缓冲**：`make(chan os.Signal, 1)` 防信号在 Notify 注册前到达而丢失；收到后通常 `signal.Stop(ch)` 避免重复触发。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 怎么感知退出？ | 说不清 signal.Notify |
| L2 | 常用哪些信号？ | 说不清 SIGINT/SIGTERM |
| L3 | 各信号值/语义？ | 说不清 2/15 |
| L4 | 为何不监听 SIGKILL？ | 说不清不可捕获 |
| L5 | channel 为何缓冲？ | 说不清防丢失/Stop |

## 版本与兼容性
| 信号 | 值 | 语义 | 可捕获 |
|------|----|------|--------|
| SIGHUP | 1 | 终端挂断 | 是 |
| SIGINT | 2 | Ctrl+C | 是 |
| SIGQUIT | 3 | Ctrl+\ (core) | 是 |
| SIGTERM | 15 | kill 默认 | 是 |
| SIGKILL | 9 | kill -9 | 否 |

## 关键代码
```go
sig := make(chan os.Signal, 1)
signal.Notify(sig, syscall.SIGINT, syscall.SIGTERM) // 只监听可捕获的退出信号
defer signal.Stop(sig)
<-sig // 阻塞直到收到 SIGINT/SIGTERM，再走优雅关闭逻辑
// SIGKILL=9 无法在此拦截，进程会被内核直接终止
```

## 总结与追问预判
核心：**signal.Notify 把可捕获信号转 channel，主 goroutine 阻塞等待；SIGKILL 不可监听**。追问拐向「收到信号后怎么关服务」——备好 `http.Server.Shutdown(ctx)`（见 `713-http-graceful-shutdown.md`）；Kafka 消费者侧收尾见 `1420-graceful-shutdown.md`。

## ⚠️ 原文纠错
1. 事实核校： [经验] 原文信号清单「SIGHUP=1、SIGINT=2、SIGQUIT=3、SIGTERM=15、SIGKILL=9」——准确；本卡补入「SIGKILL 内核级不可捕获故不监听」的成因，并建议 channel 带缓冲 + `signal.Stop` 防重复触发（原文未提）。
2. 崩坏词归一：源码将 signal / 信号 / 协程 / channel / 退出 等音译为多组崩坏词，本卡统一为规范术语。
