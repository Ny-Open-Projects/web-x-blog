# 1264 LSM 的 compaction：归并三步、写放大，以及"key 频繁变化"为何是禁区

> 分类：数据库 / 存储引擎 | 难度：L4 | 题型：原理题 | 频率：中 | 关键词：**compaction、归并排序、写放大、读放大、空间放大、tombstone、物理删除**

> 原文锚点：第 15~18、68~77 段「key 经常变化会导致 Tendis 频繁的触发压缩，从而影响性能…可以通过 compaction，也就是压缩操作，来将数据下层进行合并、清理已经标记为删除的数据，从而降低存储空间的占用以及对读取效率的影响，但是 compaction 又会带来写放大的问题…压缩实际上就是一个归并排序的过程，它会将第 n 层的数据选入到 n+1 层，并且过滤掉已经删除的数据，从而实现数据的物理删除…第一步是准备…第二步是进行处理…第三步是写入，会将排序的数据写入到 n+1 层的 SST 文件，然后更新元数据信息」

## 一句话总述
**compaction** 是 LSM 树的"回收与整理"：**把第 n 层的数据选入 n+1 层，过滤掉已标记删除的数据，实现物理删除**；本质是一次**归并排序**，分**准备 → 处理 → 写入**三步。它**降低空间占用、缓解读放大**，但自身是**资源密集操作**（要读大量数据排序、消耗较多 CPU），并带来**写放大**——这也是 **Tendis 不适合 "key 经常变化" 场景**的根本原因。

## 面试官视角
- 考察意图：能否把 compaction 从"后台压缩"讲成**一次有明确输入输出的归并排序**，并说清它**解决什么、又引入什么**。
- 分档：P5 知道 LSM 需要合并；P6 能说 compaction 清理已删除数据、减少空间；P7 能讲出**三步流程**、**写放大**，并把它与"**key 频繁变化会拖垮 Tendis**"这条工程结论串起来。
- 红旗答案：以为 compaction 只是"压缩一下变小"；只说好处不说**写放大与 CPU 消耗**。
- 惊艳点：**compaction 是 LSM 里唯一真正"物理删除"的地方**——tombstone 标记的记录要到这里才被真正清掉 `[源码]`。

## 主问答
**Q（面试官原话）：** compaction 到底做了什么？为什么会有写放大？

1. **结论**：compaction **将第 n 层的数据选入 n+1 层，并过滤掉已经删除的数据，从而实现数据的物理删除**；**它本质上就是一个归并排序的过程** `[源码]`。
2. **为什么需要它**：由于 LSM 不能原地更新，**冗余与无效数据会占用磁盘空间**，且**读取时内存未命中要逐层查 SST 文件、读效率下降**；因此需要 compaction **把数据下层合并、清理已标记删除的数据**，**降低存储空间占用并减少对读效率的影响** `[源码]`。
3. **三步流程**：
   - **① 准备**：**根据一定的条件和优先级，从 Ln 到 Ln+1 选定需要合并的 SST 文件**，**确定需要处理的 key 的范围** `[源码]`。
   - **② 处理**：**将要合并的 key 数据进行归并排序**，**并处理不同类型的 key 操作**（普通值 / 更新后的新版本 / tombstone）`[源码]`。
   - **③ 写入**：**把排序后的数据写入到 Ln+1 层的 SST 文件**，然后**更新元数据信息** `[源码]`。
4. **代价 · 写放大**：compaction **会带来写放大的问题**——同一份数据在合并过程中被**反复读写多次**，实际落盘量远大于用户写入量 `[源码]`。
5. **代价 · 资源密集**：compaction **属于资源密集操作**，**需要读取大量的数据进行排序，消耗较多的 CPU** `[源码]`。
6. **策略可调**：它**支持使用不同的 compaction 策略，来达到读、写、空间的最优平衡** `[源码]`。
7. **工程结论**：这正是 **Tendis 不适合 "key 经常变化" 场景**的原因——**key 频繁变化会频繁触发压缩，从而影响性能** `[源码]`。

**加分层：** 三个"放大"要配套记：**空间放大**（冗余数据占盘）、**读放大**（逐层查 SST）、**写放大**（compaction 反复重写）。compaction 缓解前两者，代价是制造第三者——这就是 LSM 的核心取舍。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | compaction 做什么？ | 答不出合并 + 清理已删数据 |
| L2 | 本质是哪种算法？ | 答不出归并排序 |
| L3 | 分几步？ | 答不出准备/处理/写入三步 |
| L4 | 代价是什么？ | 答不出写放大 + CPU 消耗 |
| L5 | 为什么 key 频繁变化不合适？ | 答不出频繁触发压缩 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| RocksDB 通用 | compaction 三步稳定 | 准备 → 处理 → 写入 |
| 策略可选 | level / universal / fifo | 按读写与空间权衡 |
| Tendis | 默认单进程 10 实例 | 压缩压力按实例分摊 |
| 全版本 | 物理删除只在 compaction | tombstone 之前仍占空间 |

## 关键代码
```go
// RocksDB compaction 观测与触发（grocksdb 绑定）
package main

import (
	"fmt"

	"github.com/linxGnu/grocksdb"
)

func main() {
	opts := grocksdb.NewDefaultOptions()
	opts.SetCreateIfMissing(true)
	// 用 level 风格 compaction：多级 SST，逐级归并
	db := grocksdb.OpenDB(opts, "/tmp/rocksdb-compaction-demo")
	defer db.Close()

	wo := grocksdb.NewDefaultWriteOptions()
	ro := grocksdb.NewDefaultReadOptions()

	// 构造"key 频繁变化"负载：同一个 key 反复更新 -> 产生大量冗余版本
	for i := 0; i < 100000; i++ {
		db.Put(wo, []byte("hot-key"), []byte(fmt.Sprintf("v%d", i)))
	}
	db.Delete(wo, []byte("hot-key")) // 只写 tombstone，尚未物理删除

	// 手动触发 compaction：Ln -> Ln+1 归并排序，过滤 tombstone，实现物理删除
	db.CompactRange(grocksdb.Range{Start: nil, Limit: nil})
	fmt.Println("compaction done: 冗余版本与 tombstone 被物理清除")

	// 读放大缓解效果：合并后层数减少，未命中时逐层查找的成本下降
	_, err := db.Get(ro, []byte("hot-key"))
	fmt.Println("get after compaction err:", err)

	// 观察写放大：实际写入字节数 >> 用户写入字节数
	fmt.Println("stats:\n", db.GetProperty("rocksdb.stats"))
}
```

## 总结与追问预判
**最爱追问的是"compaction 能不能关掉"**——不能，但可以**调策略**：RocksDB 提供不同 compaction 策略来平衡**读 / 写 / 空间**；写密集场景可放宽合并频率以降低写放大，读密集场景则更积极合并。追问常接"那 Tendis 为什么怕 key 频繁变化"——因为**每次变化都是一次追加写，很快堆满 memtable 与 L0，逼着 compaction 高频运行**，CPU 与 IO 被合并吃掉，业务延迟随之抖动。选型评估时这是**硬门槛**之一。

## ⚠️ 原文纠错
1. 事实核校：compaction 将 Ln 选入 Ln+1 并过滤已删数据实现物理删除、本质是归并排序、三步为准备/处理/写入、带来写放大、属资源密集且消耗 CPU、支持不同策略平衡读写空间、key 频繁变化会频繁触发压缩——均与 RocksDB/LSM 实现一致 `[经验]`。
2. 补充：原文用"压缩"一词容易与**通用数据压缩算法**（LZ4 / Snappy / Zlib）混淆——**compaction 是"合并整理"，压缩算法是"编码降体积"**，两者不同但常同时启用；另外写放大的直观量级是**同一条数据被反复重写多次**，实际落盘量可达用户写入量的数倍乃至数十倍 `[经验]`。
3. 崩坏词归一：源码将 compaction、SST、tombstone、归并排序、RocksDB 等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
