---
title: [OPS-162] 小程序 CI（miniprogram-ci）怎么接入发布流水线？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-162：小程序 CI（miniprogram-ci）怎么接入发布流水线？
**答**：
- miniprogram-ci 用私钥鉴权在 CI 侧完成上传/预览，替代人工"开发者工具点上传"；私钥走 CI secret 不入库。
- 版本号取 package.json + CI build 号，desc 带 git 最新提交信息，审核与回溯都有据可查。
- codeProtect 开启代码保护（混淆），提高反编译成本。
- 体验版二维码自动生成并推送 QA 群，替代人肉截图转发。
- 提审后轮询审核状态，审核通过自动发布——把"审核等待"纳入流水线而非靠人盯。

```javascript
// scripts/upload-mp.js：小程序 CI 自动上传与预览，接入发布流水线
const ci = require('miniprogram-ci');
const { execSync } = require('child_process');

(async () => {
  const project = new ci.Project({
    appid: process.env.MP_APPID,
    type: 'miniProgram',
    projectPath: './dist',
    privateKeyPath: process.env.MP_PRIVATE_KEY_PATH,   // 密钥走 CI secret，绝不入库
    ignores: ['node_modules/**/*'],
  });

  const version = require('../package.json').version;
  const buildNo = process.env.CI_BUILD_NUMBER;
  const msg = execSync('git log -1 --pretty=%s').toString().trim();

  // 1. 上传：codeProtect 混淆防反编译
  await ci.upload({
    project,
    version,
    desc: `build ${buildNo} ${msg}`,
    setting: { es6: true, minify: true, codeProtect: true },
    onProgressUpdate: console.log,
  });

  // 2. 体验版预览二维码推给 QA（发到群机器人）
  const qrcode = await ci.preview({ project, qrcodeFormat: 'base64' });
  await postToGroup(`版本 ${version}#${buildNo} 体验码已生成，提审信息：${msg}`);

  // 3. 提审后轮询审核状态，通过即调用发布 API（把审核等待纳入流水线，OPS-160）
})();
```
