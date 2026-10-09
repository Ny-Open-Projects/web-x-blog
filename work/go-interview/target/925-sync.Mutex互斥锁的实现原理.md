# 925 sync.Mutex 互斥锁的实现原理

> 分类：并发模型 | 难度：L3 | 题型：原理题 | 频率：中 | 关键词：**state 位布局** / **CAS 快路径** / **自旋** / **饥饿模式 handoff**
> 原文锚点：第 99~139 段「互斥锁结构含 state 与 sema…CAS 快速上锁…饥饿模式信号量 FIFO 唤醒」

## 一句话总述
Mutex 用 state(int32) 记录锁/唤醒/饥饿位与等待数、sema 做信号量；加锁先 CAS 快路径，失败进 lockSlow 自旋抢占，极度竞争或长等时切饥饿模式用 sema 按 FIFO 唤醒并 handoff 让渡执行权。

## 面试官视角
- 考察意图：能否讲清"快路径+自旋+饥饿模式"三层与公平性权衡
- P5 知 state+sema / P6 能讲自旋四种终止 + 饥饿模式含义 / P7 能讲 handoff 与正常模式吞吐权衡
- 红旗：说"Go 锁纯自旋"；把饥饿模式说成默认
- 惊艳点：饥饿模式下解锁者通过 runtime_Semrelease 第 2 参 handoff=true，把锁直接交给队首等待者并放入 P.runnext 优先跑 `[源码]`

## 主问答
**Q：** Mutex 底层怎么实现的？
**A：**
1. **位布局**：state 低 3 位分别表 locked/woken/starving，高位存 waiter 数（state>>3）`[源码]`。
2. **两层加锁**：先 CAS(state 0→locked) 快路径；失败进 lockSlow 在 for 循环里自旋抢（procyield 约 30 次 PAUSE）`[源码]`。
3. **饥饿模式**：等待超阈值（约 1ms）转饥饿模式，解锁经 sema 按 FIFO 唤醒且 handoff=true 让渡执行权，避免尾延迟 `[源码]`。
**加分层：** 正常模式偏向吞吐（新来的可能抢到），饥饿模式偏向公平（队首优先），二者按等待时长切换。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 两个字段 | 概念 | state+sema | 换题 |
| L2 | 快路径 | 机制 | CAS | 判 P5 |
| L3 | 自旋何时停 | 边界 | 4 终止条件 | 判 P6 |
| L4 | 饥饿模式 | 权衡 | 公平vs吞吐 | 判 P6+ |
| L5 | handoff | 实战 | runnext 优先 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| go1.9+ 饥饿模式 | go1.9 前无饥饿模式，可能写者饿死 | 照"快路径+CAS+自旋+饥饿模式 handoff"答；说明 go1.9 引入公平化 |

## 关键代码
```go
// 示意，未验证：Mutex 结构与加锁快路径（简化自 src/sync/mutex.go）
type Mutex struct { state int32; sema uint32 }
const (
    mutexLocked      = 1 << 0
    mutexWoken       = 1 << 1
    mutexStarving    = 1 << 2
    mutexWaiterShift = 3
)
func (m *Mutex) Lock() {
    if atomic.CompareAndSetInt32(&m.state, 0, mutexLocked) { return } // 快路径
    m.lockSlow() // 自旋 + sema
}
```

## ⚠️ 原文纠错
未发现技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 护事锁→互斥锁、勾浪→Go、构入t→goroutine、安诺克斯→unlockSlow、失duback→procyield 等拼写还原），技术结论未做更正。

## 总结与追问预判
- Mutex = 快路径 CAS + 自旋抢锁 + 饥饿模式 sema FIFO handoff。
- 深入见 925.md（自旋四条件、饥饿阈值与 handoff 细节）。
