---
title: [WCN-936] 跨端 token 动态下发：服务端按租户下发覆盖层，客户端怎么热更新不闪屏
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-936：跨端 token 动态下发：服务端按租户下发覆盖层，客户端怎么热更新不闪屏

**答**：
- 结论先行：动态 token 覆盖层要做「先备好后切换」——新 token 先解析成完整变量集，再一次性原子替换 CSS 变量，避免逐个赋值导致的中间态闪屏。
- 协议：服务端下发 `{ overrides: { 'color.primary': '#f00' } }`，客户端在基础 token 上 merge 得到完整集，校验通过后用 `document.documentElement.style.setProperty` 批量写入（可在 rAF 中一次完成）。
- 缓存与版本：token 带版本号，客户端缓存上次结果，命中则直接用缓存渲染首屏，网络返回新版本再热替换（先缓存后校验）。
- 一致性：多端（Web/小程序/原生）用同一份覆盖协议与版本号，避免 A/B 端不同版本导致界面分裂。
- 追问钩子：面试官问「覆盖层写错色值怎么办」——答：客户端用 schema 校验（对比度/格式）失败则回退到基础 token 并告警，不让错误 token 上屏。

```javascript
// 原子热替换 token：先在内存 merge，再一次写入，避免逐条闪烁
let current = { 'color.primary': '#1677ff', 'color.bg': '#fff' };
function applyOverride(overrides) {
  const next = { ...current, ...overrides };       // 先算完整集
  requestAnimationFrame(() => {
    for (const [k, v] of Object.entries(next))
      document.documentElement.style.setProperty('--' + k, v); // 同帧批量
    current = next;
  });
}
// 租户下发覆盖：
applyOverride({ 'color.primary': '#f00' });
console.log(current); // 旧值仍在（rAF 后才切换，首屏不闪）
```
