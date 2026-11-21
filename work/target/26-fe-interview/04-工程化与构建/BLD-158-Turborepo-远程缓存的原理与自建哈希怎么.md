---
title: [BLD-158] Turborepo 远程缓存的原理与自建：哈希怎么算、签名怎么校验？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-158：Turborepo 远程缓存的原理与自建：哈希怎么算、签名怎么校验？
**答**：
- **哈希计算**：任务哈希 = hash(包内文件内容 + lockfile + turbo.json 中该任务配置 + 依赖闭包各包哈希 + 环境变量（`env` 声明）+ 全局依赖)；**输入变 → 哈希变 → 必 miss**，这保证了命中即等价（正确性根基）。
- **协议**：`GET /v8/artifacts/<hash>` 拉取、`PUT /v8/artifacts/<hash>` 上传，body 是 tar.gz（outputs 里声明的文件 + turbo-run? 元数据）；服务端只是"哈希寻址的对象存储"，自建门槛很低。
- **签名**：`signature: true` 时上传前用 TURBO_TOKEN（HMAC）对内容签名，拉取端校验，防止缓存被恶意替换（供应链安全项）；`teamId` 做租户隔离。
- 命中率的两大杀手：环境变量未声明（构建读到外部变量 → 同哈希不同产物）与 `globalDependencies` 遗漏（turbo.json 外的共享配置变更不进哈希）。

```json
// turbo.json：远程缓存的正确性配置（哪些输入必须进哈希）
{
  "$schema": "https://turbo.build/schema.json",
  "globalDependencies": [".env.example", "tsconfig.base.json"],
  "globalEnv": ["NODE_ENV", "CI"],
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"],
      "inputs": ["$TURBO_DEFAULT$", "!**/*.test.ts"],
      "env": ["APP_VERSION", "SENTRY_DSN"],   // 读到的环境变量必须声明，否则哈希不含它
      "passThroughEnv": ["AWS_REGION"]         // 影响构建但不进哈希（慎用，正确性风险）
    },
    "test": { "outputs": ["coverage/**"] }
  },
  "remoteCache": { "signature": true }         // 上传/下载校验签名，防缓存投毒篡改
}
```

```bash
# 自建远程缓存的最小服务（Node 版协议实现，哈希寻址对象存储 + 签名校验）
# server.js —— 部署在内网，TURBO_API 指向它即可
const express = require('express');
const crypto = require('crypto');
const app = express();
const TOKEN = process.env.TURBO_TOKEN;         // 与团队共享的签名密钥
const store = new Map();                       // 生产替换为 OSS/S3

const check = (req, res, next) => {
  const team = req.get('x-turbo-team');
  const sig = req.get('x-signature') ?? '';
  const expect = crypto.createHmac('sha256', TOKEN).update(req.path).digest('hex');
  if (team !== 'main' || (process.env.REQUIRE_SIG === '1' && sig !== expect)) {
    return res.status(401).end();              // 租户隔离 + 可选签名校验
  }
  next();
};
app.route('/v8/artifacts/:hash')
  .get(check, (req, res) => {
    const hit = store.get(req.params.hash);
    if (!hit) return res.status(404).end();    // 404 = miss，turborepo 自动真实构建
    res.set('content-type', 'application/octet-stream').send(hit);
  })
  .put(check, express.raw({ type: '*/*', limit: '2gb' }), (req, res) => {
    store.set(req.params.hash, req.body);      // 200 = accepted
    res.end();
  });
app.listen(3000);
# 使用：turbo build --api=http://cache.internal --token=$TURBO_TOKEN --team=main
```
