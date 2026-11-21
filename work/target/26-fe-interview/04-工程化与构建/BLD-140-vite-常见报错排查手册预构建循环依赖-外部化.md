---
title: [BLD-140] vite 常见报错排查手册：预构建循环依赖、外部化失效、双实例 Vue。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-140：vite 常见报错排查手册：预构建循环依赖、外部化失效、双实例 Vue。
**答**：
- **"optimized dependencies changed. reloading"**：运行中新增裸依赖触发预构建重建。排查：`--debug optimizeDeps` 看触发源；根治是把它写进 `optimizeDeps.include` 或让扫描器可达（静态 import）；CI 预热 `vite optimize`。
- **外部化失效（dev 正常 build 报 "Could not resolve" 或包内引用泄露）**：monorepo 里 workspace 包指向源码但 build 忘加 alias；或 rollupOptions.external 写了包名但子路径（`pkg/sub`）没匹配——external 要用函数或正则匹配前缀。
- **双实例 Vue/React**：症状 `Invalid hook call`、`provide/inject 失效`、组件 instanceof 校验失败。根因三连：lockfile 里同名多版本（pnpm why vue）、workspace 包 peerDependencies 没声明导致子包自装、预构建把 vue 打进两个 chunk。修复：peerDeps + pnpm overrides 锁单版本 + 必要时 `dedupe`。
- 快速定位命令：`pnpm why vue`、`find node_modules -name vue -maxdepth 4`、`ls node_modules/.vite/deps | grep vue`。

```bash
# 双实例 Vue 的完整排查流程（面试可背的操作序列）
pnpm why vue                       # 1. 看依赖树里 vue 出现几次、被谁引入
ls node_modules/.vite/deps | grep -i vue   # 2. 预构建产物是否出现 vue_v2/vue_v3 双份
grep -rn '"vue"' pnpm-lock.yaml | head     # 3. lockfile 层面确认版本分裂
# 修复一：workspace 包一律 peerDependencies（pnpm-workspace.yaml 支持 catalog 统一版本）
#   packages/ui/package.json: "peerDependencies": { "vue": ">=3.4" }
# 修复二：根 package.json overrides 强制收敛
#   "pnpm": { "overrides": { "vue": "3.4.21", "react": "18.3.1" } }
# 修复三：vite 配置兜底（让两个包名解析到同一物理路径）
```

```javascript
// vite.config.ts：双实例与外部化的代码级修复
import { fileURLToPath } from 'node:url';
export default defineConfig({
  resolve: {
    alias: {
      // 强制所有入口（含链接的 workspace 包）都指向同一份 vue
      vue: fileURLToPath(require.resolve('vue')),
      // 外部化失效修复：子路径也要覆盖
      // build 侧等价：rollupOptions.external = [/^vue($|\/)/, /^@vue\//]
    },
    dedupe: ['vue', '@vue/reactivity'],   // vite 内置 dedupe：resolve 时收敛到同一实例
  },
  build: {
    rollupOptions: {
      external: [/^vue($|\/)/, /^@vue\//], // 用正则覆盖 vue、vue/macros 等子路径（SSR 场景）
    },
  },
});
```

## 十五章 Rollup 深入与库构建（BLD-141 ~ BLD-148）
