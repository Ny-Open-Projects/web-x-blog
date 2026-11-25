---
title: [PER-989] Trusted Types 是什么？如何用类型系统消灭 DOM XSS
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-989：Trusted Types 是什么？如何用类型系统消灭 DOM XSS

**答**：
- Trusted Types 让 innerHTML/src 等sink 只接受 TrustedHTML 类型对象，字符串直接赋值直接抛错——把 DOM XSS 从运行时漏洞变成强制类型错误。
- 接入：响应头 require-trusted-types-for script；先 Report-Only 收集所有裸赋值点。
- 配套：默认策略（default policy）兜底旧代码过渡，业务代码逐步迁移到显式 createPolicy。
- 边界：不覆盖 XSS 的所有类型（URL 类 sink 有独立机制），需配合 CSP 与编码规范。

```javascript
// Report-Only 阶段收集污染点
addEventListener('securitypolicyviolation', e => {
  if (e.violationType === 'trusted-types-sink-violation')
    report({ sink: e.sample?.slice(0, 40), src: e.sourceFile, line: e.lineNumber });
});
// 正式阶段：只留一个显式策略
const tt = trustedTypes.createPolicy('sanitize', {
  createHTML: input => DOMPurify.sanitize(String(input)),
});
el.innerHTML = tt.createHTML(raw);   // 唯一合法入口
```
