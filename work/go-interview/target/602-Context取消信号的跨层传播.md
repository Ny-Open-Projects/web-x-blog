# 602 Context 取消信号的跨层传播

> 分类：并发模型 | 难度：L2 | 题型：工程题 | 频率：高 | 关键词：**取消传播** / **select** / **Done** / **提前返回**
> 原文锚点：第 33~35、68~103 段「上层取消或超时通知下层退出…用 select 监听 Done 提前返回」

## 一句话总述
取消是协作式的：父 context 超时/调用 cancel 后只关闭自己的 Done channel，需要每一层 goroutine 主动 select <-ctx.Done() 才能收尾退出，否则不会自动杀协程。

## 面试官视角
- 考察意图：是否理解 context 取消是"通知"而非"强杀"，依赖下游配合。
- P5 知 select ctx.Done() / P6 能讲清楚父取消如何经 Done 传到子 / P7 知不监听 Done 会导致泄漏。
- 红旗：以为 cancel 会直接终止子 goroutine；只靠 time.Sleep 模拟超时而不读 Done。
- 惊艳点：cancel 仅关闭 Done channel 并释放定时器，不中断正在运行的子协程，必须子协程自己 return `[源码]`。

## 主问答
**Q（面试官原话）：** context 取消之后，下面那层 goroutine 是怎么知道的？
**A：**
1. **结论**：取消是信号而非强杀，父 ctx 超时/cancel 后关闭其 Done channel。
2. **机制**：子 goroutine 用 `select { case <-ctx.Done(): ... }` 感知关闭并 return，逐层向上收尾。
3. **边界**：若某层不监听 Done，该层协程不会被取消，会持续占用资源直至逻辑自然结束。
**加分层：** 耗时操作务必把 ctx 透传进底层并在每个阻塞点 select Done，否则超时形同虚设。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 怎么感知取消 | 概念 | select Done | 换题 |
| L2 | 父取消咋传子 | 机制 | 关 Done 信号 | 判 P5 |
| L3 | 不监听会怎样 | 边界 | 协程泄漏 | 判 P6 |
| L4 | 强杀可行吗 | 权衡 | 只能协作 | 判 P6+ |
| L5 | 真实泄漏排查 | 实战 | pprof goroutine | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| go1.7 起稳定 `[源码]` | 无 | 取消协作语义自 1.7 不变；cancel 只关 channel 不改运行状态 |

## 关键代码
```go
// 示意，未验证：逐层透传并监听 Done
func slow(ctx context.Context) error {
	select {
	case <-time.After(3 * time.Second):
		return nil
	case <-ctx.Done(): // 外层 1s 超时即走到这里
		return ctx.Err()
	}
}
```

## 总结与追问预判
- 取消=关 Done；子协程必须 select Done 才会退出，否则泄漏。
- 预判：cancel 应在哪调用 → 见 602（及时 cancel）。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：重点核对取消传播与 select 监听机制及版本行为；仅做机翻解码（consol→cancel、contestdown→Done channel、time点after→time.After、HTTV→HTTP 等还原），技术结论未做更正。
