# 913 WaitGroup 实现原理：计数、移位与 CAS

> 分类：Go 并发/sync | 难度：L3 | 题型：源码题 | 频率：中 | 关键词：**原子操作**/**CAS**/**左移32位**/**唤醒所有**/**信号量**
> 原文锚点：第 26~50、56~59 段「Add 原子增 counter；Wait 增 waiter 并阻塞；counter=0 唤醒；state 用 CAS」

## 一句话总述
WaitGroup 本质是**一个原子计数器 + 信号量**：`Add(delta)` 把 delta **左移 32 位**加到 state 高位的 counter；`Done()`=Add(-1)；`Wait()` 增加低位 waiter 并 CAS 自旋阻塞，直到 counter 归零唤醒所有等待者——全程 CAS 原子操作，比加锁高效。

## 面试官视角
- 考察意图：能否把「Add/Done/Wait」映射到 state 位域的原子操作，讲清阻塞与唤醒时机。
- 分档：P5 知维护计数器、三方法操作；P6 知 Add 左移32加 counter、Wait 右移取 waiter、CAS 操作；P7 知 counter=0 唤醒所有、CAS 优于加锁。
- 红旗答案：以为 Wait 是忙等死循环；或不知 Add 为何要左移 32 位。
- 惊艳点：点出「Add 左移 32 位是因为 counter 在高 32 位、waiter 在低 32 位，须精准落位」，以及「CAS 比较并交换比单纯加锁更高效」 [经验]。

## 主问答
**Q（面试官原话）：** WaitGroup 的 Add/Wait 内部怎么实现的？
**A：**
1. **Add：移位加 counter**：`Add(delta)` 用原子操作把 `delta` **左移 32 位**后加到 state 高位（counter 在低位是 waiter，故须移位落位）；delta 可正（增等待数）可负（减等待数）[经验]。
2. **Done = Add(-1)**：`Done()` 即调用 `Add(-1)`，把一个 goroutine 标记完成、counter 减一 [经验]。
3. **Wait：增 waiter + 阻塞 + 唤醒**：`Wait()` 增加低位 waiter 数（右移 32 位取 waiter）、用 **CAS** 自旋检查；counter≠0 时当前 goroutine 入等待队列并阻塞；一旦 `Done` 使 counter 归零，便**唤醒所有等待者**令其继续。全程 CAS 原子，比加锁更高效 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | Done 是什么？ | 语义 | Add(-1) | P5 |
| L2 | Add 为何左移？ | 位域 | counter 在高32位需移位 | P6 |
| L3 | Wait 怎么等？ | 阻塞 | 增 waiter+CAS 自旋 | P6 |
| L4 | 何时唤醒？ | 时机 | counter=0 唤醒所有 | P7 |
| L5 | 为何用 CAS？ | 性能 | 比加锁高效 | P7+ |

## 版本与兼容性
- CAS 实现属 Go runtime 标准手段；与 1019（并发陷阱）、913-waitgroup-state（字段布局）互补 [边界]。

## 总结与追问预判
WaitGroup 三卡（用法/字段/原理）合起来即「会用+懂源码」。与 errgroup、channel 关闭信号等选型对比，是并发编排题的加分项。

## ⚠️ 原文纠错
1. 事实核校： [经验] Add 左移32加 counter、Done=Add(-1)、Wait 增 waiter+CAS 阻塞、counter=0 唤醒所有、CAS 优于加锁——均正确。
2. 崩坏词归一：源码将若干术语音译为崩坏词，本卡统一为规范术语（WaitGroup、原子操作、比较并交换、计数器、信号量、等待队列等）。

```go
// WaitGroup 核心位域操作（示意）
func (wg *WaitGroup) Add(delta int) {
    // 把 delta 加到高32位 counter：左移 32 位
    v := wg.state.Add(uint64(delta) << 32)
    counter := int32(v >> 32) // 高32位=未完成 goroutine 数
    waiter := uint32(v)       // 低32位=等待者数
    if counter == 0 && waiter > 0 {
        // 唤醒所有等待者（sema 信号量）
        for ; waiter > 0; waiter-- {
            runtime_Semrelease(&wg.sema, false, 0)
        }
    }
}
// Wait: 右移 32 位增加 waiter，CAS 自旋直到 counter==0
```
