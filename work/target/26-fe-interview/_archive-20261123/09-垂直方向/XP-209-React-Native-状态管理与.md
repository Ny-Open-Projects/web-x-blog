---
title: [XP-209] React Native 状态管理与跨桥数据流
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-209：React Native 状态管理与跨桥数据流

**答**：
- 题目：RN 状态管理选型——Redux/Zustand 在 RN 中的适配（持久化/导航状态分离）、跨桥数据（Native 事件 → JS 状态）。
- 思路：状态分层——业务状态（Redux/Zustand）与导航状态（React Navigation 独立）；Native 事件 → NativeEventEmitter → JS 回调 → store dispatch。
- 评分点：状态分层；Native 事件桥接；持久化（AsyncStorage）。

```javascript
// RN 状态分层
const stateDesign = {
  business: 'Zustand store（业务数据）',                       // 业务状态
  navigation: 'React Navigation（导航栈独立）',                 // 导航状态
  persistence: 'AsyncStorage 持久化（Zustand persist 中间件）',
};
// Native 事件 → JS 状态
import { NativeEventEmitter, NativeModules } from 'react-native';
const emitter = new NativeEventEmitter(NativeModules.BluetoothModule);
emitter.addListener('deviceFound', (device) => {
  useStore.getState().addDevice(device);                       // Native 事件 → store
});
// 持久化：zustand/middleware persist → AsyncStorage（JSON 序列化）
// 选型：轻量业务用 Zustand（少样板）；复杂中间状态用 Redux Toolkit
```
