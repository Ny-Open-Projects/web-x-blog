---
disableNunjucks: true
title: "815 p 的本地运行队列与 runnext"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：并发模型 | 难度：L3 | 题型：原理题 | 频率：高 | 关键词：**runq** / **runnext** / **工作窃取** / **256**
> 原文锚点：第 78~92 段「runq 是 256 个元素的数组…runnext 不为空时优先执行它里面的 g」

## 一句话总述
每 P 有一个 256 无锁环形本地队列 runq(runqhead/runqtail 做下标)，runnext 存"下一个要跑的 G"且优先级高于 runq；从 go1.5 起被唤醒/阻塞返回的 G 注入 runnext 以获优先执行 `[源码]` runtime2.go。

## 面试官视角
- 考察意图：是否理解本地队列为何快、runnext 解决什么问题
- P5 知道 runq 是 256 本地队列 / P6 讲清 runnext 优先级与 go1.5 注入 / P7 讲 work-stealing 与全局队列关系
- 红旗：把 runq 当有锁队列；答不出 runnext 存在的理由
- 惊艳点：runnext 让"刚被唤醒的 G"立刻续跑而非重新排队，避免被偷走、降低延迟 `[源码]` runtime/proc.go

## 主问答
**Q：** P 的本地队列怎么组织，runnext 干嘛用？
**A：**
1. **runq(256, 无锁)**：runqhead/runqtail 是环形下标，本地入队出队无锁，快于全局队列 `[源码]`。
2. **runnext 高优先级**：非空的 runnext 直接优先跑，不进 runq 竞争 `[源码]`。
3. **go1.5 注入**：被阻塞返回的 G 放进 runnext，立即续跑、避免重排被偷 `[源码]`。
**加分层：** runq 满才转全局队列；空闲 P 会从别 P 偷一半(runq 半数)做 work-stealing。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | runq 大小 | 概念 | 每 P 256 无锁 | 换题 |
| L2 | runnext 干嘛 | 机制 | 优先执行的 G | 判 P5 |
| L3 | 满了对策 | 边界 | 转全局队列 | 判 P6 |
| L4 | 偷几个 | 权衡 | 偷半数，保持均衡 | 判 P6+ |
| L5 | 队列饥饿调优 | 实战 | 看 runq 长度与偷取率 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| go1.5+ runnext 注入 | go1.5 引入 runnext 优先续跑 `[源码]` runtime2.go | 答"runnext 高优先级、go1.5 起阻塞返回 G 注入"即可 |

## 关键代码
```go
// 示意，未验证：p 的本地运行队列字段（节选）
type p struct {
	runqhead uint32       // 队头下标
	runqtail uint32       // 队尾下标
	runq     [256]guintptr // 本地可运行 G 环形数组
	runnext  guintptr     // 下一个优先执行的 G
}
```

## ⚠️ 原文纠错
未发现技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 勾浪→Go、rankq→runq、runx→runnext 等拼写还原），技术结论未做更正。

## 总结与追问预判
- runq 是 256 无锁本地队列，runnext 优先续跑被唤醒 G；满则转全局、空闲则偷半数。
- 深入见 815.md（本地/全局队列与 work-stealing）。
