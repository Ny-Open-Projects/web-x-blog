# 1019 不等待 goroutine 完成

> 分类：并发模型 | 难度：L2 | 题型：事故题 | 频率：高 | 关键词：**WaitGroup** / **time.Sleep** / **自旋**
> 原文锚点：第 33~57 段「不用 WaitGroup/channel 同步，子 goroutine 可能随主退出；用 bool 自旋轮询低效」

## 一句话总述
启动 goroutine 后若不同步等待，主 goroutine 退出时子协程可能还没跑完（cnt 大概率<100）；用 `WaitGroup` 或 `channel` 等，别用 `time.Sleep` 也别用 bool 变量自旋轮询。

## 面试官视角
- 意图：是否掌握正确的 goroutine 同步手段，识破 sleep/自旋这类伪同步。
- P5 知用 WaitGroup / P6 说清 Add/Done/Wait + 自旋费 CPU / P7 知计算密集下 sleep 永不保险。
- 红旗：用 `time.Sleep` 赌 goroutine 跑完；用循环读 bool 变量判断完成。
- 惊艳点：计算密集型任务里 **sleep 多久都无法保证** goroutine 在时限内完成，只能靠同步原语 `[经验]`。

## 主问答
**Q（面试官原话）：** 我开了 100 个 goroutine 自增，为什么最后数不到 100？
**A：**
1. **结论**：主 goroutine 打印时子协程还没执行完，所以计数偏小且每次不同；要用 WaitGroup/channel 等其结束。
2. **机制**：`time.Sleep` 只是赌时间，计算密集场景 goroutine 未必在 sleep 内跑完；bool 自旋轮询则空转占 CPU，还违背"用通信共享内存"哲学。
3. **边界**：即便主协程是永久阻塞的 HTTP 服务，启动的 goroutine 也需单独确认已完成，不能假设 `[经验]`。
**加分层：** 地道做法：启动前 `wg.Add(1)`，结束 `wg.Done()`，主协程 `wg.Wait()`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 现象 | 概念 | 计数偏小 | 换题 |
| L2 | 手段 | 机制 | WaitGroup | 判 P5 |
| L3 | 反例 | 边界 | sleep/自旋 | 判 P6 |
| L4 | 为什么错 | 演进 | 不保证 | 判 P6+ |
| L5 | 长驻服务 | 实战 | HTTP场景 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本稳定 | 无 | WaitGroup/channel 语义长期稳定 `[源码]` sync 包 |

## 关键代码
```go
// 示意，未验证：WaitGroup 正确等待
package main

import (
	"fmt"
	"sync"
)

func main() {
	var cnt int32
	var wg sync.WaitGroup
	for i := 0; i < 100; i++ {
		wg.Add(1)
		go func() { defer wg.Done(); cnt++ }() // 仅演示等待；真实计数需 atomic/mutex
	}
	wg.Wait()
	fmt.Println(cnt)
}
```

## 总结与追问预判
- 不等 goroutine 会漏算；WaitGroup/channel 才是正解，sleep/自旋是反例。
- 预判：WaitGroup 与 channel 之外的坑 → 见 1019-channel-deadlock。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 购入器/携程→goroutine、淡→Done 等拼写还原），技术结论未做更正。
