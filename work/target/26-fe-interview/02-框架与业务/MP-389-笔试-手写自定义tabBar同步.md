---
title: [MP-389] 笔试：手写自定义 tabBar（选中态同步与徽标）
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## MP-389：笔试：手写自定义 tabBar

**答**：实现 custom-tab-bar 组件：① 每个页面独立实例的选中态同步（getTabBar().setData 在各 tab 页 onShow）——封装成 Behavior 自动化；② 未读徽标（全局 store 订阅——badge 数字变化全 tab 实例同步）；③ 中间凸起按钮（特殊 item 处理——点击走 switchTab 之外的逻辑）；④ 双击回到顶部（同 tab 再点击 → 通知当前页 scrollTop）；⑤ 渲染性能（徽标数字变化只 setData badge 字段）。写出实现。

```javascript
// custom-tab-bar/index.js
Component({
  data: { selected: 0, badges: {} },
  lifetimes: { attached() {
    getApp().event.on('badge', (b) => this.setData({ badges: b }));    // 全局订阅
  } },
  methods: {
    onTap(e) {
      const { index, type } = e.currentTarget.dataset;
      const page = getCurrentPages().at(-1);
      if (page.route === TABS[index].path) {           // 同 tab 再点: 双击回顶
        page.onTabReselect?.();
        return;
      }
      if (type === 'action') return this.onAction();   // 中间凸起: 特殊逻辑
      wx.switchTab({ url: TABS[index].path });
    },
  },
});
// 自动同步 Behavior (每个 tab 页使用):
export const tabBarSync = (index) => Behavior({
  pageLifetimes: {
    show() { this.getTabBar()?.setData({ selected: index }); },   // 独立实例同步
  },
});
// 双击回顶: 页面实现 onTabReselect() { wx.pageScrollTo({ scrollTop: 0, duration: 200 }) }
```

**评分点**：
- 每页独立实例的同步机制（getTabBar + onShow Behavior 自动化）
- 徽标全局订阅（badge 事件 → 各实例 setData）
- 同 tab 再点的「双击回顶」协议（page.onTabReselect）
- 中间凸起按钮的非 tab 逻辑分流
