---
title: [PER-003] INP 和 FID 有什么区别？为什么用 INP 替代 FID？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-003：INP 和 FID 有什么区别？为什么用 INP 替代 FID？

**答**：
- FID 只统计**第一次交互**的**输入延迟**（从点击到事件处理开始），既不覆盖后续交互，也不包含处理与渲染耗时。
- INP 统计页面**整个生命周期内所有交互**（点击、输入、键盘）的完整延迟（输入延迟 + 处理时长 + 下一帧绘制延迟），取接近最差的第 98 百分位。
- INP 更能代表真实交互体验，直接驱动开发者优化长任务与事件处理逻辑。
- 用 `web-vitals` 库可同时观测两个指标做迁移对比。

```javascript
import { onFID, onINP } from 'web-vitals';

onFID(console.log); // 旧指标：只测首次交互的输入延迟，良好小于 100ms
onINP(console.log); // 新指标：全部交互延迟的第 98 百分位，良好小于 200ms
```
