# 1012 自旋锁的实现（atomic CAS 忙等）

> 分类：Go / 并发 / 锁 | 难度：L3 | 题型：实现题 | 频率：中 | 关键词：**自旋锁** / **atomic.CompareAndSwap** / **忙等待** / **int32 状态** / **无锁编程**
> 原文锚点：第 6~18 段「spanlock 包：int32 状态(0解锁/1获取)，lock 调 atomic CAS 从0改1自旋循环直到成功，unlock 用 store/swap 置0；goroutine 自增加锁后预期2000」

## 一句话总述
自旋锁用**原子操作**实现：一个 `int32` 状态值（0=解锁、1=获取），`Lock` 在循环里 `atomic.CompareAndSwapInt32(0→1)` 不断尝试（忙等）直到成功；`Unlock` 用 `store`/`swap` 把状态置 0。获取锁的线程不睡眠、空转 CPU 直到拿到锁——本质是**无锁编程**思路。

## 面试官视角
- 意图：能否不依赖 sync.Mutex 手搓一把锁，并讲清"忙等"与"睡眠"的差异。
- P5 知用 atomic CAS 实现；P6 知状态 0/1、lock 自旋循环、unlock 置 0；P7 知"忙等空耗 CPU、适合极短临界区" `[边界]` 见 925（sync.Mutex 实现，走休眠而非忙等）、1013-mutex-pessimistic（Mutex 属悲观锁）。
- 红旗：以为自旋锁不加锁也安全；或以为自旋锁不会浪费 CPU。
- 惊艳点：点出"自旋锁是用户态无锁思路，靠 CAS 轮询；与 Go runtime M 自旋找 G 同源不同层" `[经验]`。

## 主问答
**Q（面试官原话）：** 自旋锁怎么实现？
**A：**
1. **状态字段**：用 `int32` 状态，0 表示未加锁、1 表示已加锁。
2. **Lock（忙等）**：在 `for` 循环里 `atomic.CompareAndSwapInt32(&state, 0, 1)`，只有从 0 改成 1 才算抢到锁；改不成说明别人持有，继续循环重试（自旋）。
3. **Unlock**：直接 `atomic.StoreInt32(&state, 0)`（或 `Swap`），把状态置回 0 释放锁。
4. **验证**：多 goroutine 对共享计数自增、各自加锁/解锁、WaitGroup 同步，两轮各 1000 次得 2000，证明锁有效。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 用什么实现 | 基础 | atomic CAS | 换题 |
| L2 | 状态含义 | 机制 | 0解锁/1获取 | 判 P5 |
| L3 | Lock 怎么等 | 机制 | for 循环 CAS 自旋 | 判 P6 |
| L4 | 与互斥锁区别 | 对比 | 忙等 vs 睡眠 | 判 P6+ |
| L5 | 何时不该用 | 边界 | 长持有/高竞争浪费 CPU | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本 | 无 | atomic CAS 自旋是通用写法；Go 另提供 sync/atomic 包原语 |

## 关键代码
```go
// 示意：用 atomic CAS 实现自旋锁（未做端到端验证）
type SpinLock struct{ state int32 }

func (l *SpinLock) Lock() {
    for !atomic.CompareAndSwapInt32(&l.state, 0, 1) {
        // 自旋：不断重试，不睡眠
    }
}
func (l *SpinLock) Unlock() {
    atomic.StoreInt32(&l.state, 0) // 释放
}
// 用法：多 goroutine 对 cnt 自增，加锁/解锁，预期 2000
```

## 总结与追问预判
- 自旋锁 = atomic CAS 忙等（0/1 状态），不睡眠、空转 CPU 等到拿锁。
- 预判：sync.Mutex 实现 → 见 925；Mutex 悲观锁概念 → 见 1013；锁选型 → 见 1012。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词（自旋锁/互斥锁等专有名词被错读为近似音、atomic/CAS 等英文术语写错字），本卡统一为规范术语 `[经验]`。事实核校：自旋锁=atomic CAS 忙等（0解锁/1获取）、互斥锁=无竞争先 CAS 快路径否则睡眠、读写锁底层含互斥锁故写锁不等价互斥——均正确，未做更正。
