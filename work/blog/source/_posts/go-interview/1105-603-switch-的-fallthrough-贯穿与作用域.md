---
disableNunjucks: true
title: "603 switch 的 fallthrough 贯穿与作用域"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go/语法 | 难度：L3 | 题型：细节题 | 频率：中 | 关键词：**fallthrough** / **独立作用域** / **case 块** / **最后一条语句**
> 原文锚点：第 37~71 段「case 只命中一个需 fallthrough 贯穿；case 块变量作用域独立（跨块修改不保留）；fallthrough 须为块内最后一条语句、不能最后一 case、default 内不能用」

## 一句话总述
Go 的 `switch` 默认命中一个 case 即 `break`（与他语言不同），需 `fallthrough` 才贯穿到**下一个** case 开头；`fallthrough` 受三条硬约束，且**每个 case 块是独立词法作用域**——跨块后本块变量不可见、对原型变量的就地修改也不跨块保留。

## 面试官视角
- 意图：考察对 `fallthrough` 语义与"case 块独立作用域"的精确理解，常被用来挖"为什么 fallthrough 后读到的还是原值"。
- P5 知道 fallthrough 用于贯穿；P6 能说清"贯穿到下一 case 开头、不重新求值"；P7 能解释独立作用域 + 三条约束并给反例。
- 红旗：以为 fallthrough 会重新求值 case；以为贯穿后上一块变量仍可见；以为 default 里能 fallthrough。
- 惊艳点：用"case 块是独立词法块"解释为何贯穿后读到的 n 仍是 switch 原作用域的值。

## 主问答
**Q（面试官原话）：** fallthrough 怎么用？为什么 fallthrough 后变量值没变？
**A：**
1. **结论**：case 只命中一个，`fallthrough` 把控制权传给**下一个 case 的开头**（不重新求值 case 表达式）；与他语言"默认贯穿"相反，Go 默认不贯穿。
2. **机制（作用域）**：每个 case 块是独立词法块——在 case 内声明的变量仅本块可见；即使修改的是 switch 原型变量，fallthrough 跨到下一块后，下一块读到的仍是** switch 原作用域**的变量值（源中 n 改 999 后贯穿到 default 仍打印原 3）。
3. **边界（约束）**：① fallthrough 必须是当前 case 块的**最后一条语句**（写在 if 里会编译失败）；② 不能出现在**最后一个** case（无下一 case 可贯穿）；③ `default` 内不可用（default 后无 case）`[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 为何要 fallthrough | 基础 | 默认不贯穿，需显式 | 判 P5 |
| L2 | 贯穿到哪 | 语义 | 下一 case 开头，不重求值 | 判 P6 |
| L3 | 作用域 | 关键 | case 块独立，变量不跨 | 判 P6+ |
| L4 | 约束三条 | 细节 | 末语句/非末 case/非 default | 判 P7 |
| L5 | 反例编译失败 | 实战 | if 内 fallthrough 报错 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.0 ~ 1.22+ | 无 | fallthrough 语义与 case 块独立作用域恒定；Go 1.22 起循环变量改为 per-iteration，但与 switch 作用域无关 `[经验]` |

## 关键代码
```go
func scope() {
    n := rand.Intn(5) // 0~4，假定取到 3
    switch n {
    case 0:
        n = 999         // 仅本 case 块内可见
        fallthrough
    default:
        fmt.Println(n)  // 读到 switch 作用域的 n（=3），不是 999 —— case 块独立作用域
    }
}

// 约束反例（编译失败）
// switch {
// case x > 0:
//     if y { fallthrough } // 不是当前块最后一条语句
// case x > 1:
//     fallthrough          // 最后一个 case 不能用 fallthrough
// }
```

## 总结与追问预判
- fallthrough 贯穿到下一 case 开头、不重求值；case 块独立作用域；三条约束别踩。
- 预判：case 重复常量陷阱 → 见 603；表达式省略/类型一致 → 见 603。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读并重点核对"fallthrough 贯穿到下一 case 开头且不重新求值、case 块独立作用域（改 999 后贯穿仍读原值）、fallthrough 须为块内最后语句/不能末 case/default 内不可用"的描述，与 Go 规范一致。源中"Go 1.20 前需给随机数设种子"属实（math/rand 自 1.20 自动播种），为旁支细节未纳入主卡。仅做了 ASR 解码将多组术语崩坏词（forthrough/ffault/falseroom/falsethrough/falthrough/forcethrough→fallthrough、dedeault→default、rucase→case、内支→内容 等）统一还原，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
