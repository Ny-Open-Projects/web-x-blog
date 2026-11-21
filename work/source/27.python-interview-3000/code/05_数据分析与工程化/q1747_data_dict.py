"""数据字典自动生成:从 schema 元数据渲染 markdown,注释缺失本身就是质量问题"""

TABLES = [
    {
        "name": "dwd.pay_order_d",
        "desc": "支付订单日增量",
        "owner": "team-data",
        "cols": [
            ("order_id", "string", "订单号", False),
            ("uid", "string", "用户ID", False),
            ("pay_amount", "bigint", "", False),
            ("id_card", "string", "身份证号", True),
        ],
    },
    {
        "name": "dws.user_pay_d",
        "desc": "用户支付日汇总",
        "owner": "team-data",
        "cols": [
            ("uid", "string", "用户ID", False),
            ("amt_7d", "double", "近7天支付金额", False),
        ],
    },
]


def render_dict(tables):
    out = ["# 数据字典(自动生成)", ""]
    missing = []
    for t in tables:
        out.append(f"## {t['name']}")
        out.append(f"{t['desc']} | owner: {t['owner']}")
        out += ["", "| 字段 | 类型 | 说明 | PII |", "|---|---|---|---|"]
        for col, ctype, comment, pii in t["cols"]:
            if not comment:
                missing.append(f"{t['name']}.{col}")
            out.append(f"| {col} | {ctype} | {comment or '缺注释'} | {'是' if pii else ''} |")
        out.append("")
    out.append(f"> 注释缺失 {len(missing)} 处: {', '.join(missing)}")
    return "\n".join(out)


if __name__ == "__main__":
    print(render_dict(TABLES))
    print("\n要点:字典从元数据渲染而不是手写;PII 列必须打标并联动脱敏策略;注释缺失率纳入表质量分,推动 owner 补齐")
