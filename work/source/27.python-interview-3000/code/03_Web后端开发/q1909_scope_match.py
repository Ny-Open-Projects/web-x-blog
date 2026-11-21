"""Scope 通配与最小授权: 匹配规则与越权审计(纯标准库)。"""


def scope_match(granted, required):
    """OAuth scope 语义: : 分段, 段内 * 通配; "orders:*" 授予 orders 域全部动作。

    独立的 * 或 *:* 是全局通配, 视为高危授权。
    """
    g_segs = granted.split(":")
    r_segs = required.split(":")
    if len(g_segs) != len(r_segs):
        return False
    for g, r in zip(g_segs, r_segs):
        if g != "*" and g != r:
            return False
    return True


def check_access(token_scopes, required):
    return any(scope_match(g, required) for g in token_scopes)


TOKEN = ["orders:read", "orders:write", "report:read"]
cases = [
    ("orders:read", True),
    ("orders:delete", False),
    ("report:read", True),
    ("payments:read", False),
]
for required, want in cases:
    got = check_access(TOKEN, required)
    print("token {} 需求 {} -> {}".format(TOKEN, required, got))
    assert got == want, required

# 通配令牌的代价: 一个 orders:* 等价整域, 泄露影响面爆炸
WILD = ["orders:*"]
print("orders:* 覆盖 orders:delete:", check_access(WILD, "orders:delete"))
assert check_access(WILD, "orders:delete")

# 最小授权审计: 统计端点实际用到的 scope, 找出从未使用的授予
USED = {"orders:read", "report:read"}
unused = [s for s in TOKEN if s not in USED]
print("审计发现从未使用的授予:", unused, "(下次发令牌应收窄)")
assert unused == ["orders:write"]
print("要点: 通配提升运维便利但放大泄露半径, 颁发按需、审计按实, 全局 * 必须走人工审批")
