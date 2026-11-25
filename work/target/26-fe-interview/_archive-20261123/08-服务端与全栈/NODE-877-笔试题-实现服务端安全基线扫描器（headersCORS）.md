---
title: [NODE-877] 笔试题——实现安全基线扫描器（headers/CORS/cookies）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-877：手写安全基线

**需求与边界**：
- 需求：安全基线扫描（SCN-NODE-719）——① 响应头基线（CSP/XFO/HSTS/Referrer-Policy——helmet 基线，SCN-BLD-246）；② CORS 配置审计（origin 白名单——credentials 冲突防御）；③ Cookie 安全（Secure/HttpOnly/SameSite）；④ 基线漂移（配置变更检测——SCN-ENG-861）。
- 边界：① CORS 的 credentials 与通配符冲突（origin: * + credentials 冲突——浏览器拒绝但配置层就拦）；② Cookie 属性逐项（SameSite=Lax 默认——CSRF 防御）；③ 扫描进 CI（配置漂移——SCN-ENG-861）。

**答**：
```javascript
function securityBaseline(resp, config) {
  const issues = [];
  for (const [header, expected] of Object.entries(BASELINE_HEADERS))   // CSP/XFO/HSTS
    if (!resp.headers[header] || !resp.headers[header].includes(expected))
      issues.push({ type: 'HEADER_MISSING', header, fix: `设置 ${header}: ${expected}` });
  if (config.cors.origin === '*' && config.cors.credentials)
    issues.push({ type: 'CORS_CONFLICT', fix: 'origin:* 与 credentials 冲突——枚举 origin' });   // CORS 冲突
  for (const c of config.cookies)
    if (!(c.secure && c.httpOnly && ['Lax', 'Strict', 'None'].includes(c.sameSite)))
      issues.push({ type: 'COOKIE_INSECURE', cookie: c.name, fix: 'Secure+HttpOnly+SameSite' });   // Cookie
  return { issues, gate: issues.every(i => i.level !== 'block') };   // CI 门禁（SCN-OPS-289）
}
```

**评分点**:
- 响应头基线（helmet 套件——SCN-BLD-246）。
- CORS credentials 与通配符冲突检测（安全红线）。
- Cookie 三属性逐项校验（Secure/HttpOnly/SameSite）。
- CI 门禁 + 基线漂移（SCN-OPS-289/ENG-861）。
