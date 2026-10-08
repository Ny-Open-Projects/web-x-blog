# 1020 WaitGroup.Add 时机陷阱（必须 goroutine 外）

> 分类：Go 并发/sync | 难度：L3 | 题型：陷阱题 | 频率：高 | 关键词：**Add 在 goroutine 外** / **Wait 竞态** / **计数归零提前返回** / **负计数 panic**
> 原文锚点：第 17~24 段「WaitGroup.Add 写在子协程内部→主协程 Wait 可能先于 Add 执行→计数异常」

## 一句话总述
`WaitGroup.Add` **必须在启动 goroutine 之前、Wait 之前、在主协程里调用**。若把 `Add` 写进子协程内部，goroutine 调度时机不确定，主协程的 `Wait()` 可能先于任何 `Add` 执行——计数仍是 0 则 Wait 立即返回（子任务根本没被等），或 Add 晚于 Wait 触发负计数 panic。这与"传指针/noCopy"是不同坑（见 913）。

## 面试官视角
- 考察意图：是否真理解 Add/Done/Wait 的时序契约，而不只是会写
- P5 知 Add/Done/Wait 语义；P6 能讲清"Add 放 goroutine 内→Wait 竞态"；P7 能讲负计数 panic 与修复
- 红旗：把 Add 写在 `go func(){...}` 内部；以为"先 go 后 Add 也行"
- 惊艳点：点出"goroutine 调度不确定→Wait 可能抢在 Add 前"这一竞态本质 [源码]

## 主问答
**Q（面试官原话）：** WaitGroup 用的时候还有什么坑，除了传指针？
**A：**
1. **Add 时机是隐性坑**：`Add` 必须写在 **goroutine 外、Wait 之前**；若写在子协程里，主协程 `Wait()` 可能在第一个 `Add` 执行前就跑完——计数还 0，Wait 直接返回，子任务没被等 [源码]。
2. **后果两样**：轻则"等了个寂寞"（结果小于预期如 <1000），重则 `Add` 在 `Wait` 之后发生导致 **负数计数 panic**（sync: negative WaitGroup counter）[源码]。
3. **修复=外提 Add**：启动 goroutine 前先 `Add(1)`，goroutine 内只 `Done()`，主协程 `Wait()`——时序契约稳 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | Add 干嘛 | 语义 | 增计数 | P5 |
| L2 | 放 goroutine 内 | 时序 | Wait 竞态 | P6 |
| L3 | 后果 | 边界 | 不等/负计数 | P6+ |
| L4 | 修复 | 实战 | 外提 Add | P7 |
| L5 | 替代 | 选型 | errgroup | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| go1.0+（sync） | 无 | Add 必须在 Wait 前调用的时序契约长期成立 |

## 关键代码
```go
var wg sync.WaitGroup
var cnt int32
for i := 0; i < 1000; i++ {
    // ❌ Add 写进 goroutine：Wait 可能抢在 Add 前，cnt 可能 < 1000 甚至 panic
    // go func() { wg.Add(1); atomic.AddInt32(&cnt, 1); wg.Done() }()
    // ✅ Add 写在 goroutine 外
    wg.Add(1)
    go func() { atomic.AddInt32(&cnt, 1); wg.Done() }()
}
wg.Wait() // 此刻计数已稳定为 1000
```

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡统一为规范术语（SYC→sync、勾引性→goroutine、购入t→goroutine、主学程→主协程、勾引性的调度→goroutine 调度等）；技术结论未做事实性更正 [经验]。

## 总结与追问预判
- Add 外提、Done 在 goroutine 内、Wait 在主协程，是 WaitGroup 时序铁律。
- WaitGroup 传指针/noCopy 与循环变量坑见 913-waitgroup-usage（只引不重述）；配套"锁配对"见 1020-lock-pairing-reentrant。
