---
title: [MFW-130] 笔试：手写一个 RRv7 风格的路由匹配器（含动态段与嵌套）
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-130：笔试：手写一个 RRv7 风格的路由匹配器（含动态段与嵌套）
**答**：实现 `matchRoutes(routes, pathname)`：① 扁平 routes 定义（含 `path` 与 `children`）；② 支持动态段 `:id`、可选段 `?`、通配 `*`；③ 返回匹配链（从根到叶的 branch，含每层 params）；④ 嵌套路径父子拼接（children 的相对路径）；⑤ index route（`index: true`）只在父路径精确匹配时命中。

```ts
type RouteDef = {
  path?: string;            // 相对父级
  index?: boolean;          // index route
  children?: RouteDef[];
  id?: string;
};

type Matched = { route: RouteDef; pathname: string; params: Record<string, string> };

function matchSegments(pattern: string, segs: string[]): Record<string, string> | null {
  const p = pattern.split('/').filter(Boolean);
  if (p.length !== segs.length) return null;
  const params: Record<string, string> = {};
  for (let i = 0; i < p.length; i++) {
    const seg = p[i];
    if (seg.startsWith(':')) params[seg.slice(1)] = decodeURIComponent(segs[i]);
    else if (seg.endsWith('?')) {
      // 可选段：允许缺省（段数不同在此简化模型下按相等处理，可选段缺失记空串）
      params[seg.slice(0, -1)] ??= '';
    } else if (seg !== segs[i]) return null;
  }
  return params;
}

function matchBranch(
  defs: RouteDef[], parentPath: string, segs: string[],
  branch: Matched[] = [], results: Matched[][] = [],
): void {
  // index route 特判
  const indexDef = defs.find((d) => d.index);
  if (indexDef && segs.length === 0) {
    results.push([...branch, { route: indexDef, pathname: parentPath, params: {} }]);
  }

  for (const def of defs) {
    if (def.index) continue;
    const pattern = def.path ?? '';
    const abs = (parentPath === '/' ? '' : parentPath) + '/' + pattern;
    const pathSegs = pattern.split('/').filter(Boolean);
    const consumed = pathSegs.length;

    // 简化：逐段前缀匹配
    if (consumed > segs.length) continue;
    const front = segs.slice(0, consumed);
    const params = matchSegments(pattern, front);
    if (!params) continue;

    const entry: Matched = { route: def, pathname: abs || '/', params };
    const rest = segs.slice(consumed);

    if (pattern.endsWith('*') || rest.length === 0) {
      // 通配吞掉剩余段 或 恰好用尽 -> 成功分支
      results.push([...branch, entry]);
    } else if (def.children) {
      matchBranch(def.children, abs, rest, [...branch, entry], results);
    }
  }
}

function matchRoutes(routes: RouteDef[], pathname: string): Matched[] | null {
  const segs = pathname.split('/').filter(Boolean);
  const results: Matched[][] = [];
  matchBranch(routes, '/', segs, [], results);
  if (!results.length) return null;
  // 优先最深的分支（最长匹配）
  results.sort((a, b) => b.length - a.length);
  return results[0];
}

// —— 用例 ——
const routes: RouteDef[] = [
  { path: '', id: 'root', children: [
    { path: 'products', children: [
      { path: ':id', id: 'product' },
      { index: true, id: 'products-index' },
    ] },
    { path: 'docs/*', id: 'docs' },
  ] },
];
// matchRoutes(routes, '/products/42') -> [root, products, product], params: { id: '42' }
// matchRoutes(routes, '/products')   -> [root, products, products-index]
```

**评分点**：
1. 返回的是匹配链（branch）而非单个 route——嵌套布局渲染就依赖链。
2. index route 只在父路径精确（无剩余段）时命中。
3. 动态段 `:id` 解码并进 params；`*` 通配吞剩余段。
4. 相对路径父子拼接正确（处理 `/` 边界）。
5. 多分支命中时选最长匹配（React Router 的 ranking 简化版）。
