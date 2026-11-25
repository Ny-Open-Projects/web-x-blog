---
title: [CSS-386] CSS 代码评审清单：引擎视角的 CR
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## CSS-386：CSS 代码评审清单：引擎视角的 CR

**答**：
- 失效面审查：新增选择器是否带祖先/兄弟方向（失效扩大）、是否破坏列表 ComputedStyle 共享（nth-child/属性选择器）、:has 范围是否局部
- 管线审查：动画是否只动 transform/opacity、will-change 是否会移除、是否引入大面积 backdrop-filter/blend、大元素 clip-path 动画
- 体积审查：重复样式是否该抽 token/class、新第三方样式的体积与隔离（iframe/scoped）、未用的预置样式是否进包
- 语义与可维护：z-index 是否入档、间距是否用 token、物理属性还是逻辑属性、层级/主题变量是否绕过语义层
- 变更风险自查：改动是否影响共享组件（失效面跨页面）、新增媒体查询断点是否与现有断点体系冲突、是否需要视觉回归快照更新

```text
CR checklist (节选):
  [ ] 高频路径动画仅 transform/opacity
  [ ] 列表项样式无 nth-child / 属性选择器
  [ ] :has 限定在组件子树内
  [ ] z-index 使用 token 档位
  [ ] 间距/颜色引用 token, 无硬编码
  [ ] will-change 有对应移除逻辑
  [ ] 涉及视觉变化已更新/新增截图基线
```
