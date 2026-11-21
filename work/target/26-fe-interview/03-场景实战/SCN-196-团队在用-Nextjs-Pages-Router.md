---
title: [SCN-196] 团队在用 Next.js Pages Router，传闻要迁 RSC（React Server Components），如何做迁移评估而不是盲目跟风？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-196：团队在用 Next.js Pages Router，传闻要迁 RSC（React Server Components），如何做迁移评估而不是盲目跟风？
**答**：
- RSC 的收益是有条件的：内容重、数据聚合多、客户端 bundle 大的页面收益明显；重交互、重状态的后台页面收益趋近于零。评估第一步是现状盘点，不是学 API。
- 盘点三件事：组件树里 server-safe 组件占比（无状态、无事件、可服务端渲染）、客户端 bundle 构成（数据获取库占了多少）、数据流复杂度（多少瀑布式请求能被服务端聚合掉）。
- 成本面：数据获取模式变化（fetch 缓存语义）、第三方库兼容（依赖 window/Context 的库不能进 server 组件）、团队心智（server/client 边界调试成本）。
- 结论输出为决策矩阵：按页面逐个标"直接迁/改造后迁/不迁"，给出预估收益（bundle 减少 x%、TTFB 改善），而不是全站口号式迁移。

```jsx
// RSC 迁移评估：组件树盘点脚本 + 决策矩阵
// scripts/rsc-audit.tsx：扫描组件树，评估 server-safe 占比
import { parse } from '@babel/parser';
import traverse from '@babel/traverse';
import fg from 'fast-glob';

const CLIENT_SIGNALS = ['useState', 'useEffect', 'useReducer', 'useContext', 'onClick', 'onChange'];
const BANNED_IN_SERVER = ['window', 'document', 'localStorage', 'framer-motion', 'react-hook-form'];

export async function auditRscReadiness(pagesDir = 'src/pages') {
  const report = [];
  for (const file of await fg(`${pagesDir}/**/*.tsx`)) {
    const ast = parse(readFile(file), { sourceType: 'module', plugins: ['tsx'] });
    let hooks = 0, handlers = 0, clientOnlyImports = [];
    traverse.default(ast, {
      CallExpression(p) { if (CLIENT_SIGNALS.includes(p.node.callee.name)) hooks++; },
      JSXAttribute(p) { if (/^on[A-Z]/.test(p.node.name.name)) handlers++; },
      ImportDeclaration(p) {
        const src = p.node.source.value;
        if (BANNED_IN_SERVER.some(b => src.includes(b))) clientOnlyImports.push(src);
      },
    });
    report.push({
      file,
      serverSafeRatio: 1 - Math.min(1, (hooks + handlers * 0.5) / 20), // 启发式：交互越少越安全
      blockers: clientOnlyImports,
      verdict: hooks + handlers === 0 && !clientOnlyImports.length ? 'direct' // 可直接转 server 组件
        : clientOnlyImports.length < 3 ? 'refactor' : 'keep-client',       // 需改造 / 保持 client
    });
  }
  // 输出决策矩阵：按页面给出迁移建议与预期 bundle 收益
  return report.sort((a, b) => a.serverSafeRatio - b.serverSafeRatio);
}
// 评估结论示例：
//   pages/list       serverSafe 0.9  verdict direct       预期 bundle -40%（表格纯展示）
//   pages/dashboard  serverSafe 0.3  verdict keep-client  重交互后台，不迁
```
