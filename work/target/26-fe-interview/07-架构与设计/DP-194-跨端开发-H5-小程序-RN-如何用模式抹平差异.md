---
title: [DP-194] 跨端开发（H5/小程序/RN）如何用模式抹平差异？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-194：跨端开发（H5/小程序/RN）如何用模式抹平差异？（高频）
**答**：
- 桥接模式：把"平台能力"抽象成统一接口（storage、request、navigate），各端实现各自的桥接实现（DP-040）；适配器：把三端组件 API 形状对齐（className↔class↔style 对象）。
- 工厂：构建期/运行期判定平台产出实现族（process.env.TARO_ENV / Taro.getSystemInfo）；策略：平台特有行为（下拉刷新、安全区）走平台策略文件。
- 分层纪律：业务代码只 import 抽象层，永远不出现 `if (isWeapp)` 散落在业务里——平台分支收敛到桥接实现内部。

```javascript
// 1 统一抽象接口（桥接的抽象侧）
// interface Platform { request(cfg): Promise<any>; setStorage(k, v): void; navigateTo(url): void; }
// 2 各端实现族（桥接的实现侧 + 适配器抹平参数差异）
class H5Platform {
  request(cfg) { return fetch(cfg.url, { method: cfg.method ?? 'GET', body: JSON.stringify(cfg.data) }).then((r) => r.json()); }   // 适配：data → body
  setStorage(k, v) { localStorage.setItem(k, JSON.stringify(v)); }
  navigateTo(url) { location.href = url; }
}
class WeappPlatform {
  request(cfg) { return new Promise((resolve, reject) => wx.request({ ...cfg, success: resolve, fail: reject })); }   // 适配：回调 → Promise
  setStorage(k, v) { wx.setStorageSync(k, v); }                // 小程序原生不需要序列化
  navigateTo(url) { wx.navigateTo({ url }); }
}
class RNPlatform {
  request(cfg) { return fetch(cfg.url, { method: cfg.method ?? 'GET', body: JSON.stringify(cfg.data) }).then((r) => r.json()); }
  setStorage(k, v) { AsyncStorage.setItem(k, JSON.stringify(v)); }
  navigateTo(url) { Navigation.navigate(url); }                // 适配：路由语义映射
}
// 3 工厂：平台判定只出现一次
export const platform = factories[process.env.TARO_ENV ?? 'h5']();
const factories = { h5: () => new H5Platform(), weapp: () => new WeappPlatform(), rn: () => new RNPlatform() };
// 4 业务代码：零平台分支（依赖倒置的收益）
export const userService = {
  getProfile(id) { return platform.request({ url: `/api/users/${id}` }); },
  saveProfile(u) { platform.setStorage('draft', u); return platform.request({ url: '/api/users', method: 'PUT', data: u }); },
  goDetail(id) { platform.navigateTo(`/pages/detail?id=${id}`); },
};
// 平台特有行为走策略文件：safe-area.h5.js / safe-area.weapp.js 同名导出，构建期按平台解析
import { useSafeArea } from './platform/safe-area';            // 构建器决定加载哪份实现
```
