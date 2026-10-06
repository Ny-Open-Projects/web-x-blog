# 44 Go 包管理发展史时间线

> 分类：Go 工程化 | 难度：L3 | 题型：演进题 | 频率：中 | 关键词：**GOPATH 2009**/**godep 2013**/**glide 2014**/**govendor 2015**/**Go Modules 2018**
> 原文锚点：第 109~115 段「主流包管理方式对应的发布时间与版本」

## 一句话总述
Go 包管理从「无版本控制的 GOPATH 模式(2009)」出发，经社区三工具（godep 2013 / glide 2014 / govendor 2015），最终由官方 Go Modules(2018, go1.11) 一统江湖（go1.13 默认）。记住这条时间线，能从一堆标准答案里脱颖而出。

## 面试官视角
- 考察意图：看你是否关心 Go 生态演进，而非只会背 GOPATH/Modules 两个词。
- 分档：P5 知 GOPATH→Modules；P6 知社区三工具及年份；P7 知每个工具的版本节点与「为什么被取代」。
- 红旗答案：说不出社区阶段；或把 Go Modules 当成一开始就有的。
- 惊艳点：点出「官方推荐工具一度多达 15 种，但主流只需记这三种」这一细节。

## 主问答
**Q（面试官原话）：** 讲讲 Go 包管理的发展历史。
**A：**
1. **GOPATH 模式（2009-11-10 起）**：Go 诞生即支持，无版本控制，靠 `$GOPATH/src` 摆包。
2. **godep（2013）**：第一个社区工具，workspace 快照式管理依赖。
3. **glide（2014）**：yaml+lock 声明式记录依赖版本，像 npm/pip。
4. **govendor（2015-08-19）**：基于 vendor 目录（GO15VENDOREXPERIMENT），把依赖拷进工程。
5. **Go Modules（2018-08-24，go1.11）**：官方终局方案，go1.13 起默认启用，一统江湖。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 最早怎么管依赖？ | 基础 | GOPATH 模式 | P5 |
| L2 | 社区有哪些工具？ | 演进 | godep/glide/govendor | P6 |
| L3 | Go Modules 哪年来？ | 版本 | 2018, go1.11 | P6 |
| L4 | 为什么需要 Modules？ | 原理 | GOPATH 无版本、社区碎片化 | P7 |
| L5 | 官方推荐过多少种工具？ | 细节 | 一度达 15 种 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Go 1.0 → 1.11 → 1.13 | GOPATH 主导 → Modules 推出 → Modules 默认 | 时间线：2009 GOPATH / 2013 godep / 2014 glide / 2015 govendor / 2018 Modules |

## 关键代码
```bash
# 历史快照：查看当前 Go 版本对应的默认模式
go version          # >=1.13 默认 Go Modules
echo $GO111MODULE   # auto/on/off
```

## 总结与追问预判
时间线是「GOPATH → godep → glide → govendor → Modules」，关键是每个节点的年份与动机。下一步可深问 go.mod/go.sum 的内部机制（见 404-go-modules）。

## ⚠️ 原文纠错
1. 事实核校： [经验] 时间线 2009 GOPATH / 2013 godep / 2014 glide / 2015 govendor / 2018-08-24 Go Modules(go1.11) / 1.13 默认、官方曾推荐多达 15 种工具——均正确。
2. 崩坏词归一：源码将 Go 音译为勾那/购、Golang 音译为 golwn/godown、godep 音译为 go第一批、glide 音译为 glade、govendor 音译为 gorender、Go Modules 音译为 gomodels、GO15VENDOREXPERIMENT 音译为 go十五renderexperiment；源码将 Go 语言 音译为崩坏词，本卡统一为 Go 语言。
