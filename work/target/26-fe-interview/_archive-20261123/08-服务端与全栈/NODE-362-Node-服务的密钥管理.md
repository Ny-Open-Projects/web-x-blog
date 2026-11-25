---
title: [NODE-362] Node 服务的密钥与环境变量管理如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-362：Node 服务的密钥与环境变量管理
**答**:
- 密钥来源分层：本地开发 .env（gitignore，提供 .env.example 模板）、CI/CD 注入（secret manager 注入构建环境，产物不含密钥）、运行时 K8s Secret/Vault/云 KMS 动态注入（支持轮换）。
- 规范：密钥不进代码与日志（lint/扫描防泄漏——gitleaks 扫历史）、不同环境不同密钥（prod 泄漏不影响 test）、密钥有轮换机制（JWT 签名密钥 kid 双密钥过渡期）。
- 使用收口：config 模块集中读取 + 启动校验（必需密钥缺失 fail fast，NODE-413 思想），业务代码只碰 config 不碰 process.env。
- 加密存储的密钥（DB 字段加密）：KMS 信封加密（数据密钥加密数据，KMS 加密数据密钥）；本地缓存解密密钥注意内存安全。
- 泄漏应急：轮换流程（旧密钥进入过渡期 → 全量换发 → 废旧）；泄漏密钥立即失效而非等待轮换周期。
```javascript
// config 集中与校验
const envSchema = z.object({
  DB_URL: z.string().url(), JWT_SECRET: z.string().min(32), REDIS_URL: z.string().url()
});
export const config = envSchema.parse(process.env);              // 缺密钥启动即失败
// 轮换：JWT 验签支持 [kid: new, kid: old]，签发用 new，旧 kid 过渡期后移除
```
