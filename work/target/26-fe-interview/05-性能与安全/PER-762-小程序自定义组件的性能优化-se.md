---
title: [PER-762] 小程序自定义组件的性能优化： setData 边界、组件间通信与复用池
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-762：小程序自定义组件的性能优化： setData 边界、组件间通信与复用池

**答**：
- 自定义组件的 setData 隔离：组件内 setData 只触发该组件的跨线通信与 diff——把高频更新收进小组件（如倒计时组件内部 setData）而不是页面级 setData，能大幅降低通信量。
- 组件通信：properties 传大数据（完整列表）会让每次父渲染都触发子组件 observer——传 id/索引由子组件自行取数；observer 里做 diff（值没变直接 return）。
- 复用池：列表项组件（重的如视频卡片）回收复用（组件实例池），避免频繁创建销毁（创建含组件树构建，约 10~50ms/个）。
- 静态节点优化：纯静态子树用 `pure` 数据或直接写 wxml 静态片段（不进 data），减少 diff 范围；Skyline 引擎下组件通信成本进一步变化要重测。

```javascript

// 高频更新收敛到小组件 + observer diff
Component({
  properties: {
    itemId: String,                                             // 只传 id，子组件自取数
  },
  observers: {
    itemId(v, old) { if (v === old) return; this.loadData(v); } // 值没变不触发
  },
  lifetimes: {
    attached() { this.timer = setInterval(() => this.tick(), 1000); },  // 倒计时收进组件
    detached() { clearInterval(this.timer); }                   // 严格清理
  },
  methods: {
    tick() { this.setData({ remain: this.remain() }); },        // 只更新本组件
    async loadData(id) {
      const item = await getItemById(id);
      this.setData({ title: item.title, price: item.price });   // 最小字段
    },
  },
});
// 组件复用池：重列表项回收复用，避免每次创建组件树
```
