# 925 sync.RWMutex 读写锁的实现原理

> 分类：并发模型 | 难度：L3 | 题型：原理题 | 频率：中 | 关键词：**基于 Mutex** / **readerCount** / **readerWait** / **双信号量**
> 原文锚点：第 140~167 段「读写锁基于互斥锁实现…readerCount 原子操作…readerWait 唤醒写锁」

## 一句话总述
RWMutex 复用一把 Mutex 做写者互斥，用 readerCount 记录活跃读者数、readerWait 记录写者前的离去读者数，配 readerSem/writerSem 两个信号量实现"读并发、写独占、写等读尽"。

## 面试官视角
- 考察意图：能否讲清读/写加解锁的原子操作与信号量配合
- P5 知"基于 Mutex" / P6 能讲 readerCount<0 表示有写者等待 / P7 能讲写者如何等读尽(readerWait)
- 红旗：说"RWMutex 完全独立实现"；说"写锁也用原子加即可"
- 惊艳点：RWMutex.Lock 先把 readerCount 减 rwmutexMaxReaders（约 1<<30）变负以挡新读，再按原读者数累加到 readerWait 等待读尽 `[源码]`

## 主问答
**Q：** 读写锁底层怎么区分读和写？
**A：**
1. **读加锁**：readerCount 原子 +1，≥0 即返回（仅一次原子加）；<0 说明有写者等待，睡 readerSem `[源码]`。
2. **读解锁**：readerCount -1；若仍 <0 表示有写者，readerWait -1，归零则唤醒 writerSem 上的写者 `[源码]`。
3. **写加锁**：先 `w.Lock()` 拿内部互斥锁，再把 readerCount 减上限变负挡新读，按活跃读者数累加到 readerWait，非零则睡 writerSem 等读尽 `[源码]`。
**加分层：** RWMutex 本质是在 Mutex 之上用 readerCount 做"读写通信"，写锁开销比纯 Mutex 多几次原子操作。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 基于啥 | 概念 | Mutex | 换题 |
| L2 | 读锁成本 | 机制 | 1 原子加 | 判 P5 |
| L3 | readerCount<0 | 边界 | 有写者等 | 判 P6 |
| L4 | 写等读尽 | 权衡 | readerWait | 判 P6+ |
| L5 | 写饥饿 | 实战 | 长读挡写 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| go1.0+ 结构稳定 | rwmutexMaxReaders=1<<30 自早期稳定 | 照"基于 Mutex + readerCount + 双 sema"答 |

## 关键代码
```go
// 示意，未验证：RWMutex 关键字段与 RLock 快路径（简化自 src/sync/rwmutex.go）
type RWMutex struct {
    w           Mutex
    writerSem   uint32
    readerSem   uint32
    readerCount int32
    readerWait  int32
}
const rwmutexMaxReaders = 1 << 30
func (rw *RWMutex) RLock() {
    if atomic.AddInt32(&rw.readerCount, 1) < 0 {
        runtime_SemacquireMutex(&rw.readerSem, false, 0) // 有写者等待，睡
    }
}
```

## ⚠️ 原文纠错
未发现技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 护事锁→互斥锁、勾浪→Go、构入t→goroutine、安log→unlock 等拼写还原），技术结论未做更正。

## 总结与追问预判
- RWMutex = Mutex + readerCount(readerWait) + readerSem/writerSem。
- 对比见 925.md（底层 Mutex 的 state/sema 与自旋/饥饿）。
