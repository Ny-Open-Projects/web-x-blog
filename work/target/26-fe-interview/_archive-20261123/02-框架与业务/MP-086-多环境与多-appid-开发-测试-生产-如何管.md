---
title: [MP-086] 多环境与多 appid（开发/测试/生产）如何管理？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-086：多环境与多 appid（开发/测试/生产）如何管理？
**答**：
- 环境：dev/staging/prod 三套 baseUrl + 云环境 envId，编译时注入（Taro defineConstants / uni-app .env 文件）。
- 多 appid：测试号与生产号分开，project.config.json 的 appid 按环境脚本替换，CI 上传到对应 appid。
- 原则：环境判断只发生在构建期与请求层，业务代码无感知。

```javascript
// config/env.js —— 构建期注入，业务代码只 import
const ENV = process.env.APP_ENV || 'dev'
const envMap = {
  dev:     { baseUrl: 'https://dev-api.example.com',  appId: 'wxDev123' },
  staging: { baseUrl: 'https://stg-api.example.com',  appId: 'wxStg456' },
  prod:    { baseUrl: 'https://api.example.com',      appId: 'wxProd789' }
}
module.exports = envMap[ENV]
```
