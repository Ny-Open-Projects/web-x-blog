---
title: [BLD-070] Rollup 的核心配置项有哪些？input、output formats、external、globals 怎么用？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-070：Rollup 的核心配置项有哪些？input、output formats、external、globals 怎么用？
**答**：
- input：入口（可数组/对象多入口）；output.format：esm / cjs / umd / iife / amd / system，UMD/IIFE 必须配 name。
- external：排除在 bundle 外的依赖（peer、node 内置）；支持数组、正则、函数返回 boolean；打库时 peerDependencies 必须全部 external。
- globals：UMD/IIFE 下 external 模块对应的全局变量映射；paths 可让 external 引用变成外部 URL（CDN）。
- treeshake: { moduleSideEffects } 控制副作用假设；output.entryFileNames/assetFileNames 控文件名；多输出复用同一 input。

```javascript
// rollup.config.js：formats + external 详解
import json from '@rollup/plugin-json';

export default [
  // 一份构建 输出多格式
  {
    input: { index: 'src/index.js', utils: 'src/utils.js' },
    external: (id) => /^node:/.test(id) || ['react', 'lodash-es'].includes(id),
    treeshake: { moduleSideEffects: 'no-external' }, // external 模块视为无副作用
    output: [
      { dir: 'dist/esm', format: 'esm', entryFileNames: '[name].mjs', preserveModules: true },
      { dir: 'dist/cjs', format: 'cjs', entryFileNames: '[name].cjs' },
      {
        dir: 'dist/umd', format: 'umd', name: 'MyLib',
        globals: { react: 'React', 'lodash-es': '_', lodash: '_' },
        paths: { react: 'https://cdn.example.com/react/index.js' }, // iife/amd 下转 URL
        exports: 'named',
      },
    ],
    plugins: [json()],
  },
];

// preserveModules: true（text 代码块）：
// 保留源码目录结构逐文件输出 适合 monorepo 内部包 消费方 shaking 更友好
```
