"""依赖许可证检查:deny/allow 清单加 unknown 人工复核"""

from fnmatch import fnmatch

LICENSE_DB = {
    "requests": "Apache-2.0", "numpy": "BSD-3-Clause",
    "pandas": "BSD-3-Clause", "gpl-tool": "GPL-3.0-only",
    "lgpl-binding": "LGPL-2.1", "mystery-pkg": None,
}
DEPS = ["requests", "numpy", "pandas", "gpl-tool", "lgpl-binding", "mystery-pkg"]
DENY = ["GPL-*", "AGPL-*"]
ALLOW = ["MIT", "Apache-*", "BSD-*", "LGPL-*"]


def check(dep):
    lic = LICENSE_DB.get(dep)
    if lic is None:
        return "unknown", "许可证未知,人工复核后登记"
    if any(fnmatch(lic, p) for p in DENY):
        return "blocked", f"{lic} 具传染性,禁止引入"
    if any(fnmatch(lic, p) for p in ALLOW):
        return "ok", lic
    return "review", f"{lic} 不在白名单,评审后决定"


if __name__ == "__main__":
    counts = {"ok": 0, "review": 0, "blocked": 0, "unknown": 0}
    for dep in DEPS:
        state, msg = check(dep)
        counts[state] += 1
        print(f"{dep:<14} {state:<8} {msg}")
    print(f"汇总: {counts}")
    if counts["blocked"]:
        print("门禁: 存在 blocked 依赖,合并被拒绝,先找替代品")
    print("要点:许可证检查放进 CI,license 数据库随锁文件一起更新;unknown 不是 ok,积压 unknown 等于失去合规视野;传染性许可看链接方式,法律问题交给法务兜底")
