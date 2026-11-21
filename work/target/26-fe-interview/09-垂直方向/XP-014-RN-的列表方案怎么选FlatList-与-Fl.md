---
title: [XP-014] RN 的列表方案怎么选？FlatList 与 FlashList 的性能差异？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-014：RN 的列表方案怎么选？FlatList 与 FlashList 的性能差异？
**答**：
- FlatList 基于 VirtualizedList：虚拟化窗口渲染 + 一次性 mount 批量（windowSize/initialNumToRender 控制），瓶颈是 item mount 走 JS 线程 + 空白率（blank areas）。
- FlashList（Shopify）核心优化：**cell 复用**（复用原生视图而非重建）、布局下沉到主线程（v1 借助原生测量）、减少 JS 参与，blank area 与内存显著下降。
- 实践建议：固定高度用 `getItemLayout`；复杂 item 用 `React.memo` + 细粒度拆分；图片用渐进加载；万级数据避免 FlatList。
- 通用铁律：减少不可见渲染、避免 item 内深 diff、滚动中不做同步重排。

```jsx
// FlatList 关键参数优化
<FlatList
  data={feeds}
  renderItem={({ item }) => <FeedCard item={item} />}   // FeedCard 用 React.memo 包裹
  keyExtractor={(i) => i.id}
  initialNumToRender={8}     // 首屏渲染条数，越小 TTI 越快
  maxToRenderPerBatch={8}    // 每批 mount 数量，降低 JS 线程尖刺
  windowSize={5}             // 视口外保留 5 屏，平衡内存与回滚体验
  getItemLayout={(d, index) => ({ length: 120, offset: 120 * index, index })} // 定高免测量
  removeClippedSubviews      // Android 裁剪屏外子视图
/>

// FlashList：单元格复用是本质差异
import { FlashList } from '@shopify/flash-list';
<FlashList
  data={feeds}
  estimatedItemSize={120}    // 必填：供原生侧预估布局，替代逐项测量
  renderItem={({ item }) => <FeedCard item={item} />}
  masonry // 瀑布流场景用 MasonryFlashList
/>
// 对比结论：FlashList mount 复用原生视图、JS 参与更少 → 长列表 FPS 与内存均优于 FlatList
```
