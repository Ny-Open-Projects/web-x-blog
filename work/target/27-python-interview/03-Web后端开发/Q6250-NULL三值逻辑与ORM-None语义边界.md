---
title: "[Q6250] NULL 的三值逻辑：SQL UNKNOWN 与 ORM None 的语义边界"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6250 · NULL 的三值逻辑：SQL UNKNOWN 与 ORM None 的语义边界

难度：P6 ｜ 标签：NULL、三值逻辑、UNKNOWN、IS NULL、count 语义、NOT IN 陷阱、COALESCE、ORM None、聚合函数

**问**：SQL 的 NULL 与 Python 的 None 差在哪——为什么 `WHERE score != 90` 会把 score 为 NULL 的行"悄悄"滤掉？`count(*)` 与 `count(col)` 差异、NOT IN 子查询遇 NULL 为什么返回空集？聚合函数（SUM/AVG）对 NULL 的处理与业务语义陷阱？"没有值"和"值为 0"在设计上怎么区分（ORM 默认值/DEFAULT 0/允许 NULL 的选型）？

**答**：
结论：NULL 在 SQL 里是**未知（UNKNOWN）**而非"空值"——三值逻辑（TRUE/FALSE/UNKNOWN）的核心规则：**任何与 NULL 的比较结果都是 UNKNOWN**（`NULL != 90` 是 UNKNOWN、`NULL = NULL` 也是 UNKNOWN），而 WHERE 只保留 TRUE 的行——所以 `WHERE score != 90` 悄悄丢掉所有 score IS NULL 的行（UNKNOWN 不满足"TRUE"），这不是 bug 是三值语义，是"过滤条件漏数据"的头号来源；判空必须显式 `IS NULL / IS NOT NULL`（COALESCE/IFNULL 把 NULL 折算成业务默认值是第二常用工具）。三组高频差异：①**count**：`count(*)` 数行数（含 NULL 行）、`count(col)` 数 col 非 NULL 的行数——"订单总数"与"有评分的订单数"一字之差语义全变；②**NOT IN 子查询**：`WHERE id NOT IN (SELECT score FROM t)` 当子查询结果含 NULL 时——`id != NULL` 是 UNKNOWN，任何 id 都无法为 TRUE，**整条查询返回空集**（经典事故形态：子查询某行变 NULL，报表从有数据变零数据）；正解 `NOT EXISTS` 或子查询过滤 NULL；③**聚合**：SUM/AVG/MAX 忽略 NULL（AVG = SUM(非NULL)/COUNT(非NULL)——"平均分"的分母悄悄变小），SUM 空集返回 NULL 而非 0（Python 侧拿到 None 做 `None + 1` 直接 TypeError）——聚合语义要显式 COALESCE。**设计层**：列"允许 NULL"是 schema 决策不是默认——NULL 与 0/空串语义不同（"未评分"vs"0 分"、"未填地址"vs"空地址"），混用会污染统计（AVG 把 0 分算进分母）；ORM 侧 Django/SQLAlchemy 的 None 与 NULL 一一映射，但 **Python 侧的 None 蔓延**（查询结果 None 流入业务代码）要在序列化层收口（DTO 默认值/字段 optional 标注），"NULL 允许但业务层必须收敛"。

取舍：a) schema 选型矩阵：状态/金额类关键列 NOT NULL + DEFAULT（查询永不踩 UNKNOWN），可选信息列允许 NULL（语义真实）；**DEFAULT 0 vs NULL 的选择**看"缺省值是否合法业务值"——0 分是合法值就 NOT NULL DEFAULT 0，0 不是合法值才 NULL；b) ORM 默认值的层次：DB DEFAULT（数据库层兜底）、ORM 层 default（insert 时填充）、应用层初始化——三层不一致时"插入路径不同默认值不同"，选一层为主（通常 ORM default）+ DB DEFAULT 兜底；c) 唯一索引与 NULL：多数 DB 里 NULL 行不参与唯一约束（NULL != NULL，多个 NULL 可共存）——"可选唯一字段"（可空手机号）恰好利用此语义，但要明白"多个 NULL 不冲突"是特性不是 bug；d) 查询规范：所有比较条件显式考虑 NULL 分支（code review 清单项），聚合查询的 count 口径写进指标定义（Q2200 的指标口径纪律）；e) Python 侧防线：查询结果的 None 在 DAO 层收敛（`row.score or 0` 的语义陷阱——0 会被 `or` 吞掉！必须 `0 if row.score is None else row.score`），`or` 链的 None 处理是 Python 侧第二事故源。

实战：事故形态是"风控报表的'异常订单数'用 `WHERE amount != 0` 统计——历史数据迁移时 amount 为 NULL 的行全部漏算，报表长期少 12%；另一个是 `NOT IN (SELECT parent_id ...)` 子查询出现 NULL 后整报表空窗 2 小时。修复：统计口径显式 `IS NULL` 分支 + NOT IN 全改 NOT EXISTS + 聚合层 COALESCE 收口 + 指标定义文档写明 NULL 口径；ORM 查询结果的 None 在 DTO 层统一默认值"。下面用 sqlite3 实测三值逻辑、count 口径与 NOT IN 陷阱。

```python
# NULL 三值逻辑: UNKNOWN 过滤、count 口径与 NOT IN 陷阱
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE t_order (id INTEGER PRIMARY KEY, amount REAL, score REAL)")
conn.executemany("INSERT INTO t_order VALUES (?,?,?)",
                 [(1, 100.0, 90), (2, 200.0, None), (3, 300.0, 80), (4, 0.0, None)])

print("[1] 三值逻辑: NULL 与任何值比较都是 UNKNOWN, WHERE 只留 TRUE")
print("    score != 90 的行:", conn.execute("SELECT id FROM t_order WHERE score != 90").fetchall(),
      "(id=2/4 的 NULL 行被悄悄滤掉!)")
print("    显式判空版本:", conn.execute(
    "SELECT id FROM t_order WHERE score != 90 OR score IS NULL").fetchall())

print("[2] count(*) 与 count(col): 行数 vs 非空数, 指标口径一字之差")
print("    count(*):", conn.execute("SELECT count(*) FROM t_order").fetchone()[0],
      "| count(score):", conn.execute("SELECT count(score) FROM t_order").fetchone()[0],
      "(NULL 不计)")

print("[3] NOT IN 子查询遇 NULL: 整条查询返回空集 (经典事故)")
conn.execute("CREATE TABLE t_block (pid INTEGER)")
conn.execute("INSERT INTO t_block VALUES (1)")
print("    子查询含 NULL 的 NOT IN:", conn.execute(
    "SELECT id FROM t_order WHERE id NOT IN (SELECT score FROM t_order)").fetchall(), "<- 空!")
print("    NOT EXISTS 等价写法:", conn.execute(
    "SELECT id FROM t_order o WHERE NOT EXISTS "
    "(SELECT 1 FROM t_order t2 WHERE t2.score = o.id)").fetchall(), "(按需过滤 NULL 后语义清晰)")

print("[4] 聚合函数: 忽略 NULL, AVG 分母悄悄变小; SUM 空集返回 NULL")
print("    AVG(score) =", conn.execute("SELECT avg(score) FROM t_order").fetchone()[0],
      "=(90+80)/2, 分母 2 不是 4!")
print("    SUM(空集) =", conn.execute("SELECT sum(score) FROM t_order WHERE score > 999").fetchone()[0],
      "(None! Python 侧 None+1 直接 TypeError)")
print("    COALESCE 收口:", conn.execute(
    "SELECT coalesce(sum(score), 0) FROM t_order WHERE score > 999").fetchone()[0])

print("[5] Python 侧 None 收敛: or 链会吞 0, 必须 is None 显式判断")
score = 0
bad = score or 10                    # or 链: 0 被当成假!
good = 10 if score is None else score
print(f"    score=0 时: score or 10 -> {bad} (0 被吞!) | is None 判断 -> {good}")

print("[6] 设计纪律: 关键列 NOT NULL+DEFAULT, 可选列才允许 NULL; NULL 与 0 语义分开")
print("[rule ] 三值逻辑下任何 NULL 比较都是 UNKNOWN; 判空必 IS NULL; NOT IN 遇 NULL 返回空集; 聚合分母注意")
```

**追问一**："NULL 允许" vs "NOT NULL + DEFAULT 哨兵值"的选型怎么定？哨兵值方案（如 amount=-1 表示无效）的历史包袱是什么？—— 决策矩阵：①**缺省值是合法业务值** → NOT NULL + DEFAULT（如状态列 default 'active'、数量 default 0）——查询永不踩 UNKNOWN，统计口径干净；②**"没有值"本身是真实业务状态且不可与其他值混淆** → 允许 NULL（"未评分"≠0 分、"暂无上级"≠某个具体人）——代价是所有查询要显式处理 NULL 分支；③**哨兵值方案**（-1/空串/'N/A' 表示缺失）——历史的被迫选择（老 DB/ETL 管道），包袱：哨兵值**参与聚合与唯一约束**（-1 混进 AVG、多个 'N/A' 撞唯一索引）、类型系统失去表达力、应用层到处是哨兵判断——除非历史包袱已存在，新 schema 一律 NULL 或 NOT NULL+合法默认，不引入哨兵。灰色地带的处理："可空但高频判空"的列可以 NOT NULL + DEFAULT + 附加"是否已填"布尔列（显式表达缺失状态）——把 NULL 的语义压进类型系统，查询成本换来统计清晰。原则：**NULL 的代价是所有下游查询的心智负担**——能不 NULL 就不 NULL，真 NULL 就全链路显式处理。

**追问二**：ORM 层对 NULL 的处理有哪些"看起来对但语义错"的写法？Django/SQLAlchemy 的 None 查询陷阱与序列化层收口怎么落地？—— 典型错误写法：①**`filter(score=None)` 的语义**——Django 里 `filter(score=None)` 等价 `score IS NULL`（正确），但 `exclude(score=None)` 排除 NULL 行后，**非 NULL 但等于条件的行保留**——与三值逻辑直觉不同；SQLAlchemy 的 `filter(User.score == None)` 是 IS NULL（`is_(None)` 更显式），但 `filter(User.score != 90)` 同样悄悄丢 NULL 行（与裸 SQL 一致）——**ORM 不会替你补 IS NULL 分支**，它忠实翻译 SQL 语义；②**`or_` 链的 Python 陷阱**——查询结果的 None 用 `or` 收敛吞 0（本卡 [5]）；③**聚合结果 None 流入**——`sum()` 返回 None 直接参与运算 TypeError；④**对象属性 None 蔓延**——可空字段 None 穿过三层函数后在模板/序列化层炸。收口落点：**DAO/序列化层统一**——DTO 的 optional 字段显式标注默认值（Pydantic 的 `Optional[int] = 0` 或 None 明确区分"缺失"与"零"，Q098 的模型契约）、DAO 返回前对"业务上不可为 None"的字段断言（fail-fast 而非延迟炸）、指标类聚合全部 COALESCE 到业务零值。规范形态："NULL 策略"是 schema 文档的一部分——每张表标注哪些列允许 NULL、NULL 的业务含义、下游消费契约，把三值逻辑的心智负担从"每次写查询现想"变成"设计期一次性定义"。

## 背诵要点
- 三值逻辑核心：NULL 与任何值（含 NULL 自己）比较都是 UNKNOWN，WHERE 只留 TRUE——`!= x` 悄悄滤掉 NULL 行；判空必须 IS NULL/IS NOT NULL，COALESCE 折算默认值。
- 三组高频差异：count(*) 含 NULL 行 vs count(col) 只数非空；NOT IN 子查询含 NULL → 整查询返回空集（正解 NOT EXISTS）；SUM/AVG 忽略 NULL（AVG 分母变小）、SUM 空集返回 None。
- 设计纪律：缺省是合法值 → NOT NULL+DEFAULT，"没有值"是真实状态才 NULL，不引入哨兵值；Python 侧 None 收敛在 DAO/DTO 层，`or` 链会吞 0 必须 `is None` 判断。

## 复盘追问
- 为什么 WHERE amount != 0 会少算数据、NOT IN 报表空窗怎么发生的？（NULL 比较是 UNKNOWN 不满足 TRUE；NOT IN 子查询出现 NULL 后所有行 UNKNOWN → 空集，改 NOT EXISTS + 口径显式 IS NULL）
- "未评分"和"0 分"为什么必须分开、Python 侧怎么收敛 None？（NULL=未知、0=合法值，混用污染 AVG 分母与统计；关键列 NOT NULL+DEFAULT，None 在 DAO/DTO 层显式默认，禁用 or 链收敛）
