---
title: [WCN-971] SSR 为什么必须「首屏即无障碍」：不能等 hydration 后才补 ARIA
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-971：SSR 为什么必须「首屏即无障碍」：不能等 hydration 后才补 ARIA

**答**：
- 结论先行：屏幕阅读器在 HTML 到达时就开始解析无障碍树，若 role/aria/label 要等 JS 水合后才注入，视障用户在首屏拿到的是「无名按钮/无语义 div」——无障碍是 SSR 的硬需求而非增强项。
- 服务端必须输出完整语义：原生标签优先（button/a/input），必要的 role 与 aria-* 在 SSR 阶段就写好，label 与控件用 for/id 精确关联。
- DSD 场景：shadow root 内的 ARIA 在服务端随模板一起输出，客户端不重建；hydration 只接事件，不改无障碍树结构。
- 验证手段：用 axe-core 对「禁用 JS 的 SSR HTML」直接跑审计，而非只测水合后页面。
- 追问钩子：面试官问「动态列表的 aria 依赖运行时数据怎么办」——答：服务端从同一数据源渲染时一并输出 aria（如 aria-setsize/aria-posinset），保证首屏与运行时一致。

```javascript
// SSR 输出：语义完整，无需等 JS
function renderButtonSSR({ label, disabled }) {
  return `<button type="button" ${disabled ? 'disabled' : ''}
    aria-label="${label}">${label}</button>`; // 服务端就带 aria
}
// 禁用 JS 时屏幕阅读器依然能识别按钮与名称
const html = renderButtonSSR({ label: '加入购物车', disabled: false });
console.log(html);
// 审计：对纯 SSR HTML 跑 axe，而非等 hydrate
// axe.run(document.body, { rules: { 'button-name': { enabled: true } } });
```
