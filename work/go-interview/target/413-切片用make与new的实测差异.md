# 413 切片用 make 与 new 的实测差异

> 分类：Go 基础 / slice | 难度：L3 | 题型：代码题 | 频率：中 | 关键词：**make 非 nil** / **new 返回 *[]T 需解引用** / **len/cap** / **nil 判定**
> 原文锚点：第 14~42 段「slice1 经 make len=cap=10 非 nil；slice2 经 new 是指针需解引用才能 append 且仍 nil；s1~s5 的 nil 判定」

## 一句话总述
同一切片，用 `make([]int,10)` 得到**非 nil、len=cap=10、元素零值**的 `[]int`，可直接 append；用 `new([]int)` 得到 `*[]int`，其指向的 slice **仍是 nil**，append 前必须解引用（`*p`）且解引用后仍是空切片——这是 new/make 差异在 slice 上最直观的落点。

## 面试官视角
- 考察意图：能不能用一段最小代码证伪"new 出来的 slice 能直接用"
- P5 知 make 的 slice 非 nil；P6 能讲 new 返回指针需解引用、且 *p 仍为 nil；P7 能讲清 s1~s5 的 nil 判定逻辑
- 红旗：以为 `new([]int)` 得到的 slice 能直接 append（需先解引用且仍 nil）
- 惊艳点：用"经 make 的 s1 非 nil、经 new 的 s2/s3 为 nil、未初始化的 s4 为 nil、字面量 s5 非 nil"一组判定现场演示 [源码]

## 主问答
**Q（面试官原话）：** 用 make 和 new 创建一个切片，行为上差在哪？
**A：**
1. **make 版就绪可用**：`s1 := make([]int, 10)` 得到 `[]int`，len=cap=10、元素全零值、**非 nil**，可直接 append 或下标赋值 [源码]。
2. **new 版是指针且仍 nil**：`p := new([]int)` 得到 `*[]int`，其指向的 slice **仍是 nil**；append 必须传值而非指针，所以要解引用 `*p`；即便解引用，它也只是个**空切片（len=cap=0）**，不是已分配 10 个元素 [源码]。
3. **nil 判定分组**：`make` 出来的 s1 **非 nil**（引用已初始化）；`new` 出来的 s2/s3 和仅声明的 s4 **都是 nil**；字面量 `s5 := []int{}` 与 make 一样**非 nil**——判定看"引用有没有被初始化"，不看是不是指针 [源码]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | make 的 slice nil? | 基础 | 非 nil | P5 |
| L2 | new 的 slice 能 append? | 机制 | 需解引用且仍 nil | P6 |
| L3 | 解引用得到啥 | 细节 | 空切片 len0 | P6+ |
| L4 | s5 字面量 nil? | 边界 | 非 nil | P7 |
| L5 | map 同理? | 迁移 | new(map) 也是 nil | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Go 全版本 | 无 | make 初始化引用→非 nil；new 仅清零→slice/map/chan 为 nil |

## 关键代码
```go
s1 := make([]int, 10)   // []int, len=cap=10, 非 nil
p  := new([]int)        // *[]int, *p 是 nil 空切片
// append 需值类型：append(*p, 1)；但 *p 本身 len=cap=0
s5 := []int{}           // 字面量，非 nil，等价 make([]int,0)
fmt.Println(s1 == nil, *p == nil, s5 == nil) // false true false
```

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡统一为规范术语（六→new、mac→make、耳en→append、反引用→解引用、凝值→零值、字变量→字面量等）；技术结论未做事实性更正 [经验]。

## 总结与追问预判
- 一句话：make 的 slice 非 nil 可直接用；new 的 slice 是 nil 指针，用前还要初始化。
- 核心区别总览见 413；new 实战定位见 413；数组声明见 414（只引不重述）。
