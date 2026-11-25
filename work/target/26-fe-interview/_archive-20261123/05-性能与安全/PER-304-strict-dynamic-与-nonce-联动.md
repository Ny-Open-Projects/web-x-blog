---
title: [PER-304] CSP 的 strict-dynamic 是什么？它与 nonce 如何配合解决"动态加载脚本"问题？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-304：CSP 的 strict-dynamic 是什么？它与 nonce 如何配合解决"动态加载脚本"问题？

**答**：
- 问题：现代打包器/加载器会在运行时动态插入 script（chunk 加载），静态白名单根本写不完；而 `unsafe-inline`/宽域名白名单又等于没设防。
- strict-dynamic 语义：**被页面信任的脚本（带 nonce/hash）通过 createElement('script') 加载的脚本自动被信任**，信任沿加载链传递；同时它使同策略里的主机白名单对"动态加载"失效（向后兼容的老浏览器仍走白名单，新浏览器优先 strict-dynamic）。
- 组合形态：`script-src 'nonce-xxx' 'strict-dynamic' https:` —— 新浏览器走 nonce+strict-dynamic，老浏览器（不认识 strict-dynamic）忽略它走 https 白名单，两端都安全。
- 注意：JSONP 类"URL 由数据拼接"的加载仍要校验（strict-dynamic 信任的是"由信任脚本发起"，若信任脚本被注入污染，信任链也被污染——所以 strict-dynamic 是纵深一环，不是全部）；worker/script 的 importScripts 同样受信传递。

```html
<!-- 服务端模板注入一次性 nonce（每次响应随机） -->
<script nonce="{{cspNonce}}" src="/main.js"></script>
<!-- main.js 里动态加载 chunk：无需为每个 chunk URL 加白名单 -->
<script nonce="{{cspNonce}}">const s = document.createElement('script');
s.src = '/chunk-' + route + '.js'; document.head.append(s);</script>
```
```text
响应头：
Content-Security-Policy: script-src 'nonce-E3x9...' 'strict-dynamic' https: 'unsafe-inline' https:;
语义解读（新浏览器）：'unsafe-inline' https: 被忽略（strict-dynamic 存在时降级），只认 nonce 与信任链；
老浏览器：忽略 'nonce' 'strict-dynamic'，退回 'unsafe-inline' https:（弱策略兜底）。
```
