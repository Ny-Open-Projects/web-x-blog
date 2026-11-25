---
title: [XP-235] Flutter 场景专项：长列表优化（ListView.builder 与 sliver）
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-235：Flutter 场景专项：长列表优化（ListView.builder 与 sliver）

**答**：
- 题目：Flutter 长列表掉帧——ListView.builder 惰性构建 + itemExtent（定高优化）+ SliverPersistentHeader（吸顶）。
- 思路：ListView.builder（惰性，只构建可视区）；itemExtent 定高（跳过测量）；Sliver 系列（吸顶/视差/分组）；keepAlive（tab 切换保活）。
- 评分点：builder 惰性；itemExtent；Sliver 组合。

```javascript
// 长列表优化
ListView.builder(
  itemCount: 10000,
  itemExtent: 80,                                                  // 定高：跳过逐项测量
  itemBuilder: (context, index) => ItemWidget(items[index]),        // 惰性构建
);
// Sliver 组合：吸顶 + 分组
CustomScrollView(slivers: [
  SliverAppBar(pinned: true, title: Text('分组列表')),               // 吸顶
  ...groups.map((g) => [
    SliverPersistentHeader(pinned: true, delegate: GroupHeader(g)),   // 组吸顶
    SliverList(delegate: SliverChildBuilderDelegate(
      (context, i) => ItemWidget(g.items[i]),
      childCount: g.items.length)),
  ]).expand(),
])
// 检验：Flutter DevTools → Performance → 帧率（target 60fps）
```
