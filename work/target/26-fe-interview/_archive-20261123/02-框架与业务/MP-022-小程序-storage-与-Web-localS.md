---
title: [MP-022] 小程序 storage 与 Web localStorage 的隔离差异？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-022：小程序 storage 与 Web localStorage 的隔离差异？
**答**：
- 隔离维度：Web 按**域名（同源策略）**隔离；小程序按 **appid** 隔离，与域名无关，不同小程序互不可见。
- 容量：localStorage 约 5MB；小程序 storage 总量 10MB、单 key 1MB。
- 生命周期：localStorage 可被用户清除/受隐私模式影响；小程序 storage 由 native 持久化管理，删除小程序才清空（系统清理行为除外）。
- 小程序没有 Cookie，也不受浏览器分区存储（localStorage 的 7 天限制等策略）影响。

```javascript
// 本设备上不同 appid 的小程序之间互相隔离
wx.setStorageSync('secret', 'only-visible-to-this-appid')
const info = wx.getStorageInfoSync()
console.log(info.keys, info.currentSize, info.limitSize) // limitSize 单位 KB，10240 = 10MB
```

---

## 四、组件体系（023-030）
