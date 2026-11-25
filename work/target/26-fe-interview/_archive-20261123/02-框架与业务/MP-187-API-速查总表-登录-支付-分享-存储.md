---
title: [MP-187] API 速查总表（登录/支付/分享/存储）？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-187：API 速查总表（登录/支付/分享/存储）？
**答**：
- 高频 API 的"入口 → 关键参数 → 坑"三列速查；考前记忆锚点。

```json
{
  "login": {
    "wx.login": { "returns": "code(5min一次性)", "pitfall": "服务端 code2session, session_key 不下发" },
    "wx.checkSession": { "returns": "session_key 是否有效", "pitfall": "失效需重新 login" },
    "getPhoneNumber": { "params": "button open-type=getPhoneNumber", "pitfall": "新方案 code 换手机号免 session_key" }
  },
  "pay": {
    "wx.requestPayment": { "params": "timeStamp/nonceStr/package/signType/paySign", "pitfall": "参数全部来自服务端统一下单" },
    "回调": { "pitfall": "验签+幂等+金额比对" }
  },
  "share": {
    "onShareAppMessage": { "returns": "title/imageUrl/path", "pitfall": "path 带归因参数需验签" },
    "onShareTimeline": { "note": "单页模式打开, 不走 onLoad query 全量" },
    "showShareMenu": { "note": "开启转发/朋友圈按钮" }
  },
  "storage": {
    "wx.setStorageSync": { "limit": "单 key 1MB, 总 10MB", "pitfall": "不走 LRU, 自管清理" },
    "wx.getStorageInfo": { "returns": "currentSize/keys" }
  }
}
```
