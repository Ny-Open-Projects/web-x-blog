---
title: [MP-046] getUserProfile 之后，用户信息（头像昵称）获取的现状？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-046：getUserProfile 之后，用户信息（头像昵称）获取的现状？
**答**：
- 旧 `wx.getUserInfo` 早已停止返回真实信息；`getUserProfile` 曾需用户点击触发并弹窗，但 2022 年 10 月后接口**回收**，返回的全是"微信用户"与灰色头像。
- 现行推荐："头像昵称填写能力"——头像用 `<button open-type="chooseAvatar">` 让用户选择/拍照，昵称用 `<input type="nickname">` 唤起键盘上方的昵称快捷填入。
- 面试要点：能说清"从静默获取到用户主动填写"的产品逻辑变化。

```xml
<!-- 头像：open-type=chooseAvatar -->
<button open-type="chooseAvatar" bind:chooseavatar="onChooseAvatar">
  <image src="{{avatarUrl}}" mode="aspectFill" />
</button>

<!-- 昵称：type=nickname 唤起快捷填入 -->
<input type="nickname" placeholder="请输入昵称" bind:blur="onNickname" />
```
