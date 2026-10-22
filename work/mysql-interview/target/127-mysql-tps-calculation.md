# 127 TPS 怎么算，和 QPS 有什么不同

> 分类：管理监控 | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**TPS** / **Com_commit** / **Com_rollback** / **写事务**
> 原文锚点：第 80~86 段「TPS 是 MySQL 每秒所处理的事务数量，把这些语句的计数器值加起来，再除以间隔时间」

## 一句话总述
严格口径下 **TPS = (Com_commit + Com_rollback) 增量 ÷ 时间**；把 insert/update/delete 累加得到的其实是**写 QPS**，两者常被混为一谈。

## 面试官视角
- **考察意图**：能不能分清「事务数」与「语句数」——这是判断是不是真看过监控脚本的细节。
- **P5** 知道 TPS 是每秒事务数 / **P6** 能给出 commit+rollback 口径 / **P7** 会补「只读事务不计入 commit 计数，所以读写混合业务的 TPS 会低于直觉」。
- **红旗**：「TPS 就是 insert+update+delete 之和」；「TPS 和 QPS 一个数」；「TPS 越高说明性能越好」。
- **惊艳点**：`Com_commit` **不统计只读事务**（InnoDB 只读事务不做提交流程），所以纯读业务 TPS 会接近 0 —— 验证：只读压测下对比 `Com_commit` 与 `Questions`（8.0.36 `[经验]`）。

## 主问答
**Q：TPS 怎么算？和 QPS 有什么区别？**
**A：**
1. **先给结论**：QPS 数的是**请求（语句）**，TPS 数的是**事务**；TPS 用 `(Com_commit + Com_rollback)` 的两次采样差值除以时间。
2. **再给机制**：一个事务里可能有多条 SQL，所以 QPS 通常**远大于** TPS；反过来长事务会让 TPS 很低但 QPS 不低，两者结合能看出「是不是都堆在长事务里」。
3. **最后给边界**：把 `Com_insert/update/delete` 相加得到的是**写请求速率**，不是严格 TPS——很多团队的监控大盘把它标成 TPS，属于口径放宽，沟通时要先对齐定义。
**加分层**：判断写压力要看 TPS + `Innodb_row_lock_time_avg`（行锁等待），单独看 TPS 只能知道忙，不能知道卡不卡。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | TPS 全称 | 概念 | 每秒事务数 | 换题 |
| L2 | 用哪两个变量 | 基础 | Com_commit + Com_rollback | 判 P5 |
| L3 | 与 QPS 的关系 | 机制 | 一事务多语句 | 判 P6 |
| L4 | 只读事务算吗 | 边界 | 不计入 commit | 判 P6+ |
| L5 | 长事务怎么体现 | 实战 | TPS 低但 QPS 不低 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.6~8.0（验证 8.0.36） | 计数器语义无版本变化；8.0 可从 `performance_schema.global_status` 直接查 | 用 commit+rollback 口径，并说明团队口径差异 |

## 关键代码
```sql
-- 严格 TPS：10 秒窗口内 (commit+rollback) 增量 / 10
SELECT (SELECT VARIABLE_VALUE FROM performance_schema.global_status WHERE VARIABLE_NAME='Com_commit') +
       (SELECT VARIABLE_VALUE FROM performance_schema.global_status WHERE VARIABLE_NAME='Com_rollback') AS trx_total;
-- 对比：写请求速率（常被误标为 TPS）
SELECT SUM(CAST(VARIABLE_VALUE AS UNSIGNED)) AS write_stmts
FROM performance_schema.global_status
WHERE VARIABLE_NAME IN ('Com_insert','Com_update','Com_delete','Com_replace');
```

## ⚠️ 原文纠错
原文把 TPS 定义为「把 insert/update/delete 等语句计数器加起来再除以时间」——这实质是**写请求速率**，与社区通行的「`Com_commit + Com_rollback`」口径不一致；本卡按严格口径给出，并保留原文口径作为「常见但放宽的团队习惯」加以说明，避免面试时被追问口径而答不上。未发现其他技术错误。

## 总结与追问预判
- TPS 数事务，QPS 数语句；口径先对齐再谈数值。
- 下一题：见 126（QPS 计算）、128（并发数与连接数）。
