# 1228 innodb_large_prefix 与文件格式（解除 767 限制的版本演进）

> 分类：MySQL 存储 / 配置 | 难度：L3 | 题型：原理题 | 频率：中 | 关键词：**innodb_large_prefix** / **Antelope** / **Barracuda** / **file format** / **5.6/5.7/8.0 默认**
> 原文锚点：第 17~40 段「5.6 默认 Antelope+compact+large_prefix off→767；需 Barracuda+dynamic/compressed+开 large_prefix 才解 767(仍≤3072)；5.7 默认 Barracuda/dynamic+large_prefix on；8.0 默认 dynamic 且 large_prefix 配置移除」

## 一句话总述
解除 767 限制靠两把钥匙：**文件格式**切到 Barracuda（支持 DYNAMIC/COMPRESSED 行格式）+ 开 `innodb_large_prefix`。版本默认值一路放宽：5.6 默认 Antelope+COMPACT+large_prefix OFF→死守 767；5.7 默认 Barracuda+DYNAMIC+large_prefix ON→3072；8.0 默认 DYNAMIC 且 `innodb_large_prefix` 配置**被移除**（3072 成为事实默认）。

## 面试官视角
- 考察意图：是否知道"767 限制是历史配置产物、现代版本已默认放宽"
- P5 知 5.7+/8.0 默认放宽；P6 能讲 Antelope vs Barracuda + large_prefix 两把钥匙；P7 能讲清 8.0 移除 large_prefix 配置、以及 5.6 为何最易踩坑
- 红旗：以为"所有 MySQL 都只能 767"；在 8.0 上找 innodb_large_prefix 配置（已无）
- 惊艳点：点出"Antelope 只支持 redundant/compact、Barracuda 才支持 dynamic/compressed——文件格式是行格式的开关" [源码]

## 主问答
**Q（面试官原话）：** 怎么让 MySQL 索引突破 767 字节限制？
**A：**
1. **两把钥匙**：行格式设为 DYNAMIC/COMPRESSED（需文件格式 **Barracuda**），并开启 `innodb_large_prefix`——二者齐备才从 767 放宽到 3072 [源码]。
2. **版本默认演进**：5.6 默认 Antelope+COMPACT+large_prefix OFF→**最易踩 767**；5.7 默认 Barracuda+DYNAMIC+large_prefix ON→默认 3072；8.0 默认 DYNAMIC 且 **`innodb_large_prefix` 配置已移除**（3072 成为默认）[源码]。
3. **文件格式是行格式开关**：Antelope 仅支持 REDUNDANT/COMPACT，Barracuda 才支持 DYNAMIC/COMPRESSED——所以切 Barracuda 是前提 [源码]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 怎么解 767 | 配置 | large_prefix+Barracuda | P5 |
| L2 | 两格式区别 | 机制 | Antelope vs Barracuda | P6 |
| L3 | 5.6 为何坑 | 版本 | 默认 Antelope+off | P6+ |
| L4 | 8.0 呢 | 演进 | 默认 dynamic、配置移除 | P7 |
| L5 | 仍受啥限 | 边界 | 总≤3072 | P7+ |

## 版本与兼容性
| 版本 | 默认文件格式 | 默认行格式 | large_prefix | 单索引上限 |
| --- | --- | --- | --- | --- |
| 5.6 | Antelope | COMPACT | OFF | 767 |
| 5.7 | Barracuda | DYNAMIC | ON | 3072 |
| 8.0 | — | DYNAMIC | 已移除 | 3072 |

## 关键代码
```sql
-- 5.6 解除 767 限制的两步
SET GLOBAL innodb_file_format = Barracuda;
SET GLOBAL innodb_large_prefix = ON;
CREATE TABLE t (a VARCHAR(500), KEY(a)) ROW_FORMAT=DYNAMIC CHARSET=utf8mb4; -- 500*4=2000 ≤3072 OK
-- 8.0 无需上述 SET：默认 DYNAMIC，innodb_large_prefix 配置已不存在
```

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡统一为规范术语（InnoDB→inoDB、innodb_large_prefix→inlooTVlargeprayfix/inlodblargeprofix/inLDB垃圾perfects、innodb_file_format→乐indvsomeformat/innerDVfreformat、Antelope→艾特乐普/安特乐普、Barracuda→百/barriccoda 等）；技术结论未做事实性更正 [经验]。

## 总结与追问预判
- 解 767：Barracuda + DYNAMIC + large_prefix；5.7+/8.0 已默认，8.0 配置移除。
- 行格式四种与默认演进见 1215-row-format-overview（只引不重述）；索引长度阈值见 1228-index-length-limit。
