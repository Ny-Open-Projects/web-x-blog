---
title: [XP-043] uni-app 的运行时原理？编译时与运行时如何混合？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-043：uni-app 的运行时原理？编译时与运行时如何混合？
**答**：
- **双引擎架构**：Vue 源码经**编译器**（vue-cli/vite 插件）按目标端输出——小程序端编译成 WXML/JSON/JS；App 端（HBuilderX/nvue）保留运行时渲染。
- 小程序端模式与 Taro 类似：运行时把 Vue 的渲染函数产物转为 setData 数据流；H5 端直接走标准 vue-dom。
- **App 端分两路**：vue 页面走 WebView 渲染；nvue 页面走原生渲染（weex 系，适合长列表/视频页性能敏感场景）。
- 条件编译是差异收敛手段：`#ifdef MP-WEIXIN / APP-PLUS / H5` 控制代码与样式分支，编译期剔除无关代码。
- 取舍：编译时方案产物更"原生"（模板在编译期生成，运行时包更小），但语法受限（Vue 模板子集）；运行时方案灵活但性能与包体有损耗。

```javascript
// uni-app：条件编译 + 运行时补丁示意
// pages/pay/index.vue（编译期按端拆分）
// <template>
//   <view class="pay">
//     <!-- #ifdef MP-WEIXIN -->
//     <button open-type="requestPayment" @tap="wxPay">微信支付</button>
//     <!-- #endif -->
//     <!-- #ifdef H5 -->
//     <button @tap="h5Pay">跳转收银台</button>
//     <!-- #endif -->
//   </view>
// </template>

export default {
  methods: {
    async wxPay() {
      // 编译进小程序端：uni.requestPayment 最终映射 wx.requestPayment（运行时 API 抹平层）
      await uni.requestPayment({
        provider: 'wxpay', timeStamp, nonceStr, package: prepayId, signType: 'RSA',
      });
    },
    h5Pay() { location.href = cashierUrl; },
  },
};
// 编译产物（MP-WEIXIN）：
//   wxml：模板编译产物，含通用渲染模板与事件绑定 eh
//   js：Vue 运行时 + uni-app 运行时，commit 时收集补丁 → setData
// 编译产物（H5）：标准 Vue SPA，uni.* 映射到浏览器/自研 H5 实现
// 编译产物（APP-PLUS vue）：WebView 渲染；nvue：原生控件渲染（weex 管线）
```
