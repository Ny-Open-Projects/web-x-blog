"""SQL 模板渲染:值参数走占位符,标识符走白名单,拒绝字符串拼接"""

import re

IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
ALLOWED_TABLES = {"pay_order_d", "visit_d"}


def render(template, params, table):
    """table 是标识符必须白名单校验;params 保持绑定参数不内插"""
    if not IDENT.match(table) or table not in ALLOWED_TABLES:
        raise ValueError(f"非法表名: {table!r}")
    for k, v in params.items():
        if isinstance(v, str) and ("'" in v or ";" in v):
            raise ValueError(f"参数含危险字符: {k}={v!r}")
    return template.format(table=table), params


if __name__ == "__main__":
    sql, params = render(
        "SELECT * FROM {table} WHERE dt = %s AND city = %s",
        {"dt": "2025-10-28", "city": "华东"},
        "pay_order_d",
    )
    print("渲染 SQL:", sql)
    print("绑定参数:", params)
    for bad_table in ("pay_order_d; DROP TABLE x", "unknown_t"):
        try:
            render("SELECT * FROM {table}", {}, bad_table)
        except ValueError as e:
            print("已拦截:", e)
    try:
        render("SELECT * FROM {table} WHERE city = %s", {"city": "华东'; --"}, "pay_order_d")
    except ValueError as e:
        print("已拦截:", e)
    print("要点:值用占位符交给驱动转义;标识符(表名/列名)驱动管不了,必须白名单;模板渲染永远不把值拼进 SQL 字符串")
