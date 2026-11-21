---
title: [MFW-478] 笔试：手写 SSR 页面 Cache-Control 推导器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-478：SSR 页面 Cache-Control 组合推导器
**需求**：实现 `deriveCacheControl(page)`：1) page = { render: 'static'|'isr'|'dynamic', revalidate, personal, cookies, auth }；2) 推导规则：static → `public, max-age=31536000, immutable`；isr → `public, s-maxage=X, stale-while-revalidate=Y`（Y = min(revalidate, 60)）；dynamic → 有 cookie/auth/personal 任一 → `private, no-store`；否则 `public, s-maxage=60, must-revalidate`；3) 冲突裁决：dynamic 但带 personal 必须同时加 `Vary: Cookie`（或干脆 no-store，二选一给理由）；4) 输出 { header, vary, reason }（每条决策带理由——缓存头评审要用）。

```javascript
export function deriveCacheControl(page) {
  const { render, revalidate = 60, personal, cookies, auth } = page
  if (render === 'static')
    return { header: 'public, max-age=31536000, immutable', vary: null,
      reason: 'build-time output, content addressed' }
  if (render === 'isr')
    return { header: `public, s-maxage=${revalidate}, stale-while-revalidate=${Math.min(revalidate, 60)}`,
      vary: null, reason: 'CDN cache + background regen' }
  // dynamic
  if (personal || auth || cookies)
    return { header: 'private, no-store', vary: 'Cookie',
      reason: 'per-user content; no-store over Vary (Vary alone risks cache poisoning on multi-value Cookie)' }
  return { header: 'public, s-maxage=60, must-revalidate', vary: null,
    reason: 'shared dynamic content, short CDN TTL' }
}
```

**评分点**：
- 三渲染模式头分离（static 的 immutable 与 ISR 的 SWR 语义不同）
- 个人化/鉴权 → private no-store（Vary: Cookie 不足以放心——多 Cookie 值爆炸）
- SWR 上限钳制（stale 窗口过长 = 用户长期看旧价）
- reason 字段随行（缓存头是评审文档，不是黑魔法）
