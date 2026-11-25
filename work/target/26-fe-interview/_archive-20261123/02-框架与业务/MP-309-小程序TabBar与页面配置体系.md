---
title: [MP-309] 小程序 TabBar 与页面配置体系
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## MP-309：小程序 TabBar 与页面配置体系

**答**：
- 原生 tabBar vs 自定义 tabBar：原生（配置简单、性能好、样式受限）；自定义（custom: true + custom-tab-bar 组件——自由样式、红点/动态渲染，但每 tab 页都要渲染组件实例）
- 自定义 tab-bar 的坑：每个 tab 页面的 custom-tab-bar 是「独立实例」（不共享）——选中态同步用 getTabBar() 手动触发（onShow 里 setData 选中项）
- 页面配置层级：全局 window 配置 < 页面 json 配置（navigationBarTitleText/enablePullDownRefresh 等覆盖）；动态改用 wx.setNavigationBarTitle
- navigationStyle: custom：自绘导航栏——「胶囊按钮对齐」（wx.getMenuButtonBoundingClientRect 计算可用区域）是自定义导航的核心公式
- 深水点：自定义导航的安全区公式：状态栏高度 + 胶囊高度 + 边距 = 导航内容高度；全屏页面还要处理底部安全区（env(safe-area-inset-bottom) 等价能力）

```javascript
// 自定义导航栏高度计算
function navBarMetrics() {
  const { top, height, bottom } = wx.getMenuButtonBoundingClientRect();
  const statusBarHeight = top;                       // 胶囊顶 = 状态栏底
  const navBarHeight = (bottom - top) + (top - wx.getSystemInfoSync().statusBarHeight) * 2;
  return { statusBarHeight, navBarHeight, total: statusBarHeight + navBarHeight };
}
// 自定义 tab 选中态同步(每个 tab 页 onShow):
onShow() { this.getTabBar()?.setData({ selected: 1 }); }
```
