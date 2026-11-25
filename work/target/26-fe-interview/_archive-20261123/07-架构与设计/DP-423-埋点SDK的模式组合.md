---
title: [DP-423] 案例：埋点 SDK 的模式组合
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 面试题, 设计模式]
type: 面试题
---

## DP-423：埋点 SDK 组合

**答**：
- 埋点 SDK 模式全景：观察者（自动采集：click/pv 事件订阅）、责任链（上报管道：采样→压缩→批量→发送）、策略（上报策略：即时/批量/页面隐藏触发）、代理（track API 的封装——业务无感知）、备忘录（失败落盘恢复）
- 自动采集的设计：声明式（data-track 属性 + 全局委托——零埋点成本）+ 命令式（track() 显式——关键业务事件）
- 曝光埋点：IO observer 封装（进视口 + 停留时长 + 会话去重——三条件标准协议）
- 深水点：埋点的「性能红线」——批量/上限/丢弃计数（埋点不能拖垮业务页面）——SDK 自身的性能预算

```javascript
class Tracker {
  #queue = createBatcher({ maxSize: 20, windowMs: 5000, flush: send });
  track(event, props) { this.#queue.add({ event, props, t: Date.now(), ...commonFields }); }
  // 自动采集: document.addEventListener('click', (e) => {
  //   const t = e.target.closest('[data-track]');
  //   t && this.track('click', { target: t.dataset.track });
  // }, true);
}
// flush 时机: 满 20 / 5s / pagehide — 三触发
```
