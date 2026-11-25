---
title: "[Q6155] RBAC 权限检查每请求成本账与缓存"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6155 · RBAC 权限检查每请求成本账与缓存

难度：P7 ｜ 标签：RBAC、权限、缓存、成本工程、失效

**问**：一次请求里的权限检查（角色→权限解析、资源级判断）的成本构成是什么？"每请求现算"与"角色权限集合预展开缓存"在什么规模下差距拉大？权限缓存失效（改角色/换岗立即生效）与命中率怎么平衡？资源级判断（这条订单能否访问）为什么没法预展开？

**答**：
结论：权限检查两段成本：① **静态授权**（user → roles → permissions 的解析）：角色层次深、权限多时是图遍历（每请求 3-5 次查询或一次大 JSON 解析），纯 CPU+IO，可缓存；② **动态授权**（user + resource 实例 → allow/deny）：依赖资源属性（owner、部门、金额），无法预展开，只能请求时算。成本账：现算 = 每请求 O(查询次数 × RTT)；预展开 = 每请求 O(集合成员判断，微秒级) + 失效复杂度。差距在"角色数 × 权限数"上：50 角色 500 权限的解析约毫秒级，QPS 5000 时每秒烧掉 5s CPU——必须缓存。失效三策略：TTL 短（30-60s，允许延迟生效）、写时失效（改角色时显式删 key，精确但要有写路径）、版本号（全局 epoch + 用户级 epoch 双层，改配置只 bump epoch）。资源级判断的优化方向不是缓存结果，而是**把判断数据前置**（SQL 层 owner 条件、批量校验接口）。

取舍：权限模型选择即成本模型——RBAC（可预展开）< ABAC（属性计算，难缓存）< ReBAC（关系图，如 Zanzibar 风格，需专门服务+子问题缓存）；越灵活越贵。用"扁平化权限集合"存 Redis（`user_perms:{uid}` hash/set），读路径一次 SISMEMBER/O(1)；失效用"用户维版本 + 全局维版本"双 key 拼进缓存键，改角色 bump 全局版本让所有用户自然失效（省遍历删除，代价是全量重建一次）。

实战：中间件里权限检查先查"请求级去重"（同请求同权限只算一次），再查缓存，miss 才落库解析；监控三指标：解析耗时 P99、缓存命中率、权限变更到生效延迟。

```python
import time

# 1) 模型：角色层次 + 权限展开
ROLE_TREE = {
    "viewer": {"perms": ["doc:read"]},
    "editor": {"parents": ["viewer"], "perms": ["doc:write"]},
    "admin":  {"parents": ["editor"], "perms": ["user:manage", "audit:read"]},
}
USER_ROLES = {"alice": ["admin"], "bob": ["editor"]}

def resolve_perms(user):                      # 每请求现算：DFS 展开
    perms = set()
    stack = list(USER_ROLES.get(user, []))
    seen = set()
    while stack:
        role = stack.pop()
        if role in seen:
            continue
        seen.add(role)
        node = ROLE_TREE.get(role, {})
        perms |= set(node.get("perms", []))
        stack.extend(node.get("parents", []))
    return perms

# 现算成本画像
start = time.perf_counter()
for _ in range(10_000):
    resolve_perms("alice")
print("resolve 10k times      : %.1fms" % ((time.perf_counter() - start) * 1000))

# 2) 预展开缓存 + 双版本失效
GLOBAL_EPOCH = 0
perm_cache = {}                               # (uid, epoch) -> frozenset

def user_perms(user):
    key = (user, GLOBAL_EPOCH)
    if key not in perm_cache:                 # miss 才展开
        perm_cache[key] = frozenset(resolve_perms(user))
    return perm_cache[key]

def bump_global_epoch():                      # 改角色配置：新 key 自然失效旧缓存
    global GLOBAL_EPOCH
    GLOBAL_EPOCH += 1
    perm_cache.clear()                        # 实际实现靠版本键淘汰，这里演示语义

def has_perm(user, perm):
    return perm in user_perms(user)           # O(1) 成员判断

start = time.perf_counter()
for _ in range(10_000):
    has_perm("alice", "doc:write")
print("cached check 10k times : %.1fms" % ((time.perf_counter() - start) * 1000))
print("alice doc:write:", has_perm("alice", "doc:write"))

# 3) 资源级判断：无法预展开，前置到 SQL 条件
ORDER = {"o1": {"owner": "alice", "amount": 99}, "o2": {"owner": "bob", "amount": 99}}
def can_view_order(user, order_id):
    o = ORDER[order_id]
    return user == o["owner"] or has_perm(user, "audit:read")
print("bob view own order:", can_view_order("bob", "o2"),
      " alice view bob's (audit:read):", can_view_order("alice", "o2"))
```

**追问一**：全局 epoch 失效的代价与优化？——bump 后所有用户缓存全量 miss，第一波请求全是解析（缓存雪崩形态）；优化是"延迟 bump + 异步预热"或按用户分片 epoch（改某部门角色只 bump 该部门），把失效范围与变更范围对齐。

**追问二**：权限数据放 JWT claims 里是不是就不需要缓存了？——把展开后的权限塞 JWT 免了服务端查，但每次请求传输变大（头膨胀，Q6154）、撤销困难（token 有效期内权限冻结）、claims 体积限制；折中是 JWT 只带 role 名，服务端 role→perm 用长 TTL 缓存（角色配置变更频率低，TTL 5-15min 可接受）。

## 背诵要点
- 静态授权（role→perm 展开）可缓存、动态授权（资源实例判断）不可预展开，优化方向是数据前置。
- 失效三策：短 TTL（延迟生效）、写时删 key（精确）、版本 epoch（免遍历但全量重建）；epoch bump 有雪崩面要预热。
- 模型成本阶梯 RBAC < ABAC < ReBAC；JWT 塞权限省查询但付出传输与撤销代价。

## 复盘追问
- 改角色后"5 分钟后才生效"被投诉，如何评估切到写时失效的改造成本与风险？（写路径收口、失效遗漏风险、双策略并存灰度，讨论生效延迟 SLO）
- 权限检查 P99 从 0.5ms 涨到 30ms，如何区分是"缓存失效风暴"还是"解析路径回归"？（命中率指标与解析耗时分离、epoch bump 时间对齐，讨论告警设计）
