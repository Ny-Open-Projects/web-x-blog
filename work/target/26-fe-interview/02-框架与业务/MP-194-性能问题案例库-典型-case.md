---
title: [MP-194] 性能问题案例库（典型 case）？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-194：性能问题案例库（典型 case）？
**答**：
- 案例结构：现象 → 排查路径 → 根因 → 修复 → 验证数据；新人按案例学习排障思路。
- 典型案例覆盖：启动慢、滚动卡顿、内存闪退、接口瀑布、setData 洪水。

```javascript
// 案例库索引（每条附复现与分析代码）
const perfCases = {
  'case-01 启动 3 秒': {
    rootCause: '主包 1.9M + 首屏串行 4 个接口',
    fix: '分包至 0.9M + 接口聚合 1 个 + 缓存秒开',
    verify: '冷启动 P90 3200ms → 1400ms'
  },
  'case-02 长列表滑动掉帧': {
    rootCause: 'onScroll 每帧整列表 setData',
    fix: '虚拟列表可视区渲染 + 节流',
    verify: '低端机 FPS 22 → 55'
  },
  'case-03 iOS 浏览 20 页闪退': {
    rootCause: '大图原图加载 + 音频未 destroy',
    fix: 'CDN 缩略图 + onUnload 释放',
    verify: '页面内存峰值 480MB → 190MB'
  },
  'case-04 首屏白屏 800ms': {
    rootCause: '图片未懒加载 + setData 一次 300KB',
    fix: 'lazy-load + 路径化 diff 更新',
    verify: 'firstRender P90 1250ms → 640ms'
  }
}
```
