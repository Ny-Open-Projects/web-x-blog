---
title: [PER-893] 移动端 HTTPDNS 的接入场景与降级：什么时候值得用、失败如何回退系统 DNS
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-893：移动端 HTTPDNS 的接入场景与降级：什么时候值得用、失败如何回退系统 DNS

**答**：
- 价值场景：LocalDNS 劫持（解析到错误节点）、跨运营商解析不准、海外调度不准——表现为部分地区用户慢或失败率高。
- 实现：App 内置 HTTPDNS SDK（原生侧），H5 可通过容器桥获取解析结果或服务端下发优选 IP；结果缓存带 TTL（一般 60~300s），预解析高频域名。
- 降级链：HTTPDNS 失败/超时 → 系统 DNS；HTTPDNS 结果连不通 → 回退系统 DNS 结果重试；两者都失败 → 本地兜底 IP 列表（运维下发）。
- 注意：HTTPDNS 返回的 IP 与证书域名校验无冲突（SNI 仍带域名）；IP 直连请求必须带 Host 头。

```javascript
async function fetchWithHttpdns(path) {
  const host = new URL(BASE_URL).host;
  let ip;
  try {
    ip = await bridge.httpdnsLookup(host);                     // 1. HTTPDNS 优先
  } catch { /* 降级系统 DNS */ }
  if (ip) {
    try {
      return await requestDirect(ip, host, path);              // IP 直连，SNI/Host 带域名
    } catch { report('httpdns-direct-fail', { host }); }      // 2. 失败回退
  }
  try { return await fetch(BASE_URL + path); }                 // 系统 DNS
  catch { return requestBackupList(path); }                    // 3. 本地兜底 IP 列表
}
function requestDirect(ip, host, path) {
  return fetch(`https://${ip}${path}`, {
    headers: { Host: host },                                   // 必须带 Host
  });
}
```
