---
title: [Q6126] Cache-Control 语义混淆：no-store 与 no-cache 事故
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6126 · Cache-Control 语义混淆：no-store 与 no-cache 导致敏感页被缓存

> 难度:★★★☆☆ | 标签:事故复盘, HTTP 缓存, 安全

**问**:"no-cache 就是不缓存"这句话害过多少人？`no-cache`、`no-store`、`private`、`max-age=0, must-revalidate` 四者的精确语义差在哪？一次"离职员工在共享代理上看到他人账单"的事故链怎么还原？正确组合与测试方法是什么？

**答**:结论：四个词四件事：**no-cache = 可存、用前必验**（发条件请求 ETag/If-None-Match，304 就复用）；**no-store = 禁止存储**（任何缓存/磁盘都不能留，敏感数据唯一解）；**private = 只许浏览器私有缓存**（共享缓存——CDN/公司代理/网关——必须不存）；**max-age=0 + must-revalidate** ≈ 严格版 no-cache（过期即必验）。事故链还原：账单接口只加了 `Cache-Control: no-cache`（开发者以为"不缓存"）→ 公司出口代理认为"可存、需校验"→ 接口没实现 ETag，代理按启发式缓存直接回旧响应 → A 员工的账单页命中 B 的缓存 → 泄露。修复不只是换头：a) 敏感响应 `Cache-Control: no-store, private`（两个都写，防实现差异）；b) 检查上游——**请求头 `Cookie/Authorization` 存在时共享缓存本就该跳过**，但别赌它，自己的响应头才是事实源；c) 历史缓存里的敏感内容要换 URL 路径（缓存键换掉），旧响应无法远程作废。测试：对关键路径断言响应头 + 用缓存探测（同一连接两次请求看是否有 Via/X-Cache 变化、304 行为）验证链路。

```python
def cache_policy(path: str, has_credentials: bool, etag: str | None = None) -> dict:
    """按资源类型生成 Cache-Control 决策（返回 headers）。"""
    if path.startswith("/api/billing") or path.startswith("/profile"):
        # 敏感: 禁存 + 禁共享缓存（双保险, 防实现差异）
        return {"Cache-Control": "no-store, private", "Pragma": "no-cache"}
    if etag:                                     # 可缓存但必须校验: 走条件请求
        return {"Cache-Control": "no-cache", "ETag": etag}
    if has_credentials:                          # 带凭据的动态内容: 私有短缓存
        return {"Cache-Control": "private, max-age=30, must-revalidate"}
    return {"Cache-Control": "public, max-age=300"}   # 纯公共内容

# ---- 1) 四种语义对照 ----
for p, cred in [("/api/billing/123", True), ("/static/app.js", False),
                ("/feed", True), ("/feed", False)]:
    h = cache_policy(p, cred, etag="v3" if p == "/static/app.js" else None)
    print(f"{p:20s} cred={cred!s:5s} -> {h}")

# ---- 2) 事故判定表: no-cache 没实现 ETag 的后果 ----
def proxy_will_serve_stale(headers) -> bool:
    cc = headers.get("Cache-Control", "")
    if "no-store" in cc:
        return False
    if "no-cache" in cc:
        return "ETag" not in headers            # 必须校验但没有校验器 -> 启发式缓存兜底
    return "no-store" not in cc and "private" not in cc

incident = {"Cache-Control": "no-cache"}         # 事故现场: 只有 no-cache
fixed    = {"Cache-Control": "no-store, private"}
print("no-cache 无 ETag -> 代理可能回旧响应:", proxy_will_serve_stale(incident))
print("修复后 -> 代理必不缓存:", proxy_will_serve_stale(fixed))

# ---- 3) 测试断言模板（pytest 视角） ----
def test_sensitive_headers():
    h = cache_policy("/api/billing/1", True)
    assert "no-store" in h["Cache-Control"] and "private" in h["Cache-Control"]
    print("敏感路径断言通过: no-store + private 双头齐备")
test_sensitive_headers()
```

**追问一层**:`no-cache + ETag` 组合为什么不省流量但仍省算力？（304 往返还在、载荷免传；对"生成成本高、载荷大"的接口是收益，对高 QPS 小载荷是纯往返税，呼应 Q6070 条件请求）。
**追问二层**:`max-age=0, must-revalidate` 与 `no-cache` 在共享缓存上的差别？（语义近似"每次必验"，但 must-revalidate 只约束"过期后"，而 no-cache 是"任何复用前"；部分老缓存实现对其处理不一，敏感数据不要赌）。
**追问三层**:CDN 层如何与源站策略冲突？（CDN 默认尊重源站 Cache-Control，但部分支持面板级覆盖改写源站头——变更缓存策略要连同 CDN 配置一起评审，否则源站 no-store 被覆盖失效）。

## 背诵要点
- no-cache=存但必验（需 ETag 兜底）、no-store=禁存、private=禁共享缓存；敏感数据必须 `no-store, private` 双写。
- no-cache 而未实现 ETag → 代理启发式缓存兜底 → 串页事故；历史污染靠换 URL 缓存键清除。
- 上游凭据规则不可依赖；策略要以响应头为准并配自动化断言。

## 复盘追问
- 如何设计一个 CI 用例防止"敏感接口忘了 no-store"再犯（路由清单 × 策略矩阵断言）？
- 事故后要清理 CDN/代理里已缓存的敏感响应，有哪些手段、各自的局限是什么？
