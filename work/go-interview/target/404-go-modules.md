# 44 Go Modules 的演进与定位

> 分类：Go 工程化 | 难度：L3 | 题型：概念题 | 频率：高 | 关键词：**Go Modules**/**go1.11**/**go1.13**/**GO111MODULE**/**go.mod**/**go.sum**
> 原文锚点：第 105~115 段「Go Modules 的推出与默认启用」

## 一句话总述
Go Modules 是官方在 2018-08-24 随 Go 1.11 推出的包管理方案，很快一统江湖；go1.11/1.12 需手动开 `GO111MODULE=on`，go1.13 起默认启用。`go.mod` 声明模块与依赖、`go.sum` 记录依赖哈希用于校验。

## 面试官视角
- 考察意图：会不会讲清 Go Modules 的版本节点，以及 go.mod/go.sum 的职责。
- 分档：P5 知 Go Modules 是官方主流；P6 知 1.11 推出、1.13 默认；P7 知 GO111MODULE 三态、go.mod/go.sum 分工与哈希校验机制。
- 红旗答案：以为 Go Modules 从 1.0 就有；或说不清 go.sum 干嘛用。
- 惊艳点：点出「go.sum 存的是模块内容哈希，下载/构建时比对，不一致即报错——实现包校验与防篡改」。

## 主问答
**Q（面试官原话）：** Go Modules 是什么时候来的？go.mod 和 go.sum 干嘛用？
**A：**
1. **推出时间**：官方 2018-08-24 随 Go 1.11 推出，结束「百家争鸣」，成为最主流方案。
2. **默认启用**：go1.11/1.12 需手动 `GO111MODULE=on`；**go1.13 起默认启用**。
3. **GO111MODULE 三态**：on（强制 Modules）/ off（强制 GOPATH）/ auto（默认，有 go.mod 用 Modules）。
4. **go.mod 职责**：声明模块路径、直接/间接依赖及其版本、所需 Go 版本；执行 `go mod init` 生成。
5. **go.sum 职责**：记录每个依赖模块内容的哈希值；构建/下载时比对哈希，不一致报错，实现**包校验与防篡改**。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | Go Modules 哪版来？ | 基础 | go1.11 (2018) | P5 |
| L2 | 哪版默认开？ | 版本 | go1.13 | P6 |
| L3 | GO111MODULE 有哪三态？ | 原理 | on/off/auto | P6 |
| L4 | go.sum 干嘛？ | 机制 | 哈希校验防篡改 | P7 |
| L5 | go.mod 哈希怎么算？ | 进阶 | 模块 zip + go.mod 的哈希入 sum | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Go 1.11+ | 1.13 默认 Modules；1.16 起 GO111MODULE=on 不可关 | 新项目一律 Modules；go.sum 的哈希算法（h1:）属实现细节，能讲清「校验内容完整性」即可 |

## 关键代码
```bash
go mod init example.com/app   # 生成 go.mod
go get github.com/foo/bar@v1.2.0
go mod tidy                   # 整理依赖，更新 go.sum
```

## 总结与追问预判
Go Modules 是包管理的终局方案，记忆点是「1.11 推出 / 1.13 默认 / go.mod 声明 / go.sum 校验」。下一步常问完整发展史时间线。

## ⚠️ 原文纠错
1. 事实核校： [经验] go1.11(2018-08-24) 推出、go1.13 默认、GO111MODULE 三态、go.mod 声明/go.sum 哈希校验——均正确。源码止于列举 go.mod/go.sum 关键问题未展开算法，本卡据 Go 官方事实补全「哈希校验防篡改」定位，未杜撰具体算法。
2. 崩坏词归一：源码将 Go 音译为勾那/购、Go Modules 音译为 gomodels、go.mod 音译为 go点mode、go.sum 音译为 构点sam、Golang 音译为 godown；源码将 Go 语言 音译为崩坏词，本卡统一为 Go 语言。
