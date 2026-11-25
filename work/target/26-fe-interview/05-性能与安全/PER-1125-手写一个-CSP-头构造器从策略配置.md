---
title: [PER-1125] 手写一个 CSP 头构造器：从策略配置生成响应头
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1125：手写一个 CSP 头构造器：从策略配置生成响应头

**答**：
- 需求：实现 buildCSP(policy)。policy 为 { defaultSrc, scriptSrc: [{ value, nonce?: bool }], styleSrc, imgSrc, connectSrc, reportOnly, reportUri }；nonce: true 时由调用方传入 nonce 生成 nonce-xxx 指令；生成合法 CSP 字符串（指令用连字符形式），reportOnly 决定头名。
- 边界：未配置的类别回退 default-src；object-src/base-uri 强制 none；nonce 未传值时报错（防静默失效）；重复指令去重。
- 评分点：指令映射；nonce 校验；强制兜底指令；去重与头名

```javascript
function buildCSP(policy, nonce) {
  const map = { defaultSrc: 'default-src', scriptSrc: 'script-src',
    styleSrc: 'style-src', imgSrc: 'img-src', connectSrc: 'connect-src' };
  const parts = [];
  for (const [k, v] of Object.entries(policy)) {
    if (!(k in map)) continue;
    const items = (v ?? []).map(item => {
      if (typeof item === 'string') return item;
      if (item.nonce) {
        if (!nonce) throw new Error('nonce 配置但未传值');
        return `'nonce-${nonce}'`;
      }
      return item.value;
    });
    parts.push(`${map[k]} ${[...new Set(items)].join(' ')}`.trim());
  }
  parts.push("object-src 'none'", "base-uri 'none'");
  const value = parts.join('; ');
  return { header: policy.reportOnly
    ? 'Content-Security-Policy-Report-Only' : 'Content-Security-Policy',
    value: value + (policy.reportUri ? `; report-uri ${policy.reportUri}` : '') };
}
```
