---
title: [WCN-546] 「SSR 信号快照注入器」如何实现 computed 值的序列化与直读恢复？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-546：「SSR 信号快照注入器」如何实现 computed 值的序列化与直读恢复？

**答**：
- 结论：注入器在服务端遍历 computed，输出 {name, value, deps签名}；客户端直读模块据此恢复缓存。
- 只注入被标记为 ssr:true 的 computed，控制体积。
- 客户端恢复时校验 deps 签名，一致则用注入值，否则重算并覆盖。
- 追问：如何防止注入脚本被 XSS 篡改？（答：转义 < 字符 + CSP hash 校验）

```javascript
function collectSnapshot(computeds) {
  const out = {};
  for (const [name, c] of computeds) {
    if (!c.ssr) continue;
    out[name] = { value: c.peek(), deps: c.deps.map(d => d.peek()).join('|') };
  }
  return `<script id="__SIG__" type="application/json">${JSON.stringify(out).replace(/</g,'\\u003c')}</script>`;
}
function restoreSnapshot(computeds, json) {
  const data = JSON.parse(document.getElementById('__SIG__').textContent);
  for (const [name, c] of computeds) {
    const hit = data[name];
    if (hit && hit.deps === c.deps.map(d => d.peek()).join('|')) c.setCache(hit.value);
  }
}
```
