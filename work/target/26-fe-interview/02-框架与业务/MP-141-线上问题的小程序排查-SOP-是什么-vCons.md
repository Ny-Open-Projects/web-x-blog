---
title: [MP-141] 线上问题的小程序排查 SOP 是什么（vConsole/realtime log）？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-141：线上问题的小程序排查 SOP 是什么（vConsole/realtime log）？
**答**：
- 第一步**定性**：运维中心看错误趋势/影响版本/平台分布；是全量劣化（发版引入）还是个例（机型/账号相关）。
- **realtime log**（实时日志）：用户投诉带 openid/时间点，后台按用户检索其打点日志（wx.getRealtimeLogManager），比 console 上报全且实时。
- 端内复现：让用户打开调试（vConsole）截图，或给用户发**体验版**（带同环境）复现；公众号后台可拉用户Debug 信息。
- 数据补充：自建 APM 查该用户请求流水；必要时拉用户到客服群远程指导。
- 处置：热修（revert 发版）或配置开关降级；事后复盘写案例库。

```javascript
// 实时日志打点封装
const rt = wx.getRealtimeLogManager ? wx.getRealtimeLogManager() : null
const rtlog = {
  info(tag, data) { rt && rt.info(tag, JSON.stringify(data).slice(0, 2000)) },
  error(tag, err) { rt && rt.error(tag, String(err && err.stack || err).slice(0, 2000)) },
  warn(tag, data) { rt && rt.warn(tag, JSON.stringify(data)) }
}
Page({
  async onSubmit() {
    rtlog.info('order-submit', { skuId: this.skuId, price: this.price })
    try { await api.createOrder() } catch (e) {
      rtlog.error('order-submit-fail', e)   // 用户投诉时后台按 openid 检索
      throw e
    }
  }
})
```

## 十七、工程化深化（142-147）
