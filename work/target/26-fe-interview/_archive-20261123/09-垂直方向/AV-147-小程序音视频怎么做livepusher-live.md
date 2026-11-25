---
title: [AV-147] 小程序音视频怎么做？live-pusher/live-player 有什么限制？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-147：小程序音视频怎么做？live-pusher/live-player 有什么限制？（高频）
**答**：
- 组件：live-pusher（推流）/live-player（拉流），需要主体类目资质声明，个人主体不可用；组件是原生层渲染。
- 模式：live-player mode="RTC" 走 RTC 链路（延迟 <500ms），mode="live" 走 CDN（1-3s）；连麦 = 双组件（自己推 + 订阅对方）。
- 限制：不支持 MSE/WebRTC JS 栈；切后台即断流（音频后台模式需单独申请）；原生组件层级最高，覆盖 UI 必须用 cover-view。
- 与 H5 互通：同一信令与 SFU，小程序走原生组件、Web 走 MSE/WebRTC，业务层协议统一（关联 AV-126）。
- 状态驱动：bindstatechange 返回码表驱动重连与 UI 状态，错误码要全量映射。

```html
<!-- 小程序连麦页面（WXML 形态） -->
<live-pusher id="pusher" url="{{pushUrl}}" mode="RTC"
  enable-mic="true" enable-camera="true" autopush
  bindstatechange="onPushState"
  style="width:180rpx;height:320rpx" />
<live-player id="player" url="{{playUrl}}" mode="RTC" autoplay
  bindstatechange="onPlayState"
  style="width:750rpx;height:422rpx" />
<cover-view class="ctrl-btn" bindtap="toggleMic">静音</cover-view>
<!-- 注意：原生组件层级最高 普通view会被盖住 必须cover-view -->
<script>
// pushUrl/playUrl 由业务服务端生成（含防盗链签名） 小程序端不落密钥
function onPushState(e) {
  const code = e.detail.code;
  if (code === -1307) reconnectPush();        // 断网码表驱动重连
  if (code === 3002) reSignPushUrl();         // 推流URL签名过期 重新拉取
}
</script>
```
