---
title: [PER-353] DNS 预解析与预连接什么时候有效什么时候浪费？资源提示的收益判定方法？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-353：DNS 预解析与预连接什么时候有效什么时候浪费？资源提示的收益判定方法？

**答**：
- 有效场景：预解析/预连接要打在"即将用到且当前未连接"的域上——三方脚本域（用户交互后加载）、字体 CDN、图片 CDN、下一跳页面（导航前）。有效收益 = 省 DNS+TCP+TLS（约 1~3 个 RTT，弱网 200~600ms）。
- 浪费场景：当前页面已经与目标域建连（HTTP2 多路复用下同一连接复用）——预连接白开；预连接太多（>4~5 个域）挤占连接池与 socket，反而挤掉真正要用的连接；预解析域根本不会被用到（预测错误）。
- 收益判定：Resource Timing 里对比"有预连接提示"与"无提示"页面的 connect 段耗时（A/B 或同页面分半）；DevTools Network 面板看请求是否复用已建立连接（无 DNS/TCP/SSL 条）。Lazy FoT：首字节后才有响应的资源是预连接主要目标。
- 工程化：预连接清单进配置（域名+触发时机），随三方网关维护；量级控制（每页 ≤ 5 个）；失败监控无必要（预连接失败静默无害）。

```html
<!-- 有效：用户点击后才加载的三方域，提前建连 -->
<link rel="preconnect" href="https://chat.widget.io" crossorigin>
<link rel="dns-prefetch" href="https://chat.widget.io">   <!-- 老浏览器兜底 -->
<!-- 浪费：主资源已同域建连，再 preconnect 无收益 -->
<!-- 判定方法：Resource Timing 对比 connect 段 -->
```
```javascript
const res = performance.getEntriesByType('resource').find(r => r.name.includes('widget.io'));
const connect = res.connectEnd - res.connectStart;
const dns = res.domainLookupEnd - res.domainLookupStart;
// dns≈0 且 connect≈0 → 复用了预连接/已有连接（提示生效）
// dns>0 && connect>50ms → 没享受预连接（提示缺失或时机错误）
```
