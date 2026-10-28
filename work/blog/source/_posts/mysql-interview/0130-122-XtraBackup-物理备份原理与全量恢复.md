---
disableNunjucks: true
title: "122 XtraBackup 物理备份原理与全量恢复"
date: 2026-10-16 06:52:11
categories: [MySQL面试题集]
tags: [MySQL面试题集]
---

> 分类：备份恢复 | 难度：L3 | 题型：工程题 | 频率：高 | 关键词：**LSN** / **redo 追赶** / **--apply-log** / **--copy-back** / **crash recovery**
> 原文锚点：第 214~222 段「启动时记住 redo log 的日志序列号，运行后台进程监视 redo log，恢复时应用已提交事务并回滚未提交的」

## 一句话总述
XtraBackup 记下备份开始时的 **redo LSN**，边拷数据文件边让后台进程追 redo；恢复时先 `--apply-log`（前滚已提交、回滚未提交）再 `--copy-back`，效果等价于一次崩溃恢复。

## 面试官视角
- **考察意图**：是不是只知道「XtraBackup 快」，说不出「为什么在线拷文件还能保证一致」。
- **P5** 知道它是物理备份、要先 apply-log / **P6** 能讲清 LSN + redo 追赶 / **P7** 会补「apply-log 之后才算一致，且恢复必须**先停实例**再拷回数据目录、并修正属主为 mysql」。
- **红旗**：「拷过去就能直接启动」；「不需要停库恢复」；「apply-log 可以省」。
- **惊艳点**：`--copy-back` 后文件属主是执行备份的 OS 用户（常为 root），不 `chown -R mysql:mysql` 实例**起不来** —— 验证：`ls -l /var/lib/mysql` 看属主（8.0.36 `[经验]`）。

## 主问答
**Q：XtraBackup 为什么能在线备份还保证一致？恢复要走哪几步？**
**A：**
1. **先给结论**：三步——`--backup` 全备 → `--apply-log` 应用 redo → 停实例 `--copy-back` 并修属主。
2. **再给机制**：备份开始时记录当前 **redo LSN**，拷数据文件期间由后台进程持续复制新增 redo；因为拷贝跨越一段时间，文件本身是「不一致的」，靠 `--apply-log` 把已提交事务前滚、未提交回滚，收敛到一个一致点。
3. **最后给边界**：物理备份拷的是**整个数据目录**，所以恢复必须**停掉 MySQL 实例**；且只能恢复到同版本、同平台的实例，单表单库抽取极不方便。
**加分层**：`--apply-log` 只是「准备」，不是恢复；真正落盘是 `--copy-back`（或 `--move-back`），两者不要混为一谈。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | XtraBackup 属于哪类备份 | 概念 | 物理备份 | 换题 |
| L2 | 恢复第一步做什么 | 基础 | --apply-log | 判 P5 |
| L3 | 在线为什么能一致 | 机制 | LSN + redo 追赶 | 判 P6 |
| L4 | 恢复要不要停库 | 边界 | 必须停 | 判 P6+ |
| L5 | 拷回后起不来为什么 | 实战 | 文件属主不是 mysql | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| XtraBackup 2.4 支持 MySQL 5.7；**PXB 8.0 支持 MySQL 8.0**（验证 8.0.36） | 8.0 的数据字典改为 InnoDB 事务字典，2.4 无法备份 | 按「版本必须匹配：5.7 用 2.4，8.0 用 PXB 8.0」答 |

## 关键代码
```bash
# 1) 全备（可指定 --parallel 多线程）
xtrabackup --backup --parallel=2 --target-dir=/bk/full --user=root --password=***
# 2) 准备：应用 redo，使备份集一致（不是恢复！）
xtrabackup --prepare --target-dir=/bk/full
# 3) 停实例后拷回数据目录，并修正属主
systemctl stop mysqld
xtrabackup --copy-back --target-dir=/bk/full
chown -R mysql:mysql /var/lib/mysql
```
```sql
-- 恢复后校验：对比关键表的行数与最新自增/时间字段
SELECT COUNT(*) FROM db1.orders;
SELECT MAX(updated_at) FROM db1.orders;
```

## ⚠️ 原文纠错
原文演示用 `innobackupex` 命令——该脚本在 **XtraBackup 2.4 之后已被移除**（官方改为直接使用 `xtrabackup`），已在本卡代码中改用 `xtrabackup` 并注明。原文「记 LSN + 后台进程监视 redo log」的原理描述正确，保留。机翻「xtapickup / redoleonly / readolog」还原为 **XtraBackup / --apply-log / redo log**。

## 总结与追问预判
- 记 LSN → 追 redo → apply → copy-back → chown，五步闭环。
- 下一题：见 123（增量备份与恢复）、118（工具选型）。
