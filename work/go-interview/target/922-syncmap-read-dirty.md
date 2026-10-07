# 922 sync.Map 的读写分离：read map、dirty map 与 misses 计数

> 分类：Go 并发 | 难度：L4 | 题型：原理题 | 频率：高 | 关键词：**read map、dirty map、读写分离、misses、穿透、原子操作、加锁**

> 原文锚点：第 38~49、57~61 段「sync.Map 的底层数据结构本质上还是使用了 map，只不过在 map 的基础上做了优化…map 并发安全的实现有两个思路，是原子操作和加锁。原子操作是直接面向硬件的一组不可分割的指令，所以它的效率要比加锁高很多。因此 sync.Map 的基本思路就是尽可能多地使用原子操作，直到迫不得已才会使用锁机制…它使用了两个原生的 map 作为存储介质，分别是 read map 和 dirty map…读取的时候会先查 read 字段，如果不存在这个 key 就会查询 dirty 字段。写入的时候只写 dirty 字段，读取 dirty 字段的时候需要加锁」

## 一句话总述
`sync.Map` 底层仍是 map，但用**两个原生 map** 做**读写分离**：**read（只读字典）** 与 **dirty（脏字典）**。**读先查 read**，**read 没有才查 dirty**，且**读 dirty 需要加锁**；**写只写 dirty**。它遵循"**尽可能多用原子操作、迫不得已才加锁**"的设计——**read 的读取完全无锁**，**只在 dirty 上加锁**，从而大幅提升读性能。另有 **misses** 字段统计 **read 被穿透**的次数，**超过 dirty 长度时把 dirty 提升为 read**。

## 面试官视角
- 考察意图：能否讲清"为什么 `sync.Map` 读快"，而不是只背"它用了读写分离"。
- 分档：P5 知道有两个 map；P6 能说"读先 read 后 dirty"；P7 能补上 **read 读无锁（原子操作）**、**dirty 读写加锁**、**misses 触发提升**这三条机制细节。
- 红旗答案：以为读也要加锁；或以为写会同时写 read 和 dirty。
- 惊艳点：**read 是"只读快照"，读它不需要任何锁**——这是 `sync.Map` 读性能的根本来源；代价是**写入只落在 dirty，读新写入的 key 必须穿透到 dirty（加锁）** `[源码]`。

## 主问答
**Q（面试官原话）：** `sync.Map` 内部是怎么做到读不用加锁的？

1. **结论**：它**底层本质还是 map**，在此之上用 **read 与 dirty 两个原生 map** 做**读写分离**——**read 只读且可无锁访问，dirty 承载写入并加锁保护** `[源码]`。
2. **设计原则 · 原子优先**：并发安全只有两条路——**原子操作**与**加锁**；**原子操作是直接面向硬件的一组不可分割的指令，效率比加锁高很多**；所以 `sync.Map` 的基本思路是**尽可能多地使用原子操作，直到迫不得已才使用锁机制** `[源码]`。
3. **两个存储介质**：**read map（只读字典）** 与 **dirty map（脏字典）** `[源码]`。
4. **读路径**：**读取时先查 read 字段**，**如果 read 里不存在这个 key，就去查 dirty 字段**；**访问 read 里的键值不需要加锁**，**读 dirty 时需要加锁** `[源码]`。
5. **写路径**：**写入时只写 dirty 字段**；**dirty 里面包含了 map 中需要加锁读写的部分**，**通过加锁确保并发安全** `[源码]`。
6. **收益来源**：**由于只需要在 dirty 上加锁，这种读写分离的设计提高了 `sync.Map` 的读效率** `[源码]`。
7. **misses 与提升**：**misses 字段统计 read 被穿透的次数**——**所谓被穿透，就是读 read 时找不到 key 而转到 dirty 的情况**，**每发生一次就加一**；**当 miss 达到一定次数（misses 超过 dirty 的长度）时，就会把 dirty 里的键值赋给 read**（随后 dirty 置空、misses 归零）`[源码]`。

**加分层：** 这条提升机制解释了 `sync.Map` 的适用边界——**写多读少**时，新 key 不断落入 dirty，读又不断穿透加锁，misses 频繁触发提升，**性能反而差于普通 map + 锁**。所以它**只适合读多写少**（尤其是"写一次读很多次"）。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 底层是什么？ | 答不出还是 map |
| L2 | 有几个 map？ | 答不出 read + dirty |
| L3 | 读先查谁？ | 答不出先 read |
| L4 | 读 read 要加锁吗？ | 答出要加锁即错 |
| L5 | misses 到多少触发提升？ | 答不出超过 dirty 长度 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.9+ | 新增 `sync.Map` | read/dirty 双 map 结构 |
| Go 1.9 ~ 至今 | 结构未变 | 读写分离 + misses 提升 |
| 所有版本 | 仅适合读多写少 | 写密集改用分片 map 或互斥锁 |
| Go 1.19+ | 有泛型 | 可自建类型安全的并发 map |

## 关键代码
```go
package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

// 用最小模型还原 sync.Map 的 read/dirty + misses 思路
type MiniSyncMap struct {
	mu     sync.Mutex
	read   atomic.Value // 只读快照，读它不加锁
	dirty  map[string]any
	misses int64
}

func (m *MiniSyncMap) Load(k string) (any, bool) {
	// 1) 先无锁读 read
	if v, ok := m.read.Load().(map[string]any)[k]; ok {
		return v, true
	}
	// 2) 穿透到 dirty：需要加锁，并累计 misses
	m.mu.Lock()
	defer m.mu.Unlock()
	v, ok := m.dirty[k]
	if atomic.AddInt64(&m.misses, 1) > int64(len(m.dirty)) {
		m.promoteLocked() // misses 超过 dirty 长度 -> dirty 提升为 read
	}
	return v, ok
}

func (m *MiniSyncMap) promoteLocked() {
	m.read.Store(m.dirty) // 提升
	m.dirty = nil
	atomic.StoreInt64(&m.misses, 0)
	fmt.Println("promote: dirty -> read")
}

func main() {
	var m MiniSyncMap
	m.read.Store(map[string]any{})
	m.dirty = map[string]any{"a": 1}
	fmt.Println(m.Load("a"))
}
```

## 总结与追问预判
**必追问的是"写多读少会怎样"**——**会退化**：新 key 只进 dirty，读新 key 必然穿透并加锁，misses 快速累积触发提升，而提升是把整个 dirty 拷成新 read，**写越频繁提升越频繁**，开销逼近甚至超过普通 map + 锁。追问常接"read 和 dirty 的数据会不会不一致"——会，**read 是快照**，这正是它只能保证**最终一致**、不保证线性一致读的原因；删除也因此采用**标记延迟删除**（见 `922-syncmap-entry-states`）。

## ⚠️ 原文纠错
1. 事实核校：底层仍为 map、并发安全靠原子操作与加锁两条路、原子操作效率高于加锁、基本思路是原子优先、read 与 dirty 两个原生 map、读先 read 后 dirty、写只写 dirty、读 dirty 需加锁、只在 dirty 加锁提升读效率、misses 统计穿透次数且超过 dirty 长度时提升——均与 Go 标准库实现一致 `[经验]`。
2. 补充：原文称"对 dirty 进行写入时使用自旋锁、使用 CAS 操作"，**实际 `sync.Map` 对 dirty 的保护是互斥锁 `mu sync.Mutex`**，CAS 用于 **entry 指针状态的原子变更**；把两者混为一谈会在面试中被追问穿 `[经验]`。
3. 崩坏词归一：源码将 read map、dirty map、原子操作、加锁、穿透、misses 等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
