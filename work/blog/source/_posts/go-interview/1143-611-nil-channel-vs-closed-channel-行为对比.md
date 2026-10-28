---
disableNunjucks: true
title: "611 nil channel vs closed channel 行为对比"
date: 2026-10-10 13:46:23
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go 并发/channel | 难度：L3 | 题型：八股题 | 频率：高 | 关键词：**nil channel**/**closed channel**/**阻塞**/**panic**/**select**

> 原文锚点：第 2~10 段「未初始化channel是nil…关闭后的channel不是nil…关闭nil channel panic」+ 全源 nil vs 关闭语义对比

## 一句话总述
**nil channel** 与 **closed channel** 是两种不同状态，行为对比鲜明：**nil**=未初始化（收发阻塞、关闭 panic、在 select 永不选中）；**closed**=已初始化后终态（接收不阻塞、返回零值+`ok=false`、再发送 panic、重复关闭 panic、且 closed 不等于 nil）。面试常把两者混为一谈，须明辨。

## 面试官视角
综合对比题。面试官要看你能否并排给出 nil 与 closed 的"收发/关闭/零值/select"四维度差异，而非只答一点。

## 主问答
**Q（面试官原话）：** nil channel 和 closed channel 有什么区别？

**A：**

1. **收发行为**：nil channel 收发**阻塞**（同 goroutine 死锁）；closed channel 接收**不阻塞**、返回元素零值 + `ok=false`，向其**发送 panic**。
2. **关闭行为**：nil channel `close` → **panic**；closed channel 再 `close` → **panic**（重复关闭）；正常关闭一次是合法的。
3. **零值与 select**：closed channel 读得到残留数据再读零值；nil channel 在 `select` 中对应 case **永不选中**，closed channel 的 case 可正常触发。
4. **身份**：`close(ch)` 后 `ch == nil` 仍为 `false`——closed **不是** nil。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|----|------|----------|--------|------------|
| L1 | nil 能 close 吗 | 是否懂 panic | close nil panic | 答不出停档 |
| L2 | closed 能发吗 | 是否懂发送panic | 发 closed panic | 答不出停档 |
| L3 | closed 收怎样 | 是否懂零值 | 不阻塞收零值ok=false | 答不出停档 |
| L4 | closed 是 nil 吗 | 是否懂身份 | close后!=nil | 答不出停档 |
| L5 | select 中差异 | 是否懂选中 | nil永不选中/closed可触发 | 答不出停档 |

## 版本与兼容性
- 行为自 Go 1.0 稳定；closed channel 的"残留先读完再零值"语义见 612。
- 重复关闭、向已关闭发送均 panic，细节见 1019/`1021-close-channel-traits`。

## 关键代码
```go
var n chan int // nil
// close(n)    // panic: close of nil channel
// n <- 1; <-n // 阻塞（同 goroutine 死锁）

c := make(chan int, 1)
c <- 1
close(c)
v, ok := <-c        // v=1, ok=true（残留先读）
v, ok = <-c         // v=0, ok=false（之后零值）
// c <- 2           // panic: send on closed channel
// close(c)        // panic: close of closed channel
fmt.Println(c == nil) // false：closed 不是 nil
```

## 总结与追问预判
- 口诀：**nil 未初始化(收发阻塞/关panic)；closed 已终态(收零值/发panic/关repeat panic)；closed≠nil**。
- 预判追问："那关闭能当广播用？"→ 能，发送方写完关门、接收方自然退出（见 612）。

## ⚠️ 原文纠错
源码将 channel 相关术语音译为崩坏词，本卡已统一为规范术语（如 channel/nil/closed/goroutine/死锁/panic/zero value/select）。纠错节不枚举任何原词崩坏词 `[经验]`。

> 边界：nil 操作总览见 611；closed 残留读/不阻塞见 612/`612-closed-channel-ops`；关闭 panic/重复关闭见 1019/`1021-close-channel-traits`；本卡只做 nil vs closed 四维度对比。
