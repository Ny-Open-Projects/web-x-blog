---
title: [R19-129] 大型 React 项目的依赖治理怎么做？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-129：大型 React 项目的依赖治理怎么做？
**答**：
- Bundle 体检：source-map-explorer / rollup-plugin-visualizer 找体积元凶与重复打包（比如同时打了 React 18 和 19）。
- 单实例红线：npm ls react 确认全树只有一个 React，多实例是微前端与组件库最常见的 Invalid hook call 根因。
- 幽灵依赖治理：pnpm 严格隔离，未在 package.json 声明的包不允许 import。
- React 升级策略：小步升级 + codemod + 第三方 peerDeps 先行确认，锁版本但保持季度体检。

```javascript
// deps-guard.ts —— 大型 React 项目的依赖治理
// 1. Bundle 体检：找出体积元凶与重复打包
//    npx source-map-explorer 'dist/assets/*.js'
//    或 vite 构建 + rollup-plugin-visualizer 生成依赖树报告

// 2. 单实例红线：确认只有一个 React 实例
//    npm ls react        # 全树必须收敛到一行
//    多实例 = 微前端/组件库最常见的 "Invalid hook call" 根因

// 3. 幽灵依赖治理：pnpm 严格隔离，未声明的包不能 import
//    .npmrc: shamefully-hoist=false

// 4. 升级流程代码化：升级前跑 codemod 与测试
import { useEffect } from 'react';

export function useDepAudit() {
  useEffect(() => {
    if (import.meta.env.DEV) {
      // 开发期断言全局只挂了一个 React 版本，双实例第一时间报警
      const versions = Object.keys(window).filter(k => k.startsWith('__reactContainer'));
      if (versions.length > 1) console.warn('检测到多个 React 实例，请检查依赖收敛');
    }
  }, []);
}
```
