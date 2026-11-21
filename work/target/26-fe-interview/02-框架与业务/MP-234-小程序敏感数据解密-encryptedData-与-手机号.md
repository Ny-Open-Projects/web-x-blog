---
title: [MP-234] 敏感数据解密：encryptedData 与手机号快速验证的取舍？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-234：敏感数据解密方案取舍？
**答**：
- 老方案：button open-type=getPhoneNumber → code（新版）或 encryptedData/iv（老版）→ 服务端解密（session_key + AES）拿手机号。
- 新版推荐：getPhoneNumber 返回 code，服务端直接调 phonenumber.getPhoneNumber API（用 access_token）——不再依赖 session_key，解耦登录时序。
- encryptedData 风险：依赖 wx.login 时序（session_key 必须与 encryptedData 同批），过期即解密失败——时序 bug 高发区。
- 实名信息（昵称头像）：getUserProfile 已收紧，改用头像昵称填写能力（input type=nickname）。
- 合规：手机号获取需用户主动点击 + 隐私协议勾选，审核敏感。
