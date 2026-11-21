---
title: [MP-126] 如何解密用户敏感数据（encryptedData/iv）？新版方案呢？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-126：如何解密用户敏感数据（encryptedData/iv）？新版方案呢？
**答**：
- 旧版：`getPhoneNumber`/`getUserProfile` 等返回 `encryptedData + iv`，服务端用 **session_key + AES-128-CBC** 解密得到明文（手机号/openid 等）；session_key 过期会导致解密失败（-41008），需 `checkSession` 后重 login。
- 新版（推荐）：直接用 `code` 调服务端 `getuserphonenumber` 接口拿 access_token 换手机号，或 `cloudID` 云开发直解，**绕开 session_key 管理**。
- 解密结果要校验 `watermark.appid` 与自家 appid 一致，防止跨小程序数据混用。
- 手机号属于敏感个人信息：明文不落日志、按需展示脱敏，遵守《个人信息保护法》最小化原则。

```javascript
// 服务端解密 encryptedData（旧版）
const crypto = require('crypto')
function decryptData(encryptedData, iv, sessionKey, appid) {
  const key = Buffer.from(sessionKey, 'base64')
  const decipher = crypto.createDecipheriv('aes-128-cbc', key, Buffer.from(iv, 'base64'))
  decipher.setAutoPadding(true)
  let decoded = decipher.update(Buffer.from(encryptedData, 'base64'), 'binary', 'utf8')
  decoded += decipher.final('utf8')
  const data = JSON.parse(decoded)
  if (data.watermark.appid !== appid) throw new Error('watermark appid mismatch') // 校验来源
  return data // { phoneNumber, purePhoneNumber, countryCode, ... }
}
// 新版：code 换手机号，无 session_key 依赖
const phone = await fetchJSON(`https://api.weixin.qq.com/wxa/business/getuserphonenumber?access_token=${token}`, {
  method: 'POST', body: JSON.stringify({ code: req.body.phoneCode })
})
```
