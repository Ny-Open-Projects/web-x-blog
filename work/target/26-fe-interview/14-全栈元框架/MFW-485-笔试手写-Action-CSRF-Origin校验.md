---
title: [MFW-485] 笔试：手写 Server Action CSRF Origin 校验中间件
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-485：Server Action CSRF Origin 校验中间件
**需求**：实现 `actionCsrf(req, { hosts })`：1) 所有 Action 请求（POST + `Next-Action` 头存在）必须校验 Origin 头与 Host 匹配（同源策略——Action 天然防 CSRF 的实现原理）；2) Origin 缺失：非浏览器客户端（curl/服务端调用）放行但打标 `non-browser`（写审计日志）；3) Origin 是自家多域名之一（hosts 白名单）也放行；4) 其余一律 403 并计入 `blocked` 计数（阈值告警由调用方处理）；5) GET 请求不校验（Action 不接受 GET）。

```javascript
export function actionCsrf(req, { hosts = [] } = {}) {
  const method = (req.method || 'GET').toUpperCase()
  if (!['POST', 'PUT', 'PATCH', 'DELETE'].includes(method))
    return { pass: true, tag: 'not-mutation' }
  if (!req.headers.get('next-action'))
    return { pass: true, tag: 'not-action' }

  const origin = req.headers.get('origin')
  if (!origin) {
    // 非浏览器客户端没有 Origin：放行但必须留痕（防伪装成服务端调用需另配 mTLS/签名）
    return { pass: true, tag: 'non-browser', warn: true }
  }
  const allowed = [req.headers.get('host'), ...hosts]
    .filter(Boolean)
    .map(h => h.replace(/^https?:\/\//, '').split(':')[0])
  try {
    const o = new URL(origin).hostname
    if (allowed.includes(o)) return { pass: true, tag: 'same-site' }
  } catch { /* malformed origin */ }
  return { pass: false, tag: 'csrf-blocked', status: 403 }
}
```

**评分点**：
- 只对 POST + Next-Action 头校验（缩小判定面，GET 不误伤）
- Origin 与 Host 同源比较取 hostname（端口/协议差异处理明确）
- 缺 Origin 放行但留痕（非浏览器调用合法，但必须可审计）
- 畸形 Origin 进 403（try/catch 不吞判——解析失败即不可信）
