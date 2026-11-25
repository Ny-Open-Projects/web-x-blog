---
title: [MP-303] WXS 与 Skyline：渲染层脚本的演进
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## MP-303：WXS 与 Skyline：渲染层脚本的演进

**答**：
- WXS（WeiXin Script）：渲染层内运行的 JS 子集——与视图同线程，响应数据变化即时更新（无跨线程延迟）；限制：语法 ES5 子集、不能调业务接口
- WXS 的招牌场景：滚动联动（scroll-view 的滚动位移驱动样式）、手势动画（touchmove 实时跟手）——setData 方案在这些场景必然卡顿
- Skyline 渲染引擎：新一代渲染层（非 WebView，自绘）——worklet 语法（类 Reanimated）在渲染线程跑 UI 函数；WXS 的进化版
- Skyline 的能力解锁：真正的同步 DOM 查询、手势系统、更好的列表性能——但组件覆盖度/兼容性是迁移成本
- 深水点：worklet 与 WXS 的关系——worklet 是 Skyline 下的新范式（函数序列化到渲染线程），WXS 是 WebView 时代的方案；迁移时两者不混用

```javascript
// WXS: 滚动联动
// <wxs module="fx"> module.exports = { transform: function(scrollTop) { return 'translateY(' + scrollTop/2 + 'px)' } } </wxs>
// <view style="{{fx.transform(scrollTop)}}">  ← 渲染层即时计算, 无 setData
// Skyline worklet:
// wx.worklet.shared(scrollY); UI 侧 worklet 函数直接响应 shared 值变化 → 同线程更新
```
