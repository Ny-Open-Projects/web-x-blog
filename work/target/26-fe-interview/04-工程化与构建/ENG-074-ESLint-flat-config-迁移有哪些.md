---
title: [ENG-074] ESLint flat config 迁移有哪些要点？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-074：ESLint flat config 迁移有哪些要点？
**答**：
- 入口从 .eslintrc* 变为 eslint.config.js（mjs），导出数组按顺序合并，后者覆盖前者。
- 老的 extends/overrides 换成数组展开与 files 过滤：configs 里手动展开插件推荐集。
- ignore 用单独的全局项（ignores 只出现一个键时表示全局忽略），替代 .eslintignore。
- 老插件不兼容时用 FlatCompat 转换层过渡；ESLint v9 起已移除 eslintrc 支持必须迁移。

```javascript
// eslint.config.mjs flat config
import js from '@eslint/js';
import tseslint from 'typescript-eslint';
import reactHooks from 'eslint-plugin-react-hooks';

export default tseslint.config(
  { ignores: ['dist/**', 'coverage/**', 'node_modules/**'] },
  js.configs.recommended,
  ...tseslint.configs.recommended,
  {
    files: ['**/*.{ts,tsx}'],
    plugins: { 'react-hooks': reactHooks },
    rules: {
      ...reactHooks.configs.recommended.rules,
      'no-console': ['warn', { allow: ['warn', 'error'] }],
    },
  },
  {
    // 局部覆盖：构建脚本允许 console
    files: ['scripts/**/*.ts'],
    rules: { 'no-console': 'off' },
  }
);
```
