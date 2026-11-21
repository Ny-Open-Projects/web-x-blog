---
title: [Q2011] 依赖库许可证检查:deny/allow 清单门禁
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2011 · 依赖库许可证检查:deny/allow 清单门禁

> 难度:★★★☆ | 标签:许可证, 合规

**问**:为什么引入一个 GPL 的库可能有法律风险?工程上怎么系统性把关?

**答**:GPL 类许可证有传染性,链接了它的代码可能被要求整体开源,服务商用会承担合规义务,所以许可证检查要进 CI 而不是靠记忆。实现四件套:license 数据库(随锁文件更新)、deny 清单(GPL 与 AGPL 系列)、allow 清单(MIT/Apache/BSD/LGPL)、unknown 处理——许可证未知要人工复核后登记,不是放行。实测六个依赖里 gpl-tool 被 blocked 拒绝合并,mystery-pkg 被标记 unknown。两个延伸:传染性判断与链接方式有关(动态链接、进程隔离义务不同),法律结论交给法务,工程侧把 deny 清单当硬门禁;内部二进制依赖和 SaaS 调用也要人工登记进同一张表。

```python
# file: code/05_数据分析与工程化/q2011_license_check.py
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
```

**追问**:
- 追问 1:为什么 unknown 不能放行?—— 放行一个 unknown 清单就永远不再全绿,合规视野从此失真;unknown 必须显式人工关闭。
- 追问 2:依赖没升级但上游改了许可证怎么发现?—— 锁文件升级时重跑检查,加定期全量重扫,上游改许可证的事件真实发生过。
