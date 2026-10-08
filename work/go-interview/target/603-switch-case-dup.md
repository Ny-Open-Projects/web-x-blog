# 603 switch 的 case 重复常量陷阱

> 分类：Go/语法 | 难度：L2 | 题型：细节题 | 频率：中 | 关键词：**switch** / **case 重复** / **布尔常量特例** / **编译期错误**
> 原文锚点：第 17~25 段「case 常量表达式不能重复否则编译失败；布尔类型常量 case 可重复且能编译通过；Go 1.20 官方编译器对重复常量一律拒绝；命中即 break 只执行第一个」

## 一句话总述
Go 的 `switch` 里普通类型（int/string 等）的**常量 case 表达式不能重复**，重复直接编译失败；唯独**布尔常量 case 允许重复**且能编译通过——但命中后默认 break，只执行第一个匹配的 case。这是极易在面试里被追问的反直觉细节。

## 面试官视角
- 意图：考察对 Go `switch` 语义边界的掌握，尤其是"看似编译错误实则合法"的布尔特例。
- P5 知道 case 不能重复；P6 能说出布尔常量重复是语言允许的特例；P7 能讲清"为何允许"及"命中即 break 只走第一个"。
- 红旗：以为所有重复 case 都编译失败；或以为布尔重复后两个分支都会执行。
- 惊艳点：引用 Go 语言规范"Duplicate cases are allowed if they are all boolean constants"。

## 主问答
**Q（面试官原话）：** switch 的 case 后面能写重复的常量吗？
**A：**
1. **结论**：普通类型的常量 case 表达式**不能重复**（如两个 `case "a"` 或两个 `case 1`），重复即 `duplicate case ... in switch` 编译失败，含多值 `case 1, 1` 也是同样错误。
2. **机制**：唯独**布尔常量 case 可重复**（如两个 `case false:`），Go 规范明确允许；但 `switch` 命中某 case 后默认 `break`，所以只会执行**第一个**匹配的布尔 case，后续重复的永远走不到。
3. **边界**：Go 1.20 官方编译器对重复常量 case 一律拒绝（由编译器在编译期保证，非运行时）；这是语法静态检查，与运行时取值无关 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 常量能重复吗 | 基础 | 普通不能，布尔可 | 判 P5 |
| L2 | 布尔为何可重复 | 规范 | 语言特例，命中即 break | 判 P6 |
| L3 | 多值 case 重复 | 细节 | 含重复值也失败 | 判 P6 |
| L4 | 重复后走哪个 | 语义 | 只走第一个 | 判 P6+ |
| L5 | 哪个版本行为 | 版本 | 1.20 起编译器统一拒绝 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.0 ~ 1.22+ | 无 | 普通常量 case 不可重复是恒定规则；布尔常量重复特例自 Go 1.0 即存在，Go 1.20 起官方编译器对重复非布尔常量严格拒绝 `[经验]` |

## 关键代码
```go
// 普通类型常量 case 重复 → 编译失败
// switch s {
// case "a":
// case "a": // duplicate case "a" in switch
// }

// 多值 case 内含重复值 → 同样编译失败
// switch n {
// case 1, 1: // duplicate case 1 in switch
// }

// 布尔常量 case 重复 → 编译通过，但只执行第一个匹配的 case
func demo() {
    switch {
    case false: // 第一个 false，命中即 break
        fmt.Println("first false")
    case false: // 编译器允许重复布尔常量，但永远走不到
        fmt.Println("never reached")
    default:
        fmt.Println("default")
    }
}
```

## 总结与追问预判
- 普通常量 case 不可重复（编译失败）；布尔常量 case 重复合法但只走第一个。
- 预判：switch 表达式缺省为 true / 类型一致 → 见 603-switch-default-expr；fallthrough 贯穿 → 见 603-switch-fallthrough。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读并重点核对"常量 case 不可重复、布尔常量 case 可重复、Go 1.20 编译器行为、命中即 break 只走第一个"的描述，与 Go 语言规范一致。仅做了 ASR 解码将多组术语崩坏词（如"曲具"→求值、"星区"→星期、"ffault/forthrough/falsethrough/falthrough"→fallthrough、"构兑"→Go 等）统一还原为规范术语，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
