---
title: [MP-211] Taro 下样式方案的跨端适配（Tailwind/单位/暗黑模式）？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-211：Taro 样式跨端适配？
**答**：
- 单位：源码写 px，编译期按设计稿基准（750）转 rpx（小程序）/rem 或 vw（H5/RN）——postcss 插件统一处理。
- Tailwind：Taro 官方支持 weapp-tailwindcss 插件——处理小程序对类名的限制（转义特殊字符）与 rpx 转换。
- 全局样式差异：app.wxss vs H5 global css；条件编译按端写差异样式。
- 暗黑模式：小程序 darkmode 主题变量 + CSS 变量双通道。
- 陷阱：小程序不支持部分选择器（通配符/属性选择器受限）、伪元素支持有限——写样式前查端支持表。
