"""Q2866 敏感级路由:按数据分级选供应商 PII 只走内网。

不是所有请求都能发给外部云厂商:含 PII 的请求必须留在自托管模型,
哪怕自托管正宕机,也宁可拒绝服务(fail-closed)也不能降级外发。
公有数据才允许沿健康度降级链走。分级路由把合规约束变成路由前置闸。
"""

HEALTH = {"selfhost": False, "cloud_pro": True, "cloud_lite": True}

ROUTE = {
    "pii": ["selfhost"],
    "internal": ["selfhost", "cloud_pro"],
    "public": ["cloud_pro", "cloud_lite"],
}


class PolicyRefusal(Exception):
    """合规拒绝:宁可失败不可外泄。"""


def route(data_class, health):
    for m in ROUTE[data_class]:
        if health.get(m):
            return m
    raise PolicyRefusal("无可用且合规的供应商,拒绝处理:" + data_class)


def main():
    # public:正常走云
    assert route("public", HEALTH) == "cloud_pro"
    # internal:自托管宕机,允许降到云
    assert route("internal", HEALTH) == "cloud_pro"
    # pii:自托管宕机,云再健康也不能去 —— fail-closed
    try:
        route("pii", HEALTH)
        raise AssertionError("必须拒绝")
    except PolicyRefusal as exc:
        msg = str(exc)
    assert "拒绝处理:pii" in msg, msg
    # 自托管恢复后 pii 立即回归内网
    health2 = dict(HEALTH, selfhost=True)
    assert route("pii", health2) == "selfhost"
    # 全部宕机:任何分级都拒绝而不是硬选一个
    down = {k: False for k in HEALTH}
    for cls in ("pii", "internal", "public"):
        try:
            route(cls, down)
            raise AssertionError("应当拒绝")
        except PolicyRefusal:
            pass
    print("public ->", route("public", HEALTH))
    print("internal 自托管宕机 ->", route("internal", HEALTH))
    print("pii 自托管宕机 ->", msg)
    print("要点:pii 链路里根本没有云厂商,想降级都无处可降")


if __name__ == "__main__":
    main()
