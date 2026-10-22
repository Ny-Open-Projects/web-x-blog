# 123 XtraBackup 增量备份与增量恢复

> 分类：备份恢复 | 难度：L3 | 题型：工程题 | 频率：中 | 关键词：**--incremental** / **--incremental-basedir** / **--apply-log-only** / **最后一次**
> 原文锚点：第 377~390 段「增量备份基于上一次全量或增量备份，需要指定 --incremental-basedir；恢复时必须依次应用」

## 一句话总述
增量备份靠 `--incremental-basedir` 指向上一次备份；恢复时要**先对全备 `--apply-log-only`，再逐个应用增量**，最后一个增量应用完**不能再加 `--apply-log-only`**。

## 面试官视角
- **考察意图**：这是 XtraBackup 最容易记反的地方——考的就是 `--apply-log-only` 的**顺序与最后一次例外**。
- **P5** 知道增量要靠 basedir / **P6** 能说清逐个应用且有序 / **P7** 会补「中间步骤必须加 `--apply-log-only`，**只有最后一步不加**，否则未提交事务被提前回滚、后续增量无法应用」。
- **红旗**：「增量恢复只要最后一份」；「所有步骤都不加 --apply-log-only」；「顺序无所谓」。
- **惊艳点**：中间步骤漏了 `--apply-log-only` 会直接报错或导致后续增量无法应用，恢复链就此作废（8.0.36 `[经验]`）。

## 主问答
**Q：XtraBackup 怎么做增量备份？恢复流程是什么？**
**A：**
1. **先给结论**：备份加 `--incremental` 与 `--incremental-basedir`（指向上次全量或增量目录）；恢复时**全备先 prepare-only，再按时间顺序逐个应用增量**，最后一步不加只读标记。
2. **再给机制**：增量只拷贝自 basedir 之后**变化的页**；应用时把增量页合并回全备目录，所以顺序错了就前功尽弃。
3. **最后给边界**：增量恢复**只能追到最后一次备份那一刻**——之后到故障点之间的数据**不在备份集里**，必须靠 binlog 补，所以增量备份和 binlog 是配套关系，不是替代关系。
**加分层**：差异备份与增量备份的命令完全一样，区别只在于 **basedir 始终指向全量**（见 117）。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 增量靠哪个参数 | 概念 | --incremental-basedir | 换题 |
| L2 | 基于谁做增量 | 基础 | 上次全量或增量 | 判 P5 |
| L3 | 恢复顺序 | 机制 | 全备→增量1→增量2 | 判 P6 |
| L4 | apply-log-only 何时不加 | 边界 | 最后一步 | 判 P6+ |
| L5 | 最后增量之后的数据 | 实战 | 只能靠 binlog 恢复 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| XtraBackup 2.4 / PXB 8.0（验证 8.0.36） | 2.4 起 `innobackupex` 逐步弃用，8.0 移除 | 统一用 `xtrabackup` 子命令写法 |

## 关键代码
```bash
# 全备
xtrabackup --backup --target-dir=/bk/full --user=root --password=***
# 增量：basedir 指向上一次备份（全量或增量）
xtrabackup --backup --target-dir=/bk/inc1 --incremental-basedir=/bk/full --user=root --password=***
# 恢复：先 prepare 全备（注意 --apply-log-only）
xtrabackup --prepare --apply-log-only --target-dir=/bk/full
# 再依次应用增量；最后一个增量【不加】--apply-log-only
xtrabackup --prepare --target-dir=/bk/full --incremental-dir=/bk/inc1
```
```sql
-- 恢复后确认数据已追到最近一次增量：查统计表行数与最新记录
SELECT COUNT(*), MAX(id) FROM db1.stock_stat;
```

## ⚠️ 原文纠错
原文「依次进行增量备份的恢复」方向正确，但**未点明 `--apply-log-only` 只在中间步骤使用、最后一步必须省略**这一最容易出错的规则，已补全并写入加粗结论。原文演示中输错密码生成了 6 字节的空备份目录，属操作演示噪音，不进卡。机翻「incrediment / incrementment / 引光DB」还原为 **`--incremental` / InnoDB**。

## 总结与追问预判
- basedir 定增量，apply-log-only 守中间，最后一步要放开。
- 下一题：见 124（binlog 补齐最后一公里）、117（全量/增量/差异）。
