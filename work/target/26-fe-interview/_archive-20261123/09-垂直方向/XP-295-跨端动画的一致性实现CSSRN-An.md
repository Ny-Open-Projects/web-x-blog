---
title: [XP-295] 跨端动画的一致性实现（CSS/RN Animated/Flutter Animation）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-295：跨端动画的一致性实现（CSS/RN Animated/Flutter Animation）

**答**：
- 原则：动画驱动交原生（CSS transform/RN useNativeDriver/Flutter AnimationController）——JS 驱动必卡。
- 时间函数统一：ease 系列曲线在各端数学一致（cubic-bezier 参数对齐）。
- 降级：低端机关闭非核心动画（菜单/转场保留）。

```javascript
// 动画抽象
const EASING = {
  standard: 'cubic-bezier(0.4, 0, 0.2, 1)',
  decelerate: 'cubic-bezier(0, 0, 0.2, 1)',
};
function animate({ native = true, duration = 300, easing = 'standard' } = {}) {
  return { native,                                  // RN useNativeDriver
    css: `transition: transform ${duration}ms ${EASING[easing]}`,
    flutter: Curves.easeInOut, duration };
}
// native=false 时 RN 回退 JS 驱动（仅布局动画场景）
```
