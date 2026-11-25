---
title: [MP-339] 小程序 CI/CD：miniprogram-ci 与发布流水线
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## MP-339：小程序 CI/CD：miniprogram-ci 与发布流水线

**答**：
- miniprogram-ci 能力：upload（代码上传+版本备注）、preview（预览码生成——推送到群/钉钉）、packNpm（构建 npm）、analyze（体积分析）——CI 全自动化
- 流水线设计：lint/单测 → 构建（packNpm + 压缩）→ 体积门禁（超限阻断）→ preview（体验版自动推送测试群）→ 人工验收 → upload 正式 + 提审
- 密钥管理：upload 需要小程序 CI 密钥（后台下载）——IP 白名单 + 密钥保密（CI 变量注入）
- 体验版分发自动化：preview 生成二维码 → 推送企业微信群机器人——「提测通知」的自动化闭环
- 深水点：多环境构建（测试/预发/生产 baseUrl）——构建时注入环境变量（-env 参数）+ 体验版用测试环境、正式版生产——环境错配是重大事故源

```javascript
// ci.js (Node 流水线)
const ci = require('miniprogram-ci');
const project = new ci.Project({
  appid, type: 'miniProgram',
  projectPath: './dist', privateKeyPath: './private.key',
  ignores: ['node_modules/**/*'],
});
await ci.packNpm(project);
await ci.preview({ project, desc: `feature-x ${process.env.GIT_SHA}`, setting: { es6: true }, qrcodeFormat: 'image', qrcodeOutputDest: './preview.jpg' });
// → 机器人推送 preview.jpg 到群
```
