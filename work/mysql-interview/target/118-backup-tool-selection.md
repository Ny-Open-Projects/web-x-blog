# 118 mysqldump / mysqlpump / XtraBackup 怎么选型

> 分类：备份恢复 | 难度：L2 | 题型：工程题 | 频率：高 | 关键词：**mysqldump** / **mysqlpump** / **XtraBackup** / **并行备份**
> 原文锚点：第 46~52 段「mysqldump 是最常用的逻辑备份工具，mysqlpump 是它的升级版，xtrabackup 由 Percona 提供」

## 一句话总述
**mysqldump** 单线程逻辑备份（通用、零依赖）；**mysqlpump** 是它的并行升级版；**XtraBackup** 是 Percona 的物理备份工具，大库首选。

## 面试官视角
- **考察意图**：是不是只知道 mysqldump，说得出「什么量级该换工具」。
- **P5** 知道三个工具名字与逻辑/物理归属 / **P6** 能说出 mysqlpump 的并行与压缩、XtraBackup 的 redo 追赶机制 / **P7** 会补「mysqlpump 对**单张大表仍然单线程**，且并行与一致性在 5.7.11 前互斥」。
- **红旗**：「mysqlpump 能并行备份单张大表」；「XtraBackup 是官方工具」；「有 mysqlpump 就不用 XtraBackup 了」。
- **惊艳点**：mysqlpump 的并行粒度是**库/表**，不是表内——一张 500GB 的大表它照样只有一个线程在跑（8.0.36 `[经验]`）。

## 主问答
**Q：常用的 MySQL 备份工具有哪些？你们为什么选现在这个？**
**A：**
1. **先给结论**：逻辑备份用 mysqldump（小库/单表/跨版本）或 mysqlpump（多库并行、要压缩）；物理备份用 XtraBackup（大库、要求恢复快）。
2. **再给机制**：mysqlpump 内置**多线程**与 **LZ4/ZSTD 压缩**，命令参数与 mysqldump 高度相似，迁移成本低；XtraBackup 启动时记 redo LSN，边拷文件边用后台进程追 redo，恢复时先 apply 已提交事务、回滚未提交的。
3. **最后给边界**：mysqlpump 的并行只到表级，**单表仍单线程**；XtraBackup 单表恢复麻烦、占用空间大。
**加分层**：mysqlpump 默认**不备份用户账号**（要加 `--users`），且它导出的是 `CREATE USER` + `GRANT` 语句，可用来单独迁移账号——这点比 mysqldump 方便。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 三个工具叫什么 | 概念 | dump / pump / xtrabackup | 换题 |
| L2 | 哪个是物理备份 | 基础 | XtraBackup | 判 P5 |
| L3 | mysqlpump 强在哪 | 机制 | 并行 + 压缩 | 判 P6 |
| L4 | 并行能到单表内吗 | 边界 | 不能，只到表级 | 判 P6+ |
| L5 | 怎么单独导账号 | 实战 | mysqlpump --users | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| mysqlpump 自 5.7.8 起提供（验证 8.0.36） | 5.7.11 前 `--single-transaction` 与并行**不能同时用**（已知 bug，5.7.11 修复）；XtraBackup 2.4 只支持 5.7，8.0 需 PXB 8.0 | 5.7.11+ 才同时用并行与一致性快照 |

## 关键代码
```sql
-- 备份前确认库表规模：大库/大表才值得换物理备份或评估并行收益
SELECT table_schema, table_name,
       ROUND(data_length/1024/1024) AS data_mb
FROM information_schema.tables
WHERE table_schema='db1' ORDER BY data_length DESC LIMIT 10;
```
```bash
# mysqldump：单库一致性备份
mysqldump --single-transaction --master-data=2 db1 > db1.sql
# mysqlpump：并行 + 压缩（并行只到表级）
mysqlpump --default-parallelism=4 --compress-output=ZSTD --databases db1 > db1.zst
# XtraBackup：物理全备
xtrabackup --backup --target-dir=/bk/full --user=root --password=***
```

## ⚠️ 原文纠错
原文称「xtrabackup 当前并不支持 8.0 版本的 MySQL」——这是**录课时的历史状态**；当前 Percona XtraBackup 8.0 已支持 MySQL 8.0，且 8.0 另有官方 Clone Plugin。已在版本表注明「按录课时间点理解，当前已支持」。机翻中工具名与厂商名的音译写法已统一还原为标准术语。

## 总结与追问预判
- 小库逻辑、大库物理；并行只到表级是大表备份的硬伤。
- 下一题：见 119（mysqldump 参数）、122（XtraBackup 原理）。
