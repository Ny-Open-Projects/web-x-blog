---
title: [WCN-932] 深色模式 token 映射：同一语义 token 双主题下怎么避免遗漏与错配
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-932：深色模式 token 映射：同一语义 token 双主题下怎么避免遗漏与错配

**答**：
- 结论先行：深色模式不是「颜色取反」，而是同一 semantic token 在 light/dark 两套 primitive 映射；遗漏通常因为「按 component 手改」而非「按 semantic 系统映射」。
- 做法：每个 semantic token 显式声明 light/dark 两条引用（如 color.text.primary → light:{gray900}/dark:{gray100}），编译器生成 `:root` 与 `[data-theme=dark]` 两套变量。
- 自动化校验：检查「semantic 全覆盖」——任一 token 缺 dark 映射即报错；扫描硬编码颜色（不通过 token 的色值）作为违规门禁。
- 对比度联动：dark 下 foreground/background 组合要重新跑 WCAG 对比度校验，不能假设 light 下合格 dark 也合格（深色模式是 token 场景高发 bug）。
- 追问钩子：面试官问「用户系统主题跟随怎么做到无闪烁」——答：首屏内联 critical token 到 HTML，用 `prefers-color-scheme` 在 SSR 阶段注入正确主题变量，避免先亮后暗。

```javascript
// semantic token 双主题映射 + 覆盖率校验
const semantic = {
  'color.text.primary': { light: '{gray900}', dark: '{gray100}' },
  'color.bg.page':      { light: '{white}',   dark: '{gray900}' },
};
function checkCoverage(map) {
  return Object.entries(map)
    .filter(([, v]) => !v.light || !v.dark)
    .map(([k]) => k);
}
function toCSS(map, primitive) {
  let css = ':root{';
  for (const [k, v] of Object.entries(map)) css += `--${k}:${primitive[v.light]};`;
  css += '}[data-theme=dark]{';
  for (const [k, v] of Object.entries(map)) css += `--${k}:${primitive[v.dark]};`;
  return css + '}';
}
console.log(checkCoverage(semantic)); // []（全覆盖）
console.log(toCSS(semantic, { gray900: '#1f1f1f', gray100: '#f5f5f5', white: '#fff' }));
```
