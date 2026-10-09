# 603 switch 表达式省略与类型一致性

> 分类：Go/语法 | 难度：L2 | 题型：细节题 | 频率：中 | 关键词：**switch true** / **类型一致** / **default 位置** / **表达式 case**
> 原文锚点：第 11~16、26~36 段「switch 后表达式可省略等价 true；default 位置任意但规范置底；case 与 switch 类型须一致否则编译失败；case 可为表达式或函数调用」

## 一句话总述
Go 的 `switch` 后表达式可省略，省略即等价于 `switch true`（每个 case 须是布尔表达式）；case 表达式类型必须与 switch 表达式**完全一致**（int 与 int32/int64 都算不同类型 → 编译失败）；`default` 分支位置任意（规范建议置底），case 还可是表达式或函数调用。

## 面试官视角
- 意图：考察对 `switch` 表达式"类型严格一致"与"省略即 true"的理解，常用来区分背过语法的候选人与真正用过的人。
- P5 知道 switch 可省略表达式；P6 能说清"省略 ≡ switch true"且类型必须严格一致；P7 能举例 int/int32/int64 不等并解释 default 位置自由。
- 红旗：以为省略表达式后 case 可写任意类型；以为 int 和 int32 是"同一整型"能混用。
- 惊艳点：指出 case 可为函数调用（如 `time.Now().Weekday()`），且 default 放哪都不影响"全不命中才执行"的语义。

## 主问答
**Q（面试官原话）：** switch 后面不写表达式会怎样？case 类型必须和谁一致？
**A：**
1. **结论**：省略 switch 表达式 ≡ 写 `switch true`；此时每个 case 必须是**布尔表达式**，为 `true` 的 case 命中即进；default 位置任意，执行上只在全不命中时才跑（规范建议置底）。
2. **机制**：case 表达式类型必须与 switch 表达式**完全一致**——`int` 与 `int32`/`int64` 语义不同，不能混用，否则编译失败；差异在编译期类型检查阶段拦截。
3. **边界**：case 可为任意类型，也可是**表达式或函数调用**（如 `switch time.Now().Weekday(){ case time.Sunday: ... }`）；多值 case 用逗号分隔，命中任一即进 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 省略表达式 | 基础 | ≡ switch true | 判 P5 |
| L2 | 类型一致 | 类型系统 | int≠int32/int64 | 判 P6 |
| L3 | default 位置 | 语义 | 任意，规范置底 | 判 P6 |
| L4 | case 可函数 | 细节 | 表达式/调用合法 | 判 P6+ |
| L5 | 多值命中 | 机制 | 逗号分隔任一命中 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.0 ~ 1.22+ | 无 | "省略 ≡ switch true""类型严格一致""default 位置自由"均为恒定规则，与版本无关 `[经验]` |

## 关键代码
```go
// 省略表达式 ≡ switch true：每个 case 必须是 bool 表达式
switch {
case x > 10:
    fmt.Println("big")
case x%2 == 0:
    fmt.Println("even")
default: // default 位置任意，规范置底
    fmt.Println("other")
}

// 类型不一致 → 编译失败（int 与 int32 是不同类型）
// var n int = 5
// switch n {
// case int32(1): // cannot use int32(1) as int in case
// case int64(2):
// }

// case 可为函数调用
switch time.Now().Weekday() {
case time.Saturday, time.Sunday:
    fmt.Println("weekend")
}
```

## 总结与追问预判
- 省略表达式 ≡ switch true；case 类型必须严格一致；default 位置自由置底为佳。
- 预判：case 重复常量陷阱 → 见 603；fallthrough 贯穿 → 见 603。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读并重点核对"省略表达式等价 switch true、case 类型须严格一致（含 int/int32/int64 不等）、default 位置任意、case 可为表达式/函数调用"的描述，与 Go 规范一致。仅做了 ASR 解码将多组术语崩坏词（如"曲具"→求值、"星区"→星期、"构兑"→Go、"ffault"→fallthrough 等）统一还原为规范术语，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
