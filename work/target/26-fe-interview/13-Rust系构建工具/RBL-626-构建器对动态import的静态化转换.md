---
title: [RBL-626] 动态 import 的静态化转换：模板字符串路径与变量表达式的处理边界
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-626：动态 import 的静态化转换：模板字符串路径与变量表达式的处理边界

**答**:
- `import('./pages/' + name)` 这类动态表达式无法静态确定模块——构建器的处理光谱：1) **可静态化模式**（import.meta.glob / require.context）：框架提供 DSL，构建期展开成显式映射（路径 → () => import()），运行时查表——推荐解法，产物可控可分析；2) **宽松打包**（webpack 的部分动态：前缀目录全打包成 context chunk）：体积不可控但兼容旧代码；3) **拒绝 + 诊断**（严格模式：报错并给迁移建议）。现代工具（rolldown/vite）倾向 1+3。
- 静态化的语义细节：`import(`./locales/${lang}.json`)` 展开时要处理——路径参数的注入风险（`../` 逃逸出目录，glob 展开必须做前缀锁定）、重名冲突（a/b.js 与 a.b.js 的 key 归一化）、扩展名歧义（.ts/.js 同名）。Vite glob 的 `eager`/`query` 选项覆盖懒/急两种需求。
- 运行时查表方案的 hash 关联问题：映射表里的 chunk URL 要用 manifest 当前值——映射表必须由构建器生成（RBL-598 的级联 hash 联动），不能手写路径，否则发布后 404。
- 动态 import 与 tree shaking 的交互：动态入口的「使用面」未知 → 其闭包全部保留（不能 shake 掉任何导出）——这也是「动态入口越多、shake 效果越差」的原因；glob 展开成显式映射后，映射值的导出面仍未知，但至少路径集确定。
- 追问钩子：为什么「全打包 context」模式在 monorepo 场景是事故源？——目录扫描范围失控（node_modules 巨大目录被卷入）、依赖变化触发 context 全量失效；显式 glob 模式把范围与缓存键都收紧了。

```javascript
// import.meta.glob 的构建期展开
// 源码：const pages = import.meta.glob('./pages/*.vue')
// 展开为：
const pages = {
  './pages/Home.vue': () => import('/src/pages/Home.vue'),
  './pages/List.vue': () => import('/src/pages/List.vue'),
};
// eager 模式：import('/src/pages/Home.vue') -> 直接 import 语句（同步包含）

// 构建期展开实现要点
function expandGlob(pattern, files, { base }) {
  const out = {};
  for (const f of files) {
    const rel = path.relative(base, f);                  // 相对调用方
    if (!micromatch.isMatch(rel, pattern.slice(2))) continue;
    if (rel.includes('..')) throw new Error('glob 逃逸');  // 前缀锁定，防路径注入
    out('./' + rel) = `() => import('/src/${rel}')`;     // 显式映射 -> manifest hash 联动
  }
  return out;                                            // 运行时查表，路径集构建期固定
}

// 动态入口的 shake 代价（对比）
// static:  import { A } from './lib'      -> lib 未用的 B/C 可删
// dynamic: import('./lib')                -> lib 整体保留（使用面未知）
```
