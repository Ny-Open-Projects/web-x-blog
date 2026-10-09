# 803 词法分析（Lexer/Scanner）

> 分类：Go 编译 | 难度：L3 | 题型：八股题 | 频率：中 | 关键词：**词法分析**/**token**/**scanner**
> 原文锚点：第 35~94 段「词法分析器将源码转 token…scanner.go 与 tokens.go」

## 一句话总述
词法分析（前端第一步）由 scanner 把源码字符流切分为 token 序列（关键字/标识符/运算符/分隔符）；Go 因原生支持 Unicode 按"字符"而非"字节"扫描。

## 面试官视角
- 考察意图：是否理解编译器前端第一阶段的输入/输出与 token 概念。
- 分档：P5 知有"分词"这步；P6 懂 token 是什么、scanner 作用；P7 能指出源码位置。
- 红旗答案：把词法分析和语法分析混为一谈；以为按字节扫描。
- 惊艳点：**Go 源码用 UTF-8，scanner 按 rune（字符）扫描而非 byte**——这是它天然支持 Unicode 标识符的基础 `[源码]`。

## 主问答
**Q（面试官原话）：** 什么是词法分析？产出什么？
**A：**
1. **结论**：词法分析器（scanner/lexer）把源码字符流切分为 token 序列，每个 token 是一个词法单元（关键字、标识符、运算符、分隔符等）。
2. **机制**：scanner 逐字符读取，跳过空白/换行/tab，按关键字与分隔符切分，并记录每个 token 的行列位置供后续报错定位；源码在 `cmd/compile/internal/syntax/scanner.go`，token 定义在同包 `tokens.go` `[源码]`。
3. **边界**：词法分析只做"切词"，不校验语法/语义——"括号是否匹配、类型对不对"是语法/类型检查阶段的事。

**加分层：** 词法分析错误（如非法字符）在最早阶段就被拦截，比运行期才发现高效得多。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 词法分析做什么？ | 基础 | 字符→token | P5 |
| L2 | token 有哪几类？ | 概念 | 关键字/标识符/运算符/分隔符 | P6 |
| L3 | Go 按字节还是字符扫？ | 细节 | rune（Unicode），非 byte | P6 |
| L4 | 源码在哪？ | 源码地图 | syntax/scanner.go + tokens.go | P7 |
| L5 | 与语法分析边界？ | 划分 | 切词 vs 组树 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Go 1.0+ | scanner 路径随重构微调 | 答"syntax 包内 scanner.go，按 rune 扫描" |

## 关键代码
```go
// 调用 go/scanner 体验 token 切分（标准库封装了编译器同款逻辑）
var s scanner.Scanner
fset := token.NewFileSet()
s.Init(fset.AddFile("x.go", -1, len(src)), src, nil, 0)
for tok := s.Scan(); tok != token.EOF; tok = s.Scan() {
    _ = tok // 逐个 token
}
```

## 总结与追问预判
词法分析=切词成 token，是编译最前端；按 rune 扫描支撑 Unicode。追问接"语法分析怎么把 token 组树"。

## ⚠️ 原文纠错
1. 原文机翻崩坏源码路径：`scanago`/`compare`/`sentence` 实为 **`cmd/compile/internal/syntax/scanner.go`**（词法器）与同包 **`tokens.go`**（token 定义）；`compare` 应为 `compile` 包、`sentence` 应为 `syntax` 包 `[源码]`。
