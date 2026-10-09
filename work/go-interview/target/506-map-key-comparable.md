> 原文锚点：第 13~23 段「只可比较的类型才能作为 map 的 k…除 slice/map/functions 几种类型外其他类型都可比较…数组元素类型不可比较则数组不可比较…结构体全部字段可比较才可比较…切片不能作为 map 的 k，只能作为值」（可比较类型作 key 前提 + slice/map/func 不可作 key + 数组/结构体字段细则）

## 一句话总述
**map 的 key 类型必须是「可比较（comparable）」类型**——`func`/`map`/`slice` 三者不可比较，因此**直接作 key 会编译报错**；数组/结构体只有在「所有元素/字段都可比较」时才可作 key。这是把「类型可比较性」（见 509.md`）落到 map 实战的硬约束。

## 面试官视角
这题考「可比较性」与「map key」的连接。考点：① 哪三类绝对不能作 key（编译期就拒）；② 数组/结构体作 key 的细则；③ 把「可比较」概念迁移到「map 约束」的能力。能说「`map[[]int]int` 编译不过」比只背「slice 不可比较」更显实战。

## 主问答
**Q（面试官原话）：** float 或切片可以作为 map 的 key 吗？为什么？

**A：**
1. **前提：key 必须可比较**。Go 规定 map key 类型必须满足 `comparable` 约束——只有「可比较类型」才能作 key，不可比较类型作 key 在**编译期**直接报错（`invalid map key type`）。
2. **slice/map/func 绝对不能作 key**：这三类类型彼此不可比较（且无法哈希），声明 `map[[]int]int` 或 `map[map[string]int]int` 会**编译失败**；切片只能作 map 的 **value**，不能作 key。
3. **数组/结构体的细则**：数组只有在「元素类型可比较」时才可比较、才可作 key（如 `[3]int` 可作 key）；若数组元素含 `map`/`slice`/`func` 则整体不可比较、不能作 key。**结构体**同理——所有字段都可比较（不含 map/slice/func 字段）才可作 key，否则编译报错。
4. **float 可作 key 但有坑**（见 506.md`）；指针可作 key 但按**地址**比较（见 506.md`）——二者合法但行为反直觉。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 哪类不能作 key | 编译约束 | func/map/slice | 答不出算 L1 未过 |
| L2 | 报错在何时 | 编译期 | 声明即 invalid map key type | 说「运行时」算 L2 未过 |
| L3 | 数组能作 key? | 字段细则 | 元素全可比较才可 | 说「不能」算 L3 未过 |
| L4 | 结构体作 key? | 字段细则 | 含 map/slice 字段则不可 | 无边界算 L4 未过 |
| L5 | 与可比较清单关系 | 迁移能力 | key 约束=可比较性落地 | 孤立答算 L5 未过 |

## 版本与兼容性
- 可比较类型清单（`509-comparable-types.md`）自 Go 1.0 恒定；`comparable` 约束对 map key 同样恒定，无版本差异。
- Go 1.18+ 引入 `comparable` 约束（泛型），但 map key 的 comparable 语义不变。
- 注意与「map 并发/无序/float key 风险」（`914-map-concurrency-float.md`）区分：本卡只讲「key 类型合法性」，那张讲「float key 取值异常 + 并发 panic + 无序」。

## 总结与追问预判
收口：**map key 必须 comparable → func/map/slice 编译期拒、数组/结构体看字段；切片只能当 value**。预判追问：① float key 的精度与 NaN 诡异（见 506.md`）；② 指针 key 按地址（见 506.md`）。回答时把「`map[[]int]int` 编译报错」一句抛出，最显你把概念落到了代码层。

## ⚠️ 原文纠错
源视频转写将 Go / map key / 可比较类型 / 切片 等音译为若干崩坏词，本卡已统一还原为规范术语（Go / map 键 / 可比较（comparable）类型 / 切片 slice）。交付卡禁止保留任何原词崩坏写法。

> **[经验]** 答「切片能作 key 吗」**直接给编译错误**最稳：`var m map[[]int]int` 报 `invalid map key type []int`。比泛泛说「slice 不可比较」更能证明你真踩过——编译器在 key 合法性上比人严，运行前就拦。

```go
package main

// slice/map/func 作 key → 编译报错（invalid map key type）
// var bad1 map[[]int]int            // ❌ []int not comparable
// var bad2 map[map[string]int]int  // ❌ map not comparable

// 数组元素可比较 → 可作 key
var ok1 map[[3]int]int // ✅ [3]int 可比较

// 结构体：字段全可比较才可作 key
type Good struct{ A, B int }       // ✅ 可作 key
type Bad  struct{ M map[int]int }  // ❌ 含 map 字段 → 不可比较 → 不可作 key
// var ok2 map[Good]int // ✅
// var bad2 map[Bad]int // ❌ compile error

func main() {
	_ = ok1
	_ = Good{}
	_ = Bad{}
}
```
