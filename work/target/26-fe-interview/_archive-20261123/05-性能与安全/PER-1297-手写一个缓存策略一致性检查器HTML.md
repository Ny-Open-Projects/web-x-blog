---
title: [PER-1297] 手写一个"缓存策略一致性"检查器（HTML 与资源）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1297：手写一个"缓存策略一致性"检查器（HTML 与资源）

**答**：
- 需求：implement cachePolicyCheck(htmlPolicy, assetPolicies)。htmlPolicy 为 { maxAge }；assetPolicies 为 [{ path, maxAge, hashNamed }]；规则：hashNamed 资源 maxAge 应 >= 1 年；非 hash 资源 maxAge 应 <= html maxAge（否则旧资源引用混乱）；HTML 不应强缓存；输出 { violations, pass }。
- 边界：hashNamed 缺失按 false；maxAge 秒；html maxAge > 0 即违规（除非 no-cache 显式声明）；空资产列表只查 HTML。
- 评分点：HTML 规则；hash 规则；非 hash 上限；一致性

```javascript
function cachePolicyCheck(htmlPolicy, assetPolicies) {
  const violations = [];
  if (htmlPolicy.maxAge > 0 && !htmlPolicy.noCache)
    violations.push({ rule: 'HTML 不应强缓存', path: '/index.html' });
  for (const a of assetPolicies) {
    if (a.hashNamed && a.maxAge < 31536000)
      violations.push({ rule: 'hash 资源应 max-age >= 1 年', path: a.path });
    if (!a.hashNamed && a.maxAge > (htmlPolicy.maxAge || 0))
      violations.push({ rule: '非 hash 资源 maxAge 超 HTML', path: a.path });
  }
  return { violations, pass: !violations.length };
}
// 违规示例：HTML max-age 3600 且资源 max-age 86400 -> 发布后旧 HTML 引用新资源错位；
```
