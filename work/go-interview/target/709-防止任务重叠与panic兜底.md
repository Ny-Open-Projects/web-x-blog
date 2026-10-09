# 709 防止任务重叠与 panic 兜底

> 分类：工程实践 | 难度：L3 | 题型：工程题 | 频率：中 | 关键词：**串行不重叠** / **Recover** / **主协程常驻**
> 原文锚点：第 20~21 段「recover 确保 panic 被捕获不退出」「任务状态 running」；第 35~36 段「主协程常驻」

## 一句话总述
cron 单条 Job 默认**串行**：前一次未结束、下次到点不会并发重叠（调度器在 `run` 中标记 `running` 后调用）`[源码]`；用 `cron.Recover(logger)` 经 `NewChain` 包裹可捕获 Job 内 panic 避免调度器退出；主协程须常驻。

## 面试官视角
- 意图：是否懂任务执行模型、panic 兜底与生产常驻。
- P5 知 recover 捕获 panic / P6 说清串行不重叠 / P7 知长时间任务需自管并发与超时。
- 红旗：以为到点必并发；以为 panic 不会拖垮调度器。
- 惊艳点：cron v3 单 Job 串行、不重叠 —— 验证源码 `run()` 先置 running 再调 Run `[源码]`。

## 主问答
**Q（面试官原话）：** 定时任务执行超时或 panic 了会怎样？怎么防？
**A：**
1. **结论**：v3 单条 Job 串行执行、到点不重叠；Job 内 panic 会向上传播，需用 `cron.Recover(logger)` 经 `NewChain` 包裹来捕获。
2. **机制**：调度器在 `run()` 里先加锁并标记 `running`，再调用 Job 的 `Run()`；panic 被 Recover 中间件 `recover()` 截住并记日志，调度循环继续 `[源码]`。
3. **边界**：若单次执行超过间隔，下次会被跳过（仍串行）；耗时任务应自建 goroutine + `context` 超时，别依赖调度器并发。
**加分层：** Recover 只救 panic，不救"执行太慢"，慢任务要自管超时与告警。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | panic 咋办 | 概念 | Recover | 换题 |
| L2 | 串行否 | 机制 | running 标记 | 判 P5 |
| L3 | 超时处理 | 边界 | 自建超时 | 判 P6 |
| L4 | 重叠策略 | 权衡 | 自管并发 | 判 P6+ |
| L5 | 漏执行告警 | 实战 | 监控兜底 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| robfig/cron v3 | v3 引入 `NewChain`/`Recover`/`WithLogger` | 用 `cron.NewChain(cron.Recover(logger)).Then(job)` `[源码]` |

## 关键代码
```go
// 示意，未验证：[第三方] robfig/cron/v3
logger := cron.DefaultLogger
c := cron.New()
// 用 NewChain 包 Recover，panic 被捕获不退出
c.AddJob("*/1 * * * *", cron.NewChain(cron.Recover(logger)).Then(myJob))
c.Start()
```

## 总结与追问预判
- 单 Job 串行不重叠；Recover 经 NewChain 防 panic 退出；慢任务自管超时。
- 预判：注册方式 → 见 709；与 Ticker 对比 → 见 709。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 利用→nil、勾浪→Go、首时→守时 等拼写还原），技术结论未做更正。
