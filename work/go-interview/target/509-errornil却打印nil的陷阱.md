# 509 error != nil 却打印 nil 的陷阱

> 分类：Go/类型系统 | 难度：L3 | 题型：陷阱题 | 频率：高 | 关键词：**error nil 陷阱** / **nil interface** / **nil pointer** / **类型信息非 nil**
> 原文锚点：第 5~10、37~59 段「read 返回 error 指针，打印显示 nil 但 != nil；根因：error 底层 type 为指针类型非 nil；用 printerr 看 tab/data；nil interface(全空) ≠ nil pointer(类型非空)」

## 一句话总述
经典陷阱：函数返回 `error`（底层是指针类型如 `*ReadError`），**打印出来是 nil，但 `err != nil` 却为 true**。根因是接口比较看 **type + data 值**——此时 `err` 的 **type 是非空的指针类型**（*ReadError），所以接口整体不等于 nil，即使 data 指向的指针值是 nil。只有 **type 和 data 都空**才是真 nil interface。

## 面试官视角
- 意图：这是 interface 比较题的**最高频实战陷阱**——考察能否区分"nil interface"和"值为 nil 的指针赋给 interface"。
- P6 能复现陷阱现象；P7 能讲清根因（type 非 nil → 接口非 nil）并给出排查手段（用 `reflect`/printerr 看 type，或返回前显式 `return nil` 而非返回 nil 指针）。
- 红旗：以为"打印 nil 就是接口 nil"（打印只输出 data 值，掩盖了 type）；用 `err == nil` 判断却返回了 `*T(nil)`。
- 惊艳点：给出工程规避——"返回 error 时永远 `return nil` 而不是 `return (*MyErr)(nil)`；或在函数出口用 `if err == nil { return nil }` 归一化"。

## 主问答
**Q（面试官原话）：** 为什么我的 error 打印是 `<nil>`，但 `err != nil` 却是 true？
**A：**
1. **结论**：因为该 error 的底层**动态类型是指针类型（如 `*ReadError`）**，赋给 error 接口后，接口的 **type 字段是非空的**（*ReadError），所以接口整体不等于 nil——即使 data 指向的指针本身是 nil。`Fmt` 打印只看 data 值（显示 `<nil>`），掩盖了 type 非空的事实。
2. **机制（nil interface vs nil pointer）**：
   - **真 nil interface**：type 和 data **都为空** → `== nil` 为 true。
   - **nil pointer 赋给 interface**：type = *T（非空），data = nil 指针 → 接口**不等于 nil**。二者天壤之别。
3. **排查**：用 `reflect.TypeOf(err)` 或打印接口底层 tab/data（如 `printerr` 类工具）能看到 type 实际是 *ReadError，data 是 nil。
4. **规避（工程）**：返回 error 的函数**永远 `return nil`**，不要 `return (*MyError)(nil)`；或在出口归一化：`if realErr == nil { return nil }` `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 现象复现 | 基础 | 打印 nil 但 != nil | 判 P5 |
| L2 | 根因 | 机制 | type 非 nil → 接口非 nil | 判 P6 |
| L3 | nil interface vs nil ptr | 深度 | type 都空才真 nil | 判 P6+ |
| L4 | 怎么排查 | 实践 | reflect 看 type | 判 P7 |
| L5 | 怎么规避 | 工程 | return nil 归一化 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.0 ~ 1.22+ | 无 | nil interface ≠ nil pointer 行为恒定；`error` 接口含 type+data 两字段恒定 `[经验]` |

## 关键代码
```go
package main

import (
    "fmt"
)

type ReadError struct{}

func (r *ReadError) Error() string { return "read error" }

// 陷阱：返回 *ReadError(nil)，赋给 error 接口 → type=*ReadError 非 nil
func readBad() error {
    var p *ReadError = nil
    return p // 返回的 error 接口 type=*ReadError, data=nil → err != nil 为 true！
}

// 正确：显式 return nil
func readGood() error {
    var p *ReadError = nil
    if p == nil {
        return nil // 真 nil interface
    }
    return p
}

func main() {
    err := readBad()
    fmt.Println(err)        // <nil>（打印只输出 data 值）
    fmt.Println(err != nil) // true！type=*ReadError 非 nil
}
```

## 总结与追问预判
- 陷阱根因：error 底层是指针类型 → type 非空 → 接口 != nil，即使 data 为 nil；打印只显 data 值。
- 预判：比较底层 → 见 509；可比较清单 → 见 509；避坑归一化 → 见本方工程规避。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读并重点核对"read 返回 error 指针、打印显 nil 但 != nil、根因是 error 底层 type 为指针类型非 nil(空接口/非空接口比较看 type+data)、nil interface 与 nil pointer 区别、用 printerr 看 tab/data 类型信息"的描述，与 Go interface 语义一致（指针类型赋给接口后接口非 nil 是公认陷阱；fmt 打印只看 data 值）。仅做了 ASR 解码将源码中的若干术语崩坏词统一还原为规范术语，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
