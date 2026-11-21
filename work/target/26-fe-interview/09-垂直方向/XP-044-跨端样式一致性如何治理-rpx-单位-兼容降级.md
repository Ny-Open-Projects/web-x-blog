---
title: [XP-044] 跨端样式一致性如何治理（rpx/单位/兼容降级）？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-044：跨端样式一致性如何治理（rpx/单位/兼容降级）？
**答**：
- 单位策略：**设计稿对齐**——Taro/uni-app 的 px→rpx/upx 转换（designWidth 配置），H5 端转 vw 或运行时换算；RN 用 PixelRatio 注入 dp 概念。
- 三大差异源：**盒模型与默认样式**（小程序各端 reset 不一）、**安全区/刘海**、**字体渲染与行高**。治理靠：统一 reset 样式包 + PostCSS 编译期转换 + 安全区变量注入。
- 兼容降级：低版本 WebView/基础库不支持的新特性（如 flex gap）用 PostCSS 插件自动降级或运行时探测。
- 视觉走查自动化兜底：CI 多端截图对比（见 XP-072），把"样式漂移"变成可度量指标。
- 原则：**样式分支只允许出现在样式文件内（条件编译/平台后缀），禁止业务 JSX 里写平台 if**。

```javascript
// 样式一致性工程化：PostCSS 管线（Taro/uni-app 同构思路）
// postcss.config.js
module.exports = {
  plugins: [
    require('postcss-pxtransform')({            // 设计稿 750 宽：px → rpx(小程序)/rem(vw)(H5)
      platform: process.env.TARO_ENV,
      designWidth: 750,
      deviceRatio: { 750: 1 },
    }),
    require('postcss-preset-env')({ browsers: ['iOS >= 10', 'Android >= 8'] }), // 语法降级
    require('./plugins/safe-area-variable')(),  // 兜底：bottom: calc(20rpx + env(safe-area-inset-bottom))
    require('autoprefixer'),
  ],
};
// 平台差异样式收敛（只允许出现在样式层）：
//   index.scss 中：
//   .badge { color: #fff; }
//   /* #ifdef MP-ALIPAY */
//   .badge { line-height: 1.2; }   // 支付宝渲染差异
//   /* #endif */
// 文件后缀法：index.rn.scss / index.weapp.scss 由构建器按端选择
// 统一 reset：packages/style/reset.scss 引入各端_normalize 差异（button::after 清除等）
```
