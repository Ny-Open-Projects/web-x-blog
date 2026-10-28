---
disableNunjucks: true
title: "1025 Singleflight 源码：合并如何只执行一次"
date: 2026-10-10 11:15:29
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go 并发 | 难度：中高 | 题型：源码 | 频率：中高 | 关键词：**Group、call、WaitGroup、map 合并、Do 逻辑**

> 原文锚点：第 36~60 段「Group 结构体(mu+map)、call(wg+val+chan)、Do 判断 key、首个执行其余 wait」

## 一句话总述
核心结构：Group 持有一把锁和一个 `map[key]*call`；call 内含 WaitGroup、结果值 val 与 channel。Do 进来先加锁查 map：key 不存在→建 call、放入 map、解锁后执行 fn，结束用 `WaitGroup.Done` 唤醒等待者；key 已存在→不执行 fn，直接 `WaitGroup.Wait` 等结果，返回同一 val。一句话背法：**「singleflight 靠 map[key]*call 去重 + WaitGroup 等待，首请求跑 fn 写 val，其余共享」**。

## 面试官视角
源码题是加分项。考官期待你讲清「加锁保护 map」「第一个请求写 map 并跑 fn，其余阻塞在 WaitGroup」「fn 结果存进 call.val，等待者共享」。能补一句「Forget 可删除 map 项让同 key 重新执行」更完整。
- **P5**：说出核心结构 Group(mu+map)。
- **P6**：讲清首请求建 call 跑 fn、其余 WaitGroup.Wait。
- **P7**：点出结果存 call.val 共享、Forget 重置。

## 主问答
**Q（面试官原话）：** singleflight 底层是怎么合并请求的？

**先铺垫（由浅入深第 1 层）**：合并请求的关键不是"少发几次"，而是"只让一个人真正去干、其他人在旁边等、干完了一起拿结果"。要做到这点，需要一张"正在进行中的请求表"记录谁在干，再用一个等待机制让后来者等结果。这就是 Group + map + WaitGroup 的设计。

1. **数据结构（第 2 层）**：Group 含 `mu sync.Mutex` 与 `m map[string]*call`；call 含 `wg sync.WaitGroup`、结果 `val/err` 与 `ch chan struct{}`（用于中断/通知）。
2. **首请求路径（第 3 层）**：加锁查 map，key 不存在则 new 一个 call 并 `m[key]=c`、解锁；执行 fn，完成后 `c.wg.Done()` 唤醒其他等待者，并把结果写入 `c.val`。
3. **后续请求路径（第 4 层）**：map 中已存在该 key，说明有请求在执行，直接 `c.wg.Wait()` 阻塞；fn 结束后拿到 `c.val` 返回，自身不执行 fn。
4. **安全性（第 5 层）**：锁保护 map 读写；WaitGroup 保证首请求结束前其余都在等，从而实现「只执行一次、结果共享」。
5. **重置（第 6 层）**：`Forget(key)` 删除 map 中该项，使后续同 key 请求重新执行 fn（而非搭车），用于结果需主动失效的场景。

## 追问链
| 档位 | 追问 | 答得到（背这句） | 答不出停在哪档 |
|------|------|------------------|----------------|
| L1 | 核心结构？ | Group(mu + map[key]*call) | — |
| L2 | 首请求做什么？ | 建 call 跑 fn 写 val | 停 L2：说不清 |
| L3 | 后续请求？ | WaitGroup.Wait 等结果 | 停 L3：说不清等待 |
| L4 | 结果在哪？ | 存 call.val 共享 | 停 L4：说不清共享 |
| L5 | 怎么重置？ | Forget(key) 删 map 项 | 停 L5：说不清 Forget |

## 版本与兼容性
| 维度 | 说明 |
|------|------|
| 所属包 | `golang.org/x/sync/singleflight`（标准库外） |
| Group.mu + map | 保护请求合并表，并发安全 |
| call.wg | 首请求完成前其余等待者阻塞 |
| 共享结果 | fn 结果写入 call.val/err，等待者直接读取 |
| 重置 | `Forget(key)` 删表项，后续同 key 重新执行 |
| Go 版本 | 与 Go 版本无关，本项目实测 Go 1.26.5 |

## 关键代码
```go
package main

import (
	"fmt"
	"sync"
)

// 极简 singleflight 重实现，证明「map 去重 + WaitGroup 等待 = 只执行一次」
type call struct {
	wg  sync.WaitGroup
	val interface{}
	err error
}

type Group struct {
	mu sync.Mutex
	m  map[string]*call
}

func (g *Group) Do(key string, fn func() (interface{}, error)) (interface{}, error) {
	g.mu.Lock()
	if c, ok := g.m[key]; ok { // 后续请求：直接等
		g.mu.Unlock()
		c.wg.Wait()
		return c.val, c.err
	}
	c := &call{}
	c.wg.Add(1)
	g.m[key] = c // 首请求：建表项
	g.mu.Unlock()

	c.val, c.err = fn() // 只有首请求真正执行 fn
	c.wg.Done()         // 唤醒所有等待者
	return c.val, c.err
}

func main() {
	var g Group
	g.m = make(map[string]*call)
	var hits int
	fn := func() (interface{}, error) { hits++; return hits, nil }

	var wg sync.WaitGroup
	for i := 0; i < 10; i++ { // 10 并发同 key
		wg.Add(1)
		go func() {
			defer wg.Done()
			v, _ := g.Do("k", fn)
			_ = v
		}()
	}
	wg.Wait()
	fmt.Println("fn 执行次数:", hits) // 1 —— 只执行一次，其余共享
}
```

## 总结与追问预判
**背这三句就够**：① **Group 用 `mu + map[key]*call` 记录进行中的请求，并发安全**；② **首请求建 call 跑 fn 写 val，后续请求 `wg.Wait()` 共享同一结果**；③ **Forget(key) 删表项让同 key 重新执行**。
**预判追问**：
- 「具体怎么用？返回值是什么？」→ `g.Do(key, fn)` 返回 `(val, err, shared)`，shared 标是否搭车（见 1025 用法）。
- 「合并结果能主动失效吗？」→ 用 `Forget(key)`（见 1025 Forget）。
- 「它和 CyclicBarrier 区别？」→ singleflight 是请求合并，CyclicBarrier 是多 goroutine 等齐（见 1025 扩展）。

## ⚠️ 原文纠错
1. 事实核校：Group(mu+map)、call(wg+val+chan)、Do 查 key/首执行/余等待、结果共享——均正确，本卡为准。
2. 崩坏词归一：源码将 Go/goroutine/WaitGroup/singleflight 等音译为崩坏词；本卡统一为规范术语。
3. 补强：本卡将「伪代码」升级为**完整可运行的极简重实现**（package main），实际运行可验证 fn 仅执行 1 次，把源码机制落到可跑证据。
