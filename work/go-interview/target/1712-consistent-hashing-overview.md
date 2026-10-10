# 1712 一致性哈希总览（2^32 哈希环）

> 分类：分布式/一致性哈希 | 难度：L3 | 题型：总览 | 频率：中 | 关键词：**一致性哈希**/**2^32取模**/**哈希环**/**扩容迁移**/**相邻区间**

> 原文锚点：第 1~21 段「那本节呢我们来看看一次性哈希算法…应该存储我们这个 k 一数据的节点」（海量数据分布式存储 → 取模分片 → 扩容全量迁移灾难 → 一致性哈希 2^32 取模哈希环 → 节点与数据两步映射 → 顺时针寻址）

## 一句话总述
一致性哈希是一种**把节点和数据都映射到一个固定大小（2^32）哈希环上的分布式寻址算法**，节点增删时只迁移环上相邻区间的数据（平均约 1/N），从而避免了普通取模哈希在扩容时导致全量数据搬迁、缓存雪崩的灾难。

## 面试官视角
面试官想确认你**真的踩过扩容的坑**，而不是背定义。核心考点：① 普通 `hash(key) % N` 为什么一扩容就崩；② 一致性哈希靠什么把「迁移量」从 O(N) 降到 O(1/N)；③ 数据倾斜怎么解（虚拟节点）；④ 能不能讲清工程实现差异（经典 Karger 环 vs Redis Cluster 槽位）。

## 主问答
**Q（面试官原话）：** 一致性哈希算法解决了什么问题？为什么不直接用哈希取模把数据分到机器上？

**A：**
1. **普通取模哈希的扩容灾难**：`node = hash(key) % N`，当节点数 N 从 3 变 4 时，几乎所有 key 的取模结果都变了，存量数据必须全量重新计算并搬迁。海量数据下这等于缓存瞬间全部失效 → 请求穿透到数据库 → **缓存雪崩**，DB 直接被打挂。
2. **一致性哈希用「固定哈希空间」解耦节点数**：它对 `2^32`（0 ~ 2^32-1）取模，构成一个**首尾相连的逻辑环（哈希环）**；节点和数据都映射到这个环上，哈希空间大小与机器数量无关，扩容不再改变 key 的映射基准。
3. **顺时针寻址只动相邻区间**：数据 key 哈希后在环上**顺时针找第一个节点**存放；新增/删除一个节点，只影响该节点在环上顺时针相邻的**后驱区间**（平均仅 1/N 的数据需迁移），其余数据原地不动。
4. **收益与代价权衡**：它牺牲了「节点在环上绝对均匀分布」这一性质，换来了**水平扩容时迁移量可控、系统可平滑伸缩**的能力——这正是分布式缓存/存储愿意接受的取舍。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 普通取模哈希扩容为什么不行？ | 是否理解取模与 N 强耦合 | 讲 N 变化 → 全量重映射 → 雪崩 | 只说「会迁移」算 L1 未过 |
| L2 | 哈希环大小为什么是 2^32？ | 对哈希空间基准的理解 | 环是固定逻辑空间，与节点数解耦 | 说成「和机器数有关」算 L2 未过 |
| L3 | 增删节点到底迁移多少数据？ | 对相邻区间迁移的量化 | 平均 1/N，只影响后驱区间 | 答「一半」算 L3 未过 |
| L4 | 节点少时数据倾斜怎么办？ | 虚拟节点概念 | 引入虚拟节点打散分布 | 没听过虚拟节点算 L4 未过 |
| L5 | Redis Cluster 用一致性哈希吗？ | 工程实现辨析 | 它用 16384 哈希槽，思想同源但非经典虚拟节点 | 把 slot 当虚拟节点算 L5 未过 |

## 版本与兼容性
- 算法层面**跨语言、跨版本无差异**，是纯数学映射，Go/Java/C++ 实现一致。
- **工程实现辨析（重要）**：经典一致性哈希（Karger et al. 1997，用于 Memcached/Ketama、Cassandra、Dynamo）用「虚拟节点」打散环；而 **Redis Cluster 用的是 16384 个哈希槽（slot）**做数据分片，思想同源（都是为减少迁移），但**不是经典虚拟节点实现**——面试中两者不可混为一谈。
- Go 标准库无内置一致性哈希，常用 `github.com/cespare/consistent` 或自实现（见下）。

## 关键代码

```go
// 一致性哈希环最小可用实现（含虚拟节点）
type HashFunc func(data []byte) uint32

type ConsistentHash struct {
	hash     HashFunc
	replicas int
	ring     map[uint32]string // 虚拟节点 hash -> 真实节点
	sorted   []uint32          // 有序虚拟节点 hash，用于二分查找
	nodes    map[string]struct{}
}

func New(replicas int, h HashFunc) *ConsistentHash {
	if h == nil {
		h = crc32.ChecksumIEEE
	}
	return &ConsistentHash{hash: h, replicas: replicas, ring: map[uint32]string{}, nodes: map[string]struct{}{}}
}

func (c *ConsistentHash) Add(node string) {
	for i := 0; i < c.replicas; i++ {
		vh := c.hash([]byte(fmt.Sprintf("%s#%d", node, i)))
		c.ring[vh] = node
		c.sorted = append(c.sorted, vh)
	}
	sort.Slice(c.sorted, func(i, j int) bool { return c.sorted[i] < c.sorted[j] })
	c.nodes[node] = struct{}{}
}

// Get 顺时针找第一个 >= h 的虚拟节点（环回处理）
func (c *ConsistentHash) Get(key string) string {
	if len(c.sorted) == 0 {
		return ""
	}
	h := c.hash([]byte(key))
	idx := sort.Search(len(c.sorted), func(i int) bool { return c.sorted[i] >= h })
	if idx == len(c.sorted) {
		idx = 0 // 越过环尾，回到环首
	}
	return c.ring[c.sorted[idx]]
}
```

## 总结与追问预判
一句话收口：**一致性哈希 = 固定哈希环 + 顺时针寻址，把扩容迁移量从「全量」降到「相邻 1/N 区间」**。预判追问会往两个方向走：① 数据倾斜的解法（虚拟节点，见 1712.md`）；② 环的具体实现与查找复杂度（见 1712.md` 与深卡）。回答时务必把「经典环」和「Redis 槽位」区分开，这是高阶分水岭。

## ⚠️ 原文纠错
源视频为机器转写，将 consistent hashing / hash ring / virtual node / 顺时针 / 取模 等术语音译为若干崩坏词（如「一次性哈希」「希环」「后聚节点」「lode/node」混写），本卡已统一还原为规范术语（一致性哈希 / 哈希环 / 后驱节点 / 节点 node）。**禁止在交付卡中保留任何原词崩坏写法**。

> **[经验]** 展示时务必区分「经典一致性哈希（Karger 1997）」与「Redis Cluster 哈希槽（16384 slot）」两种工程实现：前者用虚拟节点打散环，后者用预分配槽位做分片迁移，思想同源但机制不同。把 slot 说成虚拟节点是典型扣分点。
