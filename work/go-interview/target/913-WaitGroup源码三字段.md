# 913 WaitGroup 源码三字段：noCopy / state / sema

> 分类：Go 并发/sync | 难度：L3 | 题型：源码题 | 频率：中 | 关键词：**noCopy**/**state uint64**/**高32 counter**/**低32 waiter**/**sema 信号量**
> 原文锚点：第 34~43、51~55 段「WaitGroup 三字段：noCopy/state/sema；state 高32 counter 低32 waiter」

## 一句话总述
WaitGroup 源码三字段：**noCopy** 空结构体（防复制检测）、**state**（`atomic.Uint64`，高 32 位=counter 未完成 goroutine 数、低 32 位=waiter 等待者数）、**sema**（`uint32`，实现信号量用于阻塞/唤醒）。

## 面试官视角
- 考察意图：是否读过 WaitGroup 源码、理解「一个 uint64 塞下两个计数」的位域设计。
- 分档：P5 知有 counter/waiter 两个概念；P6 知 state 高32=counter、低32=waiter、sema 信号量；P7 知 noCopy 防复制、能解释位域拆分动机。
- 红旗答案：以为 counter 和 waiter 是两个独立字段；不知高/低 32 位拆分。
- 惊艳点：点出「单 uint64 原子变量同时装 counter+waiter，配合 CAS 比两把锁更高效」，以及「noCopy 是编译期+运行时双重防复制」 [经验]。

## 主问答
**Q（面试官原话）：** WaitGroup 内部怎么存的？
**A：**
1. **noCopy 防复制**：`noCopy` 是空结构体字段，标记 WaitGroup 不应被复制；`go vet` 与运行时检测拷贝即报错（对应不传指针的 panic）[经验]。
2. **state 位域（核心）**：`state` 为 `atomic.Uint64`，**高 32 位 = counter**（尚未完成的 goroutine 数），**低 32 位 = waiter**（已调用 `Wait` 的 goroutine 数）；一个原子变量装下两个计数 [经验]。
3. **sema 信号量**：`sema` 为 `uint32`，用于 `Wait` 的阻塞与唤醒——counter 归零时唤醒所有等待者，使 `Wait` 返回 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 几个字段？ | 结构 | noCopy/state/sema | P5 |
| L2 | state 怎么分？ | 位域 | 高32 counter/低32 waiter | P6 |
| L3 | sema 干嘛？ | 同步 | 阻塞 Wait/唤醒等待者 | P6 |
| L4 | noCopy 怎么检？ | 防复制 | vet+运行时检测拷贝 | P7 |
| L5 | 为何单 uint64？ | 设计 | 原子+CAS 比双锁高效 | P7+ |

## 版本与兼容性
- 字段布局随 Go 版本微调，但「高32 counter/低32 waiter + sema」位域设计长期稳定；与 1019 并发陷阱互补 [边界]。

## 总结与追问预判
字段布局清楚后，Add/Done/Wait 如何操作这个位域（移位+CAS），下一张讲。

## ⚠️ 原文纠错
1. 事实核校： [经验] 三字段 noCopy/state/sema、state 高32=counter 低32=waiter、sema 信号量唤醒——均正确。
2. 崩坏词归一：源码将若干术语音译为崩坏词，本卡统一为规范术语（WaitGroup、原子类型、计数器、等待者、信号量、复制检测等）。

```go
// sync.WaitGroup 源码三字段（示意，非逐字）
type WaitGroup struct {
    noCopy noCopy        // 防复制：vet/运行时检测拷贝即报错
    state  atomic.Uint64 // 高32位 counter(未完成goroutine数) | 低32位 waiter(等待者数)
    sema   uint32        // 信号量，用于 Wait 阻塞与唤醒
}
```
