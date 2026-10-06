# 711 提交任务与超时控制

> 分类：并发模型 | 难度：L3 | 题型：工程题 | 频率：中 | 关键词：**select** / **time.After** / **阻塞超时**
> 原文锚点：第 19~36 段「withtimeout 用 time.After 判超时返回 error」

## 一句话总述
提交任务时，用 `select` 同时监听"信号量可写/队列可入"与 `time.After(超时)`，到点未提交成功就返回超时错误，避免永久阻塞。

## 面试官视角
- 意图：是否掌握 select + time.After 这套 Go 标准超时范式。
- 分档：P5 知能超时 / P6 说清 select 双路 / P7 知 time.After 泄漏与 ctx 替代。
- 红旗：用 sleep 轮询；以为 time.After 自动取消。
- 惊艳点：`time.After` 返回 `<-chan Time`，到点触发使 select 走超时分支 `[源码]` 标准库。

## 主问答
**Q（面试官原话）：** 协程池满了，提交任务怎么设超时？
**A：**
1. **结论**：`select` 一路等信号量/队列，一路等 `time.After(timeout)`，先到者胜出。
2. **机制**：超时 channel 到点发值，select 命中超时分支返回自定义 `timeoutError`（含任务名，便于排查）。
3. **边界**：`time.After` 底层是定时器，未触发前不被 GC，高频短超时易堆积，生产应改用 `context` + `AfterFunc`。
**加分层：** select 超时范式通用，但 time.After 有定时器泄漏隐患，长生命周期服务慎用。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 怎么超时 | 概念 | select 双路 | 换题 |
| L2 | 原理 | 机制 | time.After | 判 P5 |
| L3 | 错误返回 | 边界 | timeoutError | 判 P6 |
| L4 | 泄漏隐患 | 演进 | 定时器堆积 | 判 P6+ |
| L5 | ctx 替代 | 实战 | context | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本稳定 | 无 | select + time.After 范式长期不变 `[源码]` 标准库 |

## 关键代码
```go
// 示意，未验证：select 实现提交超时
func submit(task func(), timeout time.Duration) error {
    select {
    case sem <- struct{}{}:
        go run(task)
        return nil
    case <-time.After(timeout):
        return fmt.Errorf("task %s timeout", name)
    }
}
```

## 总结与追问预判
- select 双路，time.After 到点返回超时错误。
- 预判：worker 崩溃怎么办 → 见 711-pool-panic-recover。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 利用→nil、勾浪→Go、首时→守时 等拼写还原），技术结论未做更正。
