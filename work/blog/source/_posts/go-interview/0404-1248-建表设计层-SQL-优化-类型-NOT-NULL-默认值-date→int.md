---
disableNunjucks: true
title: "1248 建表设计层 SQL 优化（类型 / NOT NULL / 默认值 / date→int）"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：MySQL · 表设计 | 难度：L3 | 题型：工程题 | 频率：高 | 关键词：**类型选择** / **NOT NULL** / **默认值** / **date 转 int** / **联合索引最左列**
> 原文锚点：第 2~21 段「表设计建议：恰当类型/ NOT NULL / 默认值 / 只建必要索引 / date 存 int」

## 一句话总述
SQL 优化很大程度依赖表设计：用**恰当且更小的类型**省磁盘、尽量 **NOT NULL**（省 NULL 标志位、避免索引变长、优化器易优化）、设**默认值**防插入遗漏、频繁比较的 **date 存为 int**（省日期函数转换、数值直接比）。

## 面试官视角
- 意图：是否理解"优化前移"——好表结构比事后调 SQL 更省力。
- 分档：P5 知小类型省空间；P6 知 NOT NULL 收益；P7 能讲 date→int 与联合索引最左列选型。
- 红旗：所有字段一律 `VARCHAR(255)` + 允许 NULL；或不知道 NULL 影响索引。
- 惊艳点：点出"可为 NULL 的列被索引时，每个索引记录多 1 字节，甚至使定长索引变变长"。

## 主问答
**Q（面试官原话）：** 表设计阶段怎么为 SQL 性能埋好伏笔？
**A：**
1. **类型恰当**：能用 `TINYINT` 不用 `SMALLINT`、能用 `SMALLINT` 不用 `INT`、能用 `INT` 不用 `BIGINT`；变长字段额外存长度信息，定长更省。
2. **尽量 NOT NULL**：NULL 列需额外标志位；可为 NULL 的列被索引时每条记录多 1 字节，甚至使整数单列索引变成变长；且优化器对 NULL 列的统计/比较更复杂。
3. **设默认值**：插入未给值的字段按默认值落库，避免意外 NULL 与后续判空逻辑。
4. **date→int**：频繁比较的日期存为 `INT`（如时间戳），避免 MySQL 用日期函数把字符串转成日期值再比；数值类型直接比较，比字符串逐字符比较快得多。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 类型怎么选 | 基础 | 小类型优先 | P5 |
| L2 | NOT NULL 好处 | 机制 | 省标志位/索引变长 | P6 |
| L3 | NULL 影响索引 | 机制 | 每条多 1 字节 | P6+ |
| L4 | date 为何转 int | 进阶 | 省函数转换/直接比 | P7 |
| L5 | 联合索引最左列 | 设计 | 选最常用字段 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| MySQL 全版本（行格式 5.1 前 REDUNDANT 例外） | 无 | 类型/NOT NULL/默认值/date→int 长期成立 `[经验]` |

## 关键代码
```sql
-- 反例：过度宽类型 + 允许 NULL
CREATE TABLE bad (
  id BIGINT,                 -- 本可用 INT
  status VARCHAR(255) NULL,  -- NULL 使索引变长
  created DATE NULL          -- 比较需函数转换
);
-- 正例：恰当类型 + NOT NULL + 默认值 + date 转 int
CREATE TABLE good (
  id INT NOT NULL,
  status TINYINT NOT NULL DEFAULT 0,
  created_ts INT NOT NULL     -- 时间戳，数值直接比
);
```

## 总结与追问预判
- 表设计是 SQL 优化的第一现场：小类型、NOT NULL、默认值、date→int。
- 预判：行格式 NULL 存储细节 → 见 1215；查询层索引失效 → 见 1221。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词（如 circle→SQL、浪值→NULL、ln值→NULL、缩引→索引、asside→某、redealn→REDUNDANT 行格式），本卡统一为规范术语 `[经验]`。未做事实性更正。
