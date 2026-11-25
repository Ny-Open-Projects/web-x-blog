---
title: [MP-352] Page 构造器与页面级复用：全局 Behavior 模式
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## MP-352：Page 构造器与页面级复用：全局 Behavior 模式

**答**：
- Page 也能用 behaviors：页面级 Behavior（埋点/授权检查/分享统一）——Component 构造器构造页面（Component({...}) 带 behaviors）是现代写法
- 页面级 Behavior 的典型：埋点 Behavior（PV/停留时长自动上报——onShow/onHide 时间差）、授权 Behavior（进入页面检查登录态重定向）、性能 Behavior（onLoad→onReady 计时）
- 复用与拦截：Behavior 的生命周期先于页面执行——「前置校验拦截」（未登录 redirect）的实现位置
- 全局 Behavior 挂载：App 里无法全局注册 behavior——封装「页面工厂」（createPage(options) 合并 behaviors）——工厂函数是治理手段
- 深水点：Page 构造器的 wrap 能力——包装 setData（监控/合帧）在工厂层做一次，全站生效——「入口收敛」的治理价值

```javascript
// 页面工厂: 统一 behaviors + setData 包装
function createPage(options) {
  return Component({
    behaviors: [trackBehavior, authBehavior, perfBehavior],
    ...options,
    lifetimes: {
      attached() { this._origSetData = this.setData.bind(this);
        this.setData = wrapSetData(this._origSetData, this.route);   // 全站 setData 监控
        options.lifetimes?.attached?.call(this); },
    },
  });
}
Page(createPage({ data: {}, onLoad() {} }));   // 所有页面走工厂
```
