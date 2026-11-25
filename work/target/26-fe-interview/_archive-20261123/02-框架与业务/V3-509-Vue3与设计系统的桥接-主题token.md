---
title: [V3-509] Vue3 与设计系统的桥接：主题 token 的工程化
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## V3-509：Vue3 与设计系统的桥接：主题 token 的工程化

**答**：
- token 管道：Figma tokens（JSON）→ 脚本生成 CSS 变量 + TS 类型（token 常量）→ 组件库消费——单一来源，杜绝手抄
- 主题切换载体：data-theme + CSS 变量（CSS 侧完成）——Vue 层只管「切换属性 + 持久化」，不搞 JS 遍历组件改样式
- 组件库定制：第三方库（Element Plus）的 CSS 变量覆盖层——按品牌维护 override.css，升级组件库时 diff 变量兼容性
- 暗色模式细节：el-dar 组件类切换（`html.dark`）+ 图表配色 token 化（ECharts 主题从 token 生成）——图表不接 token 就会出现暗色下白底图表
- 校验闭环：视觉回归截图（light/dark × 关键组件矩阵）+ 对比度 lint（axe-core CI）——token 系统的质检

```javascript
// token 生成脚本产物
:root { --color-primary: #1677ff; --radius-md: 8px; }
[data-theme='dark'] { --color-primary: #4d9fff; }
// 组件库覆盖
.el-button { --el-button-bg-color: var(--color-primary); }
```
