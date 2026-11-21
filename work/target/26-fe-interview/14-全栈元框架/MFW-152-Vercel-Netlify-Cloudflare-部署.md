---
title: [MFW-152] Vercel、Netlify、Cloudflare Pages 部署元框架的差异？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-152：Vercel、Netlify、Cloudflare Pages 部署元框架的差异？
**答**：
- Vercel：Next 官方平台，特性零延迟跟进（PPR/Cache 组件/ISR 全原生）；函数按 Serverless 区域部署，Edge Middleware 支持；锁定感最强、费用随流量增长。
- Netlify：多框架适配（Next via OpenNext 桥接层、Astro/RRv7 一等支持）；Edge Functions 能力中等；特色是 Deploy Preview 与表单/身份等平台服务。
- Cloudflare Pages/Workers：全球边缘网络 + Workers KV/D1/R2 存储全家桶；运行时是 workerd（类 Edge），Next 支持走 OpenNext Cloudflare adapter；国内可达性需自行评估。
- 共同抽象：三者都收敛到「SSR 函数 + 静态资源 + 边缘中间件」三件套，元框架经 Nitro/OpenNext adapter 适配——**框架层适配器是自托管之外的主流解**。
- 选型口径：Next 重度 → Vercel；预算敏感 + 全球边缘 → Cloudflare；多框架杂烩 + 预览流程 → Netlify；国内业务 → 自建 K8s。

```yaml
# 同一 Astro 项目三平台的配置面

# Cloudflare Pages：wrangler.toml
# name = "site"
# compatibility_flags = ["nodejs_compat"]
# pages_build_output_dir = "dist"

# Netlify：netlify.toml
# [build]
#   command = "npm run build"
#   publish = "dist"
# [[edge_functions]]  # 边缘函数目录约定

# Vercel：vercel.json
# { "framework": "astro" }  # 零配置

# 自托管 K8s（对照）：
# npm run build && node dist/server/entry.mjs   # adapter-node 产物 + Deployment
```
