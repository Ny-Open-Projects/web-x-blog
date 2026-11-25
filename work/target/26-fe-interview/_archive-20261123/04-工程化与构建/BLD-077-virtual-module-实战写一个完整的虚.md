---
title: [BLD-077] virtual module 实战：写一个完整的虚拟模块插件。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-077：virtual module 实战：写一个完整的虚拟模块插件。
**答**：
- 虚拟模块 = 构建期动态生成的代码，路径用 `\0`（或 `virtual:`）约定前缀，resolveId 识别、load 返回内容、transform 可再加工。
- 典型场景：路由自动注册、i18n 词条聚合、构建信息注入、把配置文件编译成 TS 模块。
- 关键点：resolveId 返回带 `\0` 前缀 id（Vite 中防止被其他插件误处理、fs 无该文件）；load 按 id 分发；内容变更时通过 server.moduleGraph 触发 HMR。

```javascript
// vite-plugin-routes.js：路由自动注册虚拟模块（完整可运行）
import fs from 'node:fs';
import path from 'node:path';

const VIRTUAL_ID = 'virtual:app-routes';
const RESOLVED = '\0' + VIRTUAL_ID;

export default function vitePluginRoutes({ pagesDir = 'src/pages' } = {}) {
  let server;

  const genRoutes = (root) => {
    const files = fs.readdirSync(path.join(root, pagesDir), { recursive: true })
      .filter((f) => f.endsWith('.vue') || f.endsWith('.tsx'));
    return files.map((f) => {
      const routePath = '/' + f.replace(/\.(vue|tsx)$/, '').replace(/\\/g, '/').replace(/\/?index$/, '');
      const comp = '/' + path.posix.join(pagesDir, f.replaceAll('\\', '/'));
      return `{ path: '${routePath}', component: () => import('${comp}') }`;
    }).join(',\n  ');
  };

  return {
    name: 'vite-plugin-routes',
    resolveId(source) {
      return source === VIRTUAL_ID ? RESOLVED : null; // 识别虚拟模块
    },
    load(id) {
      if (id !== RESOLVED) return null;
      const root = process.cwd();
      // 标记虚拟模块依赖 pages 目录 触发 HMR 监听
      this.addWatchFile(path.join(root, pagesDir));
      return `export const routes = [\n  ${genRoutes(root)}\n];`;
    },
    configureServer(s) { server = s; },
    handleHotUpdate({ file, server: s }) {
      if (file.includes(pagesDir)) {
        const mod = s.moduleGraph.getModuleById(RESOLVED);
        if (mod) return [mod]; // 页面文件增删 虚拟模块热更新
      }
      return null;
    },
  };
}

// src/router.ts 消费侧（text 代码块）：
// import { routes } from 'virtual:app-routes';
// export const router = createRouter({ history: createWebHistory(), routes });
```
