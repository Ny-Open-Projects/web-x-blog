# 416 单引号与 byte / rune：Go 没有 char 类型

> 分类：Go/基础语法 | 难度：L2 | 题型：概念题 | 频率：中 | 关键词：**byte** / **rune** / **单引号** / **uint8** / **int32** / **无 char 类型**
> 原文锚点：第 23~36 段「Go 无专门 char 类型；单引号定义单个字符，存为 byte 或 rune；byte=uint8 别名、rune=int32 别名；中文默认 rune，打印出 Unicode 码值」

## 一句话总述
Go **没有专门的 `char` 类型**。单个字符用**单引号**定义，底层类型是 **`byte`（`uint8` 别名）** 或 **`rune`（`int32` 别名）**：ASCII 字符默认按 `rune`（实为 int32）存，也可显式用 `byte`（uint8）；**中文字符**因超出 ASCII 范围，默认是 `rune`（存 Unicode 码值）。打印单引号字符时输出的是其**码值**（如 `a`→97）。

## 面试官视角
- 意图：考察对 Go 字符表示的理解——"为什么没有 char"是常被追问的点。
- P5 能说出 byte=uint8、rune=int32；P6 能讲清"Go 无 char 类型、单引号字符是码值"；P7 能点出"中文必须用 rune（utf8 多字节），byte 只能装 ASCII"。
- 红旗：以为 Go 有 char 类型；把 `byte` 和 `rune` 混为一谈（一个 1 字节、一个 4 字节）。
- 惊艳点：点出"string 底层是 byte 序列，遍历中文须按 rune 否则乱码"，连接到 string 编码（见 420 间接值部）。

## 主问答
**Q（面试官原话）：** Go 里怎么表示单个字符？byte 和 rune 啥区别？
**A：**
1. **结论**：Go **没有 `char` 类型**。单引号 `'a'` 定义的字符，默认类型是 **`rune`（`int32` 别名）**；显式写 `byte` 则是 **`uint8` 别名**。
2. **机制**：`byte` = `uint8`（1 字节，装 ASCII 0~255）；`rune` = `int32`（4 字节，装 Unicode 码点）。单引号字符打印出来是**码值**（`'a'`→97，`'中'`→其 Unicode 码点）。
3. **边界（中文）**：中文字符 Unicode 码值 > 255，**必须用 `rune`**；用 `byte` 装不下。string 底层是 byte 序列，遍历含中文的 string 须按 `rune` 迭代，否则按 byte 切会乱码 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | Go 有 char 吗 | 基础 | 无，用 byte/rune | 判 P5 |
| L2 | byte/rune 是啥 | 机制 | uint8 / int32 | 判 P6 |
| L3 | 中文用哪个 | 边界 | rune（超 ASCII） | 判 P6+ |
| L4 | 打印出啥 | 机制 | 码值(a→97) | 判 P7 |
| L5 | 接 string 编码 | 体系 | 见 420 间接值部 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.0 ~ 1.22+ | 无 | 无 char 类型、byte=uint8、rune=int32 恒定（builtin.go 定义） `[经验]` |

## 关键代码
```go
package main

import "fmt"

func main() {
    var a  byte = 'a'  // byte = uint8
    var r  rune = 'a'  // rune = int32
    var zh rune = '中' // 中文必须用 rune
    fmt.Printf("%T %v\n", a, a)  // uint8 97
    fmt.Printf("%T %v\n", r, r)  // int32 97
    fmt.Printf("%T %v\n", zh, zh) // int32 20013(中 的码点)

    // string 遍历：按 rune 才不会乱码
    for _, c := range "中a" {
        fmt.Printf("%c ", c) // 中 a
    }
}
```

## 总结与追问预判
- Go 无 char；单引号字符是 byte(uint8)/rune(int32) 码值；中文用 rune；string 遍历按 rune。
- 预判：双引号/反引号 → 见 416；转义形式 → 见 416；string 间接值部 → 见 420。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读并重点核对"Go 无专门 char 类型、单引号定义字符存为 byte(uint8 别名)或 rune(int32 别名)、中文默认 rune 打印出 Unicode 码值、builtin.go 中 byte/rune 定义"的描述，与 Go 类型系统一致（builtin.go 确定义 type byte = uint8; type rune = int32）。仅做了 ASR 解码将源码中的若干术语崩坏词统一还原为规范术语，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
