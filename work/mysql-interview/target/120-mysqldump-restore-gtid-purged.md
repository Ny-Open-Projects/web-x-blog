# 120 用 dump 文件恢复时 GTID 报错怎么破

> 分类：备份恢复 | 难度：L3 | 题型：事故题 | 频率：中 | 关键词：**GTID_PURGED** / **--set-gtid-purged=OFF** / **RESET MASTER** / **gtid_executed 非空**
> 原文锚点：第 121~126 段「如果当时的 GTID 值不为空，是不能够使用 GTID 的……先把它设置为空，再来恢复」

## 一句话总述
带 GTID 的 dump 文件导入时报 `@@GLOBAL.GTID_PURGED cannot be changed`，根因是**目标实例 `gtid_executed` 非空**；两条路：备份时就用 `--set-gtid-purged=OFF`，或导入前 `RESET MASTER`。

## 面试官视角
- **考察意图**：见过这个报错没有——它是「从别人那拿了个 dump 想导进来」的必踩坑。
- **P5** 知道报错与 GTID 有关 / **P6** 能说出 `RESET MASTER` 或 `--set-gtid-purged=OFF` 两种解法 / **P7** 会补「解法二有前提：目标实例不能是从库、且必须确认它不再需要原有 GTID 历史」。
- **红旗**：「直接删掉文件里那行 SET 语句」；「`RESET MASTER` 随便敲」；「这是权限问题」。
- **惊艳点**：`RESET MASTER` 会**清空本机 binlog 与 `gtid_executed`**，在一个正在提供复制服务的实例上执行等于毁掉复制基线 —— 验证：`SELECT @@gtid_executed` 执行前后对比（8.0.36 `[经验]`）。

## 主问答
**Q：拿一个 dump 文件往库里导，报 GTID_PURGED 改不了，怎么回事？怎么解决？**
**A：**
1. **先给结论**：dump 文件头有 `SET @@GLOBAL.GTID_PURGED='...'`，而目标实例 `gtid_executed` **不为空**时，MySQL 拒绝设置，于是报错中断。
2. **再给机制**：`GTID_PURGED` 只能在 `gtid_executed` 为空时设置（两者互斥，官方限制），备份时若用 `--set-gtid-purged=ON`（GTID 模式下默认），文件里就会带这行。
3. **最后给边界**：两种解法——① 备份时加 `--set-gtid-purged=OFF`，文件里只留 `SET @@SESSION.SQL_LOG_BIN=0`，导进去不产生 GTID；② 导入前在目标实例执行 `RESET MASTER` 清空 GTID 历史。
**加分层**：解法②是**高危操作**，会清空 binlog 与 `gtid_executed`；只在新搭的、确认无复制关系的实例上用，从库或主库上绝对不能敲。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 报错关键字是什么 | 概念 | GTID_PURGED | 换题 |
| L2 | 根因是什么 | 基础 | gtid_executed 不为空 | 判 P5 |
| L3 | 怎么绕过 | 机制 | 关 purged 或 RESET MASTER | 判 P6 |
| L4 | RESET MASTER 的代价 | 边界 | 清 binlog 与 gtid 历史 | 判 P6+ |
| L5 | 什么时候用哪个 | 实战 | 新建实例用②，常态备份用① | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.6~8.0（验证 8.0.36） | 8.0.17 起 `RESET MASTER` 会同时清 `mysql.gtid_executed` 表；此前行为略有差异 | 统一按「清空 GTID 历史」理解，操作前先确认实例角色 |

## 关键代码
```bash
# 解法一（推荐）：备份时就不写 GTID_PURGED
mysqldump --single-transaction --set-gtid-purged=OFF db1 > db1.sql
```
```sql
-- 解法二：导入前清空本机 GTID 历史（高危，仅限无复制关系的新实例）
SELECT @@gtid_executed;   -- 先确认确实要清
RESET MASTER;
```

## ⚠️ 原文纠错
原文只说「把 GTID 值置为空再恢复」，**未点明两条更安全/更常用的路径**（`--set-gtid-purged=OFF` 与 `RESET MASTER` 的取舍），也未提示 `RESET MASTER` 会一并清空 binlog 的高危性；已补全并加风险提示。机翻「GTD / GTIDprog」统一还原为 **GTID**。未发现其他技术错误。

## 总结与追问预判
- 报错根因是 `gtid_executed` 非空；优先改备份参数，别动 `RESET MASTER`。
- 下一题：见 112（GTID 前置参数）、124（binlog 增量恢复）。
