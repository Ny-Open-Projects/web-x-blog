---
title: [Q1909] Scope 通配与最小授权
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1909 · Scope 通配与最小授权

> 难度:★★★☆ | 标签:OAuth, 安全

**问**:scope 的 orders:* 和 orders:read 怎么匹配?通配符有什么风险?

**答**:scope 常用冒号分段:资源域:动作,段内 * 通配,orders:* 覆盖该域全部动作,比较时段数必须一致。匹配语义是"任一授予命中需求即可":接口要求 orders:read,令牌持有 orders:read 或 orders:* 都通过。风险在泄露半径:一把 orders:* 的令牌泄露等于整域沦陷,全局 *:* 等价 root,必须人工审批加短期过期。工程配套三条:颁发按需——界面默认勾最小集;审计按实——统计端点实际消费的 scope,找出从未使用的授予,下次发令牌收窄;轮换做 diff——新令牌比旧令牌多了什么权限一目了然。面向第三方的令牌建议禁用通配,内部服务间才放宽,通配便利与安全是跷跷板。

```python
# file: code/03_Web后端开发/q1909_scope_match.py
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
```

**追问**:
- scope 与 RBAC 角色什么关系?——scope 描述令牌能做什么(能力),角色描述用户是谁(身份),授权时先角色后 scope 叠加判定。
- 动作粒度怎么定?——read/write/delete 分开,admin 类动作独立 scope,避免大而全的粗粒度。
