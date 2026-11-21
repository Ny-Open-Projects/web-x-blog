---
title: [BLD-139] 构建期环境变量在 vite 中的注入与安全：import.meta.env 的泄露面有多大？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-139：构建期环境变量在 vite 中的注入与安全：import.meta.env 的泄露面有多大？
**答**：
- 注入规则：只有 `VITE_` 前缀的变量会进客户端产物（`import.meta.env.VITE_X`），加载顺序 `process.env < .env < .env.local < .env.[mode] < .env.[mode].local`；`envDir` 可改 .env 目录。
- **泄露面**：所有 VITE_ 变量会被**静态替换进每个引用点**（define 机制），因此"前端产物中的环境变量 = 公开信息"——密钥放 VITE_ 前缀是事故级错误；`import.meta.env` 整体解构、动态 key（`env[name]`）拿不到值（编译期替换只认字面量）。
- 服务端变量：`vite loadEnv(mode, root, '')` 第三参空前缀可取全部，但只许在 SSR/配置文件用；`import.meta.env.SSR` 布尔由构建器注入做分支裁剪。
- 治理：约定命名空间（VITE_PUBLIC_）、CI 里 secret 扫描卡口（gitleaks 检查 dist 中 key 模式）、敏感值走运行时注入（HTML 里服务端写 `window.__CFG__`）。

```bash
# .env.production：前端可见 vs 服务端专属的边界示例
VITE_API_BASE=https://api.example.com      # 会进客户端产物（公开）
VITE_SENTRY_DSN=https://k@o.example.com/1  # DSN 本就公开，可以放
# DB_PASSWORD=xxx                          # 千万不要 VITE_ 前缀；且不要写在 .env 里给前端目录
```

```javascript
// vite.config.ts：loadEnv 的正确用法与运行时注入兜底
import { defineConfig, loadEnv } from 'vite';
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '');       // 空前缀：全部变量（仅配置/SSR 用）
  const publicEnv = Object.fromEntries(
    Object.entries(env).filter(([k]) => k.startsWith('VITE_'))
  );
  return {
    define: {
      // 自定义前缀注入（等价 envPrefix 扩展写法）
      ...Object.fromEntries(
        Object.entries(publicEnv).map(([k, v]) => [`import.meta.env.${k}`, JSON.stringify(v)])
      ),
    },
    // 客户端把"运行时配置"与"编译期配置"分离：
    // 编译期：VITE_API_BASE（构建时定死）
    // 运行时：服务端模板注入 window.__RUNTIME_CONFIG__（发布后可不重建改配置）
  };
});

// src/config.ts：安全使用模式
const env = import.meta.env;
export const API_BASE = window.__RUNTIME_CONFIG__?.apiBase ?? env.VITE_API_BASE;
// 反模式（构建期替换不生效，值为 undefined）：
// const key = 'VITE_API_BASE'; import.meta.env[key]      ← 动态 key 拿不到
// const { VITE_API_BASE } = import.meta.env              ← 解构某些版本可拿到，但依赖实现，别用
```
