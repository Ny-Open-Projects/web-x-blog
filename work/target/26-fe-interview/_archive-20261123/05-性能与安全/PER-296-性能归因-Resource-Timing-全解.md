---
title: [PER-296] Resource Timing 的完整字段怎么读？如何用它在 RUM 里拆解"每个请求慢在哪一段"？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-296：Resource Timing 的完整字段怎么读？如何用它在 RUM 里拆解"每个请求慢在哪一段"？

**答**：
- 字段时间轴：startTime（开始）→ redirectStart/End（重定向，跨域不可见）→ domainLookupStart/End（DNS）→ connectStart/End（TCP+TLS，secureConnectionStart 是 TLS 开始）→ requestStart（请求发出）→ responseStart（首字节，TTFB）→ responseEnd（接收完）。
- 段拆解公式：DNS = domainLookupEnd - domainLookupStart；TCP = connectEnd - connectStart（减去 TLS 部分）；TLS = connectEnd - secureConnectionStart；请求等待 = responseStart - requestStart（网络+服务端）；下载 = responseEnd - responseStart。
- 归因规则：DNS 长 → DNS 预解析/本地缓存；TCP/TLS 长 → 复用连接（同域名、HTTP2）、预连接；请求等待长 → 服务端或 RTT（结合 Server-Timing 区分）；下载长 → 体积或带宽（CDN）。
- RUM 采集注意：跨域资源默认只有时长无分段（Timing-Allow-Origin 头放开）；buffered 观察全量资源，体积大要采样上报（按资源类型分层采样，图片/脚本重点）。

```javascript
function breakdown(res) {
  const d = (a, b) => Math.round(b - a);
  return {
    url: res.name.split('/').pop().slice(0, 40),
    dns: d(res.domainLookupStart, res.domainLookupEnd),
    tcp: d(res.connectStart, res.secureConnectionStart > 0 ? res.secureConnectionStart : res.connectEnd),
    tls: res.secureConnectionStart > 0 ? d(res.secureConnectionStart, res.connectEnd) : 0,
    wait: d(res.requestStart, res.responseStart),      // 网络 + 服务端（看 Server-Timing 细分）
    download: d(res.responseStart, res.responseEnd),
    transferSize: res.transferSize,                    // 0 = 命中缓存（无传输）
    decodedBodySize: res.decodedBodySize,
  };
}
new PerformanceObserver((l) => {
  for (const r of l.getEntries()) {
    if (r.duration > 1000 || r.decodedBodySize > 500 * 1024) report({ type: 'slow-resource', ...breakdown(r) });
  }
}).observe({ type: 'resource', buffered: true });
// 响应头需要 Timing-Allow-Origin: * 才能读到分段字段（否则全是 0）
```
