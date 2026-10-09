# 1022 协程泄露的具体触发场景（除 channel 收发外）

> 分类：Go 运行时 · 并发缺陷 | 难度：L3 | 题型：事故题 | 频率：高 | 关键词：**协程泄露**/**defer 误用**/**nil channel**/**空 select**/**文件句柄堆积**
> 原文锚点：第 9~39 段「defer 误用致文件句柄堆积；nil channel 读写永久阻塞；空 select 永久阻塞；channel 收发不匹配」

## 一句话总述
协程泄露的底层都是"协程被创建却永不退出"；除经典的 channel 收发不匹配外，还有三类 `1019` 未覆盖的具体坑：**defer 误用**（开十万文件、函数退出才统一关闭 → 文件句柄堆积）、**nil channel 读写**（只声明未 make 的 channel 读写都永久阻塞）、**空 `select{}`**（无分支永久阻塞）。识别它们靠 `runtime.NumGoroutine()` 看数量只增不减 `[经验]`。

## 面试官视角
- 考察意图：能否不止背"概念"，还能枚举真实代码里会踩的具体泄露形态。
- 分档：P5 知泄露=不退出；P6 能举 defer/nil channel/空 select 三类具体坑；P7 能对比 1019 的 channel 三类并说清本卡三类的不同触发点。
- 红旗：以为只有 channel 才会泄露；或以为 `select{}` 能当正常等待用。
- 惊艳点：点出"defer 误用是**资源**泄露（文件句柄）而非仅内存——句柄耗尽比 OOM 更隐蔽"；以及"nil channel 读写阻塞是编译通过、运行卡死最阴险的一类"。

## 主问答
**Q（面试官原话）：** 除了 channel 收发，还有哪些具体写法会泄露协程？
**A：**
1. **defer 误用（资源泄露）**：循环打开十万文件、用 `defer f.Close()` 在函数末尾统一关——函数不返回就一个都不关，十万句柄堆积。**修法**：把"打开+处理+关闭"封进独立函数，让 defer 对每个文件立即生效 `[经验]`。
2. **nil channel 读写**：只 `var ch chan int`（未 make）就往里写/读，运行期永久阻塞——十万协程全卡在这。任何只声明未初始化的 channel 都是 nil channel。
3. **空 `select{}`**：`select` 不带任何 case，当前协程永久阻塞（常误当"等 forever"用）。
4. **边界**：以上与 `1019` 的"for-select 不判 ok 空转 / 发送超缓冲阻塞 / ticker 不 Stop"是**互补两组**——本卡偏"资源+nil+死等"，1019 偏"channel 使用三形态"。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 还有啥坑？ | 广角 | defer/nil/空select | P5 |
| L2 | defer 咋漏？ | 机制 | 函数末才关句柄 | P6 |
| L3 | nil channel？ | 反直觉 | 未 make 读写阻塞 | P6+ |
| L4 | 空 select 用？ | 误区 | 永久阻塞别当等待 | P7 |
| L5 | 怎么发现？ | 实战 | NumGoroutine/pprof | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Go 1.0+ | nil channel 语义、空 select 阻塞长期稳定 | 答"defer 误用(nil channel/空 select) 三类具体坑 + NumGoroutine 观测；与 1019 的 channel 三类互补" |

## 关键代码
```go
// nil channel：只声明未 make → 读写都永久阻塞
var ch chan int // nil
go func() { ch <- 1 }() // 永久阻塞（不是 panic，是卡死）

// 空 select：永久阻塞
go func() { select {} }() // 协程永远停在这

// defer 误用修复：封装成函数，让 defer 每文件立即生效
func handleOne(path string) error {
    f, err := os.Open(path)
    if err != nil { return err }
    defer f.Close() // 函数返回即关，不堆积
    return process(f)
}
```

## 总结与追问预判
本卡三类坑都是"协程创建后卡死"的具体形态，与 `1019` 的 channel 三形态互补。预防体系（context/超时/协程池）见 1022。

## ⚠️ 原文纠错
1. 事实核校：defer 在函数退出才执行致句柄堆积、nil channel 读写永久阻塞、空 select 永久阻塞、均导致协程不退出——正确 `[经验]`。
2. 崩坏词归一：源码将 goroutine 音译为过入/购入器、defer 音译为底份/抵份、channel 音译为签到/牵到、select 音译为死莱克/select、nil 音译为 neo/neochannel、leak 音译为集成泄漏；源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
