---
title: [ENG-156] Module Federation 怎么工程化？共享配置 版本协商 独立部署怎么做？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-156：Module Federation 怎么工程化？共享配置 版本协商 独立部署怎么做？
**答**：
- MF 核心是运行时 import 远端模块：remotes 声明远端清单、exposes 暴露本端模块、shared 声明共享依赖协商规则。
- 版本协商：shared 配 singleton + requiredVersion，运行时取双方可用版本；strictVersion 让冲突显式告警。
- remoteEntry 地址必须版本化（带版本目录或 hash），防止长缓存钉死旧版本；远端不可达要有 fallback 组件。
- 独立部署：远端清单（remotes 地址表）由配置中心下发而非写死在构建里，实现不重发主应用切换远端版本。

```javascript
// host/vite.config.ts —— Module Federation 主端配置
import { defineConfig } from 'vite'
import federation from '@originjs/vite-plugin-federation'

export default defineConfig({
  plugins: [
    federation({
      name: 'host',
      remotes: {
        cart: 'https://cdn.corp.com/cart@2.1.0/assets/remoteEntry.js', // 版本化地址 防长缓存钉死
      },
      shared: {
        react: { singleton: true, requiredVersion: '^18.2.0', strictVersion: true },
        'react-dom': { singleton: true, requiredVersion: '^18.2.0' },
      },
    }),
  ],
  build: { target: 'esnext' },
})

// 消费侧 + 容错
// const Cart = React.lazy(() => import('cart/CartPage').catch(() => import('./CartFallback')))
```
