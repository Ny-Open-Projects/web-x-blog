---
title: [SCN-105] 监控平台发现前端日志里打出了用户手机号与 token，如何做脱敏治理？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-105：监控平台发现前端日志里打出了用户手机号与 token，如何做脱敏治理？
**答**：
- 三处治理：入口（上报前统一脱敏管道：字段名黑名单 + 正则识别手机号/身份证/银行卡做掩码）、存量（已上报日志批量删除或加密，评估合规影响）、根因（生产构建 drop console，业务禁止随手 log 敏感数据）。
- 脱敏管道必须封装进 logger/上报函数内部，让业务"绕不开"，而不是依赖每个人自觉。
- 递归处理对象与数组，嵌套 payload 里的敏感字段也要覆盖。

```javascript
// 日志脱敏管道：上报前统一清洗，字段黑名单 + 正则掩码双层拦截
const SENSITIVE_KEYS = /^(password|token|authorization|idcard|session)$/i;

const PATTERNS = [
  { re: /1[3-9]\d{9}/g, mask: (m) => m.slice(0, 3) + '****' + m.slice(7) },  // 手机号
  { re: /\b\d{17}[\dXx]\b/g, mask: () => '**********' },                     // 身份证
  { re: /\b\d{16,19}\b/g, mask: (m) => '****' + m.slice(-4) },               // 银行卡
];

function sanitize(value, key = '') {
  if (value == null) return value;
  if (SENSITIVE_KEYS.test(key)) return '***';          // 字段名命中直接掩码
  if (typeof value === 'string') {
    return PATTERNS.reduce((s, p) => s.replace(p.re, p.mask), value);
  }
  if (Array.isArray(value)) return value.map((v) => sanitize(v));
  if (typeof value === 'object') {
    return Object.fromEntries(
      Object.entries(value).map(([k, v]) => [k, sanitize(v, k)]));
  }
  return value;
}

// logger 封装：所有上报必经脱敏，业务绕不开
function report(payload) {
  navigator.sendBeacon('/api/monitor', JSON.stringify(sanitize(payload)));
}

// 根因防线：生产构建剔除 console，防止业务随手 log 敏感数据
// vite.config.js -> esbuild: { drop: ['console', 'debugger'] }
```
