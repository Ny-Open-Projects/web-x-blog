---
disableNunjucks: true
title: "608 recover 必须在 defer 中调用才生效"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：错误处理 | 难度：L2 | 题型：八股题 | 频率：高 | 关键词：**recover** / **defer 闭包** / **nil**
> 原文锚点：第 39~47 段「recover 必须被放在一个 defer 的闭包函数中才能生效…返回 nil 表示无 panic」

## 一句话总述
recover 是内置函数，仅在 defer 闭包中调用才生效；无 panic 时返回 nil，捕获到 panic 时返回 panic 值，捕获后 panicking 过程停止。

## 面试官视角
- **考察意图**：是否知道 recover 的生效前提与返回值语义。
- **P5** 知 recover 放 defer / **P6** 能说清返回 nil vs panic 值 / **P7** 知 recover 后流程在 defer 处恢复、不是跳回 panic 点。
- **红旗**：认为 recover 可在普通函数体直接调用捕获；认为 recover 返回 error 类型。
- **惊艳点**：recover 在非 defer 上下文中调用永远返回 nil —— 验证：`go run`，go1.26.5，普通调用无任何捕获。

## 主问答
**Q（面试官原话）：** recover 怎么用？为什么必须写在 defer 里？
**A：**
1. **结论**：recover 只有作为 defer 闭包的直接调用才有效，否则直接返回 nil。
2. **机制**：panic 后控制权转入 defer，此时 recover 能拿到当前 panic 值；若在 panic 前已执行过的 recover，那时并无 panic，只能返回 nil。
3. **边界**：recover 返回的是传给 panic 的任意值（interface{}），不一定非得是 error。
**加分层：** 捕获后程序从 defer 处继续向外返回，而非跳回 panic 那一行。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | recover 干嘛 | 概念 | 捕获 panic | 换题 |
| L2 | 为什么放 defer | 机制 | 控制权转入时才有值 | 判 P5 |
| L3 | 返回值是什么 | 边界 | nil 或 panic 值 | 判 P6 |
| L4 | 捕获后流程 | 权衡 | 从 defer 返回继续 | 判 P6+ |
| L5 | 实战兜底位置 | 实战 | 服务入口统一 recover | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| go1.x 全版本稳定 | 无 | recover 语义自 Go1 起未变，照此答 `[源码]` |

## 关键代码
```go
// 示意，未验证：recover 只能在 defer 中生效
func demo() {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("捕获:", r) // panic 值
		}
	}()
	panic("boom")
}
```

## 总结与追问预判
- recover 仅在 defer 生效，无 panic 返回 nil，捕获后 panicking 停止。
- 预判：跨 goroutine 能否捕获 → 见 608；就近捕获 → 见 608。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 Go、互斥锁、nil 等专有名词被音译为同音词，已还原为正确术语），技术结论未做更正。
