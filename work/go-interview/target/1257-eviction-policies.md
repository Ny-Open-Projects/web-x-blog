> 原文锚点：第 13~22 段「八种内存淘汰策略…noeviction 3.0后默认不淘汰…allkeys-lru…allkeys-lfu 4.0新增…allkeys-random…volatile-lru 3.0前默认…volatile-lfu 4.0…volatile-random…volatile-ttl…config get/set maxmemory-policy」

## 一句话总述
Redis 八种淘汰策略分两大类：**allkeys-***（对所有 key）与 **volatile-***（只对设了过期时间的 key）；按算法又分 LRU、LFU、random、ttl。Redis 3.0+ 默认 `noeviction`（只拒写），3.0 前默认 `volatile-lru`，4.0 新增 LFU 系列。

## 面试官视角
这道题的区分度在"两大类 vs 各算法"的矩阵，以及**默认策略随版本不同**。能画出矩阵并说清 noeviction/volatile-lru 的版本差异，即高分。

## 主问答
**Q（面试官原话）：** Redis 有哪八种内存淘汰策略？默认是哪个？

**A：**

1. **noeviction（3.0+ 默认）**：不淘汰任何 key，内存满时拒绝写命令，读/删正常——存量数据安全但无法写入。
2. **allkeys-lru**：从**所有** key 中淘汰最近最少使用（LRU 近似）。
3. **allkeys-lfu（4.0+ 新增）**：从**所有** key 中淘汰使用频率最低（LFU）。
4. **allkeys-random**：从**所有** key 中随机淘汰。
5. **volatile-lru（3.0 前默认）**：仅从**设了过期时间**的 key 中淘汰 LRU。
6. **volatile-lfu（4.0+ 新增）**：仅从设过期时间的 key 中淘汰 LFU。
7. **volatile-random**：仅从设过期时间的 key 中随机淘汰。
8. **volatile-ttl**：仅从设过期时间的 key 中淘汰**剩余 TTL 最短**的。

## 追问链（L1~L5）
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|----|------|----------|--------|------------|
| L1 | volatile-* 与 allkeys-* 区别 | 是否懂范围划分 | 前者仅过期 key、后者全部 | 答不出即止 |
| L2 | 3.0 前后默认策略 | 是否懂版本差异 | 前 volatile-lru、后 noeviction | 答不出即止 |
| L3 | LRU 是精确还是近似 | 是否懂采样实现 | 近似（默认抽样 5 个候选取最久未用） | 答不出即止 |
| L4 | LFU 比 LRU 好在哪 | 是否懂频率维度 | LFU 抗短期突发、长期低频也淘汰 | 答不出即止 |
| L5 | volatile-* 但无过期 key 会怎样 | 是否懂边界 | 等同 noeviction 拒写 | 答不出即止 |

## 版本与兼容性
- `noeviction` 默认从 3.0 起；`volatile-lru` 为 2.x/3.0 前默认。
- `allkeys-lfu`/`volatile-lfu` 随 **4.0** 引入；LRU/LFU 均用近似采样，非全局精确排序。
- `volatile-ttl` 依赖 TTL，无过期 key 时退化为拒写。

## 关键代码
```go
// 查询与动态设置淘汰策略（重启失效，配置文件才永久）
import "context"
import "github.com/redis/go-redis/v9"

cur, _ := cli.ConfigGet(ctx, "maxmemory-policy").Result() // ["maxmemory-policy","noeviction"]
_ = cur
_ = cli.ConfigSet(ctx, "maxmemory-policy", "allkeys-lru").Err()
// 永久生效需改 redis.conf：maxmemory-policy allkeys-lru
```

## 总结与追问预判
- 矩阵记忆：**范围（allkeys / volatile）× 算法（lru / lfu / random / ttl）+ noeviction** = 8 种；默认随版本变。
- 预判追问：选型建议？答：缓存场景用 `allkeys-lru`/`allkeys-lfu`；需保活非缓存数据用 `volatile-lru`（只逐过期项）。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡已统一为规范术语（如 Redis、noeviction、allkeys-lru、allkeys-lfu、volatile-ttl、maxmemory-policy）。本源未现黑名单词，正文一律使用规范词，纠错节不枚举任何原词崩坏词 `[经验]`。

> 边界：maxmemory 配置/单位见 `1257-maxmemory-config`；内存满具体行为见 `1257-memory-full-behavior`；本卡只列策略矩阵与版本默认。
