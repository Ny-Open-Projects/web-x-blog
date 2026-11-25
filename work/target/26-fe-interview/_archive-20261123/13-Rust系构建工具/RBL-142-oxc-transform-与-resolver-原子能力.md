---
title: [RBL-142] oxc-transform 与 oxc-resolver：原子能力怎么单独用
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-142：oxc-transform 与 oxc-resolver：原子能力怎么单独用

**答**：
- oxc-transform 是独立小件集合：strip types（去类型）、React refresh 注入、常量折叠、Inject Global/polyfill 等，比整套 SWC 轻量，适合"只要一个转换"的场景。
- oxc-resolver 对标 webpack 的 enhanced-resolve，Rust 实现且支持 yarn/pnpm pnp、tsconfig paths、extension/exts 别名策略；Vite/Rolldown 用它做模块解析提速。
- 单独可用的意义：不用引入整个打包器也能获得解析一致性——比如自己写构建脚本、依赖审计工具时，用 oxc-resolver 复现宿主打包器的模块解析行为。
- transform 组件都是"单文件进、单文件出"的纯函数，天然可并行（worker/线程池），适合批量脚本。
- 追问钩子：解析差异是"双内核一致性"问题的重灾区——用 oxc-resolver 后要与 webpack 行为对齐 mainFields/alias 等关键项。

```javascript
// 1) resolve：在脚本里解析 @/components/Button 实际指向哪个文件
import { ResolverFactory } from 'oxc-resolver';
const rf = new ResolverFactory({
  extensions: ['.tsx', '.ts', '.jsx', '.js', '.json'],
  tsconfig: { references: undefined, configFile: './tsconfig.json' },
});
const resolved = rf.sync('/proj/src/pages', '@/components/Button');
// { path: '/proj/src/components/Button.tsx', error: undefined }

// 2) transform：单独去类型（不引入打包器）
import { transform } from 'oxc-transform';
const out = transform('x.ts', source, { lang: 'ts', target: 'es2020' });
console.log(out.code, out.errors);
```
