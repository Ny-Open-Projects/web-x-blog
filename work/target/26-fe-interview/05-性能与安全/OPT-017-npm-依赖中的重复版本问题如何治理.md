---
title: [OPT-017] npm 依赖中的重复版本问题如何治理？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-017：npm 依赖中的重复版本问题如何治理？

**答**：
- 典型症状：A 依赖 lodash@4.17.15、B 依赖 lodash@4.17.21，npm 平铺后可能装两份；更危险的是 vue/react 装两份导致 Hook 报错、context 断裂。
- 治理手段：pnpm 的硬链接 + 严格 node_modules 天然防幽灵依赖；npm/yarn 用 `dedupe`；lockfile 提交并审查。
- 强约束兜底：Vite/webpack 的 `resolve.alias` 把关键库统一指到单一版本；`peerDependencies` 声明"宿主提供"的库避免被打进产物。
- 用 `npm ls <pkg>` / `pnpm why <pkg>` 找出引入路径，从源头收敛。

```typescript
// 一一对应：Vite alias 强制单一版本 + 手动查重
import { defineConfig } from 'vite';
import { fileURLToPath } from 'node:url';

export default defineConfig({
  resolve: {
    alias: {
      // 项目里无论哪个包 import 'vue'，都解析到同一份，防止双实例
      vue: fileURLToPath(new URL('./node_modules/vue/dist/vue.runtime.esm-bundler.js', import.meta.url)),
    },
  },
});

// 排查命令（终端执行）：
// npm ls react          查看 react 是否存在多个版本及引入链
// pnpm why lodash       查看 lodash 被谁依赖
// npm dedupe            自动去重可合并的版本
```
