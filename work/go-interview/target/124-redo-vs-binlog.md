# 124 redo log 与 binlog 的区别

> 分类：MySQL 内核 | 难度：L3 | 题型：对比题 | 频率：高 | 关键词：**redo vs binlog**/**物理vs逻辑**/**两阶段提交**
> 原文锚点：第 20~39 段「blog 和 readlog 有什么区别…用途/信息/地方/写入方式」

## 一句话总述
redo 与 binlog 四大区别——**用途**（崩溃恢复 vs 备份/复制）、**内容**（物理页改动 vs 逻辑变更）、**层级**（InnoDB 引擎层 vs server 层）、**写入**（循环写 vs 追加写）；二者靠 **两阶段提交(2PC)** 协同，保证"已提交事务"在两份日志中一致。

## 面试官视角
- 考察意图：能否从四个维度系统对比，并点出它们为何需要 2PC 协同。
- 分档：P5 知两者都记日志；P6 能说出物理/逻辑、循环/追加；P7 能讲 2PC 崩溃恢复逻辑。
- 红旗答案：只说"一个引擎层一个 server 层"，讲不出 2PC 如何关联两者。
- 惊艳点：一句话——**2PC 让 redo 的"提交"以 binlog 是否完整为判据，从而主从数据不分裂** `[经验]`。

## 主问答
**Q（面试官原话）：** redo log 和 binlog 到底有什么区别？
**A：**
1. **结论**：四不同（用途/内容/层级/写入）+ 靠 2PC 协同。
2. **机制**：① 用途 redo 保崩溃恢复(D)、binlog 保复制+PITR；② 内容 redo 记"页物理改动"、binlog 记"逻辑变更"；③ 层级 redo 仅 InnoDB、binlog 在 server 层覆盖所有引擎；④ 写入 redo 固定大小**循环覆盖**、binlog **追加写不覆盖**（按过期删）。
3. **边界**：**两阶段提交**——redo 写 `prepare` → 写 binlog → redo 写 `commit`。崩溃恢复时，redo 处于 prepare 且 binlog 完整则提交，否则借助 undo 回滚，确保两份日志的"已提交集合"一致。

**加分层：** 没有 2PC，redo 与 binlog 可能不一致，导致主库已提交、从库缺失，数据分裂。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 两者都干啥？ | 基础 | 恢复/复制 | P5 |
| L2 | 物理还是逻辑？ | 特征 | redo物理/binlog逻辑 | P6 |
| L3 | 写入方式？ | 差异 | 循环vs追加 | P6 |
| L4 | 为何要 2PC？ | 协同 | 一致性判据 | P7 |
| L5 | 崩溃恢复流程？ | 进阶 | prepare+binlog判据 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| MySQL 5.0+（XA/2PC 默认开启） | 无 | 答"四不同 + 两阶段提交靠 binlog 完整性判定提交" |

## 关键代码
```sql
-- 两阶段提交相关：保证 redo 与 binlog 一致
SHOW VARIABLES LIKE 'innodb_support_xa';          -- 应为 ON（默认）
SHOW VARIABLES LIKE 'sync_binlog';                -- 建议 1（双1）
SHOW VARIABLES LIKE 'innodb_flush_log_at_trx_commit';
```

## 总结与追问预判
redo vs binlog = 用途/内容/层级/写入四维度差异 + 2PC 协同。追问接"undo log 与二者关系"和"崩溃恢复具体流程"。

## ⚠️ 原文纠错
1. 机翻崩坏词归一：`videolog`/`radiolog`→**redo log**；`beinlog`→**binlog**；`redOOG`→**redo log**；`ininoOD`→**InnoDB**。事实正确，仅术语崩坏，本卡已归一 `[经验]`。
2. 精度补正：原文把"binlog 和 redo 都是追加写"并列——实际 redo 是**循环写（覆盖）**、binlog 才是**追加写（切文件）**；本卡已厘清，避免面试官追问写入方式时自相矛盾。
