---
title: "[Q6215] 静态资源指纹：内容哈希文件名与 immutable 的失效零成本"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6215 · 静态资源指纹：内容哈希文件名、immutable 与 HTML 的短缓存分工

难度：P6 ｜ 标签：静态资源、内容指纹、cache busting、Cache-Control immutable、缓存失效、CDN

**问**：为什么"改了 JS 但用户浏览器还是旧的"这类问题要用指纹文件名解决？`app.a1b2c3.js` 的哈希从哪来、什么变了哈希才变？`Cache-Control: immutable` 是干什么的，哪些浏览器支持？HTML 入口文件为什么**不能**长缓存，缓存策略应该怎么分层？发版瞬间"HTML 新、资源旧"的间隙怎么处理？

**答**：
结论：指纹（fingerprint/cache busting）= 把**内容哈希**编进资源文件名（`app.<hash>.js`）：内容不变 → URL 不变 → 浏览器/CDN 的长缓存永远有效；内容一变 → URL 变 → 等于一个全新的资源，旧缓存**自然失效且零清理成本**。这把"让缓存失效"从"刷缓存/等过期"变成"换个 URL"，是缓存一致性与缓存命中率的最优解。策略分层：指纹资源 `Cache-Control: public, max-age=31536000, immutable`（一年 + immutable 提示浏览器"该资源永不变，别发条件请求 revalidate"——Chrome/Firefox 支持，Safari 忽略但无害）；HTML 入口 `Cache-Control: no-cache`（可存但必须 revalidate，用 ETag/Last-Modified 协商，Q2427）或 max-age=60 极短——它是指纹 URL 的"目录"，必须新鲜才能引用到新资源。发版间隙问题：新 HTML 引用新资源 URL，只要**新旧资源 URL 都能访问**（保留旧指纹文件一段时间 / 发布顺序：先传资源后切 HTML），就不存在"404 窗口"。

取舍：a) 哈希来源：构建期对**文件内容**做哈希（webpack/whitehouse hash），不是版本号或时间戳——时间戳会让未变更资源也失效，浪费命中率；b) 长缓存与"回滚"：回滚旧版本 = 引用旧指纹 URL，前提是旧文件还在——发布保留至少 2 个版本的资源文件；c) CDN 层：指纹资源可无限期缓存（URL 即版本），HTML 不缓存或短缓存 + 主动 purge；d) `immutable` 的价值：省掉 revalidate 的往返（对已缓存的资源连 If-None-Match 都不发），高频小资源收益明显；e) 动态加载的 chunk（路由级懒加载）同样指纹化，运行时清单（manifest）随 HTML 走，避免"旧清单引用已删除 chunk"——与旧版本保留策略联动。

实战：事故形态是"发版后部分用户白屏：HTML 缓存了 1 小时（当年为性能设的），引用的旧 JS 文件在发布时被构建清理删掉，缓存里的 HTML 引用 404；修复：HTML 改 no-cache + ETag 协商，资源指纹化 immutable 一年，发布保留最近 3 个版本资源，上线顺序改为资源先行"。下面实现指纹与缓存头决策。

```python
import hashlib

RELEASE_KEEP = 3  # 保留最近 3 个版本的指纹资源


def fingerprint(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()[:12]


def build_asset(content: bytes, name: str = "app") -> tuple:
    fp = fingerprint(content)
    filename = f"{name}.{fp}.js"
    headers = {"Cache-Control": "public, max-age=31536000, immutable"}
    return filename, headers


def serve_html(content_hash: str) -> dict:
    # HTML 是指纹 URL 的目录: 必须可缓存但强制 revalidate
    return {"Cache-Control": "no-cache", "ETag": f'"{content_hash}"'}


js_v1 = b"console.log('v1')"
js_v2 = b"console.log('v2')"

n1, h1 = build_asset(js_v1)
n2, h2 = build_asset(js_v2)
print("[1] v1 资源:", n1, h1["Cache-Control"])
print("[2] v2 资源:", n2, "——内容变了才变 URL, 旧缓存零清理")
print("[3] HTML 响应头:", serve_html("html-etag-v2"), "——no-cache + 协商, 指纹目录必须新鲜")
print("[4] 发布纪律: 资源先上, 保留最近", RELEASE_KEEP, "个版本 -> 新旧 HTML 都有资源可引")
print("[5] immutable 效果: 已缓存资源不再发 If-None-Match revalidate, 省一次往返")
```

**追问一**：`no-cache` 和 `max-age=0` 的区别是什么？为什么 HTML 用前者？—— `no-cache` = "可以存副本，但每次使用前必须 revalidate"（配合 ETag/Last-Modified 得到 304 就不传 body，开销小）；`max-age=0` 单独用时语义接近但不含"必须 revalidate"的明确表达，需要配 `must-revalidate` 才严格。HTML 的理想态是"副本 + 每次校验"：命中 304 时零 body 流量，同时保证拿到最新指纹清单——这正是 no-cache + ETag 的组合。`no-store` 则是完全不存（登录页等敏感场景），别误用——它会把静态资源缓存也一并压掉（在同路径语义下）。

**追问二**：CDN 层怎么配合指纹策略，purge 还需要吗？—— 指纹资源：CDN 可用超长 TTL，回源频率≈0，purge 基本不需要（URL 变了就是新对象）；需要 purge 的只剩 HTML（或换成"HTML 也指纹化"的极端方案——但入口 URL 必须稳定，做不到）。运维上保留的 purge 能力是**兜底**：发版事故（错版本上到 HTML）、安全响应（紧急下架资源）时手动清 CDN 的 HTML 缓存。配套监控：CDN 命中率、回源量在发布窗口的波动——发布后命中率骤降若持续超过一个缓存周期，说明指纹没生效（比如 URL 带了时间戳查询参数），这是静默的缓存失效，账要盯（与 Q6056 的 CDN 卸载成本账联动）。

## 背诵要点
- 指纹 = 内容哈希进文件名：内容变则 URL 变，缓存失效零成本；时间戳/版本号哈希是反模式（未变更也失效）。
- 分层：指纹资源 max-age=31536000 + immutable（免 revalidate）；HTML no-cache + ETag 协商——HTML 是指纹目录必须新鲜。
- 发布纪律：资源先上、保留近 3 版、HTML purge 做兜底；监控 CDN 命中率发现指纹失效。

## 复盘追问
- 发版白屏：旧 HTML 引用被删除的 JS，怎么从机制上根治？（HTML no-cache+ETag、资源指纹 immutable、保留多版本、资源先行）
- immutable 与 no-cache 分别适合什么资源？（内容寻址的长缓存 vs 需要每次校验的清单型文档）
