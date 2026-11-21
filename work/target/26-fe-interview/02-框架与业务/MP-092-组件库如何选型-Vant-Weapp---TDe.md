---
title: [MP-092] 组件库如何选型（Vant Weapp / TDesign 等）？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-092：组件库如何选型（Vant Weapp / TDesign 等）？
**答**：
- 考量维度：**多端支持**（Vant Weapp 原生微信、Vant + Taro/uni 适配层、TDesign 多端官方支持）、维护活跃度、按需引入与包体积、主题定制能力（CSS 变量/暗黑模式）。
- 原生小程序：Vant Weapp 或 TDesign Weapp；Taro 项目用 taro-ui / nutui-react；uni-app 用 uview / uni-ui。
- 注意构建 npm 步骤与样式隔离配置（组件库普遍要求 addGlobalClass/shared）。

```json
{
  "usingComponents": {
    "van-button": "@vant/weapp/button/index",
    "van-field": "@vant/weapp/field/index"
  },
  "样式隔离": "组件库要求页面开启 apply-shared 才能被主题样式影响"
}
```
