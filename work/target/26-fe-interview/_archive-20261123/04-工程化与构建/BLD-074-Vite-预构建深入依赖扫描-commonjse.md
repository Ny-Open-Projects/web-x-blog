---
title: [BLD-074] Vite 预构建深入：依赖扫描、commonjs→esm、.vite 缓存与 --force 何时需要？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-074：Vite 预构建深入：依赖扫描、commonjs→esm、.vite 缓存与 --force 何时需要？
**答**：
- 依赖扫描：启动时用 esbuild 从入口沿 import 静态扫描（支持 glob），找出"裸模块导入"（bare import，来自 node_modules）作为预构建对象；动态拼接的 import 扫不到，要手动 include。
- CJS 处理：把 CJS 包（如 lodash、react 的 umd）转换成 ESM 并打平多入口（lodash 每个子模块一次请求 -> 一个文件）；同时做 interoperability（default 兼容）。
- 缓存：结果按 lockfile、vite 配置、NODE_ENV、浏览器 UA 等生成 hash 键存 node_modules/.vite/deps；命中则跳过预构建。
- --force 时机：lockfile 变更后感知异常、补丁包（patch-package）更新、手动改了 node_modules 内容、预构建产物疑似坏（esbuild 错误但依赖没变）——这些都需强制重跑。

```bash
# bash 代码块：预构建排查命令
# 查看 hash 键与缓存内容
ls node_modules/.vite/deps
cat node_modules/.vite/deps/_metadata.json | head -40

# 强制重新预构建
npx vite --force
rm -rf node_modules/.vite && npx vite

# 调试某个依赖为何被预构建
DEBUG="vite:deps" npx vite
```

```javascript
// vite.config.js：预构建精细化配置
import { defineConfig } from 'vite';

export default defineConfig({
  optimizeDeps: {
    include: ['esm-dep > cjs-sub-dep'],         // 嵌套 CJS 依赖显式声明
    exclude: ['@my/heavy-lib'],                  // 让浏览器直连源码（link 场景）
    force: true,                                 // 等价 --force
    needsInterop: ['some-cjs-pkg'],              // 手动声明 default 互操作
    holdUntilCrawlEnd: true,                     // 等扫描完成再响应防瀑布
  },
});
```
