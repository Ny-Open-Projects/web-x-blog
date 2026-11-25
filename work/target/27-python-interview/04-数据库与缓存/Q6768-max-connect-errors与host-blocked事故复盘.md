---
title: "[Q6768] 密码配错全站连不上库：max_connect_errors 与 host blocked 事故复盘"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6768 · 密码配错全站连不上库：max_connect_errors 与 host blocked 事故复盘

难度：P6 ｜ 标签：MySQL、连接失败、host blocked、容器网络、故障复盘

基线：Python 3.12；模拟按来源 IP 的连接失败计数与封禁/解禁流程，复现容器共享出口 IP 下的放大效应。

**问**：凌晨改了应用配置把数据库密码配错一个字符，重试风暴之下，整台应用的数据库连接**全部**报 `Host ... is blocked because of many connection errors`。密码错就该这一台应用连不上，为什么变成"这台主机彻底被封"？`max_connect_errors` 到底数的是什么？为什么改对密码还不行？

**答**：
- **结论**：MySQL 按**来源主机（IP）**维护连接失败计数：TLS 握手中断、认证失败、异常断连都累加，成功完成一次握手才清零；累计超过 `max_connect_errors`（默认 100）就把该 IP 加入 blocked 缓存，之后**直接拒绝**，连登录都不给试——设计目标是防暴力破解。事故链是：密码错 → 应用重试（Q2231 连接风暴）→ 短时间几百次失败 → IP 被封 → 改对密码也报 blocked（错误提示没变，人以为还是密码错）→ 解禁需要 `FLUSH HOSTS`/`mysqladmin flush-hosts`（8.0 用 `TRUNCATE performance_schema.host_cache`）或等缓存刷新。容器/K8s 环境有**放大效应**：同一节点所有 Pod 共享出口 IP，一个 Pod 配错密码等于把全节点 Pod 一起封了。
- **取舍**：① max_connect_errors 调大只是延后封禁，治标——治本是应用侧连接失败退避（指数退避 + 上限），别用无间隔重试放大错误；② blocked 提示与"密码错误"提示不同，告警要按错误类型分诊（Q1311 errno 分诊思路），全站 blocked 是"配置+重试风暴"复合事故；③ FLUSH HOSTS 是全局操作有短暂影响，生产要走变更，别随手敲；④ 共享出口 IP 的环境里"按 IP 封"天然误伤，K8s 下应通过 NetworkPolicy/代理层限制来源，或直接调大阈值+强退避。
- **实战**：① 连接串配置变更走灰度：先在单 Pod 验证再全量（Q6558 参数变更灰度）；② 应用连接失败重试统一封装：退避 + 失败熔断（Q2230 退避矩阵），杜绝 1 秒内几百次重试；③ host_cache 监控：blocked 计数、失败增长速率进巡检；④ 事故 SOP 固定：看到 blocked → FLUSH HOSTS 解禁 → 修配置 → 单实例验证 → 分批放量，顺序不能反。

```python
"""host blocked 事故模拟：按 IP 的失败计数、封禁、解禁与共享出口 IP 放大。"""
from collections import defaultdict

MAX_ERRORS = 100


class DBHostCache:
    def __init__(self, max_errors: int = MAX_ERRORS):
        self.max_errors = max_errors
        self.fail_count: dict[str, int] = defaultdict(int)
        self.blocked: set[str] = set()

    def connect(self, ip: str, password_ok: bool) -> str:
        if ip in self.blocked:
            return f"{ip} -> BLOCKED (拒绝握手, 连登录都不试)"
        if password_ok:
            self.fail_count[ip] = 0          # 成功握手清零
            return f"{ip} -> 连接成功"
        self.fail_count[ip] += 1
        if self.fail_count[ip] >= self.max_errors:
            self.blocked.add(ip)
            return f"{ip} -> 认证失败, 计数 {self.fail_count[ip]}, 触发封禁!"
        return f"{ip} -> 认证失败, 计数 {self.fail_count[ip]}/{self.max_errors}"

    def flush_hosts(self) -> str:
        n = len(self.blocked)
        self.blocked.clear()
        self.fail_count.clear()
        return f"FLUSH HOSTS 完成, 解禁 {n} 个主机"


if __name__ == "__main__":
    cache = DBHostCache()
    print("场景1: 单应用密码配错, 重试风暴打满计数")
    for i in range(99):                     # 前 99 次失败
        cache.connect("10.0.1.5", password_ok=False)
    print(cache.connect("10.0.1.5", password_ok=False))
    print(cache.connect("10.0.1.5", password_ok=True))    # 改对密码也没用
    print(cache.connect("10.0.1.6", password_ok=True))    # 同机其他应用(不同IP)正常

    print("\n场景2: K8s 同节点 Pod 共享出口 IP -> 误伤放大")
    cache2 = DBHostCache()
    for i in range(100):
        cache2.connect("172.17.0.1", password_ok=False)   # 一个 Pod 配错
    print(cache2.connect("172.17.0.1", password_ok=True))
    # 同节点的其他 Pod 全走同一出口 IP
    for pod in ("pod-a", "pod-b", "pod-c"):
        print(cache2.connect("172.17.0.1", password_ok=True))
    print(f"  -> 该节点 {3 + 1} 个 Pod 全部连不上, 事故半径从 1 个应用放大到全节点")

    print("\n场景3: 处置顺序")
    print(cache2.flush_hosts())
    print(cache2.connect("172.17.0.1", password_ok=True))
    print("结论：blocked 是'配置错误 x 无退避重试'的复合事故; 共享出口 IP")
    print("      放大半径; SOP=解禁->修配置->单实例验证->分批放量")
```

**追问一**：为什么"握手异常断连"也计入失败？这不会误伤正常抖动吗？

→ 解析：MySQL 的计数不止认证失败：TLS 握手中途断开、网络异常导致的半开连接都算——设计意图是"凡是像暴力探测的行为都计数"。代价就是网络抖动场景的误伤：LB 健康检查的超时重试、网络闪断都会累积计数。缓解是权衡：阈值默认 100 其实是"宁可误伤也别被爆破"的保守值；内网受控环境可以调大（比如 1000）配合应用退避，公网暴露的实例维持默认并配合防火墙。误伤的真问题不在阈值，而在**应用无退避重试把 1 次失败放大成 100 次**——所以应用侧连接重试的退避封装是根治点。

**追问二**：8.0 里为什么废弃了 FLUSH HOSTS？

→ 解析：FLUSH HOSTS 是历史遗留的"全局黑箱操作"，8.0 起推荐 `TRUNCATE TABLE performance_schema.host_cache`——语义相同但好处有三：一是 host_cache 变成了可查询的表，封禁状态与失败计数**可观测**（SELECT 就能看到哪个 IP 多少次失败），运维不再靠猜；二是 TRUNCATE 走标准表操作权限体系，可以精确授权给运维角色而不是全局 RELOAD 权限；三是与 performance_schema 的监控体系统一，巡检脚本直接查表。工程上更重要的启示：**能查询的状态就不要做成只有"清一下"才能处理的黑盒**——可观测性是故障处置速度的地基。
