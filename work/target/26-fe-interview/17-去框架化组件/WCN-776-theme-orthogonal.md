---
title: [WCN-776] 深浅主题与品牌自定义色如何做正交组合与冲突消解？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-776：深浅主题与品牌自定义色如何做正交组合与冲突消解？

**答**：
- 结论：把主题拆成「模式（light/dark）× 品牌（brandA/brandB）」两个正交维度，token 按 `基础色板 → 语义 token → 组件 token` 三层派生；品牌色只注入基础层，语义层按模式计算对比度。
- 冲突消解：定义明确的优先级（品牌 > 模式 > 默认），用 CSS 自定义属性在 `:root[data-mode][data-brand]` 上分层覆盖；自动校验 WCAG 对比度，不达标则回退。
- 追问钩子：深色模式下品牌主色对比度不够怎么办？考察「自动调亮/调暗 + 语义色重算」而非写死。

```javascript
// token 三层派生
const base = { brandA: { primary: '#165DFF' }, brandB: { primary: '#722ED1' } };
function semantic(brand, mode) {
  const p = base[brand].primary;
  return {
    '--color-primary': p,
    '--color-bg': mode === 'dark' ? '#111' : '#fff',
    '--color-text': mode === 'dark' ? '#eee' : '#111',
    '--color-on-primary': contrast(p, mode === 'dark' ? '#111' : '#fff') >= 4.5 ? '#fff' : '#000',
  };
}
function contrast(a, b) { return 7; }  // 简化：实际按 WCAG 公式
console.log(semantic('brandA', 'dark'));
```
