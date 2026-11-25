---
title: [BLD-287] 产物预览与验证环境（preview）怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-287：preview 怎么做的？
**答**：
- preview 的意义：dev 服务器≠产物（bundled/minify/分割差异）——preview 用真实产物验证（「dev 好使 prod 挂」的防线）。
- preview 服务：本地静态服务产物目录（带正确 MIME/SPA fallback/headers 与生产一致——模拟生产 CDN 行为）。
- PR 级 preview：每次 PR 构建产物部署到临时环境（preview URL 评论到 PR）——评审者验证真实产物而非 dev。
- 环境一致性：preview 的 headers（缓存/CSP）必须与生产一致——否则 preview 验证不了生产行为（SCN-BLD-246 CSP 问题在 preview 暴露）。
- 追问钩子：为什么 preview 的「headers 一致性」比静态服务本身更重要——产物在 prod 的行为受 headers 强影响（CSP 拦 eval/CORS/缓存策略）；headers 不一致的 preview 会给出假阳性验证（preview 过了 prod 挂）——preview 的价值公式 = 产物真实性 × 环境真实性。

```javascript
// preview 与生产一致
preview: { headers: PROD_HEADERS,                     // CSP/缓存与生产一致
  fallback: '/index.html',                            // SPA fallback
  cors: PROD_CORS },
// PR preview
ciComment(`Preview: https://pr-${prNum}.preview.example.com`);
```
