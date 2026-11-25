---
title: [CSS-357] CSS-in-JS 的运行时成本与编译时演进
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## CSS-357：CSS-in-JS 的运行时成本与编译时演进

**答**：
- 运行时 CSS-in-JS（styled-components/emotion）成本：样式插入在 JS 执行（首屏序列化 + 注入 style 标签）、动态样式每 render 序列化 class——大组件树首屏慢、hydration 后闪烁
- 运行时开销三处：字符串模板序列化、样式表插入（insertRule vs textNode 性能差异）、className 比对——这些在移动端放大（JS 慢 2~5 倍）
- 编译时演进（Panda/ vanilla-extra/ Linaria）：构建期提取静态样式为零运行时 CSS，动态样式用 CSS 变量传参——保留 DX 且去掉运行时
- 引擎失效角度：动态 className 频繁替换 → 大范围样式失效；原子化 CSS（Tailwind/unocss）class 稳定复用，共享 ComputedStyle 命中率高——引擎友好
- 选型决策：重动态主题 → 运行时可控变量层；常规应用 → 编译时/原子化；组件库 → CSS 变量 + 少量运行时（主题 token 层）

```jsx
// 运行时反模式: 每次渲染生成新 class → 样式失效 + GC
const Btn = styled.button<{ w: number }>` width: ${p => p.w}px; `;
// 编译时模式: 静态 class + 变量传值
const Btn = ({ w }) => <button className="btn" style={{ '--w': `${w}px` }} />;
/* .btn { width: var(--w); }  → 构建期提取, 运行时零序列化 */
```
