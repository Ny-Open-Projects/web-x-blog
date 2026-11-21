---
title: [DP-143] 主题系统如何用策略模式设计？tokens 与换肤的关系？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-143：主题系统如何用策略模式设计？tokens 与换肤的关系？（高频）
**答**：
- 主题 = 一组设计 token（颜色/圆角/间距）的策略集合；换肤 = 切换策略实例，消费方只读统一 token 接口（策略模式，DP-051 的 UI 化）。
- 三种实现强度：CSS 变量注入（运行时切换，主流）、Provider 注入 token 对象（组件库）、构建期多主题产物（极致性能）。
- 工程要点：token 分层（全局基座 → 组件级映射 → 页面覆盖）；跟随系统的 dark 模式 = 策略选择器 + 观察者监听 `prefers-color-scheme`。

```javascript
// 策略：每套主题产出同一形状的 token
const lightTheme = { name: 'light', colorPrimary: '#1677ff', text: '#333', bg: '#fff', radius: 8 };
const darkTheme  = { name: 'dark',  colorPrimary: '#4096ff', text: '#eee', bg: '#111', radius: 8 };
const strategies = { light: lightTheme, dark: darkTheme, auto: () => matchMedia('(prefers-color-scheme: dark)').matches ? darkTheme : lightTheme };
// 应用层：解析策略 → 注入 CSS 变量（消费方只认变量名）
function applyTheme(name) {
  const tokens = typeof strategies[name] === 'function' ? strategies[name]() : strategies[name];
  for (const [key, value] of Object.entries(tokens))
    document.documentElement.style.setProperty(`--${key.replace(/[A-Z]/g, (m) => '-' + m.toLowerCase())}`, value);
}
// 观察者：跟随系统自动换肤
const mq = matchMedia('(prefers-color-scheme: dark)');
mq.addEventListener('change', () => userPref === 'auto' && applyTheme('auto'));
// 组件消费：样式只写变量，永不写死颜色
// .btn { background: var(--color-primary); border-radius: var(--radius); color: var(--text); }
applyTheme('auto');
```
