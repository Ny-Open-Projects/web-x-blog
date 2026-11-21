"""schema 漂移检测: 实际结构与声明的对账"""
import sqlite3

EXPECTED = {
    "orders": {
        "columns": {"id": "INTEGER", "user_id": "INTEGER", "amount": "INTEGER"},
        "indexes": {"idx_orders_user": (["user_id"], False)},
    },
    "users": {
        "columns": {"id": "INTEGER", "name": "TEXT"},
        "indexes": {"uq_users_name": (["name"], True)},
    },
}

def actual_schema(c):
    out = {}
    tables = [r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")]
    for t in tables:
        cols = {r[1]: r[2].upper() for r in c.execute("PRAGMA table_info(%s)" % t)}
        idxs = {}
        for name, unique in c.execute("SELECT name, [unique] FROM pragma_index_list(?)", (t,)):
            if name.startswith("sqlite_autoindex"):
                continue
            cols_in_idx = [r[0] for r in c.execute(
                "SELECT name FROM pragma_index_info(?)", (name,))]
            idxs[name] = (cols_in_idx, bool(unique))
        out[t] = {"columns": cols, "indexes": idxs}
    return out

def drift_report(c, expected):
    actual = actual_schema(c)
    problems = []
    for t, spec in expected.items():
        if t not in actual:
            problems.append("缺失表 %s" % t)
            continue
        for col, typ in spec["columns"].items():
            if col not in actual[t]["columns"]:
                problems.append("%s 缺列 %s" % (t, col))
            elif actual[t]["columns"][col] != typ.upper():
                problems.append("%s.%s 类型漂移: 声明 %s 实际 %s"
                                % (t, col, typ, actual[t]["columns"][col]))
        for idx, (cols, uniq) in spec["indexes"].items():
            if idx not in actual[t]["indexes"]:
                problems.append("%s 缺索引 %s" % (t, idx))
            elif actual[t]["indexes"][idx] != (cols, uniq):
                problems.append("%s 索引 %s 定义漂移: 声明 %s 实际 %s"
                                % (t, idx, (cols, uniq), actual[t]["indexes"][idx]))
    for t in actual:
        if t not in expected:
            problems.append("多出表 %s (未登记的手工对象)" % t)
    return problems

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, amount TEXT)")
c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
c.execute("CREATE UNIQUE INDEX uq_users_name ON users(name)")
c.execute("CREATE TABLE hack_tmp (x INTEGER)")       # 有人手工建的对象
# 漏建 idx_orders_user, amount 类型声明成了 TEXT

problems = drift_report(c, EXPECTED)
print("漂移检测结果: %d 处" % len(problems))
for p in problems:
    print("  - %s" % p)
print("结论: schema 的事实标准是 sqlite_master/PRAGMA, 不是文档;")
print("      把声明放配置里, 上线前跑一次对账, 手工 DDL 在漂移报告里无处藏身")
