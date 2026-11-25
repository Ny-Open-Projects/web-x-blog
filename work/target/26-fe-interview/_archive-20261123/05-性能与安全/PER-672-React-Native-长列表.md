---
title: [PER-672] React Native 长列表卡顿的根因与优化：为什么 FlatList 滑快了会白屏？怎么调？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-672：React Native 长列表卡顿的根因与优化：为什么 FlatList 滑快了会白屏？怎么调？

**答**：
- 根因：FlatList 的虚拟化是窗口 + 预渲染距离"——滑动速度快时** JS 线程渲染新行的速度跟不上滚动速度**（JS 线程还要处理手势/桥通信），新行没渲染完就出现空白；图片解码/上传 bridge 也是瓶颈。
- 调参三件套：`windowSize`（默认 21，视口倍数，降为 5~7 减少渲染量）、`maxToRenderPerBatch` 与 `updateCellsBatchingPeriod`（每批渲染量与节奏，快滚时优先滚动响应）、`getItemLayout`（免测量，滑动定位零开销）、`removeClippedSubviews`（Android 离屏裁剪）。
- 结构优化：行组件 `React.memo` + 固定行高（`getItemLayout` 前提）、列表项拆薄（重交互延迟到 idle）、图片 `resizeMethod=resize`（大图降采样防 OOM）、FastImage 预加载。
- 架构方案：超长列表改用分页 + ScrollView 组合、或 FlashList（CellContainer 复用，回收机制更好）、新架构 Fabric + Hermes 减桥开销。

```javascript

const listPerf = {
  flatListProps: {
    windowSize: 7,                          // 视口倍数：默认21太大
    maxToRenderPerBatch: 8,                 // 每批渲染行数（大->填充快但掉帧）
    updateCellsBatchingPeriod: 40,          // 批间隔 ms（小->填充快，JS 压力大）
    initialNumToRender: 10,
    getItemLayout: (data, index) => ({ length: ROW_H, offset: ROW_H * index, index }), // 免测量
    removeClippedSubviews: true,
  },
  row: { memo: true, thin: '重交互拆到 idle', image: 'FastImage + resizeMethod=resize' },
  escalations: ['分页+ScrollView', 'FlashList（回收复用）', 'Fabric+Hermes 新架构'],
  diagnose: '白屏 = JS 线程跟不上滚动：看 InteractionManager 与 Perf Monitor 的 JS fps',
};
console.log(listPerf.escalations.join(' -> '));
```
