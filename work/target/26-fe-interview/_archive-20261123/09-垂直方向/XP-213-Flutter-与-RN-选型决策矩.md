---
title: [XP-213] Flutter 与 RN 选型决策矩阵
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-213：Flutter 与 RN 选型决策矩阵

**答**：
- Flutter vs RN：渲染（自绘 vs 原生桥接）、语言（Dart vs JS/TS）、生态（组件/库）、团队技能匹配。
- Flutter：自绘引擎（跨平台一致性极好）、动画流畅（Skia/Impeller）、但包体大（+10MB）与 Web 支持弱。
- RN：原生组件（系统观感）、JS 生态复用、新架构性能追上——但跨平台一致性弱于 Flutter。

```javascript
const flutterVsRN = {
  flutter: { render: '自绘（Skia/Impeller）——像素级一致',
    language: 'Dart（独立生态）', bundle: '+10MB（引擎）',
    fit: '重 UI 一致性（跨端像素级相同）/ 动画密集' },
  rn: { render: '原生组件桥接（系统观感）',
    language: 'JS/TS（前端生态复用）', bundle: '+5MB',
    fit: '已有前端团队 / 需要系统观感 / JS 生态依赖' },
  matrix: [
    ['跨端一致性', 'Flutter 优', 'RN 中（新架构改善）'],
    ['前端技能复用', 'Flutter 差（Dart）', 'RN 优'],
    ['动画性能', 'Flutter 优', 'RN 中（Fabric 改善）'],
    ['热更新', 'Flutter 差（Shorebird 有限）', 'RN 优（CodePush）'],
  ],
};
```
