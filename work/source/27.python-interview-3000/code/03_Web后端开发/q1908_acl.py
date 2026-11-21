"""资源级 ACL 检查器: 显式 ACE、拒绝优先与目录继承(纯标准库)。"""


def check(resource, user, perm, groups=None):
    """沿资源链向上找最近的显式决策: 同层拒绝优先, 越近的 ACE 越有发言权。

    主体的身份集合 = 用户名 + 所属组; owner 等价全部权限。
    返回 (allowed, 决策来源说明)。
    """
    identities = set([user])
    for g in (groups or {}).get(user, []):
        identities.add(g)
    while resource is not None:
        if user == resource.get("owner"):
            return True, "owner@" + resource["path"]
        allow_here = None
        for ace in resource.get("aces", []):
            if ace["principal"] not in identities or ace["perm"] != perm:
                continue
            if ace["effect"] == "deny":
                return False, "deny@" + resource["path"]      # 同层拒绝立即生效
            allow_here = "allow@" + resource["path"]          # 允许先记下, 本层看完
        if allow_here:
            return True, allow_here                           # 最近层已决策, 不再看远层
        resource = resource.get("parent")
    return False, "no-ace"


GROUPS = {"bob": ["group:audit-team"], "dave": ["group:audit-team"]}

# 目录树: /proj 下 bob 被 deny, /proj/audit 下 audit-team 组被 allow
tree = {"path": "/proj/audit/report.docx", "owner": "carol",
        "parent": {"path": "/proj/audit", "owner": "alice",
                   "aces": [{"principal": "group:audit-team", "perm": "read",
                             "effect": "allow"}],
                   "parent": {"path": "/proj", "owner": "alice",
                              "aces": [{"principal": "bob", "perm": "read",
                                        "effect": "deny"}]}}}

print("dave read(组继承 allow):", check(tree, "dave", "read", GROUPS))
print("bob read(更近层组 allow 覆盖远层 deny):", check(tree, "bob", "read", GROUPS))
print("carol read(owner):", check(tree, "carol", "read", GROUPS))
print("eve read(无 ACE 默认拒绝):", check(tree, "eve", "read", GROUPS))

assert check(tree, "dave", "read", GROUPS)[0]
assert check(tree, "carol", "read", GROUPS)[1] == "owner@/proj/audit/report.docx"
assert not check(tree, "eve", "read", GROUPS)[0]

# 把组 allow 挪到最远层, bob 最近的 deny 即生效
tree2 = {"path": "/proj/audit/report.docx", "owner": "carol",
         "parent": {"path": "/proj", "owner": "alice",
                    "aces": [{"principal": "bob", "perm": "read", "effect": "deny"}]}}
print("bob 无近层 allow 时远层 deny 生效:", check(tree2, "bob", "read", GROUPS))
assert not check(tree2, "bob", "read", GROUPS)[0]
print("要点: ACL 是逐层最近者胜、同层拒绝优先; 默认拒绝兜底, owner 是需要单列审计的特权入口")
