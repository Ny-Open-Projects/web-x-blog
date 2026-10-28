---
disableNunjucks: true
title: "1019 不等待 goroutine 完成"
date: 2026-10-10 10:09:42
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：并发模型 | 难度：L2 | 题型：事故题 | 频率：高 | 关键词：**WaitGroup** / **time.Sleep** / **自旋**

> 原文锚点：第 33~57 段「不用 WaitGroup/channel 同步，子 goroutine 可能随主退出；用 bool 自旋轮询低效」

## 一句话总述
启动 goroutine 后若不同步等待，主 goroutine 退出时子协程可能还没跑完（cnt 大概率<100）；用 `WaitGroup` 或 `channel` 等，别用 `time.Sleep` 也别用 bool 变量自旋轮询。一句话背法：**「不 Wait 子 goroutine 会漏算/主退出即丢；用 WaitGroup/channel 同步，sleep/自旋是伪同步反例」**。

## 面试官视角
这是 goroutine 同步的入门但高频题。考官要看你是不是真用对同步原语，还是拿 sleep 凑合。
- **P5**：知道用 WaitGroup。
- **P6**：说清 Add/Done/Wait + 自旋费 CPU。
- **P7**：知道计算密集下 sleep 永不保险。
- **红旗**：用 `time.Sleep` 赌 goroutine 跑完；用循环读 bool 变量判断完成。
- **惊艳点**：计算密集型任务里 **sleep 多久都无法保证** goroutine 在时限内完成，只能靠同步原语 `[经验]`。

## 主问答
**Q（面试官原话）：** 我开了 100 个 goroutine 自增，为什么最后数不到 100？

**先铺垫（由浅入深第 1 层）**：`go` 一去不回。主 goroutine 打印那一行时，那 100 个子协程可能还没被调度到——于是计数偏小且每次不同。光"等一阵子"解决不了根因。

1. **结论（第 2 层·机制）**：主 goroutine 打印时子协程还没执行完，所以计数偏小且每次不同；要用 WaitGroup/channel 等其结束 `[源码]`。
2. **机制（第 3 层）**：`time.Sleep` 只是赌时间，计算密集场景 goroutine 未必在 sleep 内跑完；bool 自旋轮询则空转占 CPU，还违背"用通信共享内存"哲学 `[经验]`。
3. **边界（第 4 层）**：即便主协程是永久阻塞的 HTTP 服务，启动的 goroutine 也需单独确认已完成，不能假设 `[经验]`。
4. **正确写法（第 5 层·实战）**：启动前 `wg.Add(1)`，结束 `wg.Done()`，主协程 `wg.Wait()` `[源码]` sync 包。
5. **计数注意（第 6 层）**：多 goroutine 自增要 `atomic`/`Mutex` 保护，否则又引入数据竞争（见 1018）`[经验]`。

## 追问链
| 档位 | 追问 | 答得到（背这句） | 答不出停在哪档 |
|------|------|------------------|----------------|
| L1 | 现象 | 计数偏小 | — |
| L2 | 手段 | WaitGroup 同步 | 停 L2：判 P5 |
| L3 | 反例 | sleep / 自旋 | 停 L3：判 P6 |
| L4 | 为什么错 | 不保证完成 | 停 L4：判 P6+ |
| L5 | 长驻服务 | HTTP 场景也需确认 | 停 L5：判 P7 |

## 版本与兼容性
| 维度 | 说明 |
|------|------|
| Go 全版本稳定 | WaitGroup/channel 语义长期稳定 `[源码]` sync 包 |
| time.Sleep | 伪同步：计算密集下无法保证 goroutine 在时限内完成 |
| bool 自旋 | 空转占 CPU + 仍可能是数据竞争，不推荐 |
| 推荐写法 | wg.Add(1) 在 go 外 / wg.Done() defer / wg.Wait() 主协程 |

## 关键代码
```go
package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

func main() {
	const n = 100
	var cnt int32
	var wg sync.WaitGroup

	for i := 0; i < n; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			atomic.AddInt32(&cnt, 1) // 用 atomic 避免数据竞争
		}()
	}
	wg.Wait()
	fmt.Println("cnt =", atomic.LoadInt32(&cnt)) // 稳定输出 100
}
```

## 总结与追问预判
**背这三句就够**：① **不 Wait 子 goroutine 会漏算、主退出即丢**；② **WaitGroup/channel 才是正解**；③ **sleep/自旋是伪同步反例**。
**预判追问**：
- 「WaitGroup 怎么用才对？」→ Add 在 go 外、Done 用 defer、Wait 在主协程（见 1020 Add 时机）。
- 「计数还有坑？」→ 多写自增需 atomic/Mutex，否则数据竞争（见 1018）。
- 「channel 怎么等？」→ 关闭 channel 广播 / done channel 收信号（见 1021/1023）。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 购入器/携程→goroutine、淡→Done 等拼写还原），技术结论未做更正。
