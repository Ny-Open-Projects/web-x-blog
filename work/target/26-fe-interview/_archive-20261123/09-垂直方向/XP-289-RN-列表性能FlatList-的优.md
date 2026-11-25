---
title: [XP-289] RN 列表性能：FlatList 的优化参数
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-289：RN 列表性能：FlatList 的优化参数

**答**：
- 关键参数：windowSize（渲染窗口倍数，默认 21 过大）、maxToRenderPerBatch、initialNumToRender、getItemLayout（跳过测量）。
- 坑：行组件复杂导致 JS 线程布局卡——行高固定 + memo；频繁 setState 触发全列表重渲。
- 替代：超长列表用 FlashList（recycler 性能好数倍）。

```javascript
// FlatList 优化配置
const listProps = {
  windowSize: 7,                                     // 缩小渲染窗口
  maxToRenderPerBatch: 10,
  initialNumToRender: 8,
  getItemLayout: (data, index) =>                    // 固定行高免测量
    ({ length: 80, offset: 80 * index, index }),
  keyExtractor: item => item.id,
  removeClippedSubviews: true,
};
```
