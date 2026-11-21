"""水平越权:对象归属校验,拒绝时与不存在同响应(纯标准库)。"""

orders = {1: {"owner": "alice", "amount": 100},
          2: {"owner": "bob", "amount": 200}}


def get_order_vulnerable(order_id, current_user):
    return orders.get(order_id)              # 只按 ID 查,存在越权


def get_order_safe(order_id, current_user):
    obj = orders.get(order_id)
    if obj is None or obj["owner"] != current_user:
        return None                          # 与不存在同响应,不泄露存在性
    return obj


print("未防护:alice 拿到 bob 的订单 ->", get_order_vulnerable(2, "alice"))
print("已防护:alice 访问 bob 的订单 ->", get_order_safe(2, "alice"))
print("已防护:alice 访问自己的订单 ->", get_order_safe(1, "alice"))

assert get_order_safe(2, "alice") is None
assert get_order_safe(2, "bob") is not None
assert get_order_safe(99, "alice") is None
print("越权用例全部通过")
