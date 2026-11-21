---
title: [DP-113] 如何用"外观 + 适配器"组合统一多家埋点/推送 SDK？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-113：如何用"外观 + 适配器"组合统一多家埋点/推送 SDK？（高频）
**答**：
- 外观：给业务一个稳定小接口 `track(event, props)` / `push(msg)`，业务永远不直接 import 厂商 SDK；适配器：把各厂商 API 形状抹平成内部接口。
- 换厂商 = 只换适配器注册，业务代码零改动（DIP：业务依赖内部接口而非具体厂商）。
- 附加价值：外观层统一做公共字段（userId、env）、采样、灰度开关，厂商差异不再泄漏进业务。

```javascript
// 内部统一接口（业务只认识它）
// track(event: string, props: object): void
class SensorsAdapter {                                      // 适配器1
  init(cfg) { window.sensors.init(cfg); }
  track(event, props) { window.sensors.track(event, props); }
}
class GrowingAdapter {                                      // 适配器2：字段名/调用方式都不同
  init(cfg) { window.gio('init', cfg.projectId); }
  track(event, props) { window.gio('track', event, props); }
}
class TrackerFacade {                                       // 外观：业务唯一入口
  #adapter; #common;
  constructor(adapter, common) { this.#adapter = adapter; this.#common = common; }
  static create(vendor, common) {                           // 简单工厂选适配器
    const map = { sensors: SensorsAdapter, growing: GrowingAdapter };
    return new TrackerFacade(new map[vendor](), common);
  }
  init(cfg) { this.#adapter.init(cfg); }
  track(event, props = {}) {
    this.#adapter.track(event, { ...this.#common, ...props });   // 公共字段统一注入
  }
}
export const tracker = Tracker.create('sensors', { env: 'prod', userId: store.userId });
tracker.track('pay_click', { channel: 'wechat' });          // 换厂商只改 create('growing') 一处
```
