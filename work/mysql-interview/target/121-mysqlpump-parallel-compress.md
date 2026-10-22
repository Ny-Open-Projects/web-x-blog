# 121 mysqlpump 的并行、压缩与账号导出

> 分类：备份恢复 | 难度：L2 | 题型：工程题 | 频率：中 | 关键词：**--default-parallelism** / **--compress-output** / **ZSTD** / **--users**
> 原文锚点：第 147~207 段「mysqlpump 可以用多线程对数据库进行逻辑备份……支持 LZ4 与 ZLIB 压缩……加 --users 才备份账号」

## 一句话总述
mysqlpump 相对 mysqldump 的三个增量能力：**多线程并行**（表级）、**备份即压缩**（LZ4/ZSTD）、**`--users` 导出账号**，此外同样跨平台跨版本。

## 面试官视角
- **考察意图**：用没用过 mysqlpump，知不知道它的并行粒度上限。
- **P5** 知道它能并行和压缩 / **P6** 能说出 `--default-parallelism` 与 `--compress-output` 两个参数 / **P7** 会补「默认**不备份 mysql 系统库的账号**，必须显式加 `--users`」以及「压缩后的文件要用 `zstd_decompress` / `lz4_decompress` 解开」。
- **红旗**：「并行能加速大单表」；「压缩后还是普通 sql 文本可直接导入」；「账号默认会跟着备份」。
- **惊艳点**：mysqlpump 导出的账号是 `CREATE USER` + `GRANT` **语句**（mysqldump 导的是 mysql 系统库的行数据），因此可直接拿来做账号迁移（8.0.36 `[经验]`）。

## 主问答
**Q：mysqlpump 相比 mysqldump 好在哪？有什么坑？**
**A：**
1. **先给结论**：好在**并行 + 内置压缩 + 账号导出**三点，命令参数与 mysqldump 几乎一致，迁移成本低。
2. **再给机制**：`--default-parallelism=N` 开 N 个线程（默认 2，0 表示不用并行），粒度是**库或表**；`--compress-output=ZSTD|LZ4` 边备份边压缩，输出不再是明文 SQL。
3. **最后给边界**：并行**到不了表内部**，单张超大表仍只有一个线程；压缩文件必须先解压才能导入；默认不含用户账号。
**加分层**：正因为导出的是 `CREATE USER`/`GRANT` 语句，`mysqlpump --users --exclude-databases=...` 就成了「只迁账号」的便捷手段，可替代 pt-show-grants。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | mysqlpump 是什么 | 概念 | dump 的并行升级版 | 换题 |
| L2 | 哪两个参数最关键 | 基础 | parallelism + compress-output | 判 P5 |
| L3 | 并行的粒度 | 机制 | 库或表，非表内 | 判 P6 |
| L4 | 压缩文件怎么用 | 边界 | 先解压再导入 | 判 P6+ |
| L5 | 怎么只导账号 | 实战 | --users 排除所有库 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.7.8 引入；5.7.11 修复并行与 `--single-transaction` 互斥的 bug（验证 8.0.36） | 5.7.11 之前两者不能同时用 | 5.7.11+ 才可「并行 + 一致性快照」一起开 |

## 关键代码
```bash
# 并行 4 线程 + ZSTD 压缩备份单库
mysqlpump --default-parallelism=4 --compress-output=ZSTD --databases db1 > db1.zst
# 压缩文件必须先解压
zstd_decompress db1.zst db1.sql
# 只导账号：排除所有业务库后加 --users
mysqlpump --exclude-databases=% --users > users.sql
```
```sql
-- 验证账号导出是否完整：对比源库与目标库的账号清单
SELECT user, host FROM mysql.user ORDER BY user, host;
```

## ⚠️ 原文纠错
原文说 mysqlpump 支持「LZ4 与 zlib 两种压缩算法」——按官方与 8.0 实际，8.0 提供的是 **ZSTD 与 LZ4**（早期版本才是 zlib/gzip），已按现行实现写明。原文「默认不备份 mysql 数据库账号」正确，已强化为坑点。机翻「mysqlpub / mysqlLBB / delect / deliver / curryuser」还原为 **mysqlpump / ZSTD / CREATE USER**。

## 总结与追问预判
- 并行 + 压缩 + 账号三板斧，记住粒度上限与解压步骤。
- 下一题：见 118（三款工具选型）、116（逻辑 vs 物理）。
