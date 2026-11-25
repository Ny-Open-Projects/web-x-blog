---
title: [WCN-979] 屏幕阅读器与 shadow DOM SSR：aria-label 在 DSD 里的兼容性与兜底
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-979：屏幕阅读器与 shadow DOM SSR：aria-label 在 DSD 里的兼容性与兜底

**答**：
- 结论先行：DSD 把 shadow 树放进 HTML，屏幕阅读器对 shadow DOM 内 ARIA 的支持在现代浏览器已较好，但工具链/老版本仍有差异——关键标签要在 host 与 shadow 内「双写兜底」。
- 兼容策略：host 上放 `aria-label`/`role` 作为兜底（总是被读屏器读取），shadow 内放精确的 `aria-labelledby`/语义结构；两者一致，避免重复播报。
- ID 引用跨边界问题：`aria-labelledby` 不能跨 shadow 引用外部 id（前文有修复器），DSD 内要把被引用元素一起放进 shadow，或改用 host 的 aria-label。
- SSR 验证：用 axe-core + Playwright 对 DSD 页面跑审计，覆盖主流读屏器组合（NVDA/VoiceOver），不能只看 DOM 快照。
- 追问钩子：面试官问「closed shadow 对读屏器友好吗」——答：closed 模式读屏器依然能访问无障碍树，但自动化工具难以注入检查，所以公开组件建议 open 以便审计。

```javascript
// DSD 组件：host 兜底 + shadow 内精确语义
const html = `
<ds-search aria-label="站内搜索" role="search">
  <template shadowrootmode="open">
    <label for="q">搜索关键词</label>
    <input id="q" type="search">
  </template>
</ds-search>`;
// host 的 aria-label 总被读取；shadow 内的 label/input 关联提供精确语义。
// aria-labelledby 不跨 shadow：把被引用的 label 放进同一 shadow root（如上）。
```
