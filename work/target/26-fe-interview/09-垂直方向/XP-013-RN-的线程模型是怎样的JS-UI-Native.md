---
title: [XP-013] RN 的线程模型是怎样的？JS/UI/Native 三线程如何协作？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-013：RN 的线程模型是怎样的？JS/UI/Native 三线程如何协作？
**答**：
- **JS 线程**：跑 React 渲染与业务逻辑（Hermes），长任务会掉帧但不卡原生动画。
- **UI/主线程**：原生视图布局与绘制；Fabric 下 ShadowTree 在 C++ 侧，布局不在 JS 线程。
- **Native Modules 线程**：原生模块方法默认在自己的线程池执行，耗时任务不能占主线程。
- 协作机制：JS 侧通过微任务/宏任务派发，Fabric 的 commit 在 C++ 完成后原子挂载；reanimated 让动画直接在 UI 线程跑 worklet，绕开 JS 线程抖动。
- 面试高频追问：为什么列表滚动时 setState 掉帧？——JS 线程繁忙导致渲染指令迟到，方案是 worklet 化或降低 JS 负载。

```javascript
// react-native-worklets：把逻辑下沉到 UI 线程，绕开 JS 线程抖动
import { useSharedValue, useAnimatedStyle, runOnJS, withTiming } from 'react-native-reanimated';

function useDragPanel(onSnapDone) {
  const offset = useSharedValue(0);
  const style = useAnimatedStyle(() => ({
    // worklet：此函数标记后在 UI 线程执行，不依赖 JS 线程帧调度
    transform: [{ translateY: withTiming(offset.value) }],
  }));

  function handleEnd() {                 // JS 线程（业务回调必须回 JS 侧）
    'worklet';
    runOnJS(onSnapDone)(offset.value);   // UI 线程 → JS 线程的切换点
  }
  return { offset, style, handleEnd };
}

// 线程全景：
// JS 线程：React render / 业务逻辑 / setState（Hermes 执行）
// UI 线程：原生视图挂载、手势、worklet 动画
// Native 线程：TurboModule 方法（默认非主线程）、网络栈
// Fabric C++：ShadowTree 布局与 Mounting（独立于 JS 线程）
```
