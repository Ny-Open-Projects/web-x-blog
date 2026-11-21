# 1912 海量计数器架构演进深挖

## 思路与架构
```text
海量计数器三层架构演进：
1. 缓存 + DB：key=前缀+ID，value=长整型；先 DB 后缓存。瓶颈=DB TPS(3000~6000) + 聚合穿透。适用中小规模。
2. Redis 全量：哈希分片提写、主从读写分离提读、持久化保数据。瓶颈=内存利用率≈18.5%、千亿级+副本+多中心>100T、上千台。性能理想成本爆炸。
3. Pika/RocksDB：兼容 RESP、数据落 SSD。LSM(memtable->SSTable->compaction)降写放大；block/table cache + 预读补读。成本降数量级。
选型轴：规模 × QPS × 成本预算。
```

## 方案取舍
```text
- 中小规模：缓存+DB 最简单，别过度设计。
- 中大型、预算足：Redis 全量，性能最好但烧钱。
- 海量 + 成本敏感：Pika 兼容 Redis 协议、落盘省成本，是用空间(SSD)换内存的典型。
- 写路径优化：LSM 用"内存攒批+顺序刷盘"对抗随机写放大，代价是读需查多层 + compaction 后台开销。
- 一致性：计数器多副本靠主从/quorum，Pika 亦需副本防单点。
```

## 答题技巧
```text
- 被问"海量计数器"：先抛三层演进（缓存+DB → Redis 全量 → Pika 落盘），每层点明瓶颈与适用规模。
- 必背数字：DB TPS 3000~6000、Redis 有效利用率 18.5%、千亿级>100T。
- 落到 LSM：memtable 快写、SSTable 有序不可变、compaction 合并减碎片、cache 补读。
- 收尾强调"兼容 Redis 协议"是 Pika 能被业务无感接入的关键。
```

## 细节与核心 API

```go
// 高并发计数（阅读量/点赞）：先 Redis 累加，异步批量落库，避免直打 DB
func IncrCounter(ctx context.Context, key string) (int64, error) {
    return rdb.Incr(ctx, "cnt:"+key).Result()        // 内存级 O(1)，扛百万 QPS
}
// 异步落库：定时/按阈值把 Redis 计数刷入 DB，合并写
func flush() {
    for _, key := range rdb.Keys(ctx, "cnt:*").Val() {
        v, _ := rdb.Get(ctx, key).Int64()
        db.Exec("UPDATE stat SET cnt=? WHERE k=?", v, key)
        // 注意：增量模式更好 -> INCRBY 后取差值累加，避免覆盖中间增长
    }
}
// 防丢失：DB 用“累加”而非“覆盖”；Redis 宕机前未刷部分需 AOF/RDB 兜底或写 WAL
// 选型：实时展示用 Redis，精确对账用 DB 异步收敛；强一致计数才直写 DB（性能差）
// 热点 key：单 key 过热可分片（cnt:key:0..N 取模）+ 本地聚合
```
