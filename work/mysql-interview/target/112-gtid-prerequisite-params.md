# 112 开启 GTID 复制需要哪些前置参数

> 分类：架构/复制 | 难度：L3 | 题型：工程题 | 频率：中 | 关键词：**gtid_mode** / **enforce_gtid_consistency** / **master_info_repository** / **TABLE**
> 原文锚点：第 171~180 段「要启动 GTID 模式，还要把……这个参数打开，如果是 5.7 之前的版本还要把 master_info 和 relay_log_info 放入表中」

## 一句话总述
开 GTID 不是只设 `gtid_mode=ON`：**binlog + server_id + enforce_gtid_consistency** 三件套，5.7 之前还要把 `master_info_repository` / `relay_log_info_repository` 改成 `TABLE`。

## 面试官视角
- **考察意图**：是不是只在 8.0 上开过 GTID，不知道老版本还要改存储方式（这正是升级面试的高频分水岭）。
- **P5** 能说出 `gtid_mode` 和 `enforce_gtid_consistency` / **P6** 能补上 5.7 之前的两个 repository 参数 / **P7** 会补「在线开启必须按 `OFF → OFF_PERMISSIVE → ON_PERMISSIVE → ON` 四步跳，不能一步到位」。
- **红旗**：「改配置重启一下就开了」；「`enforce_gtid_consistency` 可以不开」；「开了 GTID 就不需要 binlog」。
- **惊艳点**：`gtid_mode` 是**枚举不是布尔**，一步跳 ON 会被拒绝——必须逐级过渡，否则报错 —— 验证：`SET @@GLOBAL.GTID_MODE = ON;` 在 OFF 状态下会直接失败（8.0.36 `[经验]`）。

## 主问答
**Q：要把现有集群切成 GTID 复制，需要动哪些参数？能在线切吗？**
**A：**
1. **先给结论**：五个参数——`server_id`（唯一）、`log_bin`（开）、`gtid_mode=ON`、`enforce_gtid_consistency=ON`，5.7 之前再加 `master_info_repository=TABLE` + `relay_log_info_repository=TABLE`。
2. **再给机制**：`enforce_gtid_consistency` 禁止 `CREATE TABLE ... SELECT` 这类**无法原子记录成一个 GTID** 的语句，否则 GTID 分配会错乱；把两个 repository 放表是为了让复制元数据**崩溃安全**（配合 InnoDB），避免 relay log 位点与实际执行不一致。
3. **最后给边界**：在线切换要**逐级**改 `gtid_mode`，且**所有实例**都走完一级才能进下一级；期间不能让从库继续用旧的日志点拓扑混入。
**加分层**：从库配置改成 `MASTER_AUTO_POSITION=1` 之前，先确认两端 `gtid_mode` 都已是 ON，否则链路直接起不来。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 开 GTID 的核心参数 | 概念 | gtid_mode + enforce 一致性 | 换题 |
| L2 | 还依赖什么 | 基础 | binlog + server_id | 判 P5 |
| L3 | 5.7 之前多哪两个 | 版本感 | 两个 repository = TABLE | 判 P6 |
| L4 | 能一步切到 ON 吗 | 机制 | 不能，四步逐级 | 判 P6+ |
| L5 | 什么语句会被禁 | 实战 | CREATE TABLE AS SELECT 等 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.6 引入；5.7 支持在线开启；**8.0 起 repository 默认已是 TABLE**（验证 8.0.36） | 5.7.x 还需显式设 `master_info_repository=TABLE`；8.0 已默认，无需再配 | 5.7 讲五个参数，8.0 讲三个参数，说明版本差异 |

## 关键代码
```sql
-- 在线开启 GTID：必须逐级，不能一步到位
SET @@GLOBAL.GTID_MODE = OFF_PERMISSIVE;
SET @@GLOBAL.GTID_MODE = ON_PERMISSIVE;
SET @@GLOBAL.GTID_MODE = ON;
SET @@GLOBAL.ENFORCE_GTID_CONSISTENCY = ON;
-- 校验：确认已产生匿名事务为 0 才能安全切到 ON
SHOW STATUS LIKE 'Ongoing_anonymous_transaction_count';
```

## ⚠️ 原文纠错
原文表述为「5.7 之前的版本还要把 masterdinfo 和 relayloginput 放入表中」——实际是 **`master_info_repository=TABLE` 与 `relay_log_info_repository=TABLE`**，且官方建议从 **5.6 起**就该用表存储（5.7 更推荐），并非只在「5.7 之前」需要；已按官方演进重写。机翻「masterdinfo / relayloginput / CPIDmodel」还原为 **`master_info_repository` / `relay_log_info_repository` / `gtid_mode`**。

## 总结与追问预判
- 三个参数打底，老版本多两个 repository，切换必须逐级。
- 下一题：见 098（日志点 vs GTID 选型）、099（GTID 组成）。
