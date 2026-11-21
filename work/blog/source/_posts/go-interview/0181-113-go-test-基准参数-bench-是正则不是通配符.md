---
disableNunjucks: true
title: "113 go test 基准参数：-bench 是正则不是通配符"
date: 2026-10-07 03:57:52
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go 测试 | 难度：L3 | 题型：陷阱题 | 频率：高 | 关键词：**-bench 正则**/**-benchtime**/**-benchmem**/**-cpu**/**GOMAXPROCS**

> 原文锚点：第 44~58 段「执行时间与 CPU 参数」、第 76~81 段「按名字筛选」

## 一句话总述
用 `go test -bench` 运行基准测试，其值**是正则表达式而不是 shell 通配符**：`-bench=.` 匹配全部，`-bench=BenchmarkF` 匹配名字含该子串的函数。另可用 `-benchtime` 指定时长（默认 1 秒）、`-benchmem` 打开内存统计、`-cpu` 指定逻辑 CPU 数。

## 面试官视角
这题的陷阱是**把 `-bench` 当通配符**。考官会问「`-bench=Benchmark*` 为什么没匹配到」，正确答案是 `*` 在正则里是量词不是通配符。能顺带说出 `-cpu` 的值就是 GOMAXPROCS，说明你真的调过参数。

## 主问答
**Q（面试官原话）：** 跑基准测试有哪些常用参数？

1. **-bench 用正则**：参数值是正则表达式而非通配符；`.` 在正则中表示任意字符，因此 `-bench=.` 会匹配全部基准函数。
2. **子串匹配**：`-bench=BenchmarkF` 是未锚定的子串匹配，名字里含该片段的函数都会被执行，可用来只跑一部分。
3. **-benchtime 定时长**：默认每个基准函数执行 1 秒；指定更长时间则执行次数更多，结果相对更准确。
4. **-benchmem 看内存**：加上该参数会额外输出每次操作分配的字节数与内存分配次数。
5. **-cpu 定核数**：默认使用操作系统的 CPU 核心数；指定多个值时基准函数会在每种逻辑 CPU 数下各跑一遍，该值即 GOMAXPROCS。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 用什么命令跑？ | 说不出 go test -bench |
| L2 | -bench 的值是通配符吗？ | 误以为是通配符 |
| L3 | 默认跑多久？ | 说不出 1 秒 |
| L4 | 怎么看内存分配？ | 说不出 -benchmem |
| L5 | -cpu 和什么对应？ | 说不出 GOMAXPROCS |

## 版本与兼容性
| 参数 | 默认 | 作用 |
|------|------|------|
| -bench | 无（不跑基准） | 正则筛选函数 |
| -benchtime | 1s | 单次基准时长 |
| -benchmem | 关闭 | 输出内存指标 |
| -cpu | 本机核数 | 设置 GOMAXPROCS |

## 关键代码
```go
// 命令行示例（注释形式，便于记忆）
// go test -bench=.                      跑全部基准
// go test -bench=BenchmarkF             跑名字含 BenchmarkF 的
// go test -bench=. -benchtime=2s        每个跑 2 秒
// go test -bench=. -benchmem            附带 B/op 与 allocs/op
// go test -bench=. -cpu=2,4,8           在 2/4/8 个逻辑 CPU 下各跑一遍
```

## 总结与追问预判
核心：**-bench 传正则、默认 1 秒、-benchmem 看内存、-cpu 即 GOMAXPROCS**。追问常拐向「为什么 `-bench=Benchmark*` 不work」，备好「`*` 是正则量词，应写 `Benchmark.*`」这句。

## ⚠️ 原文纠错
1. 事实核校： [经验] 原文把 `-bench` 的参数说成「通配符」「星号表示匹配任意多个」——**错误**。该参数的值是**正则表达式**：`-bench=.` 中的 `.` 是正则的「任意字符」所以匹配全部；若按通配符思维写 `-bench=Benchmark*`，在正则里表示「Benchmark 重复任意次」，语义完全不同。
2. 事实核校： [经验] 原文称「-cpu 的数量其实就是 GOMAXPROCS 的数量」——正确；补充该参数会被转换为运行时的 GOMAXPROCS 值，用于在多组并发度下对比同一段代码。
3. 崩坏词归一：源码将基准测试 / 正则 / GOMAXPROCS 等音译为多组崩坏词，本卡统一为规范术语。
