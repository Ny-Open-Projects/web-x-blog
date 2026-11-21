"""数据字典生成器: 从样例行推断列画像 -> 渲染 Markdown 字典 -> 落盘"""
import os
import tempfile

ROWS = [
    {"order_id": "A001", "user_id": 1, "amount": 199.0, "status": "paid",   "coupon": None},
    {"order_id": "A002", "user_id": 2, "amount": 58.5,  "status": "paid",   "coupon": "NEW10"},
    {"order_id": "A003", "user_id": 1, "amount": 0.0,   "status": "refund", "coupon": None},
    {"order_id": "A004", "user_id": 3, "amount": 320.0, "status": "paid",   "coupon": "NEW10"},
    {"order_id": "A005", "user_id": 2, "amount": 120.0, "status": "paid",   "coupon": "VIP5"},
    {"order_id": "A006", "user_id": None, "amount": 66.0, "status": "paid", "coupon": None},
]

DESCRIPTIONS = {
    "order_id": "业务主键, 上游订单系统生成",
    "user_id": "下单用户 ID, 缺失多为游客单",
    "amount": "实付金额, 0 表示全额退款单",
    "status": "订单状态: paid 或 refund",
    "coupon": "使用的优惠券码, 无券为空",
}


def profile_column(col, values):
    non_null = [v for v in values if v is not None]
    types = sorted({type(v).__name__ for v in non_null})
    prof = {
        "column": col,
        "dtype": "/".join(types) if types else "none",
        "null_rate": round((len(values) - len(non_null)) / len(values) * 100, 1),
        "distinct": len({repr(v) for v in non_null}),
        "note": "",
    }
    if non_null and all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in non_null):
        prof["min"] = min(non_null)
        prof["max"] = max(non_null)
        prof["mean"] = round(sum(non_null) / len(non_null), 2)
    elif non_null and all(isinstance(v, str) for v in non_null):
        prof["max_len"] = max(len(v) for v in non_null)
        prof["sample"] = " / ".join(sorted({v for v in non_null})[:3])
    return prof


def build_dictionary(rows, table, descriptions=None):
    cols = list(rows[0].keys())
    profiles = [profile_column(c, [r.get(c) for r in rows]) for c in cols]
    lines = [
        "# 数据字典 · %s" % table,
        "",
        "样本 %d 行, 画像自动推断, 注释人工维护" % len(rows),
        "",
        "| 列 | 类型 | 空值率 | 去重数 | 画像 | 说明 |",
        "|---|---|---|---|---|---|",
    ]
    for p in profiles:
        if "min" in p:
            detail = "min=%s max=%s mean=%s" % (p["min"], p["max"], p["mean"])
        elif "sample" in p:
            detail = "max_len=%d 值域: %s" % (p["max_len"], p["sample"])
        else:
            detail = "-"
        desc = (descriptions or {}).get(p["column"], "")
        lines.append("| %s | %s | %s%% | %d | %s | %s |"
                     % (p["column"], p["dtype"], p["null_rate"], p["distinct"], detail, desc))
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    md = build_dictionary(ROWS, "ods.orders", DESCRIPTIONS)
    out = os.path.join(tempfile.mkdtemp(prefix="dict_"), "orders_dict.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write(md)
    print("已生成:", out)
    print(md.rstrip())
    print("要点: 画像自动推断省人力, 但空值率与值域要人来解释; 字典和表结构同评审, 口径分歧在源头消灭")
