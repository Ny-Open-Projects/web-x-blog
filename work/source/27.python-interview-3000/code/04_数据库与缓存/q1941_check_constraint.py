"""CHECK 约束兜底: 应用层校验失守后的数据库防线"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE orders(
    id INTEGER PRIMARY KEY,
    amount INTEGER NOT NULL CHECK (amount > 0),
    status TEXT NOT NULL CHECK (status IN ('created', 'paid', 'void')),
    CHECK (status <> 'paid' OR amount > 0)
)""")

def try_insert(label, args):
    try:
        conn.execute("INSERT INTO orders(amount, status) VALUES(?,?)", args)
        print(f"{label} -> 写入成功")
    except sqlite3.IntegrityError as e:
        print(f"{label} -> 被数据库拒绝: {e}")

try_insert("合法行", (100, "paid"))
try_insert("负金额", (-5, "paid"))
try_insert("非法状态", (10, "shipped"))
try_insert("零金额 created", (0, "created"))
print("库内行数 ->", conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0], " 坏数据全部被挡")

# CHECK 对 UNKNOWN 放行: NULL 不违反 CHECK 但会撞上 NOT NULL
try_insert("amount 为 NULL", (None, "created"))
conn.execute("CREATE TABLE t(x INTEGER CHECK (x > 0))")
try:
    conn.execute("INSERT INTO t VALUES(NULL)")
    print("纯 CHECK 列写 NULL -> 成功: UNKNOWN 不是 FALSE CHECK 放行 要挡 NULL 必须加 NOT NULL")
except sqlite3.IntegrityError:
    print("纯 CHECK 列写 NULL -> 被拒")
print("结论: 应用层校验会被脚本 直连 绕过 CHECK 是最后防线 且必须与 NOT NULL 配套覆盖 NULL 通道")
