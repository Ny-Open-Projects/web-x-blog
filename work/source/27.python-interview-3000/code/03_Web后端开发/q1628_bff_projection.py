"""BFF 聚合模式: 同一领域对象按端裁剪出不同视图(纯标准库)。"""

ORDER = {
    "id": "ord_1", "status": "paid", "amount_cents": 9900, "currency": "CNY",
    "buyer": {"uid": "u9", "phone": "13800000000"},
    "items": [{"sku": "A1", "qty": 2, "cost_cents": 4000},
              {"sku": "B2", "qty": 1, "cost_cents": 1900}],
}


def money(cents, currency):
    return f"{cents / 100:.2f} {currency}"


def mobile_view(order):
    """移动端: 小屏要决策字段, 手机号脱敏, 绝不传内部成本。"""
    phone = order["buyer"]["phone"]
    return {"id": order["id"], "status": order["status"],
            "total": money(order["amount_cents"], order["currency"]),
            "item_count": sum(i["qty"] for i in order["items"]),
            "phone_masked": phone[:3] + "****" + phone[-2:]}


def web_view(order):
    """Web 端: 页面要明细, 依然裁掉成本字段。"""
    return {"id": order["id"], "status": order["status"],
            "total": money(order["amount_cents"], order["currency"]),
            "items": [{"sku": i["sku"], "qty": i["qty"]} for i in order["items"]]}


def admin_view(order):
    """管理端: 全量字段含成本, 由独立权限网关保证不外泄。"""
    return ORDER


print("mobile:", mobile_view(ORDER))
print("web:   ", web_view(ORDER))
print("admin 含成本:", "cost_cents" in admin_view(ORDER))
print("要点: 裁剪放在 BFF 视图层而不是客户端, 上游领域模型保持单一, 各端契约各自演进")
