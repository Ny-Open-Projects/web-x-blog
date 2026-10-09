# 603 Go switch 易被忽视的细节（深挖）

> 分类：Go/语法 | 难度：L3 | 题型：综合题 | 频率：中 | 关键词：**switch 细节全景** / **fallthrough** / **类型一致** / **面试串联**
> 原文锚点：第 3~73 段「case 任意类型/多值/表达式；default 位置；常量重复与布尔特例；省略≡true；类型一致；fallthrough 贯穿与作用域；三条约束」

## 一句话总述
Go `switch` 的细节可归为四条主线：表达式与 case 形态（任意类型/多值/函数调用）、default 与省略（省略≡true、位置自由）、类型严格一致、fallthrough 贯穿与作用域——面试时按"能不能编译 + 运行走哪条"两条线串联即可。

## 思路与架构
- **编译期检查线**：case 常量不可重复（布尔例外）、case 与 switch 类型必须严格一致、fallthrough 须为块末语句/非末 case/default 内禁用——这些都在编译期拦截，答"编译失败"即得分。
- **运行期语义线**：省略表达式≡`switch true`、default 全不命中才执行、case 只命中一个、fallthrough 贯穿到下一 case 开头不重求值、case 块独立作用域——答"运行走哪条"即得分。
- 两条线交叉点：布尔重复 case 编译通过但只走第一个；fallthrough 贯穿后变量不跨块——既涉编译又涉运行，是高频追问。

## 方案取舍
- **为何 Go 默认不贯穿**：避免 C 系语言"漏写 break 意外贯穿"的经典 bug，fallthrough 显式表达意图，更安全可读。
- **为何布尔 case 允许重复**：规范特例，配合 `switch`（无表达式）写多分支布尔判断时允许并列相同条件，但只取第一个，属"合法但应避免"的写法。
- **与 if/else、type switch、select 的边界**：本卡聚焦普通 switch；type switch（`switch v.(type)`）用于类型断言、select 用于 channel 多路，三者机制不同，面试别混。

## 答题技巧
1. **先分两线**：被问"能不能编译"→ 答重复/类型/约束；被问"跑哪个"→ 答省略 true/命中即 break/fallthrough/作用域。
2. **给反例加分**：现场写 `int` vs `int32` 编译失败、`case false: case false:` 合法但只走第一个、fallthrough 后读原值。
3. **踩坑定点**：fallthrough 三条约束（末语句/非末 case/default 禁用）和 case 块独立作用域，是 P7 分水岭。
4. **关联延展**：type switch、select 可顺带提一句，显示体系化认知。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并交叉核对"case 任意类型/多值/表达式、default 位置自由、常量重复布尔特例、省略≡true、类型严格一致、fallthrough 贯穿与作用域及三条约束"四条主线，与 Go 规范一致；"Go 1.20 前需给 rand 设种子"属实（1.20 起自动播种）属旁支。仅做了 ASR 解码将多组术语崩坏词（forthrough/ffault/falsethrough/falthrough→fallthrough、dedeault→default、rucase→case、曲具→求值、星区→星期、构兑→Go、内支→内容 等）统一还原为规范术语，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
