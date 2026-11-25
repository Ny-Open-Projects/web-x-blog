---
title: [MFW-065] standalone 输出和自定义 Server 分别适合什么场景？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-065：standalone 输出和自定义 Server 分别适合什么场景？
**答**：
- `output: 'standalone'`：构建时把运行所需文件（含 trace 分析出的最小 node_modules）打包到 `.next/standalone`，镜像从 1GB+ 缩到百 MB 级，是容器化部署的标准姿势。
- 自定义 Server（`server.js` 里包一层 express/hapi）：适合必须接管 HTTP 层的场景——统一接入公司网关 SDK、WebSocket、老服务共存。代价：**放弃 Next 的原生托管优化**，且很多新特性（PPR、部分缓存行为）在自定义 server 上不受官方保证。
- 优先级建议：能用中间件/route handler 解决的不要自定义 server；能 standalone 的不要手工 COPY 整个 node_modules。
- 两者可结合：standalone 输出 + 容器内 `node server.js` 启动。

```js
// next.config.js
module.exports = {
  output: 'standalone', // 产物：.next/standalone/server.js
};
```

```dockerfile
# Dockerfile（配合 standalone）
FROM node:20-alpine AS builder
WORKDIR /app
COPY . .
RUN npm ci && npm run build

FROM node:20-alpine
WORKDIR /app
# 只拷贝 trace 出的最小集合，不再 COPY 整个 node_modules
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static
COPY --from=builder /app/public ./public
ENV NODE_ENV=production PORT=3000
CMD ["node", "server.js"]
```
