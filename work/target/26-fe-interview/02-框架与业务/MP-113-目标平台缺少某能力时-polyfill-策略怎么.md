---
title: [MP-113] 目标平台缺少某能力时，polyfill 策略怎么定？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-113：目标平台缺少某能力时，polyfill 策略怎么定？
**答**：
- 先做**能力检测**而非平台判断（`typeof wx.getFileSystemManager === 'function'`），低版本宿主也可受益。
- 三级策略：**模拟实现**（纯前端可模拟，如 storage 降级到内存 Map）、**替代方案**（没有订阅消息就发模板消息/短信）、**明确降级**（无法模拟的能力隐藏入口并埋点记录）。
- polyfill 统一放在启动早期注册，与标准 API 同签名，业务代码无感；每个 polyfill 标注适用版本范围并定期清理。
- 不可 polyfill 的关键链路（支付）要在 UI 层提前拦截，提示"当前版本不支持"。

```javascript
// 能力检测式 polyfill：旧版无 wx.getSystemSetting 时模拟
if (typeof wx.getSystemSetting !== 'function') {
  wx.getSystemSetting = () => ({
    bluetoothEnabled: false, deviceOrientation: 'portrait',
    locationEnabled: undefined, wifiEnabled: undefined
  })
}
// storage 内存降级（极少数受限环境）
const mem = {}
if (typeof wx === 'undefined' || !wx.setStorageSync) {
  globalThis.wx = {
    setStorageSync: (k, v) => { mem[k] = v },
    getStorageSync: (k) => mem[k],
    removeStorageSync: (k) => { delete mem[k] }
  }
}
```
