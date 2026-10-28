---
disableNunjucks: true
title: "44 go get / go install / go build / go run 区别"
date: 2026-10-06 18:57:42
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go 工程化 | 难度：L3 | 题型：命令辨析 | 频率：高 | 关键词：**go get**/**go install**/**go build**/**go run**/**-d 参数**/**main 包**
> 原文锚点：第 53~73 段「go get / go install / go build / go run 四命令区别」

## 一句话总述
`go get` = 克隆远程到 src + 执行 `go install`（可 `-d` 只下载）；`go install` 把可生成可执行文件的包输出到 `$GOPATH/bin`、普通包编译 `.a` 到 `$GOPATH/pkg`；`go build` 在当前目录生成可执行但不复制到 bin；`go run` 编译并运行含 main 的文件、仅供开发测试。

## 面试官视角
- 考察意图：清不清楚四个命令各自做了什么、产物去哪、依赖关系。
- 分档：P5 知 go build 在当前目录、go run 跑 main；P6 知 go get 含 install、`-d` 只下载；P7 知 go install 产物路径、main 包判定、GOPATH 依赖。
- 红旗答案：以为 go build 会把可执行放进 bin；或分不清 go get 与 go install。
- 惊艳点：点出「只有 main 包含 main 函数才能生成可执行」「go install 基于 GOPATH 不能独立目录使用」。

## 主问答
**Q（面试官原话）：** go get、go install、go build、go run 有什么区别？
**A：**
1. **go get**：两步——① 克隆远程代码到 `$GOPATH/src`；② 执行 `go install`。加 `-d` 只下载不安装。
2. **go install**：能生成可执行文件（含 main 包+main 函数）的包 → 输出到 `$GOBIN`（默认 `$GOPATH/bin`）；普通包 → 编译 `.a` 存 `$GOPATH/pkg`（编译缓存提速）。文件名与包名一致，不可指定输出目录。
3. **go build**：在当前目录编译生成可执行文件，但**不复制**到 `$GOPATH/bin`（与 go install 关键区别）；可用 `-o` 指定路径。
4. **go run**：编译并运行 go 文件，用于开发测试；不依赖 GOPATH；**只能编译可执行文件**（含 main 包 main 函数），否则报错。
5. **为什么 go get 含 install 还要 go install**：go get 第一步是下载远程依赖；若本地已有源码就用 go install 免下载。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | go build 产物在哪？ | 基础 | 当前目录 | P5 |
| L2 | go get 干了啥？ | 机制 | 下载+install，-d 只下 | P6 |
| L3 | 怎么判断可生成可执行？ | 原理 | main 包含 main 函数 | P6 |
| L4 | go install 产物去哪？ | 路径 | $GOPATH/bin 或 pkg | P7 |
| L5 | go install 能用独立目录？ | 进阶 | 不能，依赖 GOPATH | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Go 1.0~1.15 | go install 依赖 GOPATH | 1.16+ `go install pkg@version` 可脱离 GOPATH；Go Modules 下语义略变 |

## 关键代码
```bash
go get -d github.com/foo/bar   # 只下载不安装
go install github.com/foo/bar  # 装到 $GOPATH/bin
go build -o app .              # 当前目录生成 app，不进 bin
go run main.go                 # 编译并运行（仅 main 包）
```

## 总结与追问预判
四命令的记忆锚点是「下载/安装/构建/运行」与「是否进 bin」。下一步常问社区包管理工具（godep/glide/govendor）的演进。

## ⚠️ 原文纠错
1. 事实核校： [经验] go get=下载+install(-d 只下)、go install 产物路径(main→bin/普通→pkg)、go build 不进 bin、go run 仅 main、main 包判定——均正确。
2. 崩坏词归一：源码将 Go 音译为勾那/购、go get 音译为 goget、go install 音译为 goin/goingstore/goinschool、go build 音译为 gobuilill、go run 音译为 gorun、pkg 音译为 PKD、-d 参数保留；源码将 Go 语言 音译为崩坏词，本卡统一为 Go 语言。
