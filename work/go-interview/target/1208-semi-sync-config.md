# 1208 半同步复制与并行回放配置

> 分类：MySQL 内核 | 难度：L3 | 题型：实操题 | 频率：中 | 关键词：**rpl_semi_sync**/**slave_parallel**/**LOGICAL_CLOCK**
> 原文锚点：第 72~79、99~102 段「并行回放配置…半同步开启」

## 一句话总述
半同步靠插件 `rpl_semi_sync_master_enabled` / `rpl_semi_sync_slave_enabled` 开启（主从都开才生效，超时默认 10s 降级异步）；并行回放靠 `slave_parallel_type=LOGICAL_CLOCK` + `slave_parallel_workers=N` 让从库多线程回放。

## 面试官视角
- 考察意图：能否把"概念"落到"配置项"，并说清参数语义。
- 分档：P5 知有半同步；P6 懂主从两端都要开；P7 能写出并行回放两个关键参数与超时降级机制。
- 红旗答案：只在主库开半同步就以为生效；把 `LOGICAL_CLOCK` 与 `DATABASE` 模式混用。
- 惊艳点：**半同步必须主从都启用且建立 ACK 通道才进入半同步态；任一端没开或超时，便静默退化为异步**——`Rpl_semi_sync_master_status` 是核对真值的唯一指标 `[经验]`。

## 主问答
**Q（面试官原话）：** 怎么开启半同步？从库怎么并行回放？
**A：**
1. **结论**：主库 `rpl_semi_sync_master_enabled=1`、从库 `rpl_semi_sync_slave_enabled=1`（均经插件），两端就绪后主库提交等从库 ACK；从库设 `slave_parallel_type=LOGICAL_CLOCK`、`slave_parallel_workers=N` 开启并行回放。
2. **机制**：半同步 ACK 超时（默认 10s，参数 `rpl_semi_sync_master_timeout`）后主库自动降级为异步，避免阻塞；并行回放基于"逻辑时钟"（同一组提交可并行），`LOGICAL_CLOCK` 比旧的 `DATABASE`（按库并行）更细粒度 `[经验]`。
3. **边界**：并行回放提升回放吞吐，但不改变"从库数据始终落后主库一个位点"的本质，强一致仍需读主或 MGR。

**加分层：** `DATABASE` 模式仅按不同库并行，单库高并发场景增益有限；`LOGICAL_CLOCK` 能在同库内并行，是现代默认选择。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 半同步怎么开？ | 基础 | 主从都启用插件 | P5 |
| L2 | 超时怎么办？ | 机制 | 降级异步 | P6 |
| L3 | 并行回放两参数？ | 配置 | type=LOGICAL_CLOCK,workers=N | P7 |
| L4 | LOGICAL_CLOCK 含义？ | 细节 | 同组提交并行 | P7 |
| L5 | 与全同步区别？ | 进阶 | 不要求全执行完 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| MySQL 5.7+ | 并行回放 LOGICAL_CLOCK | 答"两端开半同步插件+LOGICAL_CLOCK 并行" |

## 关键代码
```sql
-- 主库
INSTALL PLUGIN rpl_semi_sync_master SONAME 'semisync_master.so';
SET GLOBAL rpl_semi_sync_master_enabled = 1;
SET GLOBAL rpl_semi_sync_master_timeout = 10000;  -- 10s
-- 从库
INSTALL PLUGIN rpl_semi_sync_slave  SONAME 'semisync_slave.so';
SET GLOBAL rpl_semi_sync_slave_enabled = 1;
```

## 总结与追问预判
半同步两端开+超时降级；并行回放 LOGICAL_CLOCK+workers。追问回"延迟根因与缓解"。

## ⚠️ 原文纠错
1. 原文半同步配置项崩坏：`strPLCMISYNCmterenable`→**`rpl_semi_sync_master_enabled`**、`RPLCMSSslaveenable`→**`rpl_semi_sync_slave_enabled`**；并行回放项 `loslaveparalleltype`→`slave_parallel_type`、`logcclope`→`LOGICAL_CLOCK`、`slaveparallelworkers`→`slave_parallel_workers`。本卡已逐一归一，事实关系正确 `[经验]`。
2. 原文默认超时写"十秒"——准确（参数默认 10000ms），无事实错误。
