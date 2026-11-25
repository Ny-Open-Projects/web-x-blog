---
title: [PER-1034] 资源预取策略：何时 prefetch 何时仅预热
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1034：资源预取策略：何时 prefetch 何时仅预热

**答**：
- 预取金字塔：DNS 预解析（最便宜）→ preconnect → prefetch 静态资源 → prefetch 数据接口 → 预渲染（Speculation Rules，最贵）。
- 判定依据：跳转概率（下一页点击率）+ 资源成本（体积）+ 缓存友好性；概率 × 成本加权决定档位。
- Speculation Rules API：declarative 预取/预渲染，浏览器托管优先级与取消；比 prefetch link 更智能。
- 风险控制：配额（并发预取上限）、按用户意图触发（hover 80ms 才预取）、计费敏感接口禁止预取。

```javascript
<script type="speculationrules">
{ "prefetch": [{ "source": "list", "urls": ["/products/*"],
    "eagerness": "moderate" }],
  "prerender": [{ "source": "document",
    "where": { "href_matches": "/products/new" }, "eagerness": "eager" }] }
</script>
<script>
// 意图触发的手动预取（老浏览器回退）
function prefetchOnHover(a) {
  let t;
  a.addEventListener('mouseenter', () => {
    t = setTimeout(() => {
      const l = document.createElement('link');
      l.rel = 'prefetch'; l.href = a.href; document.head.appendChild(l);
    }, 80);                                     // 80ms 意图延迟
  });
  a.addEventListener('mouseleave', () => clearTimeout(t));
}
</script>
```
