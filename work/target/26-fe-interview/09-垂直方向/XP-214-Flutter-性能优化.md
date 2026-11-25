---
title: [XP-214] Flutter 性能优化：构建方法拆分与 const 优化
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-214：Flutter 性能优化：构建方法拆分与 const 优化

**答**：
- 题目：Flutter 页面掉帧——build 方法频繁全量重建。优化：拆分 widget/const 构造/RepaintBoundary 隔离重绘。
- 思路：build 拆分（子 widget 独立 StatefulWidget/state，局部重建）；const Widget（编译期常量跳过重建）；RepaintBoundary（重绘边界，隔离 paint 范围）。
- 评分点：拆分策略；const 优化；RepaintBoundary。

```javascript
// 优化前：一个巨大 build 全量重建
// 优化后：
class MyPage extends StatelessWidget {
  @override
  Widget build(context) {
    return Column(children: [
      const HeaderWidget(),                                    // const：跳过重建
      const Statusbar(),
      ListSection(),                                           // 独立 StatefulWidget（局部重建）
      const Footer(),
    ]);
  }
}
class ListSection extends StatefulWidget { ... }                // 独立状态（数据变只重建这）
// RepaintBoundary：隔离重绘
RepaintBoundary(child: ComplexPaintingWidget())                 // paint 隔离（兄弟不重绘）
// DevTools 检验：Flutter DevTools → Widget rebuild stats → 重建次数/耗时
```
