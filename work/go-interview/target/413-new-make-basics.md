# 413 new 与 make 的核心区别

> 分类：Go 基础 / 内置函数 | 难度：L2 | 题型：八股题 | 频率：高 | 关键词：**new 返回 *T** / **make 返回 T** / **make 仅三类型** / **make 会初始化**
> 原文锚点：第 4~13 段「六和make都是分配内存的内置函数；make既分配又初始化且仅支持slice/map/chan；new分配任意类型返回指针；make返回类型本身、new返回*T」

## 一句话总述
`new` 和 `make` 都是 Go 内存分配内置函数，但三点本质不同：**① 适用类型**——`make` 只用于 slice/map/chan，`new` 可用于任意类型；**② 返回值**——`make` 返回类型 T 本身，`new` 返回 `*T`；**③ 是否初始化**——`make` 分配并初始化（引用结构就绪可用），`new` 只分配零值内存。

## 面试官视角
- 考察意图：是否真懂两个分配原语的语义边界，而非混用
- P5 能说"new 返回指针、make 返回本身"；P6 能讲"make 仅 slice/map/chan 且会初始化"；P7 能讲清 make 的 len/cap 参数与 nil 语义
- 红旗：说"make 能分配任意类型"；说"new 出来的 slice 能直接 append"
- 惊艳点：点出"make 对 slice/map/chan 做引用初始化，所以经 make 的 slice 非 nil 可直接用；new 出来的 slice 是 *[]T 且仍为 nil" [源码]

## 主问答
**Q（面试官原话）：** Go 里 new 和 make 有什么区别？
**A：**
1. **适用类型不同**：`make` 仅支持 **slice / map / chan** 三种引用类型；`new` 可用于**任意类型**（含基本类型、数组、结构体）[源码]。
2. **返回值不同**：`make` 返回**类型本身 T**（如 `[]int`）；`new` 返回**指向类型的指针 `*T`**（如 `*[]int`）[源码]。
3. **是否初始化不同**：`make` 分配内存并**初始化内部引用结构**，对象就绪可用；`new` 只开辟一块**零值内存**，不初始化引用——所以对 slice/map/chan 用 new 得到的是 nil 指针，还需手动初始化才有意义 [源码]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 返回啥 | 概念 | new→*T, make→T | P5 |
| L2 | make 管哪几种 | 范围 | slice/map/chan | P6 |
| L3 | 为何 make 会初始化 | 机制 | 引用结构就绪 | P6+ |
| L4 | 参数 | 细节 | make 可传 len/cap | P7 |
| L5 | new 的 slice 能用吗 | 边界 | nil 需初始化 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Go 全版本 | 无 | new/make 语义长期稳定；make 仅三类型、返回 T、会初始化 |

## 关键代码
```go
// new 返回 *T，内存清零但未初始化引用
p := new([]int)        // p 的类型是 *[]int，*p 仍是 nil slice
// make 返回 T，且初始化就绪
s := make([]int, 10)   // s 是 []int，len=cap=10，元素全零值，非 nil
m := make(map[string]int) // m 非 nil，可直接赋值
c := make(chan int, 3)    // c 非 nil，缓冲 3
```

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡统一为规范术语（六→new、mac/make→make、千到→chan、sashmap→slice/map、凝值→零值、字变量→字面量等）；技术结论未做事实性更正 [经验]。

## 总结与追问预判
- 三句话：make 仅三类型且返回 T 并初始化；new 任意类型返回 *T 仅清零。
- 切片实测差异见 413-make-vs-new-slice-demo；new 的实战定位见 413-new-pitfalls；数组声明见 414（只引不重述）。
