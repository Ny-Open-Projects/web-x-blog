# 1316 查询缓存与定向 routing 优化

> 分类：Elasticsearch | 难度：L4 | 题型：八股题 | 频率：中 | 关键词：**查询缓存**/**routing**/**term 查询**
> 原文锚点：第 33~68 段「日期拆字段转 term…定向 routing 优化」

## 一句话总述
范围查询可把日期拆成年/月/日/时多字段、用 `term` 过滤替代 `range` 以命中查询缓存；批量写入用定向 `routing` 把同路由数据打到同一分片，减少子请求扇出、避免队列打满被拒绝。

## 面试官视角
- 考察意图：是否掌握"缓存友好查询"与"减少分散度"两大写入优化。
- 分档：P5 知 routing 概念；P6 懂日期拆字段换 term；P7 能讲清 query cache 命中条件与 routing 降扇出。
- 红旗答案：以为 range(now-1h, now) 能命中缓存；以为 routing 只影响读取。
- 惊艳点：**`range` 含 `now()` 每次条件都变→永不命中 query cache；把时间取整到分钟级、或拆成年月日字段用 `term`，同一分钟内查询语句完全一致才能复用缓存** `[经验]`。

## 主问答
**Q（面试官原话）：** 怎么让 ES 查询用上缓存？批量写入怎么优化？
**A：**
1. **结论**：用确定值查询（拆日期字段 + `term`）替代含 `now()` 的 `range`；批量写入显式 `routing` 让同批数据落到少数分片，降低请求扇出。
2. **机制**：query cache 按"查询语句二进制"命中，含 `now()` 的 range 每秒都变故永不命中；定向 routing 让一次 bulk 只打少数分片而非全部分片，避免局部故障/抖动拖垮整批、防止写入队列打满被 reject `[经验]`。
3. **边界**：`term` 拆字段会增加写入时的字段冗余与存储；routing 后 `GET by ID` 必须带 `routing` 参数（默认 routing=_id，自定义 routing 改变了路由键）。

**加分层：** 自动生成的文档 ID 在默认 routing=_id 下 `GET by ID` 正常；一旦业务设了自定义 routing，单条 GET/DELETE 都必须传同一 routing 值。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | range 能缓存？ | 基础 | 含 now 不能 | P5 |
| L2 | 怎么改 term？ | 手法 | 拆日期字段 | P6 |
| L3 | routing 干嘛？ | 写入 | 降扇出 | P6 |
| L4 | GET 要带 routing？ | 边界 | 自定义 routing 必带 | P7 |
| L5 | 极限网关？ | 进阶 | 按路由合并 bulk | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| ES 2.x+ | query cache 长期存在 | 答"拆字段转 term 吃缓存；bulk 用 routing 降扇出" |

## 关键代码
```json
// 分钟级取整 + term 过滤（可缓存）
GET /logs/_search
{ "query": { "term": { "ymd": "20240401", "h": 10 } } }
// 定向 routing 写入
POST /logs/_bulk?routing=user_123
```

## 总结与追问预判
缓存友好=确定性查询；routing=减扇出。追问接"分片规划与副本策略"。

## ⚠️ 原文纠错
1. 原文日期拆字段转 term、routing 降扇出、query cache 命中逻辑正确，仅术语崩坏：routine/rout/root→**routing**、bug→**bulk（批量）**、过尔查询→**bool 查询**、测体→**查询体（query body）**、集限→**集群**、分辨→**分片**、索影→**索引**、机c→**机器**。本卡已归一，事实无错 `[经验]`。
2. 精度补正：原文称"自动生成 ID 无法通过 ID 获取单条文档"——准确说应是"设了自定义 routing 后，GET by ID 必须带 routing 参数"；默认 routing=_id 时自动 ID 的 GET 正常。本卡已在主问答边界栏修正此表述。
