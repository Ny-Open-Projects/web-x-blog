---
title: [XP-076] RN 大列表性能治理怎么做？FlatList 参数调优与 FlashList 原理？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-076：RN 大列表性能治理怎么做？FlatList 参数调优与 FlashList 原理？
**答**：
- FlatList 本质是 **VirtualizedList**：视口窗口化渲染 + 屏外批量挂载，痛点是快速滚动时白屏（blank area）与 JS 线程被 renderItem 挤占。
- 关键参数：`initialNumToRender`（首屏条数）、`getItemLayout`（定高跳过异步测量，治白屏最有效）、`windowSize`（视口倍数，降内存）、`maxToRenderPerBatch`/`updateCellsBatchingPeriod`（滚动流畅 vs 空窗权衡）、`onEndReachedThreshold`、`removeClippedSubviews`（Android 大列表）。
- 业务侧配套：item 定高或预估精准、图片固定宽高避免布局抖动、`renderItem` 与 item 组件 `React.memo` 化、避免在 item 内做重计算。
- **FlashList 原理**：借鉴 Android RecyclerView 的 **cell 复用池**——滚出屏幕的 CellContainer 不销毁而是按 `recyclingKey`（item 类型）回收复用，且布局测量在原生侧同步完成，大幅减少 JS 线程工作量；官方数据白屏率与内存显著优于 FlatList。
- 治理闭环：用 `onScroll` 采集 blankArea 比例 + JS 线程占用，指标看板（XP-069 口径）回归验证；90% 场景 FlashList 直接替换，异构 item 记得声明类型避免错位复用。

```jsx
// FlatList 调优 vs FlashList 替换
const DATA = makeItems(2000);

// 1) FlatList 极限调优
<FlatList
  data={DATA}
  renderItem={renderItem}                    // 顶层定义 + React.memo，绝不内联箭头函数
  getItemLayout={(data, index) => ({         // 定高：跳过异步 measure，滚动不再白屏
    length: ITEM_HEIGHT, offset: ITEM_HEIGHT * index, index,
  })}
  initialNumToRender={10}                    // 首屏真实可见条数即可
  maxToRenderPerBatch={8}                    // 每批渲染条数：越小越流畅，白屏窗口越长
  updateCellsBatchingPeriod={50}             // 批间隔 ms：与上行参数配合找平衡点
  windowSize={7}                             // 视口倍数，内存敏感可降到 5
  removeClippedSubviews                     // Android 长列表内存优化
  onEndReachedThreshold={0.5}
  keyExtractor={(it) => it.id}
/>

// 2) FlashList：复用池替代销毁重建
import { FlashList } from '@shopify/flash-list';
<FlashList
  data={DATA}
  estimatedItemSize={ITEM_HEIGHT}            // 唯一必填：预估高度用于滚动条与预加载
  renderItem={({ item }) =>
    item.kind === 'card' ? <CardItem item={item} /> : <AdItem item={item} />}
  // 异构 item 必须给稳定类型，否则复用池会拿错模板导致状态串位
  getItemType={(item) => item.kind}
  drawDistance={500}                         // 预渲染距离（默认 250），低端机调小降内存
/>
// 治理指标：blankArea Ratio < 2%、滚动平均 FPS >= 55（deviceTier 分档，XP-073）
```
