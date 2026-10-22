# 073 binlog_row_image 怎么给 ROW 日志瘦身

> 分类：日志类 | 难度：L3 | 题型：工程题 | 频率：中 | 关键词：**binlog_row_image** / **FULL** / **MINIMAL** / **NOBLOB**
> 原文锚点：第 366~372 段「默认情况下呢，右格式在二进制日志中呀，会记录每一行数据所有列修改前和修改后的这个值…如果我们只记录被修改的列的值的话，是不是就可以大幅减小这个二进制日志的文件体积了」

## 一句话总述
ROW 格式默认（`FULL`）记**全列前后镜像**；`binlog_row_image=MINIMAL` 只记**定位行所需列（通常主键）+ 被改动列**，日志体积可大幅下降；`NOBLOB` 是折中。

## 面试官视角
- **考察意图**：你是否知道 ROW 日志"大"是可以调的，而不是只会认命扩容磁盘。
- **P5** 知道有这个参数 / **P6** 能说清 FULL 与 MINIMAL 的差别 / **P7** 能指出 MINIMAL 的前提是**表必须有主键**且要评估数据恢复/闪回工具的兼容性。
- **红旗**：① 说 MINIMAL 会让从库丢数据；② 不知需要主键；③ 认为参数改完全局就对当前会话生效。
- **惊艳点**：MINIMAL 下**前镜像只留主键**——没主键的表匹配成本反而更高 `[源码]`。验证：无主键表改一行看 `mysqlbinlog -vv`。

## 主问答
**Q（面试官原话）：** ROW 格式日志太大了，你们怎么压？

**A：**
1. **先给结论**：调 `binlog_row_image`，生产常用 `MINIMAL`，日志体积可显著下降（宽表改单列尤其明显）。
2. **再给机制**：`FULL` 记所有列的 before/after 值，即使这列没被改；`MINIMAL` 的 before 只记**能唯一定位该行的列（主键/唯一键）**，after 只记**真正被修改的列**；`NOBLOB` 等同 FULL，但省略**未被修改的** BLOB/TEXT 列。
3. **最后给边界**：MINIMAL 强依赖主键——表没主键时无从定位行，收益归零甚至更差；另外它是**动态参数**，`SET GLOBAL` 只影响**新连接**，当前会话要 `SET SESSION`（或重连）才生效，这点演示里也踩过。

**加分层**：MINIMAL 会削弱依赖完整前镜像的能力（如部分**闪回工具**），上线前要确认工具链支持。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | ROW 日志能瘦身吗 | 参数存在性 | binlog_row_image | 换题 → 不及格 |
| L2 | 三个取值什么区别 | 机制 | FULL/MINIMAL/NOBLOB | 判 P5 |
| L3 | MINIMAL 记什么 | 细节 | 前镜像主键、后镜像改动列 | 判 P6 |
| L4 | 什么时候不生效 | 边界 | 无主键表、闪回工具依赖 | 判 P6+ |
| L5 | 改了全局为何没变 | 作用域 | GLOBAL 不影响当前 session | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 变化点 | 现在该怎么答 |
|---|---|---|
| 5.6+ | 引入 binlog_row_image | 默认 FULL |
| 5.7 / 8.0 | 取值沿用 | "宽表批量更新建议 MINIMAL" |
| 全版本 | 仅对 ROW/MIXED 生效 | STATEMENT 下无意义 |

## 关键代码
```sql
SHOW VARIABLES LIKE 'binlog_row_image';        -- 默认 FULL
SET GLOBAL binlog_row_image = 'MINIMAL';       -- 动态；只对新连接生效
SET SESSION binlog_row_image = 'MINIMAL';      -- 当前会话同步改，否则要重连
UPDATE stock SET stock_count = 30 WHERE product_id = 2030 AND warehouse_id = 1;
```

```bash
# 对比 FULL 与 MINIMAL 的行镜像差异（需 ROW 格式）
mysqlbinlog -vv /data/mysqllog/mysql-bin.000004 | sed -n '1,80p'
```

## ⚠️ 原文纠错
原文机翻「noblog」= **NOBLOB**，且只说"记录除 blog 类列之外的列"，表述不完整：NOBLOB 是 **FULL 减去未被修改的 BLOB/TEXT 列**，被修改的大字段仍会记录。原文称 MINIMAL"只记录修改后的列、修改前的库存列也没记录，用主键 ID 标识"与实现一致，结论正确。核对范围：第 366~392 段演示过程。

## 总结与追问预判
- ROW 的"大"是可控的：**MINIMAL = 主键定位 + 改动列**，前提是有主键。
- 动态参数但**会话级需单独设置**。
- 下一题：见 074（ROW 下如何看到原始 SQL）、059（binlog_cache_size）。
