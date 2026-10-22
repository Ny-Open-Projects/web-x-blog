# 210. Redis 底层数据结构实现

> 分类：数据库·缓存 | 难度：L3 | 题型：原理 | 频率：中 | 关键词：**SDS** / **ziplist** / **intset** / **skiplist** / **哈希表** / **底层编码**
> 原文锚点：第8章 8-4「底层实现：string→SDS或整数; list→ziplist(压缩列表)或双端链表; hash→ziplist或哈希表; set→intset(小整数集)或哈希表; zset→跳跃表skiplist(阈值可配)」

## 一句话总述
**Redis 五种类型在底层有多种编码，按数据量自动切换**：string→SDS/整数；list→ziplist/双端链表；hash→ziplist/哈希表；set→intset/哈希表；zset→skiplist。

## 面试官视角
- **考察意图**：是否看过《Redis 设计与实现》、懂"类型 vs 编码"两层抽象，而非只背类型名。
- **P5** 能说出常见底层（SDS、ziplist、哈希表、skiplist） / **P6** 能讲清"小数据用紧凑编码 ziplist/intset 省内存，超阈值转哈希表/链表"的切换逻辑 / **P7** 能说明各编码的时间/空间复杂度取舍。
- **红旗**：把"类型"和"底层编码"混为一谈（如认为 list 永远是链表）；不知道 ziplist 是连续内存压缩结构。
- **惊艳点**：能提到"阈值在配置文件中可调""Redis 7 起 ziplist 被 listpack 取代"等时效细节 `[经验]`。

## 主问答
**Q（面试官原话）：** Redis 这些数据类型底层是怎么实现的？

**A · 标准答案骨架：**
1. **string**：底层是 **SDS（Simple Dynamic String）**；若值能用整数表示则直接用整数存储（增减小整数更高效）。
2. **list**：数据少时用 **ziplist（压缩列表，连续内存）** 省内存，超阈值转**双端链表**。
3. **hash**：同样 ziplist 与**哈希表**两种编码，按元素数量/大小切换。
4. **set**：小整数元素用 **intset**，否则转**哈希表**。
5. **zset**：用 **skiplist（跳跃表）** 实现（见 211 卡）。

**加分层**：源文件强调"ziplist 用连续内存实现链表结构，数据少时省内存"，阈值可在配置调整——这是"类型 vs 编码"两层抽象的核心。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | string 底层 | 基本认知 | SDS / 整数 | 换题 → 不及格 |
| L2 | ziplist 是什么 | 是否懂紧凑编码 | 连续内存压缩链表 | 判 P5 |
| L3 | 何时切换编码 | 深入 | 超阈值转哈希表/链表 | 判 P6 |
| L4 | zset 底层 | 加分 | skiplist 跳跃表 | 判 P6+ |
| L5 | 各编码复杂度 | 高阶 | 哈希O(1)/跳表O(logN) | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| ziplist/intset/SDS/skiplist 长期为底层编码 | Redis 7.0 起 ziplist 被 **listpack** 取代（更省内存、防级联更新） | 面试答"ziplist 类紧凑编码"即可，补"7.0 后为 listpack"显时效 |

## 关键代码
```python
# 查看某 key 的底层编码（redis-py）[实测, redis-py]
import redis
r = redis.Redis()
print(r.object("encoding", "user:1"))   # 可能返回 hashtable/ziplist/intset/embstr
```

## ⚠️ 原文纠错
- 机翻还原：「SDS / simpledynamicstring」→ **SDS（简单动态字符串）**；「zipblist / ziplilist」→ **ziplist（压缩列表）**；「inset / inset」→ **intset（整数集合）**；「seculistst / schemelist / skilllist」→ **skiplist（跳跃表）**；「reite / REDIS」→ **Redis**。
- 原文"Redis 底层用 C 语言编写"准确（Redis 用 C 实现）；"《release 的设计与实现》"→ **《Redis 设计与实现》**（黄健宏）。
- 原文未提 Redis 7 的 listpack 替代 ziplist，已补版本栅栏（见上表）。

## 总结与追问预判
"类型 vs 编码"两层抽象：小数据用 ziplist/intset 省内存，超阈值转哈希表/链表；zset 用跳表。面试官常追问"为什么 zset 用跳表"，可衔接：**跳跃表（见 211 卡）**。
