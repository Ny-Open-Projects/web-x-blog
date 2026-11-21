---
title: [XP-058] 设计一个跨端埋点 SDK（采集层适配）？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-058：设计一个跨端埋点 SDK（采集层适配）？
**答**：
- 分层设计：**采集层**（自动采集：PV/点击/曝光/时长；手动 API）→ **处理层**（统一事件协议、公共属性注入、采样与队列）→ **发送层**（批量、重试、本地缓存、多通道）→ **适配层**（各端系统信息/存储/网络实现，XP-045 同构）。
- 统一事件模型：`{ event, ts, user, device, page, props, sdkVer, appVer }`，各端字段口径一致（对接看板 XP-069）。
- 关键实现点：曝光用 IntersectionObserver/原生可见性回调 + 去重（同 item 会话内一次）；队列本地持久化防丢；启动期埋点补发（时序问题）；时钟漂移校正。
- 性能与隐私：批量上报（满 N 条或 T 秒）、弱网降采样、敏感字段脱敏、SDK 本身体积与耗时预算（< 50KB，初始化 < 10ms）。

```typescript
// packages/tracking —— 跨端埋点 SDK 骨架
interface Event { event: string; ts: number; props: Record<string, unknown>; common: CommonFields }

class TrackSDK {
  #queue: Event[] = [];
  constructor(private adapter: ITrackAdapter) {}        // 适配层注入（storage/network/device）
  track(event: string, props = {}) {
    this.#queue.push({ event, ts: this.adapter.now(), props,
      common: this.adapter.commonFields() });            // 统一公共属性：appVer/deviceId/page/traceId
    if (this.#queue.length >= 10) this.#flush();
  }
  expose(componentId: string, ref:unknown, extra = {}) { // 曝光：适配层提供可见性探测
    this.adapter.observeVisible(ref, () => {
      this.track('expose', { componentId, ...extra });   // 内部按 id 会话去重
    });
  }
  async #flush(retry = 0) {
    const batch = this.#queue.splice(0, 50);
    try { await this.adapter.network.post('/t.gif', batch, { keepalive: true }); }
    catch {
      await this.adapter.storage.append('track_dead', batch);   // 失败落盘，下次启动补发
      if (retry < 3) setTimeout(() => this.#flush(retry + 1), 2 ** retry * 1000);
    }
  }
}
// 各端 adapter：weapp（wx.getSystemInfo/Storage/IntersectionObserver）
// h5（navigator.sendBeacon/localStorage/IntersectionObserver）、rn（NativeModules/AsyncStorage/View.onLayout）
```
