---
title: [BAS-047] package.json 里最常用的字段有哪些？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-047：package.json 里最常用的字段有哪些？
**答**：
- name/version：包名与版本；type: "module" 启用 ESM。
- scripts：自定义命令；dependencies 与 devDependencies：生产与开发依赖。
- main/module/exports：入口与导出映射；engines 约束 Node 版本；packageManager 锁定包管理器。

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "type": "module",
  "scripts": { "dev": "vite", "build": "vite build" },
  "dependencies": { "vue": "^3.5.0" },
  "devDependencies": { "vite": "^6.0.0" },
  "engines": { "node": ">=20" },
  "packageManager": "pnpm@9.0.0"
}
```
