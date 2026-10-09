# 1207 binlog 写入流程：先写 cache 再落盘

> 分类：数据库内核 | 难度：L3 | 题型：工程题 | 频率：高 | 关键词：**binlog cache** / **一次性写入** / **binlog_cache_size**
> 原文锚点：第 59~67 段「mysql 先把日志迁写到内存的 binlog cache…一个事务不能被拆开」

## 一句话总述
事务执行时先写 binlog 到线程私有的 binlog cache（内存），提交时才把 cache 内容整体刷入 binlog 文件；一个事务的 binlog 不可拆分，必须一次性写入。

## 面试官视角
- 意图：是否理解 binlog 的写入缓冲与事务原子性约束。
- P5 知先 cache 后落盘 / P6 知每线程独立 cache、事务不可拆 / P7 知 cache 超 binlog_cache_size 会触发刷盘。
- 红旗：以为 binlog 每条语句直接落盘；以为 cache 大小无限制。
- 惊艳点：binlog_cache_size 默认 32KB，超阈值即刷盘，事务必须整体写 —— 验证 `[外部/MySQL]`。

## 主问答
**Q（面试官原话）：** binlog 是怎么写进去的？cache 起什么作用？
**A：**
1. **结论**：事务中产生的 binlog 先写线程私有 binlog cache，提交时整体刷到文件。
2. **机制**：每个线程分配独立 binlog cache，避免多线程写竞争；cache 大小由 binlog_cache_size 控制（默认 32KB）。
3. **边界**：一个事务的 binlog 是原子单元，无论多大都要一次性写入，不能拆成多个文件片段；cache 超出阈值会被提前刷盘。
**加阶层：** cache 越大事务越不易因超限刷盘，但占用更多内存，需按大事务评估。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 先写哪 | 概念 | cache | 换题 |
| L2 | 每线程独立 | 机制 | 降竞争 | 判 P5 |
| L3 | 不可拆分 | 边界 | 原子写 | 判 P6 |
| L4 | cache 阈值 | 权衡 | 32KB | 判 P6+ |
| L5 | 大事务调优 | 实战 | 调 cache | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| MySQL 全版本稳定 `[外部/MySQL][经验]` | binlog_cache_size 默认 32KB 长期稳定 | 先 cache 后提交落盘 |

## 关键代码
```sql
-- 查看 binlog cache 配置（示意，未验证）
SHOW VARIABLES LIKE 'binlog_cache_size';
SHOW STATUS LIKE 'Binlog_cache_disk_use';
```

## 总结与追问预判
- 线程私有 cache、提交整体落盘、事务不可拆、binlog_cache_size 默认 32KB。
- 预判：刷盘时机 → 见 1207；两阶段提交 → 见 1207。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对 binlog cache 写入顺序、事务不可拆分与 binlog_cache_size 默认值；仅做了机翻解码（如 利用→nil、勾浪→Go、首时→守时 等拼写还原），技术结论未做更正。
