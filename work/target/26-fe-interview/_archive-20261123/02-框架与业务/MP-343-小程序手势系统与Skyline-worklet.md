---
title: [MP-343] 小程序手势系统：Skyline worklet 手势与共享状态
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## MP-343：小程序手势系统：Skyline worklet 手势与共享状态

**答**：
- Skyline 手势系统：pan/tap/longpress/fling 等手势对象——手势回调在渲染线程（worklet）执行，UI 函数直接响应——「无跨线程延迟的跟手」
- 共享状态（shared value）：逻辑层与渲染层共享的响应值（wx.worklet.shared）——逻辑层写、渲染层读（worklet 函数监听变化即时更新 UI）
- worklet 的模型：函数被序列化到渲染线程执行——闭包引用 shared 值（自动建立依赖）；逻辑层 runOnJS 回传事件
- 与 Reanimated 的对照：API 设计高度相似（shared value + worklet + withTiming/withSpring）——React Native 生态经验的迁移
- 深水点：手势冲突处理（嵌套滚动/多手势竞争）——手势优先级与父手势让位（scroll-view 与拖拽项的冲突）——worklet 手势系统的核心复杂度

```javascript
// Skyline worklet: 拖拽跟手
const offset = wx.worklet.shared(0);
// 渲染线程:
wx.worklet.runOnJS(...)  // 事件回传逻辑层
// <pan-gesture-handler onGestureEvent="{{panHandler}}">
const panHandler = wx.worklet.Gesture((e) => {
  'worklet';
  offset.value = e.state === 'active' ? offset.value + e.deltaY : 0;
  applyAnimatedStyle(cardRef, () => `translateY(${offset.value}px)`);
});
// 逻辑层: offset.value = 100 (触发渲染线程 UI 函数)
```
