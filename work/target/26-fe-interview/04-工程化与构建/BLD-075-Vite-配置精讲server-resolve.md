---
title: [BLD-075] Vite 配置精讲：server、resolve、build.rollupOptions、define、envPrefix 各管什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-075：Vite 配置精讲：server、resolve、build.rollupOptions、define、envPrefix 各管什么？
**答**：
- server：host/port/proxy（复用 http-proxy 语义）、fs.strict 防 monorepo 越权访问、hmr 配置；server 配置只影响 dev，别忘了 build 侧等价物。
- resolve：alias、dedupe、extensions（Vite 默认比 webpack 少，路径要写全）；preserveSymlinks 控制 pnpm 行为。
- build.rollupOptions：prod 是 Rollup 底座，分包（manualChunks）、external、输出格式都从这里配；build.target 决定 esbuild 转译目标。
- define：编译期全局常量替换（注意跨版本 JSON.stringify 转义）；envPrefix：约定哪些前缀的环境变量暴露到客户端（默认 VITE_，防泄漏服务端密钥的关键闸门）。

```javascript
// vite.config.js：生产级配置总览
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig(({ mode }) => ({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: { '/api': { target: 'http://localhost:7001', changeOrigin: true, rewrite: (p) => p.replace(/^\/api/, '') } },
    fs: { strict: true },
  },
  resolve: {
    alias: { '@': '/src', // 或用 fileURLToPath(new URL('./src', import.meta.url))
      '@app/ui': '/packages/ui/src' },
    dedupe: ['react', 'react-dom'],
  },
  define: {
    __APP_VERSION__: JSON.stringify(process.env.npm_package_version),
    'process.env.NODE_ENV': JSON.stringify(mode), // 兼容部分三方库读 process.env
  },
  envPrefix: ['VITE_', 'PUBLIC_'], // 暴露给客户端的白名单前缀
  build: {
    target: 'es2020',
    outDir: 'dist',
    sourcemap: true,
    rollupOptions: {
      external: [],               // CDN 外部化时配置
      output: {
        manualChunks: (id) => {
          if (id.includes('node_modules/react')) return 'vendor-react';
          if (id.includes('node_modules')) return 'vendors';
        },
      },
    },
  },
}));
```
