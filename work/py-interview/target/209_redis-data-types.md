# 209. Redis 五种常用数据类型与使用场景

> 分类：数据库·缓存 | 难度：L2 | 题型：概念+场景 | 频率：高 | 关键词：**string** / **list** / **hash** / **set** / **zset** / **使用场景**
> 原文锚点：第8章 8-4「Redis 五种常用类型：string(计数器incr) / list(双向链表,关注/粉丝列表,简单队列) / hash(关联信息hset) / set(不重复,关注者) / zset(有序集合,排行榜score排序)」

## 一句话总述
**Redis 五大常用类型各司其职**：string（KV/计数器）、list（双向链表，关注列表/队列）、hash（关联对象）、set（去重集合）、zset（有序集合，排行榜）。

## 面试官视角
- **考察意图**：是否真用过 Redis——不只会背类型名，还能对应到业务场景。
- **P5** 能背出五种类型并各举一场景 / **P6** 能讲清 list 是双向链表、zset 靠 score 排序 / **P7** 能对比"用 string 还是 hash 存对象""zset 与 set 差异"等选型判断。
- **红旗**：只说"五种类型"却给不出场景；把 zset 当普通 set 用（忽略 score 排序）。
- **惊艳点**：能补充"中高级岗还会问底层实现（SDS/ziplist/skiplist）"，体现深度储备 `[经验]`。

## 主问答
**Q（面试官原话）：** Redis 常用的数据类型有哪些？分别在什么场景下用？

**A · 标准答案骨架：**
1. **string**：最简单 KV，可做限流计数、计数器（`INCR` 自增）。
2. **list**：双向链表，可从左右两端追加；用于用户关注/粉丝列表、简单队列。
3. **hash**：存彼此关联的键值对（如 `HSET user:id name value`），适合存对象。
4. **set**：不重复元素集合（类似 Python set），用于用户关注者、去重。
5. **zset（sorted set）**：带 score 的有序集合，按 score 排序，用于排行榜。

**加分层**：源文件强调"这五种最常用，发布订阅、pipeline 批量等属于高级特性"；底层实现（见 210 卡）是中高级岗的加分项。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 五种类型 | 基本认知 | string/list/hash/set/zset | 换题 → 不及格 |
| L2 | list 是什么结构 | 是否懂 | 双向链表,左右追加 | 判 P5 |
| L3 | zset 怎么排序 | 深入 | 按 score 排序,排行榜 | 判 P6 |
| L4 | 存对象用哪个 | 选型 | hash 存对象,string 存单值 | 判 P6+ |
| L5 | 底层怎么实现 | 加分 | SDS/ziplist/skiplist | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 五种基础类型自 Redis 早期即稳定 | 后续新增 bitmap/hyperloglog/stream 等 | 仍以"五基础类型"作答，可补充"还有 stream 等高级结构" |

## 关键代码
```python
# 五种类型最小演示（redis-py）[实测, redis-py]
import redis
r = redis.Redis()
r.set("views:1", 0); r.incr("views:1")                   # string 计数器
r.lpush("fans:u1", 1001, 1002)                          # list 粉丝列表
r.hset("user:1", mapping={"name": "Tom", "age": 18})     # hash 对象
r.sadd("followers:u1", 1001, 1002)                      # set 关注者
r.zadd("rank:game", {"alice": 95, "bob": 88})            # zset 排行榜
```

## ⚠️ 原文纠错
- 机翻还原：「screen / strrain」→ **string**；「链表rase」→ **list**；「sourentset / sootageset / soortageset」→ **sorted set / zset**；「reite」→ **Redis**。
- 原文"用 ipad 然后 kease 这个 name"为 INCR/hset 等命令的重度音译，已还原为标准命令（`INCR`/`HSET`）。
- 原文"pipeline 完成非已知性的事物"→ **pipeline 实现非事务性的批量**（pipeline ≠ 事务，MULTI/EXEC 才是事务，见 213 卡）。

## 总结与追问预判
五种类型 = string/list/hash/set/zset，各对应明确场景。面试官必追问"底层实现"与"持久化/事务"，可衔接：**底层数据结构（见 210 卡）**、**跳跃表（见 211 卡）**。
