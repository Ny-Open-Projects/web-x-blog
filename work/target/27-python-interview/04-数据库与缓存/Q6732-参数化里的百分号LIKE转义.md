---
title: "[Q6732] 参数化里的百分号：LIKE 模糊查询为什么变成 ValueError"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6732 · 参数化里的百分号：LIKE 模糊查询为什么变成 ValueError

难度：P6 ｜ 标签：psycopg、DB-API、paramstyle、LIKE、SQL 注入边界

基线：Python 3.12；psycopg2/psycopg3 的 `pyformat` 占位符；纯 Python 模拟驱动的 `%` 扫描。

**问**：`cur.execute("SELECT * FROM t WHERE name LIKE '%李%'")` 直接写没问题。改成参数化写成 `cur.execute("... WHERE name LIKE '%%s%'", (kw,))`，要么报 `ValueError: unsupported format character`，要么 `IndexError: tuple index out of range`，要么查不到数据。我只是想拼一个模糊查询，`%` 到底怎么被解析的？

**答**：
- **结论**：DB-API 的 `pyformat` 风格用 `%` 做标记扫描：`%s` 是占位符，`%%` 是字面量 `%`，**其余 `%x` 一律非法**。`'%%s%'` 会被解析成"字面 `%` + 字母 `s` + 悬空 `%`"，最后一个 `%` 后没有合法字符 → `ValueError`；如果驱动宽容地跳过，参数就会错位 → `IndexError`。正确写法只有两种：`LIKE %s` 且把通配符放进参数值（`f"%{kw}%"`），或 `LIKE '%%' || %s || '%%'`（`%%` 转义成字面 `%`）。
- **取舍**：把通配符放进参数值最简单，但**必须转义用户输入里的 `%`、`_`、`\`**，否则用户搜 `50%` 会变成"以 50 开头"、搜 `a_b` 会匹配 `axb`——既是语义错误，也是慢查询来源（`%...%` 无法走 B 树索引）。SQL 侧用 `'%' || %s || '%'` 把字面通配符和值分开，可读性好一点，但索引照样失效。
- **实战**：① 封装 `like_escape(s)` 统一处理三个特殊字符，并显式写 `ESCAPE '\'`；② 前缀匹配用 `kw + '%'` 才能走索引（PG 需要 `text_pattern_ops`，MySQL 需要合适的排序规则）；③ `EXPLAIN` 确认没有因为 `%...%` 变成全表扫；④ 测试用例覆盖 `%`、`_`、`\`、中英混排四个输入。

```python
"""模仿 psycopg 的 pyformat 扫描：%s 占位、%% 字面、其他 %x 报错。"""


def bind(sql: str, params: tuple[object, ...]) -> str:
    out: list[str] = []
    idx = 0
    i = 0
    while i < len(sql):
        ch = sql[i]
        if ch != "%":
            out.append(ch)
            i += 1
            continue
        nxt = sql[i + 1] if i + 1 < len(sql) else ""
        if nxt == "%":
            out.append("%")
            i += 2
        elif nxt == "s":
            if idx >= len(params):
                raise IndexError("not enough arguments for format string")
            out.append(str(params[idx]))
            idx += 1
            i += 2
        else:
            raise ValueError(f"unsupported format character {nxt!r} at index {i + 1}")
    if idx != len(params):
        raise TypeError("not all arguments converted during string formatting")
    return "".join(out)


def like_escape(value: str, escape: str = "\\") -> str:
    """把用户输入里的通配符转成字面量，必须配合 ESCAPE '\\' 使用。"""
    for ch in (escape, "%", "_"):
        value = value.replace(ch, escape + ch)
    return value


if __name__ == "__main__":
    # 1) 正确：字面 % 用 %% 转义，值走占位符
    print("ok  :", bind("... WHERE name LIKE '%%%s%%'", ("李",)))

    # 2) 错误：'%%s%' 里 %% 吃掉两个字符，剩下裸 % 非法
    try:
        bind("... WHERE name LIKE '%%s%'", ("李",))
    except ValueError as e:
        print("bad :", e)

    # 3) 参数错位
    try:
        bind("... WHERE a = %s AND b = %s", ("x",))
    except IndexError as e:
        print("bad :", e)

    # 4) 通配符没转义 vs 转义后
    kw = "50%_off"
    raw = bind("... LIKE %s", (f"%{kw}%",))
    print("未转义:", raw, "-> _ 与 % 都成了通配符")
    safe = bind("... LIKE %s ESCAPE '\\'", (f"%{like_escape(kw)}%",))
    print("已转义:", safe, "-> 只匹配字面量")
```

**追问一**：为什么 `%...%` 一定走不了索引？
→ 解析：B 树按前缀有序，`LIKE 'abc%'` 能定位到 `abc` 这个前缀区间做范围扫；`LIKE '%abc'` 左端不确定，只能全索引扫或全表扫。要救可以上 `pg_trgm` 的 GIN 索引（三元组）或全文检索/搜索引擎，但那是另一套存储成本。

**追问二**：MySQL 驱动的 paramstyle 也这样吗？
→ 解析：`mysqlclient` 是 `format`（`%s`），`pymysql` 是 `pyformat`，`sqlite3` 是 `qmark`（`?`）。同一份 SQL 换驱动就要改占位符；`LIKE` 里的 `%` 在 `%` 系驱动里同样要 `%%` 转义，在 `qmark` 系里则完全不用转义——这就是"本地 sqlite 测试通过、上线 MySQL 报错"的经典来源。
