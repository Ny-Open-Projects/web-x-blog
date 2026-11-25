---
title: "[Q6818] sqlite3 类型适配器与 row_factory：DB 层的类型契约"
date: 2026-11-25
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6818 · sqlite3 类型适配器与 row_factory：DB 层的类型契约

难度：P6 ｜ 标签：sqlite3、类型适配器、converter、detect_types、row_factory、类型契约

基线：Python 3.12 / SQLite 3.45；用自定义 Money 类型与 JSON 列实测 adapter/converter/Row 三件套，全标准库实跑。

**问**：用 sqlite3 存金额，读出来全是字符串和浮点，Python 层到处 `float(row[3])` 转换；`SELECT` 列顺序一变，`row[2]` 全取错位。sqlite3 的 `register_adapter`、`register_converter`、`detect_types`、`row_factory` 到底各管什么？为什么说"类型契约要声明在 DB 连接层，而不是散落在业务代码里"？

**答**：

- **结论**：sqlite3 默认只认识 None/int/float/str/bytes，其他 Python 类型入库会报错或被降级成文本，读侧更不会"还原"成原类型——没有类型契约的 DB 代码必然长满散落转换。sqlite3 提供的三件套就是契约声明：① **adapter（写侧）**：`register_adapter(T, fn)` 把自定义类型编码成 DB 可存的文本/数值；② **converter（读侧）**：`register_converter("TYPENAME", fn)` + 连接参数 `detect_types=PARSE_DECLTYPES`，按**建表时声明的列类型**自动调用 fn 还原成 Python 对象——不开 detect_types 时 converter 永远不触发，读回来全是裸 str/bytes（实测可证）；③ **row_factory**：`sqlite3.Row` 让结果按列名访问（`r["user_id"]`），替代脆弱的下标位次。converter 收到的可能是 bytes，函数里要做 `decode()`。
- **取舍**：类型契约放连接层的收益是"写一次、全局生效、SQL 无法绕过"；代价是隐式转换（debug 时要意识到读出的对象是 converter 造的）与厂商锁定（这套 API 是 sqlite3 专属，PG 用 psycopg 适配器、MySQL 用 connector 的 converter 机制，思路相通但 API 不同——所以团队规范应沉淀为统一的"列类型 ↔ Python 类型"映射表，各驱动各自实现）。另一个取舍是 JSON 列：用 adapter/converter 做自动 dumps/loads 很方便，但**查询侧就失去了 JSON 函数能力**（SQL 里 `json_extract` 处理的是文本，而 Python 层拿到的是 dict——两边约定要写清）；金额这类精度敏感值绝不用 float adapter，用"分 + 货币"的自定义类型。
- **实战**：一个报表工具早期版本靠 `int(row[3])`、`json.loads(row[5])` 散落转换，一次 SQL 调整列顺序（为了加一列）改坏了 7 处下标引用，返工两天。重构：所有连接统一工厂函数创建——挂 Row 工厂、注册 Money 与 JSON converter、声明 `detect_types`；禁止业务代码出现 `row[n]` 数字下标（lint 规则）与裸 `float(` 金额转换；列类型映射表进 README。重构后同类 bug 归零，且新增一种自定义类型只改工厂一处。教训：**类型契约是基础设施，不是业务代码的随手转换**。

下面实测 adapter/converter/Row 三件套的完整行为。

```python
# Q6818 sqlite3 类型适配器与 row_factory: DB 层的类型契约
import sqlite3, json

# [1] 自定义类型 ↔ DB 文本: adapter(入库) / converter(出库)
class Money:
    def __init__(self, cents, currency="CNY"):
        self.cents, self.currency = cents, currency
    def __repr__(self):
        return f"Money({self.cents/100:.2f}{self.currency})"

def money_to_db(m):        # Money → TEXT "1200|CNY"
    return f"{m.cents}|{m.currency}"

def money_from_db(s):      # TEXT → Money (converter 收到的可能是 bytes)
    if isinstance(s, bytes):
        s = s.decode()
    cents, cur = s.split("|")
    return Money(int(cents), cur)

sqlite3.register_adapter(Money, money_to_db)
sqlite3.register_converter("MONEY", money_from_db)

conn = sqlite3.connect(":memory:",
                       detect_types=sqlite3.PARSE_DECLTYPES)   # 按 declared type 触发 converter
conn.execute("CREATE TABLE acct(id INTEGER PRIMARY KEY, balance MONEY)")
conn.execute("INSERT INTO acct VALUES(1, ?)", (Money(12345),))
row = conn.execute("SELECT balance FROM acct WHERE id=1").fetchone()
print(f"[1] 自定义适配器: 存入 Money(123.45CNY) → 读回 {row[0]!r}, 类型 {type(row[0]).__name__}")
assert isinstance(row[0], Money) and row[0].cents == 12345

# [2] row_factory=sqlite3.Row: 命名列访问 + 不再是裸元组
conn.row_factory = sqlite3.Row
conn.execute("CREATE TABLE orders(id INTEGER, user_id INTEGER, amount MONEY)")
conn.execute("INSERT INTO orders VALUES(1, 7, ?)", (Money(9900),))
r = conn.execute("SELECT id, user_id, amount FROM orders").fetchone()
print(f"[2] Row 工厂: r['user_id']={r['user_id']}, keys={r.keys()}")
assert r["user_id"] == 7 and "amount" in r.keys()
print("    → 按名取值代替脆弱的下标; SELECT 列顺序变更不再毁掉代码")

# [3] JSON 列的自动解码: converter 出库自动 loads, 写侧仍需显式 dumps
sqlite3.register_adapter(dict, lambda o: json.dumps(o, ensure_ascii=False))
def js_from_db(s):
    if isinstance(s, bytes):
        s = s.decode()
    return json.loads(s)
sqlite3.register_converter("JSONCOL", js_from_db)
conn2 = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
conn2.execute("CREATE TABLE kv(k TEXT, v JSONCOL)")
conn2.execute("INSERT INTO kv VALUES(?, ?)", ("cfg", {"timeout": 30, "tags": ["a"]}))
back = conn2.execute("SELECT v FROM kv").fetchone()[0]
print(f"[3] JSON 列双向契约: {back!r}, 类型 {type(back).__name__}")
assert isinstance(back, dict) and back["timeout"] == 30

# [4] 无 detect_types 时: 一切是 str/bytes, 类型契约由应用层自担
conn3 = sqlite3.connect(":memory:")
conn3.execute("CREATE TABLE t(x MONEY)")
conn3.execute("INSERT INTO t VALUES(?)", (Money(500),))
raw = conn3.execute("SELECT x FROM t").fetchone()[0]
print(f"[4] 不开 detect_types: 读回 {raw!r} (裸文本), converter 未触发")
assert isinstance(raw, str)
print("    → 实测 类型契约三件套: adapter(写) + converter+detect_types(读) + Row(按名访问); 不声明就全是文本")
```

**追问一**：Python 3.12 为什么废弃了 datetime 的默认适配器？这对存量代码意味着什么？—— 旧版 sqlite3 内置的 date/datetime 默认适配器用 `str()` 序列化，精度与时区语义都不受控（naive/aware 混存），Python 3.12 起 DeprecationWarning，要求显式 `register_adapter` 自己的格式（ISO 8601 + 明确时区策略）。存量代码的迁移要点：全库扫描 datetime 的存取路径，统一序列化格式（ISO 8601 微秒、UTC 存储），注册自定义 adapter/converter，并在 CI 里加 DeprecationWarning-as-error 防止新代码继续依赖默认行为。这件事的深层教训是：**隐式类型魔法被标准化收回时，自己声明契约的团队不受影响**。

**追问二**：detect_types 有两种取值（PARSE_DECLTYPES / PARSE_COLNAMES），有什么区别？—— PARSE_DECLTYPES 按建表语句的列类型（`balance MONEY`）匹配 converter，适合"类型是列的固有属性"的场景；PARSE_COLNAMES 按 SQL 别名（`SELECT x AS "m [money]"`）匹配，适合同一列在不同查询里想要不同类型（或表结构不可改、只能查询侧声明）。可以按位或叠加。工程上建议只用 DECLTYPES：类型跟列走、声明一次处处生效；COLNAMES 把类型信息散进 SQL 字符串，等于把契约又放回了业务代码——与"契约进连接层"的原则相悖。

## 背诵要点

- 三件套：`register_adapter`（写侧编码）+ `register_converter` + `detect_types`（读侧还原）+ `sqlite3.Row`（按名访问）；不开 detect_types 读回全是裸文本。
- converter 收到可能是 bytes，函数内先 decode；datetime 默认适配器 3.12 已废弃，时区/精度契约要自己注册。
- 类型契约声明在连接工厂一处生效，禁止业务代码散落转换与数字下标；金额用"分+货币"自定义类型，禁 float。

## 复盘追问

- 一次 SQL 加列导致 7 处下标引用错位，除了 row_factory 还要补什么流程？（连接工厂统一出口 + lint 禁 `row[n]`；SQL 变更走契约评审，列类型映射表随表结构演进）
- JSON 列做了自动 loads 后，SQL 里的 json_extract 还能用吗？两边怎么约定？（能用但语义分叉：SQL 侧是文本函数、Python 侧是 dict；约定 JSON 函数只在 SQL 聚合/过滤用，Python 层只做业务对象操作，写侧统一走 adapter）
