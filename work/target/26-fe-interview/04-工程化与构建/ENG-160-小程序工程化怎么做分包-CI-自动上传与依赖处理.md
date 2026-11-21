---
title: [ENG-160] 小程序工程化怎么做？分包 CI 自动上传与依赖处理？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-160：小程序工程化怎么做？分包 CI 自动上传与依赖处理？
**答**：
- 分包治理：主包只留启动页与 tabBar 页面，业务按域拆分包，preloadRule 控制预下载提升秒开。
- CI 自动上传：miniprogram-ci 用私钥在流水线里 upload，版本号与 changelog 自动生成，告别 IDE 手点。
- 依赖处理：构建期 packNpm 处理 npm 依赖（或 Taro/uni-app 编译期打包），并卡主包体积阈值。
- 质量卡口：上传前跑体验评分与包体积检查，主包超 1.5M 阻断并提示分包。

```javascript
// scripts/mp-upload.mjs —— miniprogram-ci 自动上传
const ci = require('miniprogram-ci')

async function main() {
  const project = new ci.Project({
    appid: process.env.MP_APPID,
    type: 'miniProgram',
    projectPath: './dist',
    privateKeyPath: './private.wx.key',   // 从 CI secret 落盘 权限仅 upload
    ignores: ['node_modules/**/*'],
  })
  const version = require('../package.json').version
  const result = await ci.upload({
    project,
    version,                                        // 与仓库版本号对齐
    desc: `release ${version} ${process.env.GIT_SHA ?? ''}`,
    setting: { es6: true, minify: true, autoPrefixWXSS: true },
  })
  console.log('上传成功', result.subPackageInfo)
}
main().catch(e => { console.error(e); process.exit(1) })
```
