# 1264 RocksDB 与 LSM 树：追加写、不可变 SST 与读放大

> 分类：数据库 / 存储引擎 | 难度：L4 | 题型：原理题 | 频率：中 | 关键词：**LSM 树、memtable、skiplist、SSTable、顺序写、tombstone、读放大、空间放大**

> 原文锚点：第 33~46、55~67 段「RocksDB 是基于 LSM 树将离散的随机写请求转换成批量的顺序写请求…LSM 树的主要思想是先将写入操作缓存到内存中的 memtable…当 memtable 达到一定的大小的时候，就会将数据刷新到磁盘中的 SSTable…写完之后这个数据文件是不可以更改的…查找数据的时候，首先从 memtable 开始搜索，然后在 LSM 树上每一层都使用二分查找法来搜索目标…它不能进行原地更新，因此会带来两个问题：大量的冗余和无效的数据占用了磁盘空间；读取数据的时候如果内存没有命中，需要从 L0 层开始进行查找 SST 文件，导致读效率下降」

## 一句话总述
RocksDB 基于 **LSM 树**：写先落到内存 **memtable**（默认实现是**跳表 skiplist**），写满后**顺序刷成磁盘上的 SSTable**，且**SSTable 一经写成就不可更改**；所有修改都以**追加**方式表达（insert 写新 KV、update 写修改后的 KV、delete 写一条 **tombstone**）。它把**随机写转成顺序写**换来高写入性能，代价是**不能原地更新**——带来**空间放大**（冗余数据占盘）与**读放大**（内存未命中需逐层查 SST）。

## 面试官视角
- 考察意图：能否讲清 LSM 树"**用顺序写换随机写**"的核心交易，以及它付出的两个代价。
- 分档：P5 知道 LSM 写入快；P6 能说 memtable → SSTable 的刷盘路径；P7 能补上 **SSTable 不可变**、**delete 是写 tombstone**、**读放大与空间放大**这两个代价，以及 **memtable 用跳表**这一实现细节。
- 红旗答案：把 SSTable 说成"可以就地修改的文件"；以为 delete 会立刻物理删除数据。
- 惊艳点：**`delete` 在 LSM 里是一次写操作**——写一条 tombstone 标记删除，**真正的物理删除要等到 compaction**（见 1264）`[源码]`。

## 主问答
**Q（面试官原话）：** LSM 树为什么写快？代价是什么？

1. **结论**：LSM 树把**离散的随机写请求转换成批量的顺序写请求**，从而提升写入性能；代价是**不能原地更新（in-place update）**，带来**空间放大**与**读放大** `[源码]`。
2. **写入路径**：**先将写入操作缓存到内存中的 memtable**（类似内存中的有序表）；**当 memtable 达到一定大小时，把数据刷新到磁盘中的 SSTable**（Sorted String Table） `[源码]`。
3. **顺序写且不可改**：**从内存刷新到磁盘的过程是顺序写**，**写完之后这个数据文件是不可以更改的**；**当有数据修改时会触发压缩（compaction）过程** `[源码]`。
4. **memtable 的实现与内部 key**：memtable 的默认实现是 **skiplist（跳表）**；RocksDB 会把用户传入的 key 改造成 memtable 的**内部 key**——**用户 key + 序列号 + 类型**，再加上用户传入的 value，作为一个 element 加入 skiplist `[源码]`。
5. **三种修改都是追加**：**insert 直接写入新的 KV**；**update 写入修改后的 KV**；**delete 写入一条 tombstone 来标记删除**——通过这种方式把**磁盘的随机写入转换为顺序写入** `[源码]`。
6. **查找路径**：**先从 memtable 开始搜索**，**memtable 里没有就用二分查找法查找 SSTable**，在 LSM 树**每一层都使用二分查找**直到找出指定的 KV；**查询操作会同时在 memtable 和 SSTable 中进行** `[源码]`。
7. **两个代价**：**① 空间放大**——大量**冗余和无效数据占用磁盘空间**；**② 读放大**——**内存未命中时，需要从 L0 层开始逐层查找 SST 文件，导致读效率下降** `[源码]`。
8. **层间差异**：**L1 及以上层级**的每个 SSTable **没有交叠**，可以**用二分法快速定位 key 所在的层级与 SST 文件** `[源码]`。

**加分层：** RocksDB 还用**高压缩比算法**（如 **LZ4 / Snappy / Zlib**）降低空间占用，并支持**完整的事务特性**；Tendis **默认单进程使用 10 个 RocksDB 实例** `[源码]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | LSM 写快的原因？ | 答不出随机写转顺序写 |
| L2 | 写先到哪？ | 答不出 memtable |
| L3 | SSTable 能改吗？ | 答出不可变 |
| L4 | delete 怎么实现？ | 答不出写 tombstone |
| L5 | 代价有哪两个？ | 答不出空间放大 + 读放大 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| RocksDB 通用 | LSM 结构稳定 | memtable + 多层 SST + compaction |
| 默认 | memtable = skiplist | 可换其他 memtable 实现 |
| 默认单进程 | Tendis 用 10 个 RocksDB 实例 | 按实例分摊写压力 |
| 压缩算法 | LZ4 / Snappy / Zlib | 按空间与 CPU 权衡选择 |

## 关键代码
```go
// 用 Go 直连 RocksDB（grocksdb 绑定）观察 LSM 的"追加写"语义
package main

import (
	"fmt"

	"github.com/linxGnu/grocksdb"
)

func main() {
	opts := grocksdb.NewDefaultOptions()
	opts.SetCreateIfMissing(true)
	db := grocksdb.OpenDB(opts, "/tmp/rocksdb-demo")
	defer db.Close()

	wo := grocksdb.NewDefaultWriteOptions()
	ro := grocksdb.NewDefaultReadOptions()

	// 1) insert：写一条新 KV（先落 memtable）
	db.Put(wo, []byte("k1"), []byte("v1"))

	// 2) update：不是原地改，而是再写一条"修改后的 KV"（新序列号）
	db.Put(wo, []byte("k1"), []byte("v2"))

	// 3) delete：不是立即物理删，而是写一条 tombstone
	db.Delete(wo, []byte("k1"))

	// 4) 读路径：memtable -> L0 -> L1 ... 逐层查找，未命中返回 NotFound
	_, err := db.Get(ro, []byte("k1"))
	fmt.Println("get k1 err:", err)

	// 5) memtable 达阈值后 flush 成不可变的 SSTable 文件
	db.Flush(grocksdb.NewDefaultFlushOptions())
	fmt.Println("flushed: memtable -> SSTable (immutable)")
}
```

## 总结与追问预判
**最爱追问的是"SSTable 能不能改"**——**不能**，这是 LSM 与 B+树的根本分歧：B+树**原地更新**页面，LSM **只追加**。由此推出两个必答题：**delete 是写 tombstone**、**update 是写新版本**（靠内部 key 的序列号判定新旧）。追问常接"那读不是变慢了吗"——是的，这就是**读放大**，靠 **bloom filter**、**block cache** 与 **compaction** 三者共同缓解（compaction 详见 1264）。

## ⚠️ 原文纠错
1. 事实核校：LSM 将随机写转顺序写、memtable 达阈值刷成 SSTable、刷新为顺序写且文件不可更改、memtable 默认实现为 skiplist、内部 key = 用户 key + 序列号 + 类型、三种修改均为追加、查找先 memtable 再逐层二分、不能原地更新导致空间放大与读放大、L1 及以上 SST 不交叠——均与 RocksDB/LSM 实现一致 `[经验]`。
2. 补充：**原文称 SSTable 表示"有序的可变的数据文件"，应为"有序的、不可变的"**——原文后一句也说"写完之后这个数据文件是不可以更改的"，可变属口误；另**L0 层的 SST 文件之间 key 范围可能重叠**，只有 **L1 及以上层**才保证同层不交叠 `[经验]`。
3. 崩坏词归一：源码将 RocksDB、LSM 树、memtable、SSTable、skiplist、tombstone 等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
