# 057 read_buffer_size 与临时表引擎

> 分类：服务器配置 | 难度：L3 | 题型：工程题 | 频率：中 | 关键词：**read_buffer_size** / **4K 倍数** / **磁盘临时表**
> 原文锚点：第 302~309 段「指定了对一个 MyISAM 表进行全表扫描时所分配的读缓冲大小…默认情况下这个临时表就是一个 MyISAM 的表，所以 read_buffer_size 设置很小会影响临时表与查询性能」

## 一句话总述
`read_buffer_size` 是**每线程**的顺序扫描读缓冲，取值应为 **4KB 的倍数**；它在历史上还承担**磁盘临时表**的读写，所以即便库里没有 MyISAM 表也不能无视它。

## 面试官视角
- **考察意图**：考一个"看着过时、实际还在生效"的参数，看你会不会只按字面理解。
- **P5** 知道它是 MyISAM 全表扫描读缓冲 / **P6** 补上**4KB 倍数**与临时表也用 / **P7** 说出临时表引擎的**版本翻转**。
- **红旗**：① "我们用 InnoDB，这参数没用"；② 随手设非 4KB 倍数；③ 把临时表落盘只归咎于 `tmp_table_size`。
- **惊艳点**：`Created_tmp_disk_tables / Created_tmp_tables` 可直接量化"临时表落盘率" `[经验]` —— 验证：`SHOW GLOBAL STATUS LIKE 'Created_tmp%';`

## 主问答
**Q（面试官原话）：** 库里全是 InnoDB 表，read_buffer_size 是不是就不用管了？

**A：**
1. **先给结论**：不能不管——它除 MyISAM 全表扫描外，还作用于**查询产生的磁盘临时表**，取值应保持 4KB 整数倍。
2. **再给机制**：顺序扫描时每线程分配该缓冲批量读行以减少 IO；大查询要排序/汇总时会建内部临时表，超内存阈值落盘后同样依赖这块缓冲。
3. **最后给边界**：**影响面随版本变**——8.0 前磁盘临时表默认 MyISAM，影响直接；8.0 起改 InnoDB（内存临时表用 TempTable），属"过时但不能为零"的参数。

**加分层**：临时表落盘根因多是 **SQL 写法**（多余 `GROUP BY`/`DISTINCT`）与 `tmp_table_size`/`max_heap_table_size` 偏小，先查这两个。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 这个参数管什么 | 概念 | 顺序扫描读缓冲 | 换题 → 不及格 |
| L2 | 取值有什么约束 | 细节 | 4KB 的整数倍 | 判 P5 |
| L3 | 只用 InnoDB 还要不要管 | 机制 | 磁盘临时表也会用 | 判 P6 |
| L4 | 临时表引擎是什么 | 版本翻转 | 8.0 前 MyISAM，8.0 起 InnoDB | 判 P6+ |
| L5 | 临时表落盘怎么根治 | 架构判断 | 改 SQL + 调内存阈值 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| ≤ 5.7 | 磁盘内部临时表默认 **MyISAM** 引擎 | 该参数对临时表性能影响直接 |
| 8.0 | 内存临时表改 **TempTable** 引擎、磁盘临时表改 **InnoDB** 引擎 | "MyISAM 场景减少，但仍按 4KB 倍数保守设，别设为 0" |

## 关键代码
```sql
-- 临时表落盘率：分子/分母比值越高越糟
SHOW GLOBAL STATUS LIKE 'Created_tmp_tables';
SHOW GLOBAL STATUS LIKE 'Created_tmp_disk_tables';
SHOW VARIABLES LIKE 'tmp_table_size';       -- 与 max_heap_table_size 取小者生效
SHOW VARIABLES LIKE 'max_heap_table_size';

-- 参数核对（建议保持 4KB 倍数，如 128K/256K）
SHOW VARIABLES LIKE 'read_buffer_size';
SHOW VARIABLES LIKE 'read_rnd_buffer_size';   -- 见 058 卡
```

## ⚠️ 原文纠错
两处需修正：① 原文"在 MySQL 2.0 之前的版本"为机翻崩坏，正确的时间栅栏是 **8.0 之前**磁盘内部临时表默认 MyISAM（8.0 起改为 InnoDB/TempTable）；② 原文暗示 read_buffer_size 主要服务于 MyISAM 表，需补一句它是**每线程且按 4KB 对齐**分配，调大同 050 卡一样存在连接数放大风险。原文"值一般是 4K 的倍数"正确，保留。机翻音译（readbackforsize、买sum、买desum、readbetter代）已还原为 read_buffer_size、MyISAM、MyISAM、read_buffer_size。

## 总结与追问预判
- 每线程、**4KB 倍数**、磁盘临时表也用；8.0 后影响面收窄但不为零。
- 落盘率看 `Created_tmp_disk_tables / Created_tmp_tables`。
- 下一题：见 058（read_rnd_buffer_size）、050（每线程缓冲总账）。
