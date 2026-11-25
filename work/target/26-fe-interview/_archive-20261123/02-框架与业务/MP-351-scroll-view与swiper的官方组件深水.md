---
title: [MP-351] 官方组件深水：scroll-view 与 swiper 的进阶用法
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 面试题, 交互]
type: 面试题
---

## MP-351：官方组件深水：scroll-view 与 swiper 的进阶用法

**答**：
- scroll-view 进阶：enhanced 模式（原生滚动条/惯性可配 fast-deceleration）、refresher-enabled（下拉刷新内置——refresher-triggered 双向控制）、scroll-into-view/scroll-top（编程定位——锚点跳转）、paging-enabling（滚动分页加载）
- swiper 进阶：displayMultipleItems（多 item 视口）、current 双向绑定（ indicator 同步）、性能约束（同屏 swiper-item 数量——每个是独立渲染节点，>6 个考虑虚拟化）
- 事件体系：bindscroll 的频率（每帧触发——节流处理）、bindscrolltolower（上拉加载触发的双通道：事件 vs IO observer）
- 嵌套滚动冲突：scroll-view 嵌 scroll-view（内层到底让外层滚）——方向互斥（横竖嵌套天然无冲突，同向嵌套要手势协商）
- 深水点：scroll-view 的「异步定位」——scroll-into-view 生效时机在数据渲染后（setData 完成回调里设置才可靠）——时序感知

```xml
<scroll-view enhanced show-scrollbar="{{false}}" fast-deceleration="{{true}}"
  refresher-enabled refresher-triggered="{{refreshing}}"
  bindrefresherrefresh="onRefresh" bindscrolltolower="onLoadMore"
  scroll-into-view="{{anchor}}" scroll-with-animation>
  <!-- ... -->
</scroll-view>
```

```javascript
// 异步定位时序
async function jumpTo(i) {
  await new Promise((r) => this.setData({ list: this.data.list }, r));  // 数据渲染完
  this.setData({ anchor: `item-${i}` });           // 再设置锚点才可靠
}
```
