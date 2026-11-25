---
title: "[Q6241] GraphQL 查询治理：深度/复杂度限制与持久化查询"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6241 · GraphQL 查询治理：深度/复杂度限制与持久化查询

难度：P6 ｜ 标签：GraphQL、查询深度、复杂度计算、APQ 持久化查询、恶意查询防护、resolver 成本、分页放大

**问**：GraphQL 单端点自由查询带来了什么新的攻击面——恶意深查询/大查询怎么打垮 resolver（N+1 已由 DataLoader 解，Q6022，但"单次查询本身过大"怎么防）？深度限制与复杂度计算分别怎么实现、为什么光限制深度不够？APQ（Automatic Persisted Queries）的握手协议怎么工作？

**答**：
结论：GraphQL 的单端点 + 客户端自定义查询形状 = **查询成本不可预算**，攻击面是"一次请求让服务端做指数级的活"：①**深查询**——自引用关系链（`user.friends.friends.friends...`）让 resolver 递归 N 层，每层一个扇出；②**列表放大**——一个返回 100 条的列表字段里嵌套子字段，成本 = 父列表 × 子字段 resolver 次数（DataLoader 只把每次 fan-in 合并成批量查询，**乘法本身没变**——100 条 × 10 子字段 = 1000 次 resolver 执行）；③**大字段**——不带分页的 `allOrders` 直接全表拉。治理三层：①**深度限制**——AST 上算最大嵌套层数（`query { user { friends { friends } } }` = 3），超过拒绝；实现简单但**绕过容易**：`a { b1 { c } b2 { c } ... }` 的**广度攻击**深度只有 2，成本却线性于兄弟字段数；②**复杂度计算**——给每个字段配成本系数（叶子 1、列表字段 1×列表上限、对象字段乘子），从 AST 自底向上累加：`cost(field) = own + Σ children`，列表字段乘 first/page 参数——这是把"查询形状"折算成预估 resolver 执行数，广度与深度一起兜住；③**限流/预算**——复杂度超限的分级响应（拒单 / 降分页 / 计入限流配额），配合分页上限硬约束（Q1353 的参数校验）。APQ 持久化查询：客户端先发 `{query 的 sha256}`，服务端查缓存命中直接执行、未命中返回 `PersistedQueryNotFound` 让客户端补发全文——**生产形态是"只允许白名单 hash 执行"**（服务端构建时预注册查询），自由查询面直接归零，是 BFF/移动端场景的最强治理（配合 APQ 缓存层如 Apollo 的协议：`extensions.persistedQuery.version=1&sha256Hash`）。

取舍：a) 治理梯度：APQ 白名单（最严，适合移动端/自家 BFF）> 复杂度限制（公开 GraphQL 必备）> 深度限制（辅助）> 无治理（内部玩具）；b) 复杂度系数怎么定：按 resolver 的真实执行成本标定（DB 查询字段 10-50、内存组合字段 1），用 Q6022 的 DataLoader 批量后成本下降——系数要随数据层优化**重新标定**，否则限流误伤正常查询；c) 报错面：超限响应要给出"是哪个维度超了"（depth/cost/分页），前端可自助修正；d) AST 计算的实现：不要正则解析 GraphQL——用 graphql-core 的 `parse()` 拿 AST 遍历，成熟库（graphql-python 生态的 validation rule 机制）把深度/复杂度做成 validation rule 插进校验链；e) 监控：记录每查询的实测 cost vs 预估 cost，漂移大说明系数失真——复杂度模型是"活的配置"不是一次性设置。

实战：事故形态是"公开 GraphQL 端点被爬虫用 800 层深的 `friends` 自引用查询打，单请求把 CPU 打满 90 秒；上深度限制 10 层后被绕过（100 个兄弟字段 × 每字段一个 DB 查询），P99 照样爆炸。终态：复杂度限制（列表字段乘分页上限、叶子按 DB 成本标定）+ 全部字段分页强制 + 移动端切 APQ 白名单，恶意查询在 validation 阶段就被 4xx 挡下，DB QPS 回落 87%"。下面实现深度/复杂度计算与 APQ 握手的核心逻辑。

```python
# GraphQL 查询治理: 深度限制、复杂度计算与 APQ 握手
import hashlib
import json

# 字段成本表: own = 自身执行成本, LIST = 列表字段(乘分页上限)
FIELD_COST = {
    "user": 2, "friends": 3, "orders": 8,
    "name": 0, "id": 0, "total": 1,
}
LIST_FIELDS = {"friends", "orders"}
PAGE_LIMIT = 20

def analyze(node: dict, depth: int = 1):
    """自顶向下递归: 返回 (子树最大深度, 子树总复杂度); 列表字段成本乘分页"""
    field = node["field"]
    children = node.get("children", [])
    own = FIELD_COST.get(field, 5)                      # 未知字段给高成本防漏配
    multiplier = PAGE_LIMIT if field in LIST_FIELDS else 1
    max_child_depth, child_cost = 0, 0
    for ch in children:
        d, c = analyze(ch, depth + 1)
        max_child_depth = max(max_child_depth, d)
        child_cost += c
    # 列表字段: 子树成本按每行执行一次 -> 乘分页上限
    return max_child_depth + 1, own + multiplier * child_cost

def validate(query: dict) -> dict:
    depth, cost = analyze(query)
    if depth > 6:
        return {"depth": depth, "cost": cost, "verdict": "reject: 深度超限"}
    if cost > 300:
        return {"depth": depth, "cost": cost, "verdict": "reject: 复杂度超限"}
    return {"depth": depth, "cost": cost, "verdict": "allow"}

print("[1] 正常查询: user { name orders { total } }")
normal = {"field": "user", "children": [
    {"field": "name"},
    {"field": "orders", "children": [{"field": "total"}]},
]}
print("   ", json.dumps(normal)[:44], "... ->", validate(normal))

print("[2] 深查询被深度限制拦下: user { friends { friends { friends ... } } }")
deep = {"field": "user"}
cur = deep
for _ in range(8):
    nxt = {"field": "friends"}
    cur["children"] = [nxt]
    cur = nxt
print("    8 层自引用 ->", validate(deep))

print("[3] 广度攻击: 深度只有 2, 但 20 个兄弟列表字段 -> 深度限制拦不住, 复杂度拦得住")
wide = {"field": "user", "children": [
    {"field": "orders", "children": [{"field": "total"}]} for _ in range(20)
]}
print("    20 个 orders 兄弟 ->", validate(wide))

print("[4] APQ 持久化查询: 先发 hash, 服务端查不到才要全文")
query_text = "query { user { name orders { total } } }"
query_hash = hashlib.sha256(query_text.encode()).hexdigest()
store = {query_hash: query_text}                        # 服务端/CDN 侧缓存

first_req = {"extensions": {"persistedQuery": {"version": 1, "sha256Hash": query_hash}}}
print("    第一次: 只发 hash ->", "PersistedQueryNotFound (要求补发全文)" if query_hash not in {} else "命中")
# 演示: 若 hash 不在缓存 (首次), 服务端返回 not found; 客户端补发全文后缓存
print("    补发全文后缓存:", query_hash in store, "-> 后续请求只带 hash, 查询面归零")
```

**追问一**：复杂度模型的"系数标定"怎么做才不失控？为什么"实测成本与预估成本的漂移监控"是复杂度治理的配套必备？—— 标定流程：①**按 resolver 类型分级**——纯内存组合（拼接字段）=0-1、单行 DB 查询（N+1 被 DataLoader 合并后是批量查询的均摊成本）=批量行数、聚合/全表扫描=高；②**用离线 replay 标定**——生产查询日志回放，统计每个字段的实测 resolver 执行数与 DB 行数，拟合系数（一次 DB 查询拉 500 行的字段系数不该是 1）；③**留安全余量**——系数 × 1.5 上浮，宁可让个别正常查询过限走人工白名单，不可让恶意查询贴线通过。漂移监控的必要性：数据层优化会改变真实成本——加了 `select_related`（Q761）后 orders 的实际成本降了一个量级，旧系数把正常用户挡在限外（误伤=事故）；反过来新加了昂贵聚合字段没更新系数，恶意查询用它的贴线成本打穿（漏防=事故）。工程形态：每次 schema 变更跑"系数审计 CI"（对 schema diff 出的新字段自动提 PR 补成本表），线上采样对比预估/实测分布——**复杂度模型与 schema 一样是版本化资产**。

**追问二**：APQ 白名单模式下，前端迭代频繁（每天新查询）怎么运维？"查询版本与发布节奏"怎么绑定？—— APQ 白名单把"查询即 API 契约"固化：服务端 schema 发布时同步注册当前版本全部查询 hash。运维绑定：①**构建期注册**——前端构建流水线抽取本次用到的全部查询文本 → 计算 hash → 作为构建产物随前端发布上报，后端在网关层按"版本窗口"双活（新旧 hash 并存一个发布周期，Q2171 的双运行路由同思路）；②**版本回滚**——hash 表按版本快照存储，回滚前端即回滚 hash 集（查询面与代码面同进退）；③**长尾治理**——监控"未注册 hash 被拒"的样本，若是新版本漏注册自动补录，若持续是陌生 hash（第三方爬虫试探）直接封禁计数；④**调试通道**——开发环境保留自由查询 + 只读账号/沙箱 schema，生产全白名单。这个模式的本质：把 GraphQL 的"客户端自由"收缩为"构建期协商"——牺牲了 exploratory 灵活性，换来与 REST/固定端点同等甚至更强的可预算性，是 BFF 边界（Q1628）最稳的形态。

## 背诵要点
- GraphQL 攻击面=查询成本不可预算：深查询（自引用递归）、广度攻击（深度浅但兄弟字段多）、列表放大（列表×子字段，DataLoader 合并不减乘法）。
- 治理梯度：APQ 白名单（移动端/BFF 最强）> 复杂度限制（成本系数自底向上累加、列表乘分页上限）> 深度限制（辅助）；系数要随 schema/数据层优化重新标定+漂移监控。
- APQ：先发 sha256 → 未命中返回 PersistedQueryNotFound 补发全文；生产白名单=构建期注册+版本窗口双活+回滚同快照。

## 复盘追问
- 为什么光有深度限制防不住恶意查询？（广度攻击深度只有 2 但成本线性于兄弟字段数；复杂度计算把深度广度一起折算成预估 resolver 执行数）
- APQ 白名单模式下前端高频迭代怎么运维？（构建期抽查询算 hash 上报、版本窗口双活、回滚同快照、陌生 hash 拒绝+监控；查询面与发布节奏绑定）
