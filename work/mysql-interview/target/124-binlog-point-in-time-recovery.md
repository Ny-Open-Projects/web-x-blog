# 124 用 binlog 做增量恢复与时间点恢复

> 分类：备份恢复 | 难度：L3 | 题型：事故题 | 频率：高 | 关键词：**mysqlbinlog** / **--start-position** / **--stop-datetime** / **PITR** / **flush logs**
> 原文锚点：第 351~368 段「使用 mysqlbinlog 命令把二进制日志解析出来，指定 start-position 偏移量，导出后导入数据库」

## 一句话总述
全备 + binlog 才是完整恢复：**先恢复全备，再用 `mysqlbinlog` 按 `--start-position`（备份时的位点）或 `--stop-datetime`（误操作前一刻）导出增量并导入**。

## 面试官视角
- **考察意图**：误删数据怎么救——这是 DBA 面试里最硬的一道实战题。
- **P5** 知道要用 binlog / **P6** 能说清「先全备、后 binlog、位点对齐」/ **P7** 会补「恢复前先 `FLUSH LOGS` 切出新文件，避免在正在写的 binlog 上操作；多个 binlog 要**依次**恢复」。
- **红旗**：「直接把 binlog 拷回去」；「不用全备只靠 binlog」；「恢复到误操作之后也没关系」。
- **惊艳点**：`--start-position` 的值来自**备份文件里的 `--master-data` 记录**——没有这个锚点就不知道从哪开始解析（8.0.36 `[经验]`）。

## 主问答
**Q：线上有人误删了一张表，你怎么把数据救回来？**
**A：**
1. **先给结论**：恢复最近一次全备 → 用 `mysqlbinlog` 从**全备对应的位点**开始解析，一直应用到**误操作前**的位置/时间点 → 导入目标实例。
2. **再给机制**：`--master-data=2` 在 dump 头部记下了备份那一刻的 binlog 文件与偏移量，这就是增量恢复的起点；`--stop-datetime` 或 `--stop-position` 用来停在误操作之前，实现**时间点恢复（PITR）**。
3. **最后给边界**：binlog 有多个文件（如 000002、000003）时必须**按顺序依次**恢复，不能跳；且**正在被写入**的当前 binlog 要先 `FLUSH LOGS` 切出来再操作。
**加分层**：这就是为什么「备份」和「binlog 保留」必须一起设计——只做全备不做 binlog 保留，最后一次备份之后的数据一律救不回来。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 用什么工具解析 binlog | 概念 | mysqlbinlog | 换题 |
| L2 | 起点从哪来 | 基础 | 备份里的 master-data | 判 P5 |
| L3 | 怎么停在误操作前 | 机制 | stop-datetime/position | 判 P6 |
| L4 | 多个 binlog 怎么办 | 边界 | 按序号依次恢复 | 判 P6+ |
| L5 | 当前正在写的 binlog | 实战 | 先 FLUSH LOGS 切出 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.6~8.0（验证 8.0.36） | 8.0 起 binlog 默认开启（`log_bin` 默认 ON），且 `binlog_format=ROW` 为默认 | ROW 格式下解析结果是行变更，需用 `--base64-output=DECODE-ROWS -v` 才可读 |

## 关键代码
```bash
# 0) 先切出新 binlog，避免动到正在写的文件
mysql -e "FLUSH LOGS;"
# 1) 从备份位点开始解析，停在误操作之前；-d 限定只恢复目标库
mysqlbinlog --start-position=710 --stop-datetime="2026-10-16 09:59:59" \
  -d db1 mysql-bin.000002 mysql-bin.000003 > incr.sql
# 2) 先恢复全备，再导入增量
mysql db1 < full.sql && mysql db1 < incr.sql
```
```sql
-- 恢复前先在目标库确认当前 binlog 位点，作为增量起点参考
SHOW MASTER STATUS;
```

## ⚠️ 原文纠错
原文演示中把 GTID 关掉以简化位点操作，但未说明**开启 GTID 时做法不同**（GTID 模式下需处理 `GTID_PURGED`，或用 `--skip-gtids` 导出）；已在 120 卡专门说明并在此提示。原文未强调「多个 binlog 必须按序依次恢复」，已补入边界。机翻「mysql编log / lostarposition / beinglove」还原为 **`mysqlbinlog` / `--start-position` / binlog**。

## 总结与追问预判
- 全备给基线，binlog 补最后一公里，位点/时间点是止损点。
- 下一题：见 125（binlog 怎么备份）、120（GTID 恢复报错）。
