---
title: [BLD-145] 库的 peerDependencies 与外部化策略：怎么决定一个依赖进 bundle 还是留外部？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-145：库的 peerDependencies 与外部化策略：怎么决定一个依赖进 bundle 还是留外部？
**答**：
- 决策三问：**宿主会不会有**（react/vue 这类框架依赖 → peerDependencies + external，避免双实例）、**是否需要独立演化**（utils 工具 → 直接打进 bundle，减少宿主安装成本）、**是否含原生/大依赖**（lodash 整包 → 打进或按需子路径）。
- 标准公式：`external: [/^react($|\/)/, /^react-dom($|\/)/]` + peerDependencies 声明同范围；devDependencies 装一份用于自测（pnpm 下 peer 自动装）。
- `peerDependenciesMeta: { react: { optional: true } }` 处理可选 peer；monorepo 内库互引用 `workspace:*` 发版时转真实版本（pnpm publish 自动处理）。
- 面试追问"为什么不能把 react 打进库"：双实例 → hooks 失效、context 断裂、包体积翻倍；React 的 RSC/版本特性（如 18 的 useId）依赖宿主一致。

```json
// package.json：依赖分层的标准写法
{
  "name": "my-ui-lib",
  "peerDependencies": {
    "react": ">=17 <20",           // 宿主提供的运行时
    "react-dom": ">=17 <20",
    "clsx": ">=2"                  // 常用小工具也可 peer 化让宿主统一
  },
  "peerDependenciesMeta": {
    "clsx": { "optional": true }   // 宿主没装时库内降级实现
  },
  "dependencies": {
    // 仅放"必须进 bundle"的：纯计算工具、polyfill 级依赖
    "@my-lib/geometry": "workspace:*",
    "npm-normalize-package-bin": "^3.0.0"
  },
  "devDependencies": {
    "react": "18.3.1",             // 自测用：pnpm 会自动为 peer 安装
    "react-dom": "18.3.1"
  }
}
```

```javascript
// rollup.config.mjs：外部化与 peer 对齐（含子路径与 monorepo 内部包）
import pkg from './package.json' with { type: 'json' };

const externals = [
  ...Object.keys(pkg.peerDependencies ?? {}),          // react react-dom clsx
  ...Object.keys(pkg.dependencies ?? {})
    .filter((d) => d.startsWith('@my-lib/')),          // monorepo 内部包也留外部（宿主构建时解析）
];
export default {
  input: 'src/index.ts',
  external: (id) => {
    if (id.startsWith('node:')) return true;           // node 内置模块
    return externals.some((e) => id === e || id.startsWith(e + '/'));  // 覆盖 'react-dom/client' 等子路径
  },
  plugins: [/* esbuild/typescript */],
  output: [
    { format: 'esm', dir: 'dist/esm', preserveModules: true, preserveModulesRoot: 'src' },
    // preserveModules：按源码结构出多文件（库的按需 tree-shaking 更好）
  ],
};
```
