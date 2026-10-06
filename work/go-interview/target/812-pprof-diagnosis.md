# 812 pprof 内存采样定位泄漏

> 分类：Go 调优 | 难度：L3 | 题型：工具题 | 频率：中 | 关键词：**pprof**/**heap**/**inuse_space**
> 原文锚点：第 98~101 段「PPROF 工具对运行中的程序采样…定位内存泄露源头」

## 一句话总述
Go 提供 `runtime/pprof`（或 `net/http/pprof`）对**运行中的程序**做内存采样，生成火焰图/调用图，对比多次 heap 快照即可锁定"只增不减"的分配点。

## 面试官视角
- 考察意图：是否会用工具把"内存涨"定位到具体代码，而非猜。
- 分档：P5 知有 pprof；P6 知 `go tool pprof` 看 top/inuse_space；P7 知用 baseline 对比快照、看火焰图、生产鉴权。
- 红旗答案：只会说"看 pprof"却说不出看哪个指标、怎么对比。
- 惊艳点：强调 **对比两次 heap 快照的增量** 才是定位泄漏的正解，而非单次绝对值 `[经验]`。

## 主问答
**Q（面试官原话）：** 怎么用 pprof 排查内存泄漏？
**A：**
1. **结论**：采 heap profile，看 `inuse_space`（常驻内存）与 `alloc_space`（累计分配），重点找**持续上涨、不回落**的对象。
2. **机制**：`import _ "net/http/pprof"` 后访问 `/debug/pprof/heap` 拿快照；`go tool pprof` 进入交互，`top` 看大头分配、`web`/`png` 出调用图与火焰图。
3. **边界**：线上直接开 `net/http/pprof` 要加**鉴权/防火墙**，避免暴露；也可在代码里 `pprof.WriteHeapProfile` 离线落盘再分析。

**加分层：** 同时采 `goroutine` profile 看协程数是否同涨——多数泄漏是"goroutine 泄漏"带动内存涨。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 用什么工具？ | 基础 | pprof | P5 |
| L2 | 看哪个指标？ | 指标 | inuse/alloc_space | P6 |
| L3 | 怎么定位？ | 方法 | 快照对比 | P6 |
| L4 | 线上怎么开？ | 工程 | 鉴权/离线 | P7 |
| L5 | 和 goroutine 联动？ | 进阶 | 协程泄漏带动 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Go 1.0+ | 无 | 答"net/http/pprof 采 heap，对比 inuse_space 快照找只增不减的分配点" |

## 关键代码
```go
import _ "net/http/pprof"
import "net/http"

func main() {
    go func() { http.ListenAndServe("localhost:6060", nil) }() // 暴露 /debug/pprof
    // ... 业务 ...
}
```
```bash
# 取堆快照并分析
go tool pprof http://localhost:6060/debug/pprof/heap
# 交互：top10 / web / png
# 对比两次快照增量：
go tool pprof -base heap1.pb.gz heap2.pb.gz
```

## 总结与追问预判
pprof 定位泄漏靠"快照对比增量"，看 `inuse_space` 谁只增不减，再下钻调用图。追问接"goroutine 泄漏排查"与"cgo 泄漏盲区"。

## ⚠️ 原文纠错
1. 机翻崩坏词归一：`PPROF`/`PPROF工具`→**pprof**；`火焰图调用图`→**火焰图/调用图**（原文拼对，仅大小写与连写问题）；原文把 **Go 语言** 音译为崩坏词、并写作"购物程序"等，本卡统一为 Go 程序/Go 语言。事实正确，仅术语崩坏，本卡已归一 `[经验]`。
2. 原文"PPROF 具体使用将在后面章节详细介绍"——属课程预告，本卡补出实际 `net/http/pprof` 用法与"快照对比"这一关键方法论。
