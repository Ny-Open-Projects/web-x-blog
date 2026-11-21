---
title: [ARC-244] 国际化 RTL 布局的工程化方案？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-244：国际化 RTL 布局的工程化方案？
**答**：
- 基础：`dir="rtl"` 挂 html 根节点，现代浏览器/Flex/Grid 的 start/end 语义自动翻转；关键是**代码里不用 left/right**，全部用 logical properties（margin-inline-start、inset-inline、text-align: start）。
- 迁移存量 CSS：stylelint 规则禁 physical 属性 + codemod 自动替换（left→inline-start）；第三方组件库用 postcss 插件（如 rtlcss）构建时生成翻转产物。
- 不该翻转的东西：数字、代码块、时间轴播放器方向、logo——用 `dir="ltr"` 局部钉住；图标语义（前进/后退箭头）需要人工审视。
- 测试：视觉回归跑 LTR/RTL 双基线；伪 RTL（dir=rtl + 英文文案）在 CI 里先跑一轮，提前暴露布局泄漏。

```css
/* 用逻辑属性（可被 codemod 批量替换） */
.card { margin-inline-start: 12px; padding-inline: 16px; text-align: start; }
/* 不翻转区域 */
.price, .code-block { direction: ltr; unicode-bidi: embed; }
```
```javascript
// 构建期：postcss-rtlcss 生成双份产物，按 html dir 加载
// 运行时切换：
function setLang(lang) {
  const rtl = ['ar', 'he', 'fa', 'ur'].includes(lang.split('-')[0]);
  document.documentElement.dir = rtl ? 'rtl' : 'ltr';
  document.documentElement.lang = lang;
}
```
