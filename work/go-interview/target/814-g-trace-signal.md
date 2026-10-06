# 814 g 的跟踪、信号与创建点字段

> 分类：并发模型 | 难度：L3 | 题型：原理题 | 频率：中 | 关键词：**traceseq** / **sig** / **gopc** / **startpc**
> 原文锚点：第 1~50 段「traceseq 生成跟踪事件顺序号…goPC 记录 go 语句的程序计数器」

## 一句话总述
g 内有一组"可观测性字段"：traceseq/tracelastp 供执行跟踪，sig/sigcode0/1/sigpc 供信号处理，gopc/startpc/ancestors 记录创建来源。

## 面试官视角
- 考察意图：是否理解 g 结构体如何支撑 trace/信号/栈回溯
- P5 知道 gopc 是创建点 / P6 能分三组讲清用途 / P7 能讲 trace 新版本字段的演进
- 红旗：混淆 sigpc 与 gopc；认为 traceseq 是性能字段
- 惊艳点：tracelastp 记录"最后一次发 trace 事件的 P"，便于分析调度行为 `[源码]` runtime2.go

## 主问答
**Q：** g 里那些"调试/跟踪"字段都干嘛用？
**A：**
1. **跟踪组**：traceseq 递增生成事件序号，tracelastp 指向最后发事件的 P `[源码]`。
2. **信号组**：sig/sigcode0/1 存信号号与代码，sigpc 存信号发生时的 PC `[源码]`。
3. **创建点组**：gopc 是 `go` 语句 PC，startpc 是 goroutine 函数入口，ancestors 存祖先 g `[源码]`。
**加分层：** ancestors 仅在 `GODEBUG`/调试标志开启时填充，常态为 nil `[存疑]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | gopc 是什么 | 概念 | go 语句的 PC | 换题 |
| L2 | traceseq 用途 | 机制 | 重建 trace 时间线 | 判 P5 |
| L3 | sigpc 何时写入 | 边界 | 收到信号时 | 判 P6 |
| L4 | ancestors 何时有效 | 权衡 | 调试标志开启才填 | 判 P6+ |
| L5 | 用 trace 定位调度问题 | 实战 | 看 tracelastp 分布 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| traceseq/tracelastp go1.21+ 新执行跟踪器引入 `[存疑]` | 原文称"来自 go1.20 SDK"，版本归属待核 | 答字段用途即可，版本标 `[存疑]` |

## 关键代码
```go
// 示意，未验证：g 的跟踪/信号/创建点字段（节选）
type g struct {
    traceseq   uint64   // 跟踪事件顺序号
    tracelastp uintptr  // 最后发 trace 事件的 P
    sig        uint32   // 信号号
    sigpc      uintptr  // 信号发生时的 PC
    gopc       uintptr  // 创建此 g 的 go 语句 PC
    startpc    uintptr  // goroutine 函数入口
}
```

## ⚠️ 原文纠错
原文称字段"从 go1.20 版本代码复制"，但 traceseq/tracelastp 属于新执行跟踪器，实际在 go1.21+ 引入，版本归属标 `[存疑]`。其余字段名与用途核对无误。

## 总结与追问预判
- 三组可观测字段分别服务 trace、信号、栈回溯；多数仅在调试/跟踪开启时生效。
- 下一题接「g 的 GC 辅助与竞态字段」（见 814-g-debug-gc）。
