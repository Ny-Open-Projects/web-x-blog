"""垂直越权:角色能力矩阵与默认拒绝(纯标准库)。"""

ROLES = {
    "admin":   {"user.read", "user.delete", "order.read"},
    "support": {"user.read", "order.read"},
    "user":    {"order.read"},
}


def authorize(role, permission):
    """默认拒绝:未知角色或未登记权限一律 False。"""
    return permission in ROLES.get(role, set())


TESTS = [
    ("admin", "user.delete", True),
    ("support", "user.read", True),
    ("support", "user.delete", False),
    ("user", "user.read", False),
    ("ghost", "user.read", False),        # 未知角色默认拒绝
    ("admin", "billing.export", False),   # 未登记权限默认拒绝
]
for role, perm, expect in TESTS:
    got = authorize(role, perm)
    assert got == expect, (role, perm, got)
    print(f"{role:8s} {perm:14s} -> {got}")
print("垂直越权用例全部通过,默认拒绝生效")
