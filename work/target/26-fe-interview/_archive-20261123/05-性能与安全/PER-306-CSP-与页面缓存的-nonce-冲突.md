---
title: [PER-306] nonce 版 CSP 与 CDN 缓存冲突怎么办？静态 HTML 缓存场景的正确姿势？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-306：nonce 版 CSP 与 CDN 缓存冲突怎么办？静态 HTML 缓存场景的正确姿势？

**答**：
- 冲突机理：nonce 要求"每次响应随机"；而 HTML 被 CDN/浏览器缓存后，多个用户多次请求拿到**同一个 HTML = 同一个 nonce**——nonce 形同虚设（攻击者拿到一次页面就拿到有效 nonce），且缓存命中率越高的页面风险越大。
- 方案一（首选）：静态站点改用 **hash 版 CSP**——构建时算出所有入口脚本的 SRI hash，策略里写死 `'sha256-xxx'` 列表。hash 与内容绑定，缓存无害（内容不变 hash 不变）。缺点：动态 import 的 chunk 无法穷举 hash，需要 strict-dynamic 从信任的入口脚本传递。
- 方案二：nonce 页面禁缓存（HTML `no-store` 或短 s-maxage + Vary），牺牲缓存性能换 nonce 有效性；对高流量页不划算。
- 方案三：边缘动态改写（CDN edge function 在响应时注入 nonce 并改写 CSP 头）——性能与安全兼得，但架构成本高，大厂边缘函数场景可用。
- 结论：性能与安全的经典冲突点——静态 + 高缓存放 hash/strict-dynamic，动态 SSR 才用 nonce。

```text
静态 HTML（CDN 缓存）：
Content-Security-Policy: script-src 'sha256-入口A' 'sha256-入口B' 'strict-dynamic';
构建流程：构建产物 → 计算每个入口 chunk hash → 注入策略模板 → 发布
（hash 由构建器插件生成，产物变更 = hash 变 = 策略同步发布，不留死缓存）

动态 SSR（HTML 不缓存或短缓存）：
Content-Security-Policy: script-src 'nonce-{per-request-random}' 'strict-dynamic';
每请求生成 nonce，模板注入，无缓存复用问题
```
