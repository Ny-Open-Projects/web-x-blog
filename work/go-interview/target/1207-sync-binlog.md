# 1207 sync_binlog：刷盘时机与安全权衡

> 分类：数据库内核 | 难度：L3 | 题型：工程题 | 频率：高 | 关键词：**sync_binlog** / **fsync** / **每事务提交**
> 原文锚点：第 68~84 段「sync_binlog 参数值表示每写多少次 binlog 事件之后刷新一次磁盘」

## 一句话总述
sync_binlog 控制 binlog 刷盘频率：=0 由 OS 决定、=1 每次事务提交都 fsync（最安全最慢）、=N 每 N 次事务提交 fsync 一次；崩溃时最多丢 N-1 个已提交事务的 binlog。

## 面试官视角
- 意图：是否理解持久性与写入吞吐的权衡，知道生产怎么配。
- P5 知 0/1/N 含义 / P6 知 =1 每提交 fsync、=N 控制丢失窗口 / P7 知与 redo group commit 协同、生产常设 >0。
- 红旗：说 =1 是每写一个事件刷盘；说 =0 完全不丢。
- 惊艳点：=1 指每事务提交 fsync，=N 指每 N 次提交 fsync，不是按事件计数 —— 验证 `[外部/MySQL]`。

## 主问答
**Q（面试官原话）：** sync_binlog 设成 0、1、N 分别是什么意思？
**A：**
1. **结论**：=0 OS 自管刷盘、=1 每事务提交 fsync、=N 每 N 次提交 fsync 一次。
2. **机制**：=1 每次提交都落盘，崩溃最多丢一个事务的 binlog，最安全但 fsync 开销最大；=0 依赖 OS 回写，掉电可能丢失 cache 中全部 binlog。
3. **边界**：=N(>1) 表示每累计 N 次事务提交才 fsync，丢失窗口可控（最多丢 N-1 个已提交事务的 binlog），兼顾安全与性能。
**加分层：** 生产常设 sync_binlog=1 配合 innodb_flush_log_at_trx_commit=1 达双 1 全持久，高并发可放宽到 N。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 三取值 | 概念 | 0/1/N | 换题 |
| L2 | =1 含义 | 机制 | 每提交 fsync | 判 P5 |
| L3 | =N 窗口 | 边界 | 丢 N-1 | 判 P6 |
| L4 | 双 1 配置 | 权衡 | 与 redo 协同 | 判 P6+ |
| L5 | 高并发取舍 | 实战 | 放宽 N | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| MySQL 全版本 `[外部/MySQL][经验]` | 默认值长期为 1 | 0/1/N 语义不变，生产按持久性要求选 |

## 关键代码
```sql
-- 查看与设置 sync_binlog（示意，未验证）
SHOW VARIABLES LIKE 'sync_binlog';
SET GLOBAL sync_binlog = 1;
```

## 总结与追问预判
- 0=OS、1=每提交 fsync、N=每 N 提交 fsync；=N 控制丢失窗口。
- 预判：与 redo 协同 → 见 1207-two-phase-commit；写入流程 → 见 1207-binlog-write-flow。

## ⚠️ 原文纠错
原文第 72~77 段将 sync_binlog=1 描述为「写入一个 binlog 事件就立即刷新到磁盘」，表述不准确：sync_binlog=1 指每次事务提交都 fsync binlog（一次事务含多个 binlog 事件）；sync_binlog=N(>1) 指每 N 次事务提交才 fsync 一次，而非每 N 个事件。其余 0/1/N 的安全与性能权衡与原文一致。机翻解码：勾浪→Go、利用→nil、首时→守时。
