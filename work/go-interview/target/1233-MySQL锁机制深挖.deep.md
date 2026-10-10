# 1233 MySQL 锁机制深挖

> 原文锚点：第 1~118 段「MySQL 锁体系与各类锁」

## 一句话总述
在锁总览之上，深入行级锁四型（记录/间隙/临键/插入意向）、意向锁与 auto-inc 锁，并补页锁历史与 MDL 雪崩排查。

## 主问答
**Q（面试官原话）：** 行级锁具体有哪几种，意向锁干嘛用？
**A：**
1. **行级锁四型（InnoDB）**：① 记录锁（锁单行索引）；② 间隙锁（锁索引记录间间隙，防插入，RR 隔离级下）；③ 临键锁 next-key = 记录锁+间隙锁，锁定左开右闭区间；④ 插入意向锁（INSERT 时声明插入意向，互不冲突可并发插入）。
2. **意向锁（IS/IX）**：事务给行加 S/X 前，先对表加意向锁；作用是让"表级锁请求"快速判断表内是否已被行锁占用，避免逐行扫描。
3. **auto-inc 锁**：表级特殊锁，保证 `AUTO_INCREMENT` 自增列并发插入时值连续不重；`innodb_autoinc_lock_mode` 可调其粒度。
4. **页锁（历史）**：仅 BDB（BerkeleyDB）引擎支持，开销/并发介于表锁与行锁间；**BDB 引擎已在 MySQL 5.1 移除**，现代 MySQL 基本见不到了。
5. **MDL 雪崩排查**：`performance_schema.metadata_locks` 中 `LOCK_STATUS='PENDING'` 即为等待；优先 kill 持锁的长事务/慢查询。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 行锁有哪几种？ | 基础 | 记录/间隙/临键/插入意向 | P5 |
| L2 | 临键锁范围？ | 细节 | 记录+间隙，左开右闭 | P6 |
| L3 | 意向锁干嘛？ | 细节 | 表级快速判断行锁占用 | P7 |
| L4 | auto-inc 锁作用？ | 细节 | 保证自增列并发不重 | P7 |
| L5 | MDL 等待怎么查？ | 进阶 | metadata_locks 看 PENDING | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| MySQL 5.5+ | BDB 页锁 5.1 移除 | 行锁/意向锁/auto-inc 为 InnoDB 特性；next-key 在 RR 下默认启用 |

## 关键代码
```sql
-- 观察行锁/元数据锁等待
SELECT * FROM performance_schema.metadata_locks
WHERE LOCK_STATUS IN ('PENDING','GRANTED');
```

## 思路与架构
- 行级锁是一套"记录锁 + 间隙锁"的组合体系：记录锁锁索引项，间隙锁锁区间，next-key 二者合一防幻读；插入意向锁是 INSERT 的并发优化。
- 意向锁是表级"占位符"，让表锁请求不必逐行扫描即可判断行锁冲突，是 InnoDB 行锁与表锁共存的桥梁。

## 方案取舍
- 间隙锁/next-key 锁只在 **REPEATABLE READ** 下默认启用；若业务能接受 READ COMMITTED，可关间隙锁降锁冲突，但会失幻读防护。
- `innodb_autoinc_lock_mode`：高并发插入场景设为 2（交错）可提升吞吐，但 binlog 必须为 ROW 格式才能保证从库正确重放。

## 答题技巧

## 细节与核心 API

**行级锁四型（InnoDB，RR 下默认 next-key）**：

```text
记录锁      锁单个索引项
间隙锁      锁索引记录间间隙，防插入（仅 RR）
临键锁      记录锁+间隙锁，左开右闭 [a, b)
插入意向锁  INSERT 声明插入意向，互不冲突可并发插入
```

**意向锁 / auto-inc / MDL**：

```text
意向锁 IS/IX：对行加 S/X 前先对表加意向锁，让表锁请求快速判断行锁冲突（避免逐行扫）
auto-inc 锁 ：保证自增列并发不重；innodb_autoinc_lock_mode 调粒度
```

```sql
-- MDL 雪崩排查：LOCK_STATUS='PENDING' 即等待，优先 kill 持锁长事务
SELECT * FROM performance_schema.metadata_locks
 WHERE LOCK_STATUS IN ('PENDING','GRANTED');
-- 间隙/next-key 仅 RR 默认启用；RC 可关间隙降冲突（失幻读防护）
```

> 边界：隔离级别矩阵见 1230；MVCC 见 1231；加锁规则与排查见 1235；本卡只讲锁机制四型与体系。

1. 问"行锁有几种"——按"记录/间隙/临键/插入意向"四型答，顺带点 next-key=记录+间隙。
2. 问"意向锁干嘛"——强调"表级快速判断行锁占用，避免逐行扫"，这是面试加分点。
3. 问"为什么 DDL 卡住"——引到 MDL 雪崩：长事务持读锁挡 DDL，DDL 挡后续读。
4. 页锁主动说明"BDB 已废弃"，展示你区分历史与现实。

## 总结与追问预判
InnoDB 行锁以记录/间隙/临键/插入意向四型协同，意向锁加速表级判断，auto-inc 保自增；页锁随 BDB 退出历史，MDL 等待靠 metadata_locks 排查。

## ⚠️ 原文纠错
1. 事实核校： [经验] 行锁四型、意向锁作用、auto-inc 锁、MDL 雪崩排查路径，均正确；next-key=记录锁+间隙锁（左开右闭）正确。
2. **补正**：页锁的 BDB 引擎已在 MySQL 5.1 **移除**，原文"页锁在 BDB 支持"仅历史事实，现代版不常用。
3. 崩坏词归一：哔哩哔→BDB(BerkeleyDB)引擎、零件锁→临键锁(next-key)、航机锁→行级锁、度indb→InnoDB、解组→锁、事物→事务、协作→写锁、指印→代词、fieldreadonly/fialldread→(留作思考题,略)。
