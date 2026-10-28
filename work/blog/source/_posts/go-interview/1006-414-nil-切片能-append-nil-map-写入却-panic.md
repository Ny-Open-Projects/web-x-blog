---
disableNunjucks: true
title: "414 nil 切片能 append，nil map 写入却 panic"
date: 2026-10-07 23:49:20
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go 基础 / 切片与 map | 难度：L3 | 题型：对比题 | 频率：高 | 关键词：**nil 切片、空切片、nil map、append、make、panic**

> 原文锚点：第 60~89 段「空切片它不是 nil…用 new 函数声明已经分配了内存空间，这个切片也不是 nil…s4 用 var 声明，它是 nil，但往里面追加东西并没有报错…映射是不能像切片一样声明就可以使用的，nil 类型的映射不能直接写入…切片需要通过 make 来声明或者使用字面量的方式」

## 一句话总述
切片的零值 nil 与空切片都不是「不可用」——**nil 切片可以安全 append**；而 map 的 nil 值**只能读不能写**，写入会 panic，必须先用 make 或字面量初始化。

## 面试官视角
P6 知道「map 要 make」；P7 必须讲清**切片与 map 在 nil 语义上的本质不对称**：append 是内置函数，接收 nil 切片时会自动分配底层数组；而 map 写入是运行时直接操作哈希表指针，nil 时无处可写故 panic。

## 主问答
**Q（面试官原话）：** nil 切片和 nil map 都能直接用吗？有什么区别？

1. **空切片非 nil**：`s := []int{}` 是空切片，长度为 0 但**不是 nil**，可直接 append `[源码]`。
2. **new 出的切片非 nil**：`p := new([]int)` 已分配内存，得到的是**指向切片的指针**，其指向的切片也不是 nil；但 append 需先解引用 `[源码]`。
3. **make 指定长度**：`s := make([]int, 1)` 长度为 1，内部已填充一个零值元素 `[源码]`。
4. **var 声明是 nil**：`var s []int` 的零值是 **nil**，但**往里 append 不会报错** `[源码]`。
5. **nil map 不可写**：`var m map[int]int` 后直接 `m[1] = 1` 会 **panic**；nil map 只能读（读返回零值）与 len `[源码]`。
6. **正确姿势**：map 必须先 `make` 或用字面量初始化；切片推荐用 make 或字面量，避免误判 nil 状态 `[源码]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 空切片等于 nil 吗？ | 答不出「不等」 |
| L2 | var 声明的切片能 append 吗？ | 答不出「能」 |
| L3 | nil map 能读吗？ | 答不出「能读不能写」 |
| L4 | nil map 写入会怎样？ | 答不出 panic |
| L5 | 为何二者不对称？ | 答不出「append 内置会分配，map 写入无兜底」 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本 | nil 切片可 append | 无需预先 make |
| Go 全版本 | nil map 写 panic | 必须 make 后写 |
| 所有版本 | 判空语义 | `s == nil` 只看切片，不看底层数组 |
| 所有版本 | 序列化差异 | nil 切片编码为 null，空切片为 [] |

## 关键代码
```go
package main

import "fmt"

func main() {
	var s []int // nil 切片
	s = append(s, 1) // 安全：append 自动分配底层数组
	fmt.Println(s, s == nil) // [1] false

	p := new([]int) // 指向切片的指针，已分配
	*p = append(*p, 2) // 指针需解引用后再 append
	fmt.Println(*p) // [2]

	var m map[int]int // nil map
	fmt.Println(m[1]) // 读安全，返回零值 0
	// m[1] = 1 // panic: assignment to entry in nil map

	m = make(map[int]int) // 先初始化
	m[1] = 1 // 安全
}
```

## 总结与追问预判
**nil 切片「能增」，nil map「只可读不可写」**——这是 Go 面试的高频陷阱。追问通常是「nil 切片和空切片序列化有何不同」：nil 编码为 `null`，空切片编码为 `[]`，对外 API 设计时要显式区分。

## ⚠️ 原文纠错
1. 事实核校：空切片非 nil、new 分配后非 nil 且需解引用、make 指定长度填零值、var 切片为 nil 但可 append、nil map 只读不可写——均与 Go 规范一致 `[经验]`。
2. 补充：原文说「nil 切片声明就可以使用」应更准确表述为「**可以 append，但不能索引赋值**」——`var s []int; s[0] = 1` 依然会 panic，append 之所以安全是因为内置函数会分配底层数组 `[经验]`。
3. 崩坏词归一：源码将切片、映射（map）、make、append、字面量等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
