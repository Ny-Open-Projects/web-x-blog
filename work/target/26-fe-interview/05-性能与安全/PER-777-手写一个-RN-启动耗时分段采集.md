---
title: [PER-777] 手写一个 RN 启动耗时分段采集器：native init -> bundle -> 首帧 -> 可交互四段上报（新旧架构通用）
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-777：手写一个 RN 启动耗时分段采集器：native init -> bundle -> 首帧 -> 可交互四段上报（新旧架构通用）

**答**：
- 分段锚点：native 启动（App 启动参数注入 t0）、JS bundle 加载完成（入口文件第一行 t1）、首帧渲染（首屏 onLayout t2）、可交互（首个交互 handler 就绪 + rAF t3）。
- 要点：新架构 Fabric 首帧口径变化（同步渲染后 t2 更早但可交互仍受 JS 长任务影响）；分段打点用 performance.now 差值（RN 的 performance 可用）；上报带架构标记（old/new bridge）分桶对比。
- 边界：热启动（bundle 已加载）分段不同（只测导航挂载）；崩溃样本（未到 t2）要单独计数（启动失败率）。
- 评分点：架构标记分桶与崩溃样本计数。

```javascript

// App 入口第一行
global.__t1 = performance.now();                                 // bundle 加载完成
import { NavigationContainer } from '@react-navigation/native';
function App() {
  const [ready, setReady] = useState(false);
  const onLayoutHome = () => {
    if (global.__t2) return;
    global.__t2 = performance.now();                             // 首帧 onLayout
    requestAnimationFrame(() => {
      global.__t3 = performance.now();                           // 可交互（下一帧）
      reportStartup();                                           // 四段上报
    });
  };
  return (
    <NavigationContainer>
      <Home onLayout={onLayoutHome} onReady={() => setReady(true)} />
    </NavigationContainer>
  );
}
function reportStartup() {
  const t0 = global.__nativeStart;                               // Native 注入启动时间戳
  const seg = {
    arch: global.__fabricEnabled ? 'new' : 'old',                // 架构标记分桶
    bundleLoadMs: Math.round(global.__t1 - t0),
    firstFrameMs: Math.round(global.__t2 - global.__t1),
    interactMs: Math.round(global.__t3 - global.__t2),
    totalMs: Math.round(global.__t3 - t0),
    cold: !global.__warmLaunch,
  };
  fetch('/rn-startup', { method: 'POST', body: JSON.stringify(seg) });
}
// 崩溃样本：启动 watchdog 5s 未到 t2 -> 上报 startup-failure
```
