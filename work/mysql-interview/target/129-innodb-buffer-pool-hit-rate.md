# 129 InnoDB 缓冲池命中率怎么算、低于多少要处理

> 分类：管理监控 | 难度：L2 | 题型：八股题 | 频率：高 | 关键词：**Innodb_buffer_pool_read_requests** / **Innodb_buffer_pool_reads** / **命中率**
> 原文锚点：第 104~119 段「用 read_requests 减去 reads 再除以 read_requests，得到缓冲池命中率」

## 一句话总述
命中率 = **1 − `Innodb_buffer_pool_reads` / `Innodb_buffer_pool_read_requests`**；OLTP 场景通常要求 **≥ 99%**，持续低于说明内存不足或有大范围扫描。

## 面试官视角
- **考察意图**：会不会背公式但说不出「低了该怎么办」——后半句才是分水岭。
- **P5** 知道命中率概念 / **P6** 能写出公式 / **P7** 会补「命中率低先看是**冷启动**、**全表扫描**还是**真的内存不够**，三种处理方式完全不同」。
- **红旗**：「命中率越高越好，越高越该加内存」；「99.9% 才正常」；「命中率低一定是 buffer pool 太小」。
- **惊艳点**：实例刚重启后命中率会**天然偏低**（缓存是冷的），此时调大 `innodb_buffer_pool_size` 属于误判 —— 验证：对比 `Uptime` 与命中率曲线（8.0.36 `[经验]`）。

## 主问答
**Q：InnoDB 缓冲池命中率怎么算？低于多少算有问题？**
**A：**
1. **先给结论**：`1 − Innodb_buffer_pool_reads / Innodb_buffer_pool_read_requests`；OLTP 业务一般要求 **≥ 99%**。
2. **再给机制**：分子 `read_requests` 是**向缓冲池发起的读请求总数**，分母中的 `reads` 是**不得不去磁盘读的次数**，两者之比就是「没命中」的比例。
3. **最后给边界**：命中率低不等于内存小——刚启动的实例（缓存冷）、突发的全表扫描/大范围报表查询都会把它拉低；**先排除这两类再看是否扩容**。
**加分层**：真要扩容时，`innodb_buffer_pool_size` 一般设为物理内存的 50%~70%（实例独占时），并配 `innodb_buffer_pool_instances` 减少争用（见 052）。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 命中率衡量什么 | 概念 | 缓存命中比例 | 换题 |
| L2 | 分子分母是谁 | 基础 | reads / read_requests | 判 P5 |
| L3 | 多少算合格 | 机制 | OLTP ≥ 99% | 判 P6 |
| L4 | 低了一定是内存小吗 | 边界 | 还可能是冷启动或全表扫描 | 判 P6+ |
| L5 | 扩容配到多少 | 实战 | 物理内存 50%~70% | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.6~8.0（验证 8.0.36） | `innodb_buffer_pool_size` 在 5.7.5 起支持**在线调整**（无需重启） | 扩容可在线做；`instances` 参数在 8.0 重要性下降 |

## 关键代码
```sql
-- 直接算当前累计命中率
SELECT
  (1 - (CAST((SELECT VARIABLE_VALUE FROM performance_schema.global_status
              WHERE VARIABLE_NAME='Innodb_buffer_pool_reads') AS DECIMAL(20,4)) /
        CAST((SELECT VARIABLE_VALUE FROM performance_schema.global_status
              WHERE VARIABLE_NAME='Innodb_buffer_pool_read_requests') AS DECIMAL(20,4)))
  ) * 100 AS hit_rate_pct;
-- 顺带看缓冲池大小是否合理
SELECT @@innodb_buffer_pool_size/1024/1024 AS pool_mb;
```

## ⚠️ 原文纠错
原文公式「read_requests 减去 reads，再除以 read_requests」**结果正确**，与 `1 − reads/read_requests` 等价，保留。但原文**未给出合格阈值与误判场景**（冷启动、全表扫描），已补入主问答与追问链。机翻「inoDBbuferperreaderrequest / 尹诺地利beferpread / 引流DB」还原为 **`Innodb_buffer_pool_read_requests` / `Innodb_buffer_pool_reads` / InnoDB**。

## 总结与追问预判
- 公式不难，难在「低了先排除冷启动与全表扫描」。
- 下一题：见 128（并发数与连接数）、052（缓冲池参数）。
