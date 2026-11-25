---
title: [Q6140] Vary 头与缓存键碎片化原理
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6140 · Vary 头与缓存键碎片化的原理

难度：P6-P7 | 标签：Vary、HTTP 缓存、缓存键、原理深挖

**问**：为什么给响应加 `Vary: User-Agent` 会让 CDN 缓存命中率从 90% 跌到几乎为 0？Vary 的缓存键推导规则是什么？`Vary: *` 的特殊语义？Accept-Encoding 引起的缓存碎片如何治理？

**答**：

**结论**：Vary 的语义是"此响应的表示随这些请求头变化"，缓存（CDN/代理/浏览器）因此把**每个不同的 Vary 头取值组合当作独立缓存条目**：`Vary: User-Agent` 时每个 UA 字符串都生成一个键，UA 空间近乎无限（版本号、设备型号），缓存被碎片化成海量低复用条目——命中率归零。键推导规则：对响应中列出的每个 Vary 头，取**请求中该头的原始值**（大小写规范化、多值头排序后拼接）作为次级键与 URL 组合；请求未带该头时按"无值"生成条目，同一 URL 在缓存中可能同时存在 N 个变体。`Vary: *` 表示"匹配任何请求头都不可复用"，等效于不可缓存（许多缓存直接不存）。Accept-Encoding 碎片（gzip/br/identity 变体）是常见工程点：现代 CDN 会做编码归一（存储一种编码按需转码），自建代理则要控制只缓存压缩变体并统一 vary 键。

**取舍**：治理原则——Vary 只声明"真正影响表示"的头：语言（Accept-Language）用路径化（/zh/、/en/）替代 Vary；设备差异用同构响应+CSS 响应式替代 UA-Vary；登录态差异绝不用 Vary 解决（改 Cookie 层私有缓存 `Cache-Control: private`）。验证工具：响应里检查 Vary 实际头集合，CDN 后台看 per-URL 变体数。

**实战**：自建代理（nginx）的坑：`proxy_set_header` 把上游 Accept-Encoding 固定为 gzip 可减少变体；但 Vary 头会原样透传给下游缓存——上游 API 返回的 `Vary: Origin`（CORS 常见）会让代理缓存按 Origin 碎片化，需要在网关层改写或剔除。

```python
# 用纯 Python 实现一个遵循 Vary 语义的最小缓存，展示键碎片化机制
from collections import defaultdict

class VaryCache:
    def __init__(self):
        self.store = {}                     # (url, variants) -> response
    @staticmethod
    def _variants(vary_headers, request_headers):
        if vary_headers == "*":
            return None                     # 不可复用
        return tuple(
            (h, request_headers.get(h, "")) for h in vary_headers)
    def lookup(self, url, vary, req_headers):
        v = self._variants(vary, req_headers)
        if v is None:
            return None
        return self.store.get((url, v))
    def put(self, url, vary, req_headers, body):
        v = self._variants(vary, req_headers)
        if v is None:
            return
        self.store[(url, v)] = body

cache = VaryCache()
cache.put("/api/x", ["Accept-Encoding"], {"Accept-Encoding": "gzip"}, "gzip-body")
cache.put("/api/x", ["Accept-Encoding"], {"Accept-Encoding": "br"}, "br-body")

print("gzip 变体命中 ->", cache.lookup(
    "/api/x", ["Accept-Encoding"], {"Accept-Encoding": "gzip"}))
print("同一 URL 条目数 =", len([k for k in cache.store if k[0] == "/api/x"]))

# User-Agent 碎片化演示：三个 UA 三个条目
for ua in ["Chrome/120", "Safari/17", "curl/8.4"]:
    cache.put("/page", ["User-Agent"], {"User-Agent": ua}, f"page-{ua}")
print("UA-Vary 条目数 =", len([k for k in cache.store if k[0] == '/page']))

# Vary: * -> 永不命中
cache.put("/nonce", ["*"], {}, "x")
print("Vary:* lookup ->", cache.lookup("/nonce", ["*"], {}))
```

**追问 1**：多值请求头（如多个 Accept-Language）在变体键里如何规范化？
答：规范做法是按头内值排序、去重后以逗号拼接生成键；RFC 实现差异大，这也是"同一语言不同客户端各自条目"碎片来源——应用层直接路径化语言可彻底规避。

**追问 2**：`Vary: Origin` 为什么在 CORS API 响应里常见？该如何处理？
答：当响应随 Origin 变化（Access-Control-Allow-Origin 回显请求 Origin）时必须 Vary: Origin 防止把 A 站的 CORS 头缓存给 B 站；网关侧若已知固定域名白名单，可改写为单值 Allow-Origin 并移除 Vary。

**追问 3**：CDN 的"缓存键配置"与 Vary 的关系？
答：现代 CDN（如 Fastly/CloudFront）允许自定义缓存键（忽略/归一 UA 等头），这实际上是"在键推导层覆盖 Vary 语义"——键里不包含的头不会碎片化，但要确认响应内容真的不依赖该头，否则出现内容错配。

## 背诵要点

- Vary 让缓存按"URL + 列出的请求头取值组合"生成独立条目；UA/Language 这类高基数头直接碎片化、命中率归零。
- `Vary: *` 等效不可缓存；Accept-Encoding 变体靠 CDN 转码归一或固定上游编码治理。
- 高基数头应路径化（/zh/）或响应式同构替代；CORS 的 Vary: Origin 防头错配，白名单场景可去除。

## 复盘追问

- 线上如何发现"某个头导致的缓存碎片"？(提示：CDN 变体数指标 + 响应头审计)
- 设计一个公共 API 的缓存键规范，哪些头允许入键？(提示：白名单 + 归一化规则 + 变体数上限)
