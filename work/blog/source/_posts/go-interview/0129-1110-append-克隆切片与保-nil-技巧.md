---
disableNunjucks: true
title: "1110 append 克隆切片与保 nil 技巧"
date: 2026-10-06 18:30:16
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go 语言基础 | 难度：L3 | 题型：技巧题 | 频率：中 | 关键词：**append克隆**/**预设容量**/**保 nil 特性**
> 原文锚点：第 70~93 段「append 方式克隆…三元表达式保 nil 特性」

## 一句话总述
克隆切片的惯用法是 `dst := make([]T, 0, cap(src)); dst = append(dst, src...)`；若要**保留原切片的 nil/空语义**，用三元表达式 `dst := src[:0:0]; dst = append(dst, src...)`，避免普通 make 把 nil 变成空数组。

## 面试官视角
- 考察意图：是否掌握两种克隆写法的细节差异，尤其是 len 与 cap 对 append 行为的影响。
- 分档：P5 知 append 能克隆；P6 知 `make(...,0,cap)`+append 套路；P7 能讲清"给 len 会接在默认值后"与"保 nil 的三元技巧"。
- 红旗答案：以为 `make([]T, n)` 给长度后再 append 会从 0 开始填。
- 惊艳点：点出 **`make([]T, len)` 给了长度，append 会接在默认值后面（前 len 个为 0）** 这一高频误用 `[经验]`。

## 主问答
**Q（面试官原话）：** 用 append 怎么克隆切片？怎么保留 nil 特性？
**A：**
1. **结论**：append+`...` 展开克隆，注意 len 与 cap 的差别。
2. **机制**：`make([]T, 0, len(src))` **只给容量不给长度** → append 从 0 开始填，dst 与原切片地址不同、互不干扰。若误写成 `make([]T, len, ...)` 给了长度 → append 会接在默认值（0）之后，前 len 个变成多余的 0。
3. **边界**：原切片为 nil 时，普通 `make` 会得到"空数组"而非 nil；用 `dst := src[:0:0]; dst = append(dst, src...)` 可让 dst 还原为 nil（保留"空即 nil"的语义），避免无谓分配。

**加分层：** `append([]T(nil), src...)` 也能得到具有 nil 感知的副本，是更短的写法。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | append 克隆？ | 基础 | make+append... | P5 |
| L2 | 给 len 会怎样？ | 坑 | 接在默认值后 | P6 |
| L3 | 怎么保 nil？ | 技巧 | src[:0:0] | P6 |
| L4 | 与 copy 区别？ | 对比 | 追加vs覆盖 | P7 |
| L5 | nil 感知为何重要？ | 进阶 | 语义/分配 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Go 1.0+ | 无 | 答"make(0,cap)+append(...)；保 nil 用 src[:0:0]+append" |

## 关键代码
```go
src := []int{1, 2, 3}
dst := make([]int, 0, len(src))
dst = append(dst, src...)           // 通用克隆，地址独立

// 保留 nil 特性
var nilSrc []int
dst2 := nilSrc[:0:0]
dst2 = append(dst2, nilSrc...)      // dst2 仍为 nil
```

## 总结与追问预判
append 克隆用 `make(0,cap)+append(...)`；保 nil 用 `src[:0:0]`。与 copy 的区别：copy 覆盖、append 追加。追问接"克隆性能对比"与"底层共享根因"。

## ⚠️ 原文纠错
1. 机翻崩坏词归一：`尔end`/`耳pad`/`rpad`→**append**；`六`/`利o`/`利有`→**nil**；`构版本`→**Go 版本**；`元式`/`三元索引`→**三元切片表达式**。事实推理正确，仅术语崩坏，本卡已归一 `[经验]`。
2. 原文"原切片是 nil 复制之后也是 nil"——准确（用 `src[:0:0]` 技巧），本卡给出了标准写法；并补全"make 给了长度会让 append 接在默认值后"这一常见误用。
