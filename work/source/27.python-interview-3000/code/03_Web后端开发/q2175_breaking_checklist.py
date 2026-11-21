"""破坏性变更检查清单引擎: 规则注册加 go/no-go 判定(纯标准库)。"""

OLD_SPEC = {
    "GET /v1/orders": {"resp_fields": {"id", "total", "state"}},
    "GET /v1/orders/{id}": {"resp_fields": {"id", "total", "state", "coupon"}},
}
NEW_SPEC = {
    "GET /v1/orders": {"resp_fields": {"id", "total", "state", "channel"}},
    "GET /v1/orders/{id}": {"resp_fields": {"id", "amount", "state"}},
    "DELETE /v1/orders/{id}": {"resp_fields": set()},
}
RULES = []


def rule(rid, severity):
    def deco(fn):
        RULES.append((rid, severity, fn))
        return fn
    return deco


@rule("R1-endpoint-removed", "blocker")
def removed_endpoints(old, new):
    return sorted(set(old) - set(new))


@rule("R2-field-removed", "blocker")
def removed_response_fields(old, new):
    out = []
    for path, spec in old.items():
        if path not in new:
            continue
        gone = spec["resp_fields"] - new[path]["resp_fields"]
        if gone:
            out.append("{} 失去字段 {}".format(path, sorted(gone)))
    return out


@rule("R3-endpoint-added", "info")
def added_endpoints(old, new):
    return sorted(set(new) - set(old))


def review(old, new):
    findings = []
    for rid, severity, fn in RULES:
        hits = fn(old, new)
        if hits:
            findings.append((rid, severity, hits))
    blockers = [f for f in findings if f[1] == "blocker"]
    return findings, ("no-go" if blockers else "go")


findings, verdict = review(OLD_SPEC, NEW_SPEC)
for rid, severity, hits in findings:
    print("[{:7s}] {:20s} {}".format(severity, rid, hits))
print("发布判定:", verdict)
assert verdict == "no-go"          # coupon 被删除, 必须走新版本
print("要点: 清单引擎把'什么算破坏'变成可执行规则; blocker 拦截放行, info 只提示, 规则库随复盘持续增补")
