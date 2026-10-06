# 44 GOPATH 模式与 GOPATH/GOROOT 区别

> 分类：Go 工程化 | 难度：L3 | 题型：概念题 | 频率：中 | 关键词：**GOPATH 模式**/**GOPATH vs GOROOT**/**src/pkg/bin**/**go env**/**默认目录**
> 原文锚点：第 9~53 段「GOPATH 模式与 GOPATH/GOROOT 区别」

## 一句话总述
GOPATH 模式是 Go 最早期（2009 起）的依赖管理方式，本质只是「放包的路径环境变量」，不支持版本控制；GOPATH 是工作空间（工程+第三方依赖），GOROOT 是 Go 安装目录（内置包/工具，类似 JDK），二者不可同目录。

## 面试官视角
- 考察意图：懂不懂 GOPATH 模式的本质缺陷（无版本控制），以及 GOPATH/GOROOT 的职责边界。
- 分档：P5 知 GOPATH 是工作空间；P6 知 GOPATH 模式不支持版本、GOPATH≠GOROOT；P7 知 go env 配置、目录结构、1.8 起有默认值。
- 红旗答案：以为 GOPATH 是包管理工具本身；或把 GOPATH 设成 GOROOT。
- 惊艳点：点出「GOPATH 模式 vs GOPATH 路径是两个概念——有 GOPATH 路径不代表用了 GOPATH 模式」。

## 主问答
**Q（面试官原话）：** 说说 GOPATH 模式是怎么回事？GOPATH 和 GOROOT 区别？
**A：**
1. **GOPATH 模式本质**：从 Go 诞生即支持，但它不算真正的包管理工具，只是提供「存放包的路径」的环境变量；最大缺陷是**不支持依赖版本控制**（同包导入路径相同，无法区分多版本）。
2. **两个概念区分**：GOPATH 模式=用 GOPATH 管理依赖的方式；GOPATH 路径=该环境变量的值。任何方式都可有 GOPATH 路径，但有路径不一定在用 GOPATH 模式。
3. **GOPATH vs GOROOT**：GOROOT 是 Go 安装目录（内置开发包/工具，类似 JDK）；GOPATH 是工作空间（工程代码+第三方依赖）。二者**不能是同一目录**，否则项目包与标准库重名导致编译问题。
4. **默认值**：Go 1.8 起安装后若未显式设置，默认 `$HOME/go`（Windows 为 `%USERPROFILE%\go`）；1.8 之前需手动配置。
5. **目录结构**：`src` 放源码、`pkg` 放编译后 `.a`、`bin` 放可执行文件；GOPATH 模式下工程必须放 `$GOPATH/src` 下，第三方依赖用 `go get` 拉取。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | GOPATH 干嘛的？ | 基础 | 工作空间，放工程与依赖 | P5 |
| L2 | GOPATH 模式缺陷？ | 原理 | 不支持版本控制 | P6 |
| L3 | GOPATH 和 GOROOT 区别？ | 边界 | 前者工作空间/后者安装目录 | P6 |
| L4 | 怎么看 GOPATH 值？ | 工具 | go env | P6 |
| L5 | 为什么二者不能同目录？ | 进阶 | 包名冲突致编译错 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Go 1.0~1.10 | GOPATH 模式为主流；1.11 起 Go Modules 逐步取代 | 面试仍要会答；新项目用 Go Modules，GOPATH 仅作 GOPATH/bin 路径 |

## 关键代码
```bash
# 查看 GOPATH / GOROOT
go env GOPATH GOROOT
# 配置（单用户）：~/.bash_profile 追加
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
```

## 总结与追问预判
GOPATH 模式的核心记忆点是「无版本控制」和「GOPATH≠GOROOT」。下一步常问 go get/install/build 命令区别与社区工具演进。

## ⚠️ 原文纠错
1. 事实核校： [经验] GOPATH 模式无版本控制、GOPATH/GOROOT 职责区分、目录结构 src/pkg/bin、GOPATH 模式下工程须放 src 下——均正确；源码对「1.8 起 GOPATH 默认值」口播含矛盾（先说默认空后又说给默认目录），已按 Go 官方事实修正为「Go 1.8 起有默认 $HOME/go」。
2. 崩坏词归一：源码将 Go 音译为勾那/购、GOPATH 音译为 gopass、GOROOT 音译为 goroot、go env 音译为 goinv/goENA、bash_profile 音译为 basicprofile；源码将 Go 语言 音译为崩坏词，本卡统一为 Go 语言。
