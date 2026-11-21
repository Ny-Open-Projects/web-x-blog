"""排序参数的白名单映射: 标识符不能走参数化(纯标准库)。"""

ALLOWED_SORTS = {
    "created_at": "created_at",
    "price": "price_cents",
    "rating": "rating_avg",
}


def build_order_by(sort_param):
    """只接受注册过的排序名, 一律映射到预定义列常量; 拒绝任何透传。"""
    if sort_param is None:
        return "created_at DESC"                        # 文档化的默认排序
    key = sort_param.strip().lower()
    if key not in ALLOWED_SORTS:
        raise ValueError("unsupported sort: " + sort_param)
    return ALLOWED_SORTS[key] + " DESC"


def sql_for(sort_param):
    return "SELECT id, price_cents FROM goods ORDER BY " + build_order_by(sort_param)


attacks = ["price; DROP TABLE goods;--",
           "(SELECT CASE WHEN 1=1 THEN price ELSE id END)",
           "price_cents",
           "IF(true, price, id)"]
for bad in attacks:
    try:
        build_order_by(bad)
        print("漏网!", bad)
    except ValueError as exc:
        print("拒绝: {:38s} -> {}".format(bad[:36], exc))
print("正常:", sql_for("price"))
print("默认:", sql_for(None))
assert "price_cents" in sql_for("price")
print("要点: ORDER BY 放不了占位符, 白名单映射是唯一正解; 映射目标是常量, 用户永远接触不到物理列名")
