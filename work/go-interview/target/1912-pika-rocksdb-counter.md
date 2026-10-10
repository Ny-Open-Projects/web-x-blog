# 1912 Pika/RocksDB 落盘计数器方案

> 分类：缓存与存储/高并发 | 难度：L3 | 题型：八股题 | 频率：低 | 关键词：**Pika**/**RocksDB**/**LSM树**/**磁盘**/**兼容Redis**

> 原文锚点：第 23~32 段「需兼容REDIS协议且存磁盘…Pika(tennis)基于RocksDB…LSM树写先入memtable满了flush成SStable(有序不可变)…批量写降写放大…异步IO多线程…读在memtable+SSTable合并查找…compaction重组清理碎片…多级压缩…block/table cache+预读提高顺序读」

## 一句话总述
既要兼容 Redis 协议、又要降低内存成本，成熟解法是 **Pika**：它兼容 Redis 接口，底层用 **RocksDB（LSM 树）** 把数据落磁盘——写先入内存 memtable、满了 flush 成有序不可变的 SSTable，批量落盘降低写放大；compaction 合并重组、多级压缩、block/table cache 与预读保证读性能。把"内存"换成"SSD"使成本骤降。

## 面试官视角
这是计数器架构的"终极"档。面试官想确认你了解 LSM 树的写路径（memtable→SSTable）与 compaction 机制，以及它为什么比 Redis 全量省成本。

## 主问答
**Q（面试官原话）：** 有没有既兼容 Redis 又便宜的方案？底层怎么实现的？

**A：**

1. **兼容 Redis 协议、数据落盘**：Pika 对外是 Redis 协议（业务无需改客户端），内部把计数存到磁盘，内存只做缓存，单机容量从百 G 级跃升到 TB 级，成本较 Redis 全量降一个数量级。
2. **LSM 写路径**：写先入内存 **memtable**；memtable 写满后整体 flush 成 **SSTable**（有序、不可变）；后续异步 compaction 把多个 SSTable 合并、清理被删数据、减少碎片。批量/顺序落盘**降低写放大**与磁盘随机 IO 频率。
3. **并发与 IO**：RocksDB 支持多线程并行写、采用异步 IO 充分发挥多核与 SSD 性能；读在 memtable + SSTable 中查找，靠索引/合并快速定位。
4. **读优化**：compaction 可多级调策略平衡读写与空间；**block cache / table cache** 减少磁盘 IO；预读（prefetch）机制提前加载数据块，提高顺序读吞吐。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|----|------|----------|--------|------------|
| L1 | 为什么 LSM 写快 | 是否懂 memtable | 写全在内存、批量刷盘降随机 IO | 答不出即止 |
| L2 | SSTable 是什么 | 是否懂结构 | 有序不可变表，flush 自 memtable | 答不出即止 |
| L3 | compaction 干什么 | 是否懂合并 | 合并 SSTable、清删、减碎片 | 答不出即止 |
| L4 | 读会不会比 Redis 慢 | 是否懂 cache | 有 block/table cache + 预读补回 | 答不出即止 |
| L5 | 和 Redis 成本差多少 | 是否懂选型 | SSD 远便宜于内存，降数量级 | 答不出即止 |

## 版本与兼容性
- Pika 自 2016 年开源（360），设计目标即"兼容 Redis、落盘省成本"；RocksDB（Facebook 自 LevelDB 衍生）LSM 模型长期稳定。
- 多级 compaction、block/table cache 等参数随版本可调，机制一致。

## 关键代码
```go
// 业务侧无感：仍用 Redis 协议客户端连 Pika（兼容 RESP）
func IncrOnPika(ctx context.Context, id, field string, delta int64) int64 {
    // Pika 暴露 6379 RESP 端口，go-redis 直接复用
    return rdb.HIncrBy(ctx, "count:weibo:{"+id+"}", field, delta).Val()
}
// 底层 Pika 把该写落入 RocksDB memtable -> SSTable，成本按 SSD 计
```

## 总结与追问预判
- 口诀：**Pika=Redis 协议壳 + RocksDB 磁盘心；memtable 快写、SSTable 落盘、compaction 收尾、cache 补读**。
- 预判追问："Pika 读延迟比 Redis 差多少？"答：内存命中走 cache 接近 Redis；未命中走 SSD，多一次磁盘 IO，但容量/成本优势在海量计数场景决定性。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡已统一为规范术语（如 Pika、RocksDB、LSM 树、memtable、SSTable、compaction、block cache）。本源未现黑名单词，正文一律使用规范词，纠错节不枚举任何原词崩坏词 `[经验]`。

> 边界：缓存+DB 见 1912；Redis 全量见 1912；本卡只讲 Pika/RocksDB 磁盘型方案的取舍，不重述前两种。
