# 109 用读写锁实现并发安全的 Slice

> 分类：Go/并发 | 难度：L3 | 题型：方案题 | 频率：高 | 关键词：**SafeSlice**/**RWMutex**/**读写锁封装**/**写锁append**/**读锁取值**
> 原文锚点：第 20~30 段「定义 SafeSlice(data+读写锁)、append 加写锁、取元素/长度加读锁、下标有效性校验、读多优于 channel」

## 一句话总述
并发安全 slice 的第一种实现是**读写锁封装**：定义 `SafeSlice` 结构体（内含 `data` 切片 + `sync.RWMutex`），append/修改加**写锁**保证同时只一个协程改，取值/取长度加**读锁**（多读不互斥），并对传入下标做有效性校验。读多写少场景下比 channel 串行化更高效。

## 面试官视角
- 考察意图：能否用 RWMutex 把 slice 包成并发安全结构，并说清读写锁分工。
- 分档：P5 知加锁可保护；P6 能写 SafeSlice（写锁改/读锁取）；P7 知读锁不互斥、下标校验、读多优于 channel。
- 红旗答案：读也加写锁（失去并发读）；不校验下标导致越界 panic。
- 惊艳点：点出「读锁允许多读并发、只在写时互斥」，以及「读频繁场景 RWMutex 优于 channel 串行化」 [经验]。

## 主问答
**Q（面试官原话）：** 怎么让 slice 并发安全？
**A：**
1. **结构封装**：`SafeSlice` 含 `data []T` 字段 + `sync.RWMutex` 字段，把锁与数据绑一起 [经验]。
2. **写锁改、读锁取**：append/修改元素加**写锁**（同一时刻仅一个协程改）；获取元素、取长度加**读锁**（多读不阻塞） [经验]。
3. **下标校验 + 读多更优**：取元素前校验下标有效防越界；读锁不互斥，读频繁场景比 channel 串行化效率高 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 咋封装？ | 结构 | data+锁 | P5 |
| L2 | 锁咋分？ | 分工 | 写锁改/读锁取 | P6 |
| L3 | 下标？ | 安全 | 校验防越界 | P6 |
| L4 | 读多？ | 选型 | RWMutex 优于 channel | P7 |
| L5 | 写多？ | 优化 | 分片打散锁粒度 | P7+ |

## 版本与兼容性
- 本卡只讲 RWMutex 封装；slice 非并发本质见 109、channel 串行化见 109 [边界]。
- RWMutex API 细节见 925、分片（sharded）思路见并发分片惯用法——本卡只引不重述 [边界]。

## 总结与追问预判
RWMutex 封装是最常用的并发安全 slice 方案。写多且索引随机时可进一步「分片 slice」打散锁粒度，但 append 因索引连续常集中某分片、收益有限。

## ⚠️ 原文纠错
1. 事实核校： [经验] 读写锁分工、读锁不互斥、下标校验、读多优于 channel——均正确。
2. 崩坏词归一：源码将若干术语音译为崩坏词，本卡统一为规范术语（读写锁、并发安全、切片、下标、协程等）。

```go
// SafeSlice：RWMutex 封装并发安全切片
type SafeSlice struct {
    mu  sync.RWMutex
    data []int
}
func (s *SafeSlice) Append(v int) {
    s.mu.Lock()
    defer s.mu.Unlock()
    s.data = append(s.data, v) // 写锁：同时仅一个协程改
}
func (s *SafeSlice) Get(i int) (int, bool) {
    s.mu.RLock()
    defer s.mu.RUnlock()
    if i < 0 || i >= len(s.data) { // 下标有效性校验
        return 0, false
    }
    return s.data[i], true // 读锁：多读不互斥
}
func (s *SafeSlice) Len() int {
    s.mu.RLock()
    defer s.mu.RUnlock()
    return len(s.data)
}
```
