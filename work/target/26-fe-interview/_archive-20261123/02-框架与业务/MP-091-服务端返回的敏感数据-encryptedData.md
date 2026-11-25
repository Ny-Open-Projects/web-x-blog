---
title: [MP-091] 服务端返回的敏感数据（encryptedData）如何安全解密？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-091：服务端返回的敏感数据（encryptedData）如何安全解密？
**答**：
- 旧方案：微信返回 `encryptedData + iv`，用 `session_key` 做 **AES-128-CBC** 解密得用户开放数据（手机号/运动步数等）——session_key 不能出后端。
- 新方案已尽量改为 **code 换数据**（如手机号）或**云调用**（云函数中 cloud.decrypt 直接解，免 session_key 管理）。
- 安全要点：解密只发生在服务端；校验 watermark（appid/openid）防伪造；数据不落日志。

```javascript
// 云函数中：cloudID 直接换开放数据（如运动步数），免 session_key 管理
exports.main = async (event) => {
  const { cloudID } = event.myWeRunData        // 开放数据 cloudID
  const res = await cloud.getOpenData({ list: [cloudID] })
  const steps = res.list[0].data.weRunData.stepList
  return { steps }                             // 服务端处理，数据不落日志
}
```
