---
title: [PER-686] Flutter 渲染管线的性能关注点：flutter 前端（Dart 侧）能做哪些优化与采集？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-686：Flutter 渲染管线的性能关注点：flutter 前端（Dart 侧）能做哪些优化与采集？

**答**：
- Flutter 三棵树（Widget/Element/RenderObject）性能要点：**rebuild 范围控制**（setState 只刷最小子树，const widget 复用）、**列表用 ListView.builder**（懒建）+ itemExtent（免布局测量）、避免在 build 里做重计算（moved to isolate/缓存）、图片 `cacheWidth` 降采样。
- 光栅与合成：复杂 UI（大量 Shader/模糊）导致 raster 线程慢——用 `ShaderMask/BackdropFilter` 减量、`RepaintBoundary` 隔离重绘区域。
- 采集：`SchedulerBinding.instance.addTimingsCallback` 拿 FrameTiming（build/raster 双阶段耗时），区分 UI 线程卡（build 慢）与光栅卡（raster 慢）——对应前端的 JS 卡 vs 合成卡的思路。
- 与 Web 团队协同：混合栈场景（Flutter 页嵌 H5）内存与通道开销，页面切换时释放 Flutter 引擎（engine group/多引擎取舍）。

```javascript

// Dart 侧帧采集与归因（协作者视角，前端理解双线程归因同源）
import 'package:flutter/scheduler.dart';
void installFrameProbe() {
  SchedulerBinding.instance.addTimingsCallback((timings) {
    for (final t in timings) {
      final buildMs = t.buildDuration.inMicroseconds / 1000;
      final rasterMs = t.rasterDuration.inMicroseconds / 1000;
      if (t.totalSpan.inMilliseconds > 32) {
        reportJank({
          'route': currentRoute(),
          'buildMs': buildMs,      // 高 -> Dart 侧 rebuild 过重（对应 JS 卡）
          'rasterMs': rasterMs,    // 高 -> 光栅过重（Shader/模糊/过度绘制）
        });
      }
    }
  });
}
// 治理映射：buildMs 高 -> setState 范围/const 化/延迟计算；rasterMs 高 -> RepaintBoundary/减模糊
```
