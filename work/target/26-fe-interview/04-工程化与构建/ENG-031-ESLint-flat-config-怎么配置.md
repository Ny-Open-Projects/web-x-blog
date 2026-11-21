---
title: [ENG-031] ESLint flat config 怎么配置？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-031：ESLint flat config 怎么配置？
**答**：
- ESLint 9 起默认 flat config（eslint.config.js），用数组导出配置对象，替代 eslintrc 的级联。
- 每个对象可指定 files 范围、plugins、rules；ignores 单独一项实现排除。
- 官方推荐配置（js.configs.recommended、typescript-eslint）按数组顺序叠加，后面的覆盖前面的。
- React 项目加 eslint-plugin-react-hooks，保证 Hook 规则强制生效。

```javascript
// eslint.config.js —— flat config
import js from '@eslint/js';
import reactHooks from 'eslint-plugin-react-hooks';

export default [
  { ignores: ['dist/**', 'node_modules/**'] },
  js.configs.recommended,
  {
    files: ['src/**/*.{js,jsx,ts,tsx}'],
    plugins: { 'react-hooks': reactHooks },
    rules: {
      ...reactHooks.configs.recommended.rules,
      'no-console': 'warn',
      eqeqeq: ['error', 'smart'],
    },
  },
];
```
