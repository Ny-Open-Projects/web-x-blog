---
title: [ZSM-318] 主题状态怎么分层落地（系统/用户/持久化）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-318：主题状态怎么分层落地（系统/用户/持久化）

**答**:
- 三层优先级：用户显式选择（persist）> 系统偏好（matchMedia prefers-color-scheme）> 默认值；「跟随系统」是用户选择的一种，系统变化要监听 change 事件
- 落地双通道：CSS 变量 + `color-scheme` 属性管视觉；JS 状态只存「主题模式」枚举（light/dark/system），派生实际值
- 防闪白（FOUC）：首帧前内联脚本读 storage 设置 html class/data-theme，不能等 React 水合——主题初始化必须在入口 HTML 层
- 切换动画与一致性：View Transitions API 平滑过渡；Shadow DOM 子组件透传变量

```javascript
// 入口内联（HTML head，先于 React）
// <script>document.documentElement.dataset.theme = localStorage.theme ?? matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'</script>
matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
  if (theme === 'system') apply(e.matches ? 'dark' : 'light')   // system 模式跟随
})
```
