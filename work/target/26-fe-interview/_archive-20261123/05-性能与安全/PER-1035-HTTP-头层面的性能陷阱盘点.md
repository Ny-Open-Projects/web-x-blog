---
title: [PER-1035] HTTP 头层面的性能陷阱盘点
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1035：HTTP 头层面的性能陷阱盘点

**答**：
- 陷阱一：缺 Content-Length 或错误 gzip 头导致重复下载；缺 Cache-Control 导致每次协商。
- 陷阱二：Vary 滥用（Vary: * 完全禁缓存）或漏 Vary: Origin/User-Agent 造成缓存污染。
- 陷阱三：Set-Cookie 体积大（多 cookie 累计数 KB）随每个请求上行，拖慢所有请求——合并/瘦身 cookie。
- 陷阱四：重定向链（多跳 301/302）每次多一个 RTT——直接指向最终地址，链长纳入监控。

```javascript
// 头部健康检查（响应头审计）
function auditHeaders(entry, headers) {
  const issues = [];
  if (!headers.get('cache-control')) issues.push('缺 Cache-Control');
  if (headers.get('vary') === '*') issues.push('Vary:* 禁缓存');
  if (!headers.get('content-encoding') && /\.(js|css)$/.test(entry.name)
      && !headers.get('content-length')?.startsWith('0'))
    issues.push('疑似未压缩');
  if (headers.get('set-cookie')?.length > 1000) issues.push('Cookie 过大');
  return issues;
}
// 定期跑线上资源抽样审计，头问题全站性影响最大也最便宜修复
```
