---
title: [MP-334] 小程序 web-view 与混合页面：H5 互操作
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## MP-334：小程序 web-view 与混合页面：H5 互操作

**答**：
- web-view 的定位：承载 H5 页面（企业域名白名单）——「小程序壳 + H5 内容」的混合形态（老 H5 复用/复杂富文本）
- 通信协议：小程序 → H5（URL 参数/动态改 src）——单向；H5 → 小程序（wx.miniProgram.postMessage——但消息在「特定时机」才收到（后退/销毁）——半双工现实）
- postMessage 的时机坑：小程序接收 H5 消息只在小程序后退/组件销毁/分享时（bindmessage）——实时通信不可行——「H5 主动触发小程序导航」用 wx.miniProgram.navigateTo（即时）
- JSSDK 能力：H5 侧 wx.miniProgram 可调 navigateTo/switchTab/getEnv——导航级互操作完整，数据级半双工
- 深水点：混合架构的数据一致性——H5 登录态与小程序 token 同步（URL 透传 token 或共享 Cookie 域）——「token 透传」的安全边界（短时效 ticket）

```html
<!-- H5 侧 -->
<script src="https://res.wx.qq.com/open/js/jweixin-1.6.0.js"></script>
<script>
  wx.miniProgram.postMessage({ data: { action: 'select', id: 42 } });   // 延迟送达!
  wx.miniProgram.navigateTo({ url: '/pages/detail/index?id=42' });      // 即时导航
</script>
```

```javascript
// 小程序侧
<web-view src="{{url}}" bindmessage="onMessage" bindload="onLoad" />
onMessage(e) { const data = e.detail.data.at(-1); }   // 数组: 累积消息, 取最后
// token 透传: url 拼接 ticket (一次性短时效) → H5 换正式 token
```
