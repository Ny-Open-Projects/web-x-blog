---
title: [HW-187] 手写 SW 请求重写——URL 重写规则（CDN 域切换/版本注入/query 改写）与规则热更新
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：SW 层请求重写（业务代码零改动）：fetch 事件拦截 → 规则匹配（按 URL 模式：图片域切换/版本参数注入/灰度分流）→ 重写后 fetch（缓存策略不变）→ 规则存 IDB 由消息通道热更新（SW 生命周期内生效，PER-409 持久化纪律）。

```javascript
// sw.js
let rules = [];                                            // 内存缓存（IDB 恢复）
self.addEventListener('install', (e) => e.waitUntil(loadRules()));
async function loadRules() {
  rules = (await idbGet('sw-rules', 'rules')) ?? [];
}
self.addEventListener('message', async (e) => {
  if (e.data.type === 'update-rules') {                    // 热更新：页面推送新规则
    rules = e.data.rules;
    await idbPut('sw-rules', rules, 'rules');              // 持久化（SW 重启后恢复）
  }
});
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);
  for (const rule of rules) {
    if (rule.match.test(url.href)) {
      const rewritten = url.href.replace(rule.match, rule.replace);
      if (rewritten !== url.href) {
        event.respondWith(fetch(rewritten, event.request));   // 重写后请求（凭据/模式保持）
        return;
      }
    }
  }
  // 不匹配：默认放行（不 respondWith）
});
// 规则示例：
// { match: /legacy-cdn\.example\.com/, replace: 'cdn.example.com' }         — CDN 迁移
// { match: /app\.js$/, replace: 'app.js?v=25' }                              — 版本注入
// { match: /\/api\/goods/, replace: '$&?gray=v2' }                           — 灰度分流
// 安全：规则来源必须可信（页面主文档推送 + 版本校验），禁止把请求重写到任意域（开放重定向式滥用）
```

**评分点**：
- fetch 事件按规则重写（业务零改动）——本题核心。
- 规则 IDB 持久化 + message 热更新（SW 重启恢复，PER-409）。
- 不匹配默认放行（不 respondWith 不破坏其他请求）。
- 规则来源安全约束（禁止任意域重写——开放重定向式风险）。
