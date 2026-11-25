---
title: [A280] API 网关设计：路由装配、鉴权前置、插件链与按上游故障隔离
date: 2026-11-24
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A280 · API 网关的四件套：路由装配、鉴权前置、插件链与故障隔离

> 难度:★★★★ | 标签:API 网关, 插件链, 鉴权, 路由, 熔断, 故障隔离

**问**（笔试·场景题）：「把鉴权、限流、日志做进每个微服务」维护成本爆炸——面试官要的是**网关作为产品的最小内核**：① **路由装配**：路由表支持精确路径与前缀路径两种规则，精确优先于前缀（`/api/orders/detail` 命中精确规则而非 `/api` 前缀），未命中返回 404 并带命中裁决日志；② **鉴权前置**：鉴权插件必须排在插件链最前——无 token 401、无效 token 401、非本路由角色 403，断言「未鉴权请求短路返回，根本不触发限流计数与上游调用」（用限流计数器与上游调用计数器证明）；③ **插件链**：每条路由挂自己的插件序列（auth → rate-limit → 转发），插件返回 `None` 放行、返回响应即短路——不同路由的限流阈值互不干扰（`/api/orders` 限 3 次、`/api/users` 限 5 次，各自独立计数）；④ **故障隔离**：按上游做熔断——连续 3 次失败打开熔断、冷却期后半开探测，熔断期间网关直接回降级响应，**其他上游不受牵连**（bulkhead 语义，断言 B 上游熔断时 A 上游仍正常）；⑤ 演示一条完整请求轨迹：无鉴权短路 → 鉴权通过但超限 → 鉴权通过上游熔断降级 → 鉴权通过正常转发，四种终态各有断言。请说清与 Q1885（服务端入站治理链：幂等/限流/隔离舱/熔断/降级五道门的**顺序论证**）、Q2440（Trie 路由器的段级匹配与参数段裁决）、Q980（令牌桶原语本身）、A159（网关做 API 版本重写）的分工——本题只回答「**网关内核的装配模型：路由表、插件链短路语义与按上游的故障隔离**」。

**答**：① 分工：Q1885 回答「门与门怎么排序」，Q2440 回答「路径怎么匹配」，Q980 回答「桶怎么写」，A159 回答「版本怎么重写」——没人回答「这些零件怎么**装成一台可扩展的网关**」：路由表决定「请求找谁」，插件链决定「过五关斩六将的执行模型」，按上游熔断决定「一家故障不全家陪葬」。② 插件链的执行模型是本题核心：每个插件拿到 `ctx` 做检查，返回 `None` 表示放行（链上继续）、返回 `(status, body)` 表示**短路**（链立刻终止、响应直接回客户端）——这就是「鉴权前置」能成立的结构基础：鉴权插件挂在链头，401/403 短路后，限流插件的计数器没被碰到、上游调用数为 0，**断言计数器不变就是「前置」二字的验收标准**。插件顺序即治理顺序：鉴权（身份没过，后面全免谈）→ 限流（身份过了，先挡量）→ 业务转发（最后才是真调用）。③ 限流是**每路由一份实例**而不是全局一份：路由表装配时给每条路由 new 一个桶，`/api/orders` 的突发不影响 `/api/users` 的配额——网关限流的粒度问题（全局/路由/用户三级）里，路由级是默认起点。④ 故障隔离的账：熔断器是**按上游**（upstream）而不是按路由或全局——`/api/users` 的上游挂了，打开的只是那个上游的熔断器，`/api/orders` 照常转发；降级响应在路由配置里声明（`fallback="users degraded"`），熔断期网关直接回它、不碰上游。半开探测放一个请求去试，成功则关闭熔断器恢复转发——这套状态机（closed → open → half-open）是网关「故障不扩散」的全部。⑤ 与 Q1885 再划一次界：Q1885 的五道门长在**服务自己门口**（进程内中间件），本题的插件链长在**网关上**（独立进程、对所有服务收敛）——网关化的收益是策略集中与语言无关，代价是多一跳与策略变更的爆炸半径（网关挂=全站挂，所以网关自身要做无状态水平扩展与灰度发布）。

```python
# 全部标准库；API 网关最小内核：路由装配 + 插件链短路 + 每路由限流 + 按上游熔断
import collections


class RateLimiter:
    """每路由独立实例的滑动窗口计数（(用户, 秒窗) 计数，原语版见 Q980）。"""

    def __init__(self, limit):
        self.limit = limit
        self.hits = collections.Counter()      # 计数器可被外部断言（前置证明）

    def allow(self, key, t):
        k = (key, int(t))
        self.hits[k] += 1
        return self.hits[k] <= self.limit


class Breaker:
    """按上游的熔断器：closed → open(3 连败) → half-open(冷却后探测)。"""

    def __init__(self, threshold=3, cooldown=5):
        self.threshold = threshold
        self.cooldown = cooldown
        self.fails = 0
        self.state = "closed"
        self.opened_at = -1

    def allow(self, t):
        if self.state == "open":
            if t - self.opened_at >= self.cooldown:
                self.state = "half-open"       # 放一个探测请求
                return True
            return False
        return True

    def record(self, ok, t):
        if ok:
            self.fails = 0
            self.state = "closed"
        else:
            self.fails += 1
            if self.state == "half-open" or self.fails >= self.threshold:
                self.state = "open"            # 探测失败或连败达阈 → 打开
                self.opened_at = t


class Upstream:
    def __init__(self, name, broken=False):
        self.name = name
        self.calls = 0
        self.broken = broken                   # 演示用故障开关

    def call(self):
        self.calls += 1
        return not self.broken


def plugin_auth(ctx):
    """鉴权前置：身份不过就短路，限流计数与上游调用都碰不到。"""
    user = ctx.get("user")
    if user is None:
        return 401, "no token"
    if user not in ctx["valid_tokens"]:
        return 401, "bad token"
    if ctx["route"].get("role") and ctx["route"]["role"] != ctx.get("role"):
        return 403, "forbidden"
    return None


def plugin_ratelimit(ctx):
    rl = ctx["route"]["limiter"]
    ok = rl.allow(ctx["user"], ctx["t"])
    if not ok:
        return 429, "rate limited"
    return None


def plugin_forward(ctx):
    up = ctx["route"]["upstream"]
    br = ctx["route"]["breaker"]
    if not br.allow(ctx["t"]):
        return 503, ctx["route"]["fallback"]   # 熔断期：降级响应，不碰上游
    ok = up.call()
    br.record(ok, ctx["t"])
    if not ok:
        return 502, "upstream error"
    return 200, "ok:" + up.name


class Gateway:
    def __init__(self):
        self.routes = []                       # [(rule, path, config)]，精确优先

    def route(self, path, upstream, limit, role=None, prefix=False,
              fallback="degraded"):
        self.routes.append({
            "rule": "prefix" if prefix else "exact",
            "path": path,
            "upstream": upstream,
            "limiter": RateLimiter(limit),
            "breaker": Breaker(),
            "role": role,
            "fallback": fallback,
        })

    def match(self, path):
        for r in self.routes:                  # 精确规则先扫
            if r["rule"] == "exact" and path == r["path"]:
                return r
        for r in self.routes:                  # 再扫前缀规则
            if r["rule"] == "prefix" and path.startswith(r["path"]):
                return r
        return None

    def handle(self, method, path, t=0.0, **ctx):
        r = self.match(path)
        if r is None:
            return 404, "no route"
        ctx.update(route=r, t=t)
        for plugin in (plugin_auth, plugin_ratelimit, plugin_forward):
            short = plugin(ctx)                # None=放行，非 None=短路
            if short is not None:
                return short
        return 200, "ok"


if __name__ == "__main__":
    gw = Gateway()
    up_orders, up_users = Upstream("orders"), Upstream("users")
    gw.route("/api/orders/detail", up_orders, limit=3)
    gw.route("/api/orders", up_orders, limit=3, prefix=True)
    gw.route("/api/users", up_users, limit=5)

    # ① 路由装配：精确优先于前缀，未命中 404
    assert gw.match("/api/orders/detail")["rule"] == "exact"
    assert gw.match("/api/orders/list")["rule"] == "prefix"
    assert gw.handle("GET", "/favicon.ico") == (404, "no route")
    print("路由: 精确命中 /api/orders/detail，前缀兜底 /api/orders/list，未命中 404 ✅")

    # ② 鉴权前置：无 token 401 短路——限流计数器与上游调用数都不动
    rl_before = dict(gw.match("/api/users")["limiter"].hits)
    calls_before = up_users.calls
    assert gw.handle("GET", "/api/users") == (401, "no token")
    assert gw.handle("GET", "/api/users", user="hacker",
                     valid_tokens=set()) == (401, "bad token")
    assert dict(gw.match("/api/users")["limiter"].hits) == rl_before
    assert up_users.calls == calls_before
    print("鉴权前置: 无/坏 token 均 401，限流计数与上游调用计数纹丝未动 ✅")

    # ③ 插件链：每路由限流独立，orders 第 4 次超限、users 第 5 次仍在限内
    tok = {"valid_tokens": {"alice": "t"}}
    for i in range(3):
        assert gw.handle("GET", "/api/orders", t=1.0, user="alice",
                         valid_tokens=tok["valid_tokens"])[0] == 200
    assert gw.handle("GET", "/api/orders", t=1.0, user="alice",
                     valid_tokens=tok["valid_tokens"]) == (429, "rate limited")
    assert up_orders.calls == 3                   # 超限请求没打到上游
    for i in range(5):
        assert gw.handle("GET", "/api/users", t=1.0, user="alice",
                         valid_tokens=tok["valid_tokens"])[0] == 200
    print("插件链: orders 限 3 次第 4 次 429（上游仅 3 调用），users 独立限 5 次全过 ✅")

    # ④ 故障隔离：users 上游连挂 3 次 → 熔断，orders 不受牵连
    up_users.broken = True
    for i in range(3):
        assert gw.handle("GET", "/api/users", t=2.0, user="alice",
                         valid_tokens=tok["valid_tokens"])[0] == 502
    assert gw.match("/api/users")["breaker"].state == "open"
    assert gw.handle("GET", "/api/users", t=3.0, user="alice",
                     valid_tokens=tok["valid_tokens"])[0] == 503   # 熔断期降级
    calls_at_open = up_users.calls
    assert gw.handle("GET", "/api/users", t=4.0, user="alice",
                     valid_tokens=tok["valid_tokens"])[0] == 503
    assert up_users.calls == calls_at_open        # 熔断期上游零调用
    assert gw.handle("GET", "/api/orders", t=4.0, user="alice",
                     valid_tokens=tok["valid_tokens"])[0] == 200
    assert gw.match("/api/orders")["breaker"].state == "closed"
    print("故障隔离: users 连挂 3 次 → open → 503 降级零上游调用；orders 照常 200 ✅")

    # ⑤ 半开探测恢复：冷却期后放一个请求，成功则关闭
    up_users.broken = False
    assert gw.handle("GET", "/api/users", t=8.0, user="alice",
                     valid_tokens=tok["valid_tokens"])[0] == 200
    assert gw.match("/api/users")["breaker"].state == "closed"
    print("半开恢复: 冷却后探测成功 → 熔断关闭，网关自愈 ✅")
```

**追问**：1) 鉴权为什么必须在网关做前置，而不是各服务自己验？—— 结构成本与安全面两个理由：各服务自验意味着每个服务都要接入 token 校验库、密钥分发与吊销列表，语言各异实现各异，改一次签名算法要动 N 个仓库——网关前置把「身份这一件事」收敛到一处；安全面上，鉴权后置的每一条内网链路都是攻击面（绕过网关直连服务端口即裸奔），前置后网关到服务之间是受信内网 + 服务间二次鉴权（mTLS/内部 token）。但要注意**网关鉴权只验「是谁」，授权细化（行级权限、业务规则）仍归服务**——把「这个用户能不能改这张订单」也塞进网关，网关就变成了业务耦合的巨石。2) 熔断阈值 3 连败、冷却 5s 这些数字怎么定？不是拍脑袋——错误预算倒推：SLA 允许 0.1% 错误率时，3 连败在小流量下可能是巧合（3 次失败率 100% 是小样本噪声），所以要**按时间窗失败率**（如 30s 内 >50% 且样本 ≥20）而不是纯连败计数；冷却期取「下游典型恢复时间」的 2-5 倍（连接池重建、GC 完成），太短会在下游半死状态反复探测加重负担，太长放大故障时长。本题用连败计数是演示最小版，生产实现（如 resilience4j 模型）是滑窗失败率 + 半开单探测。3) 网关自己挂了怎么办？—— 网关是全站单点，必须从架构上承认它会挂并准备三层：**无状态水平扩展**（路由与限流状态放 Redis/配置中心，实例可随死随换，限流变分布式限流）；**多活部署**（两套网关集群跨机房，DNS/负载均衡切换，A135 的流量切换是它的演练版）；**旁路预案**（网关全挂时内网服务直连注册中心仍可被内部调用，外部流量进 fallback 页——「宁可 503 不可黑洞」）。限流状态外置的代价要认账：每请求多一次 Redis 往返，所以令牌桶常用「本地预扣 + 定期对账」的折衷（允许窗口内短暂超限，换取热路径零外呼）。
