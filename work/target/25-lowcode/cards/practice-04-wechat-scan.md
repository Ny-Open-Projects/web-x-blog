---
title: 微信扫码登录全链路：ticket、XML 回调与轮询
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 实战, 微信, 登录]
---

## 微信扫码登录全链路：ticket、XML 回调与轮询

**链路**：点击登录 → 接入验证 → 生成二维码 → Redis 存 `isScan:'no'` → 用户扫码 → 微信回调 → 查/建用户签发 token、置 `isScan:'yes'` → 前端轮询拿 token。

三步生成二维码：`getAccessToken`（所有微信能力的钥匙）→ `getTicket` → 拼 `qrUrl?ticket=xxx`；临时二维码 `expire_seconds:120`；Redis key `wechat:ticket:${ticket}` 存 `{isScan:'no'}` 同步 120 秒过期——**ticket 就是扫码会话的 key**，openId 是微信用户唯一标识。

接入验证：微信回传 signature/timestamp/nonce/echostr，校验 = 三参数字典序排序 + SHA1 比对 signature，通过原样返回 echostr（响应拦截器要兼容直接返回字符串）。本地调试用花生壳内网穿透暴露 3000 端口。

回调处理：POST 收 XML，`xml2js` 解析 + 拍平（正式版 XML 流式解析 getXMLStr 在工程里仍是注释状态，实际走 JSON 形态；signature 校验留白——讲设计别讲成全链路已跑通），`FromUserName` 即 openId——按其查用户、无则插入（自动建号），新老用户都签发 JWT；Redis 存对象必须 `JSON.stringify`。

为什么用轮询不用 WebSocket？前端 `useRequest` + `debounceWait:2000` 两秒一查，实现简单且 120 秒窗口内轮询成本可接受。

出处「课程25 · 12-1~12-6、13-9」
