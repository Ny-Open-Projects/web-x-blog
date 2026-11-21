---
title: [V3-155] 多入口多页面（MPA）架构在 Vite 下怎么配置？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-155：多入口多页面（MPA）架构在 Vite 下怎么配置？
**答**：
- 适用场景：官网 + 控制台 + 活动页这类"页面间无需共享 SPA 状态"的项目，MPA 能让每个入口独立构建、按需加载、互不影响。
- 核心配置：`build.rollupOptions.input` 指定多个 html 入口；开发时访问对应路径即可。
- 目录约定：每个入口一个目录，各自 main.ts + router（createWebHistory 不同 basename）。
- 共享代码放 src/shared，通过别名引入；公共依赖注意版本一致，避免 vendor 重复体积。

```typescript
// vite.config.ts —— 多入口 MPA 完整配置
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import { resolve } from "path";
import { readdirSync, statSync, existsSync } from "fs";

// 自动收集 src/pages/*/index.html 作为入口，新增页面零配置
function getMpaInputs() {
  const pagesDir = resolve(__dirname, "src/pages");
  const inputs: Record<string, string> = {};
  for (const name of readdirSync(pagesDir)) {
    const html = resolve(pagesDir, name, "index.html");
    if (statSync(resolve(pagesDir, name)).isDirectory() && existsSync(html)) {
      inputs[name] = html; // key 即产物目录名：dist/home/index.html
    }
  }
  return inputs;
}

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: { "@": resolve(__dirname, "src") },
  },
  build: {
    rollupOptions: {
      input: {
        home: resolve(__dirname, "src/pages/home/index.html"),
        admin: resolve(__dirname, "src/pages/admin/index.html"),
        activity: resolve(__dirname, "src/pages/activity/index.html"),
      },
    },
  },
});

// 目录结构：
// src/pages/home/main.ts      -> createApp(App).use(createWebHistory 入口 router "home")
// src/pages/admin/main.ts     -> 独立 router，basename 为 /admin
// src/pages/activity/main.ts  -> 活动页可极简，不需要 router
// src/shared/                 -> 公共组件、utils、api，各入口按需引用
```
