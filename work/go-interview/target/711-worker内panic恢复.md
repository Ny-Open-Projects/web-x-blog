# 711 worker 内 panic 恢复

> 分类：并发模型 | 难度：L3 | 题型：工程题 | 频率：中 | 关键词：**recover** / **debug.Stack** / **不拖垮池**
> 原文锚点：第 50~57 段「recover 不等于 nil 时打印对栈并释放并发度」

## 一句话总述
worker 执行任务要包 `recover`：单个任务 panic 被捕获后打印堆栈、释放占用的并发槽位，避免一个坏任务拖垮整个池。

## 面试官视角
- 意图：是否知道 goroutine 内 panic 必须自回收，否则会杀进程。
- 分档：P5 知要 recover / P6 说清 recover 位置与释放 / P7 知 defer 释放槽位防死锁。
- 红旗：在 goroutine 外 recover；panic 后不释放信号量致死锁。
- 惊艳点：`debug.Stack()` 返回 `[]byte` 堆栈，转 string 打印，定位任务名 `[源码]` runtime/debug。

## 主问答
**Q（面试官原话）：** 协程池里某个任务 panic 了会怎样？怎么兜底？
**A：**
1. **结论**：worker 必须用 `defer recover()` 兜住，否则 panic 跨出 goroutine 直接崩进程。
2. **机制**：recover 非 nil 说明发生 panic，用 `runtime/debug.Stack()` 取堆栈转字符串打印（带任务名）；随后必须释放并发度槽位。
3. **边界**：recover 只在 defer 中有效，且要在 goroutine 内部；漏释放槽位会让池永久少一个名额甚至死锁。
**加分层：** 真实 ants 用 PanicHandler 暴露 panic，比静默吞掉更利于排查。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | panic 后果 | 概念 | 崩进程 | 换题 |
| L2 | 怎么兜 | 机制 | defer recover | 判 P5 |
| L3 | 释放槽位 | 边界 | 防死锁 | 判 P6 |
| L4 | 堆栈定位 | 演进 | debug.Stack | 判 P6+ |
| L5 | PanicHandler | 实战 | 暴露而非吞 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本稳定 | 无 | recover 与 runtime/debug 语义长期不变 `[源码]` 标准库 |

## 关键代码
```go
// 示意，未验证：worker 内 recover 并释放槽位
defer func() {
    if err := recover(); err != nil {
        fmt.Printf("task %s panic: %v\n%s\n", name, err, debug.Stack())
        <-sem // 释放并发度，避免池死锁
    }
}()
```

## 总结与追问预判
- worker 内 defer recover 兜 panic，并打印堆栈、释放槽位。
- 预判：运行计数如何维护 → 见 711。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 利用→nil、勾浪→Go、首时→守时 等拼写还原），技术结论未做更正。
