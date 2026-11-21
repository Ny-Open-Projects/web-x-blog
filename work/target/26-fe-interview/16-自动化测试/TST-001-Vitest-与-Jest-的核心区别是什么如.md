---
title: [TST-001] Vitest 与 Jest 的核心区别是什么？为什么新项目倾向选 Vitest？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-001：Vitest 与 Jest 的核心区别是什么？为什么新项目倾向选 Vitest？
**答**：
- 底座不同：Jest 自带一套转换链（babel-jest / ts-jest）与模块系统（CJS 为主），Vitest 直接复用 Vite 的 esbuild 转换与 ESM 原生加载，TS/JSX/路径别名零配置可用。
- 速度与缓存：Vitest 转换层吃 Vite 的依赖预构建和文件级缓存，watch 模式只重转换改动模块，冷启动和单测耗时显著低于 Jest。
- API 兼容：describe/it/expect/vi.* 与 Jest 高度兼容，`globals: true` 后甚至不用 import，迁移成本低（个别 Jest-only API 需替换）。
- 生态差异：Jest 社区更老、插件多；Vitest 与 Vite 生态（插件、配置）打通，配合 Testing Library/MSW 都有官方文档。
- 结论（追问钩子）：Vite 项目默认 Vitest，webpack 老项目且团队重度依赖 Jest 生态时可继续 Jest。

```javascript
// vitest.config.ts —— 复用 Vite 配置，Jest 需要单独维护一整套 transform/moduleNameMapper
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],                 // 与 vite.config.ts 共用插件
  resolve: { alias: { '@': '/src' } },// Jest 里要写 moduleNameMapper 正则
  test: {
    globals: true,                    // 全局 describe/it/expect，免 import
    environment: 'jsdom',             // 组件测试环境
    include: ['src/**/*.test.{ts,tsx}'],
  },
});
// Jest 等价物要配：transform(ts-jest)、moduleNameMapper、testEnvironment、setupFilesAfterEach…
```
