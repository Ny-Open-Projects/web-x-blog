"""按业务形态选择 Cache-Control 并做安全审计(纯标准库)。"""

POLICIES = {
    "auth_token":     "no-store",
    "user_profile":   "private, no-store",
    "public_catalog": "public, max-age=60, stale-while-revalidate=300",
    "contract_doc":   "public, max-age=0, must-revalidate",
}
SENSITIVE = {"auth_token", "user_profile"}


def audit(kind, header):
    if kind in SENSITIVE and "no-store" not in header:
        return "违规:敏感响应可被缓存"
    if "private" not in header and "public" not in header and "no-store" not in header:
        return "警告:未显式声明缓存可见性,默认可被共享缓存"
    return "ok"


for kind, header in POLICIES.items():
    print(f"{kind:15s} {header:55s} -> {audit(kind, header)}")
