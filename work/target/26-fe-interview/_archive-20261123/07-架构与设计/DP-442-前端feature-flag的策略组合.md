---
title: [DP-442] 案例：Feature Flag 的模式组合
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 面试题, 设计模式]
type: 面试题
---

## DP-442：Feature Flag 组合

**答**：
- Feature Flag 的模式全景：策略（分流策略：全局/灰度哈希/AB 实验）、观察者（flag 变更推送 → 订阅组件热更新）、命令（开关切换——审计）、代理（flag() 的判定封装——业务无感知）
- flag 的三语义：布尔开关（有/无功能）、多值（variant：A/B/C 方案）、灰度比例（rollout 0.3）——类型化的 flag 设计
- flag 的生命周期：创建 → 生效 → 清理（完结 flag 的代码删除——flag 债）
- 深水点：flag 的「就绪时序」——首屏渲染前 flag 必须就绪（同步注入/启动拉取——异步 flag 导致闪烁与二次渲染）

```javascript
class Flags {
  #map = new Map(); #subs = new Set();
  get(key) {
    const cfg = this.#map.get(key);
    if (!cfg) return null;
    if (typeof cfg === 'boolean') return cfg;
    if (cfg.rollout != null) return hash(`${key}:${uid}`) < cfg.rollout;   // 灰度
    return cfg.variant;                                  // 多值
  }
  setAll(map) { this.#map = new Map(Object.entries(map)); this.#subs.forEach((f) => f()); }   // 热更新
}
// 就绪时序: <script> 注入初始 flags → 启动无闪烁 → onShow 增量更新
```
