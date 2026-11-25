---
title: [XP-236] React Native 场景专项：FlatList 优化进阶（笔试）
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-236：React Native 场景专项：FlatList 优化进阶（笔试）

**答**：
- 题目：RN FlatList 优化——windowSize/viewabilityConfigOffset/getItemLayout（定高跳过测量）/keyExtractor 稳定性/memo 子项。
- 思路：windowSize（渲染窗口倍数，默认 21 → 降为 7 省内存）；getItemLayout 定高（跳过异步测量——消除空白）；keyExtractor 稳定 key；React.memo 子项（props 不变不重渲）。
- 评分点：getItemLayout；windowSize；memo+稳定 key。

```javascript
const FlatListOptimized = React.memo(({ data }) => (
  <FlatList
    data={data}
    renderItem={React.memo(({ item }) => <Item item={item} />)}     // memo 子项
    keyExtractor={(item) => item.id}                                 // 稳定 key（不用 index）
    getItemLayout={(data, index) => ({                                // 定高：跳过测量
      length: 80, offset: 80 * index, index })}
    windowSize={7}                                                    // 渲染窗口（默认 21 太大）
    initialNumToRender={10}                                           // 首屏渲染数
    maxToRenderPerBatch={10}                                          // 批量渲染数
    removeClippedSubviews={true}                                      // 裁剪不可见
  />
));
// 空白原因：异步测量未完成 → getItemLayout 跳过测量消除（HW-672 关联）
```
