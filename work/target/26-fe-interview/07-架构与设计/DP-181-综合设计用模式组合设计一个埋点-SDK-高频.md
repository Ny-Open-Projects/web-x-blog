---
title: [DP-181] 综合设计：用模式组合设计一个埋点 SDK？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-181：综合设计：用模式组合设计一个埋点 SDK？（高频）
**答**：
- 组合：外观（track 一行接入）、职责链（数据管道：公共字段→脱敏→采样→校验）、策略（采样策略：全量/比例/白名单；上报策略：beacon/fetch）、享元（批量队列合并 + 实例复用，DP-097）、单例（全局唯一）、观察者（自动埋点：监听全局 click/route/error）。
- 可靠性三件套：批量缓冲 + 失败回补 + 页面卸载 flush（visibilitychange 触发 sendBeacon）。
- 与 DP-146 差别：146 给通用 SDK 骨架，本题聚焦埋点域模型（事件分级、自动埋点、采样）。

```javascript
class Tracker {
  #queue = []; #mws = []; #strategy; #staticProps = {};
  constructor({ sample = 'all', endpoint } = {}) {
    this.#strategy = samplers[sample];                        // 策略：采样器
    document.addEventListener('visibilitychange', () => document.hidden && this.flush());  // 卸载兜底
    this.autoTrack();                                         // 观察者：自动埋点
  }
  setCommonProps(props) { Object.assign(this.#staticProps, props); }
  use(fn) { this.#mws.push(fn); return this; }                // 职责链
  track(event, props = {}) {
    let evt = { event, props: { ...this.#staticProps, ...props }, ts: Date.now() };
    for (const mw of this.#mws) { evt = mw(evt); if (!evt) return; }   // 链上可丢弃
    if (!this.#strategy(evt)) return;                         // 策略：采样否决
    this.#queue.push(evt);                                    // 享元：攒批
    if (this.#queue.length >= 10) this.flush();
  }
  flush() {
    if (!this.#queue.length) return;
    const batch = this.#queue.splice(0);                      // 快照取走
    transport.send(this.endpoint, batch).catch(() => this.#queue.unshift(...batch));  // 失败回补
  }
  autoTrack() {                                               // 观察者：全局代理埋点
    document.addEventListener('click', (e) => {
      const el = e.target.closest('[data-track]');
      if (el) this.track('click', { id: el.dataset.track });
    }, true);
  }
}
const samplers = { all: () => true, half: () => Math.random() < 0.5,
  whitelist: (e) => e.event === 'error' || e.event === 'pay' };   // 关键事件必采
const transport = {                                           // 策略：上报通道
  send: (url, data) => navigator.sendBeacon ? Promise.resolve(navigator.sendBeacon(url, JSON.stringify(data))) : fetch(url, { method: 'POST', body: JSON.stringify(data) }),
};
export const tracker = new Tracker({ sample: 'whitelist', endpoint: '/collect' })  // 单例出口
  .use((e) => ({ ...e, props: { ...e.props, uid: store.userId } }));
```
