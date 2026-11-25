---
title: [SCN-186] 同一个业务要在 H5、小程序、App 内嵌页三端实现，页面 90% 相同，如何收敛技术方案？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-186：同一个业务要在 H5、小程序、App 内嵌页三端实现，页面 90% 相同，如何收敛技术方案？
**答**：
- 先量化再选型：盘点页面清单、交互差异（手势/分享/支付）、端能力 API 重合度。90% 重合是跨端框架的甜蜜区，差异部分走"平台分支"而不是三份代码。
- 选型对比三线：跨端框架（Taro/uni-app，一套代码多端产出）、自研适配层（业务代码 + 端能力抽象接口）、微前端（不适用多端）。结论通常是跨端框架 + 薄适配层。
- 架构分层：UI 与业务逻辑归框架层，端能力（支付/分享/定位/存储）收口到 adapter 接口，三端各实现一份，业务代码零条件分支。
- 渐进迁移：新页面一律新架构，老页面按改动频率逐步迁，设"端差异只允许出现在 adapter 层"的 lint 规则。

```javascript
// 三端收敛：端能力 adapter 抽象，业务代码零平台分支
// adapter 定义：端差异只允许出现在这里
export interface PlatformAdapter {
  pay(orderNo: string): Promise<PayResult>;
  share(payload: SharePayload): Promise<void>;
  getLocation(): Promise<{ lat: number; lng: number }>;
  setNavTitle(title: string): void;
  storage: { get(k: string): any; set(k: string, v: any): void };
}

// h5Adapter.ts —— H5 实现
export const h5Adapter: PlatformAdapter = {
  async pay(orderNo) { location.href = await api.getPayUrl(orderNo, 'h5'); return { channel: 'h5' }; },
  async share(payload) { await navigator.share?.(payload).catch(() => copyLink(payload.url)); },
  getLocation() { return geo.getCurrentPosition(); },
  setNavTitle: t => (document.title = t),
  storage: localStorageLike,
};

// taroAdapter.ts —— 小程序实现（Taro API）
export const taroAdapter: PlatformAdapter = {
  async pay(orderNo) { return Taro.requestPayment(await api.getPayParams(orderNo)); },
  share: payload => new Promise((res, rej) => Taro.showShareMenu({ success: res, fail: rej })),
  getLocation: () => Taro.getLocation({ type: 'gcj02' }),
  setNavTitle: t => Taro.setNavigationBarTitle({ title: t }),
  storage: { get: k => Taro.getStorageSync(k), set: (k, v) => Taro.setStorageSync(k, v) },
};

// 业务代码：只依赖接口，不知道自己跑在哪端
export function useCheckout(adapter: PlatformAdapter) {
  return {
    async submit(orderNo: string) {
      const result = await adapter.pay(orderNo);       // 三端同一份业务逻辑
      track('pay_submit', { orderNo, channel: result.channel });
      return result;
    },
  };
}
// 平台差异 lint：业务层 import 端 API 直接报错，只能 import adapter
// eslint rule: no-restricted-imports ["error", { paths: [{ name: "@tarojs/taro", message: "业务层禁止直接使用端 API，请用 adapter" }] }]
```
