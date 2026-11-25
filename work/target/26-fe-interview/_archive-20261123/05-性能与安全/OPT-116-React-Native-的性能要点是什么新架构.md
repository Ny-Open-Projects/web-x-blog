---
title: [OPT-116] React Native 的性能要点是什么？新架构改变了什么？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-116：React Native 的性能要点是什么？新架构改变了什么？

**答**：
- 旧架构痛点：JS 与原生通过**异步 Bridge** 传 JSON 序列化消息，高频交互（滚动、手势、动画）被序列化延迟拖垮。
- 新架构（Fabric + TurboModules + JSI）：JS 直接**同步持有了原生对象引用**（JSI 无序列化）、Fabric 渲染器支持同步布局与优先级调度、TurboModule 按需加载原生模块。
- 实战要点：列表用 `FlashList`/`FlatList` 优化（`windowSize`、`getItemLayout`、`keyExtractor`）；动画全走 `react-native-reanimated` 的 **UI 线程**（worklet），不占 JS 线程；图片用 `FastImage`（原生缓存）。
- JS 侧同 Web 规则：`React.memo`、避免 render 里建函数对象传给原生组件（每次都触发原生 props 更新）。

```jsx
// 一一对应：RN 列表 + UI 线程动画 + TurboModule 按需
import React, { useCallback, useMemo } from 'react';
import { FlashList } from '@shopify/flash-list';
import Animated, { useAnimatedStyle, useSharedValue, withSpring } from 'react-native-reanimated';

// 要点 1：动画跑在 UI 线程（worklet），JS 线程卡顿也不掉帧
function FollowButton() {
  const scale = useSharedValue(1);
  // 'worklet' 指令：这段函数在 UI 线程执行，绝不走 Bridge
  const pressStyle = useAnimatedStyle(() => ({
    transform: [{ scale: withSpring(scale.value) }],
  }));
  return (
    <Animated.Pressable
      style={pressStyle}
      onPressIn={() => (scale.value = 0.9)}   // sharedValue 写入也是 UI 线程直改
      onPressOut={() => (scale.value = 1)}
    />
  );
}

// 要点 2：长列表用 FlashList + 回收复用，五个参数一个不能省
function Feed({ data }) {
  const renderItem = useCallback(({ item }) => <Card item={item} />, []); // 稳定引用
  const keyExtractor = useCallback((item) => item.id, []);
  const getItemType = useCallback((item) => item.media ? 'rich' : 'text', []); // 复用按类型分组
  return (
    <FlashList
      data={data}
      renderItem={renderItem}
      keyExtractor={keyExtractor}
      getItemType={getItemType}
      estimatedItemSize={120} // 必填：省一次测量，滚动定位直接算
    />
  );
}

// 要点 3：TurboModule 按需加载（新架构自动 codegen，JS 侧写法不变但延迟初始化）
// import NativeDevice from './specs/NativeDevice'; // 仅在调用方法时才初始化原生模块
// NativeDevice.getThermalState();

// 反面清单：render 里内联箭头传给原生组件 -> 每帧触发原生 props diff；
// state 里存大 JSON -> 每次变更都序列化过 JSI；用 setState 驱动 60fps 动画 -> 必卡
```
