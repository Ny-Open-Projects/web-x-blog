---
title: [MFW-110] 笔试：手写一个 SSG 预渲染检查器（adapter-static 前置校验）
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-110：笔试：手写一个 SSG 预渲染检查器（adapter-static 前置校验）
**题目**：用 adapter-static 时全站必须可预渲染。实现 `checkPrerenderable(routes)`：① 路由标记了 `prerender = false` 或依赖请求级数据（cookies/headers/fetch 外部 API 无 fallback）→ 报错并列出原因；② 动态路由 `:id` 没有提供 entries 列表 → 报错；③ 检查通过的返回可渲染 URL 清单。

```ts
type Route = {
  path: string;                 // 支持 :param
  prerender?: boolean;          // 显式 opt-out
  usesRequestData?: boolean;    // load 里读了 cookies/headers
  entries?: string[];           // 动态路由的具体参数清单
};

type Issue = { path: string; reason: string };

function expandStatic(path: string, entries?: string[]): string[] {
  if (!path.includes(':')) return [path];
  if (!entries?.length) return []; // 动态路由无 entries：由检查器报错
  // 只处理单段参数的简化版；多段嵌套可递归展开
  return entries.map((e) => path.replace(/:[^/]+/g, e));
}

function checkPrerenderable(routes: Route[]): { ok: true; urls: string[] } | { ok: false; issues: Issue[] } {
  const issues: Issue[] = [];
  const urls: string[] = [];

  for (const route of routes) {
    if (route.prerender === false) {
      issues.push({ path: route.path, reason: '显式声明 prerender: false，与 adapter-static 冲突' });
      continue;
    }
    if (route.usesRequestData) {
      issues.push({ path: route.path, reason: 'load 读取了请求级数据（cookies/headers），无法构建期渲染' });
      continue;
    }
    if (route.path.includes(':')) {
      if (!route.entries?.length) {
        issues.push({ path: route.path, reason: '动态路由未提供 entries，构建期不知道要渲染哪些 URL' });
        continue;
      }
      urls.push(...expandStatic(route.path, route.entries));
    } else {
      urls.push(route.path);
    }
  }

  return issues.length ? { ok: false, issues } : { ok: true, urls };
}

// —— 用例 ——
const routes: Route[] = [
  { path: '/', prerender: true },
  { path: '/products/:id', entries: ['/products/p1', '/products/p2'] },
  { path: '/account', prerender: false },        // -> 报错
  { path: '/search', usesRequestData: true },    // -> 报错
  { path: '/blog/:slug' },                       // -> 无 entries 报错
];
// checkPrerenderable(routes).issues.length === 3
```

**评分点**：
1. 三类不可预渲染情形都覆盖：显式 opt-out、请求级数据、动态路由缺 entries。
2. 动态路由用 entries 展开，能说出 adapter-static 要求 `export const entries`。
3. issues 聚合所有错误一次报出，而不是遇错即停（对构建 DX 更友好）。
4. 展开 URL 时占位符替换正确；无 entries 的动态路由不会产出错误 URL。
5. 能口头补充：adapter-static 下 POST API（+server.ts）也不可用，需走外部服务。
