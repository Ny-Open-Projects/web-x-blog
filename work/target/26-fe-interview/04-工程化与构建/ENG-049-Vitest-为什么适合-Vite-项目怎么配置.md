---
title: [ENG-049] Vitest 为什么适合 Vite 项目？怎么配置？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-049：Vitest 为什么适合 Vite 项目？怎么配置？
**答**：
- 与 Vite 共享同一套配置与转换管线：插件、alias、环境变量直接复用，无需维护两套配置。
- 原生 ESM、按需转换、开箱支持 TS/JSX，速度远快于 Jest。
- API 与 Jest 高度兼容：describe/it/expect/vi 迁移成本低。
- 配置 environment: jsdom 支持组件测试，setupFiles 引入全局测试初始化。

```javascript
// vitest.config.ts
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: ['./vitest.setup.ts'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'html'],
    },
  },
});
```
