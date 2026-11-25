---
title: [RBL-456] 笔试：手写构建配置加密注入
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-456：手写构建配置加密注入
**答**：实现 `createSecretInjector(kms)`：1) 构建期注入 secret 的安全通道：不进产物（运行时从 KMS/配置服务拉取）——构建只注入「密文的加载地址」；2) 如必须构建期注入（SSR server bundle）：加密进产物 + 运行时用部署侧密钥解密（信封加密）；3) 注入审计：哪个 secret 注入到哪个产物（审计清单）；4) 轮换支持：secret 版本号注入（运行时校验版本）；5) 防泄露扫描：注入后产物扫描确认无明文 secret（构建门禁）。

```javascript
import crypto from 'node:crypto'

export function createSecretInjector(kms) {
  const audit = []

  async function injectForServerBundle(secrets, envelopeKey) {
    // 信封加密：数据密钥加密 secrets → 部署侧 envelopeKey 解密
    const dataKey = crypto.randomBytes(32)
    const iv = crypto.randomBytes(12)
    const cipher = crypto.createCipheriv('aes-256-gcm', dataKey, iv)
    const plaintext = JSON.stringify(secrets)
    const encrypted = Buffer.concat([cipher.update(plaintext), cipher.final()])
    const tag = cipher.getAuthTag()
    const wrappedKey = kms.wrap(dataKey, envelopeKey)             // 数据密钥被部署密钥包裹

    audit.push({ secrets: Object.keys(secrets), target: 'server-bundle', at: Date.now() })
    const injected = {
      __ENVELOPE__: { wrapped: wrappedKey.toString('base64'), iv: iv.toString('base64'),
        tag: tag.toString('base64'), data: encrypted.toString('base64'),
        version: secrets.__version ?? 1 },
    }
    // 运行时解密辅助（产物内）
    injected.__decrypt = `(function(env){const d=Buffer.from(env.data,'base64'),k=kmsUnwrap(Buffer.from(env.wrapped,'base64'));const c=crypto.createDecipheriv('aes-256-gcm',k,Buffer.from(env.iv,'base64'));c.setAuthTag(Buffer.from(env.tag,'base64'));return JSON.parse(Buffer.concat([c.update(d),c.final()]).toString())})`
    return injected
  }

  function scanForLeaks(bundleContent, secrets) {
    const leaks = Object.entries(secrets)
      .filter(([k, v]) => k !== '__version' && bundleContent.includes(v))
      .map(([k]) => k)
    if (leaks.length) throw new Error(`secret 明文泄露进产物: ${leaks.join(',')}`)   // 构建门禁
    return { clean: leaks.length === 0 }
  }

  return { injectForServerBundle, scanForLeaks, audit: () => audit }
}
```
**评分点**：
- 双路径决策（前端不注入 / SSR 信封加密注入——信封加密双密钥结构）
- 注入审计（哪些 secret 到哪个产物——审计清单）
- 版本注入（运行时校验版本支持轮换）
- 泄露扫描门禁（注入后确认无明文——自查机制）
