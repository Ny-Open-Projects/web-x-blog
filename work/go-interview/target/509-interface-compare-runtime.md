# 509 interface 比较的底层结构与相等规则

> 分类：Go/类型系统 | 难度：L3 | 题型：原理题 | 频率：高 | 关键词：**iface** / **eface** / **type 字段** / **data 字段** / **动态类型**
> 原文锚点：第 11~45 段「接口底层两表示：eface(空接口)/iface(有方法接口)；均含 type+data 两指针；比较=type 相同且 data 指向值相同(非指针地址)；空接口 type+data 全空才相等；eface 一般重分配 data 内存」

## 一句话总述
interface 的底层有两种表示：**eface**（空接口，无方法）和 **iface**（有方法的接口），二者都含 **type** 和 **data** 两个指针字段。两个接口相等 = **type 字段相同** 且 **data 指向的内存值相同**（注意是"值"不是"data 指针地址"）。空接口只有 type 和 data 内容**全空**才等于 nil。这是理解"error != nil 却打印 nil"陷阱的钥匙。

## 面试官视角
- 意图：考察 interface 比较的**底层机制**——能否说出 iface/eface 结构和"比较看 type+data 值"。
- P6 能说出 iface/eface 两字段（type/data）；P7 能讲清"比较的是 data 指向的值、不是指针地址"以及"eface 通常重分配 data 内存导致指针值不同"。
- 红旗：以为 interface 比较是比较"指针地址"（实际比 data 指向的值）；把 eface/iface 混为一谈。
- 惊艳点：点出"eface 创建时一般重新分配 data 内存并拷贝值，所以多数情况 data 指针不同但仍可能相等（值相同）"，并接 error nil 陷阱（见 509-error-nil-trap）。

## 主问答
**Q（面试官原话）：** 两个 interface 变量怎么判断相等？底层是什么？
**A：**
1. **结论**：interface 底层分 **eface**（空接口）和 **iface**（有方法的接口），都含两个指针——**type**（动态类型的类型信息）和 **data**（指向动态值的内存）。
2. **机制（相等规则）**：两个接口相等需同时满足——**① type 字段相同**（同一动态类型）；**② data 指向的内存里存的值相同**。关键：**比的是 data 指向的值，不是 data 指针本身的地址**。
3. **机制（空接口 = nil）**：空接口变量只有 **type 和 data 内容都为空**（都为 nil）才 == nil。只要 type 非 nil（即使 data 是 nil 指针），接口就不等于 nil。
4. **边界（eface 内存）**：Go 创建 eface 时通常**为 data 重新分配内存并拷贝动态值**，data 指针指向新空间，所以多数情况下不同接口的 data 指针值不同——这正是"为什么接口不可简单按指针比较"，必须比 content `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 底层两表示 | 基础 | eface/iface | 判 P5 |
| L2 | 两字段 | 机制 | type + data | 判 P6 |
| L3 | 相等比什么 | 机制 | type 同 + data 值同 | 判 P6+ |
| L4 | data 比地址吗 | 深度 | 比指向的值，非地址 | 判 P7 |
| L5 | 接 nil 陷阱 | 体系 | type 非 nil 即非 nil | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.0 ~ 1.22+ | 无 | iface/eface 结构与比较规则恒定；runtime 源码 `runtime/iface.go` 定义不变 `[经验]` |

## 关键代码
```go
package main

import (
    "fmt"
    "reflect"
)

func main() {
    var a int = 1
    var b interface{} = a // eface：type=int, data 指向拷贝的 1
    var c interface{} = 1 // 另一 eface：type=int, data 指向另一份 1

    fmt.Println(b == c) // true：type 同(int) 且 data 指向的值同(1)
    // 但 b、c 的 data 指针通常不同（eface 各自重分配内存）

    // 动态类型不同 → 不等
    var d int32 = 1
    var e interface{} = d // type=int32
    fmt.Println(b == e)   // false：type 不同(int vs int32)，即便值都是 1

    // 用反射看底层 type
    fmt.Println(reflect.TypeOf(b) == reflect.TypeOf(e)) // false
}
```

## 总结与追问预判
- interface 底层 eface/iface，比较 = type 同 + data 值同（非指针地址）；空接口 type+data 全空才 nil；eface 重分配 data。
- 预判：error != nil 陷阱 → 见 509-error-nil-trap；可比较类型清单 → 见 509-comparable-types；间接值部 → 见 420-indirect-part-types。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读并重点核对"接口底层 eface(空接口)/iface(有方法接口)、均含 type+data 两指针、type 为动态类型信息、data 指向动态值、比较=type 同且 data 指向值同(非指针地址)、空接口 type+data 全空才等 nil、eface 一般重分配 data 内存并拷贝值"的描述，与 Go runtime 的 iface/eface 实现一致（runtime 中 eface{_type, data}; iface{itab, data}，itab 含类型信息）。仅做了 ASR 解码将源码中的若干术语崩坏词统一还原为规范术语，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
