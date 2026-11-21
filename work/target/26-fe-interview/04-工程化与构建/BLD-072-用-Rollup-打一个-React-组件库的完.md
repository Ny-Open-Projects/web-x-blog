---
title: [BLD-072] 用 Rollup 打一个 React 组件库的完整实战配置（多格式 + d.ts + 按需入口）。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-072：用 Rollup 打一个 React 组件库的完整实战配置（多格式 + d.ts + 按需入口）。
**答**：
- 产物矩阵：ESM（preserveModules 保留结构，消费方按需 shaking）+ CJS + 类型声明（rollup-plugin-dts 或 tsc --emitDeclarationOnly）。
- peerDependencies external + exclude 排除样式与静态资源；babel 只做语法不做 polyfill（库不注入 polyfill，交给业务方）。
- exports 字段按条件导出，types 排最前；sideEffects 声明样式文件豁免。

```javascript
// rollup.config.mjs：组件库完整配置
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import { babel } from '@rollup/plugin-babel';
import dts from 'rollup-plugin-dts';

const extensions = ['.js', '.jsx', '.ts', '.tsx'];

const common = {
  external: (id) => /^react($|\/)/.test(id) || /\.css$/.test(id),
  plugins: [
    resolve({ extensions }),
    commonjs(),
    babel({
      extensions,
      babelHelpers: 'bundled',
      exclude: 'node_modules/**',
      presets: [['@babel/preset-env', { targets: { chrome: '87' }, modules: false }], '@babel/preset-react'],
    }),
  ],
};

export default [
  { ...common, input: 'src/index.ts',
    output: { dir: 'dist/esm', format: 'esm', preserveModules: true, preserveModulesRoot: 'src' } },
  { ...common, input: 'src/index.ts',
    output: { dir: 'dist/cjs', format: 'cjs' } },
  { input: 'dist-tmp/index.d.ts', output: { file: 'dist/index.d.ts', format: 'esm' }, plugins: [dts()] },
];
```
