"""指标基数治理: label 设计与爆炸预防(纯标准库)。"""


def estimate_series(base_labels, extra_label_values):
    """基数是各 label 取值数的笛卡尔积; 返回 (总系列数, 各 label 值数)。"""
    total = 1
    detail = {}
    for name, values in list(base_labels.items()) + list(extra_label_values.items()):
        n = values if isinstance(values, int) else len(values)
        detail[name] = n
        total *= n
    return total, detail


def guard(name, total, cap=20000):
    """注册指标时做基数守卫: 超过容量上限直接拒绝上线。"""
    if total > cap:
        raise ValueError("指标 {} 的预估基数 {} 超过上限 {}".format(name, total, cap))
    return "ok"


base = {"method": 7, "route_template": 40, "status_class": 5}
total, detail = estimate_series(base, {})
print("请求计数器基数: {} = {} 的乘积".format(total, detail))
assert guard("http_requests_total", total) == "ok"

# 反例: 把 user_id 塞进 label, 千用户乘上去瞬间爆炸
try:
    total_bad, _ = estimate_series(base, {"user_id": 5000})
    print("带 user_id 的基数:", total_bad)
    guard("http_requests_by_user", total_bad)
    raise AssertionError("守卫未生效")
except ValueError as e:
    print("守卫拦截:", e)

# 正确姿势: 高基数维度进日志与追踪, 指标只留有界桶
def user_bucket(user_id):
    if user_id.startswith("enterprise-"):
        return "tier:enterprise"
    return "tier:self-serve"


total_ok, _ = estimate_series(base, {"user_tier": 2})
print("用有界桶替代 user_id 后基数:", total_ok, "样例映射:",
      user_bucket("enterprise-a"), user_bucket("u9999"))
assert guard("http_requests_by_tier", total_ok) == "ok"
print("要点: label 每加一个维度都是乘法, 指标只留可枚举维度, 用户级细节去日志和 trace 里查")
