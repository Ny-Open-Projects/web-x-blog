---
title: [RBL-780] 笔试：手写 RSC 边界泄漏检测器（闭包传播 + server-only 判定）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-780：笔试：手写 RSC 边界泄漏检测器（闭包传播 + 泄漏判定）

**需求**：实现 `detectLeak(modules)`。modules: `Record<id, { deps: string[], isClient: boolean, serverOnly?: boolean, hasSecret?: boolean }>`（isClient 由 'use client' 声明或传播）。规则：1) client 闭包传播：isClient 模块的 deps 闭包全部标记 isClient（client 组件 import 的模块自动进 client bundle）；2) 泄漏判定：client 闭包内存在 serverOnly 或 hasSecret 模块 → 泄漏 `{ leaked: id, via: [传播路径] }`（最短路径 BFS）；3) 反向问题：serverOnly 模块 import client 模块属合法（server 可渲染 client 组件）；4) 返回 `{ leaks: Array<{ leaked, via }>, clientClosure: string[] }`。边界：无 client 模块；client 与 serverOnly 直接相邻。

```javascript
function detectLeak(modules) {
  // client 闭包传播（正向 deps）
  const client = new Set();
  const spread = (id) => {
    if (client.has(id)) return;
    client.add(id);
    for (const d of modules[id].deps) spread(d);
  };
  Object.entries(modules).forEach(([id, m]) => m.isClient && spread(id));

  // 泄漏：client 闭包内的 serverOnly/hasSecret，BFS 最短路径
  const leaks = [];
  const via = (target) => {                              // 从任一 isClient 源头到 target 的路径
    const roots = Object.keys(modules).filter(id => modules[id].isClient && !isDerived(id));
    for (const root of roots) {
      const queue = [[root, [root]]];
      const seen = new Set();
      while (queue.length) {
        const [cur, path] = queue.shift();
        if (cur === target) return path;
        if (seen.has(cur)) continue;
        seen.add(cur);
        for (const d of modules[cur].deps ?? []) queue.push([d, [...path, d]]);
      }
    }
    return [];
    function isDerived(id) { return !modules[id].isClientOriginal && client.has(id); }
  };
  for (const id of client) {
    const m = modules[id];
    if (m.serverOnly || m.hasSecret) leaks.push({ leaked: id, via: via(id), kind: m.hasSecret ? 'secret' : 'server-only' });
  }
  return { leaks, clientClosure: [...client] };
}

// 自测
const modules = {
  'page.server.ts': { deps: ['Chart.client.ts'], isClient: false },
  'Chart.client.ts': { deps: ['utils.ts'], isClient: true },
  'utils.ts': { deps: ['db.ts'], isClient: false },
  'db.ts': { deps: [], isClient: false, serverOnly: true, hasSecret: true },   // 泄漏
  'safe.ts': { deps: [], isClient: false },
};
let r = detectLeak(modules);
console.log(r.clientClosure.sort().join(','));           // Chart.client.ts,db.ts,utils.ts
console.log(r.leaks.some(l => l.leaked === 'db.ts' && l.kind === 'secret'));
console.log(r.leaks[0].via.join('>'));                   // Chart.client.ts>utils.ts>db.ts

// 无泄漏
r = detectLeak({ 'a.client.ts': { deps: ['b.ts'], isClient: true },
  'b.ts': { deps: [], isClient: false } });
console.log(r.leaks.length === 0);

// 直接相邻
r = detectLeak({ 'c.client.ts': { deps: ['db.ts'], isClient: true },
  'db.ts': { deps: [], serverOnly: true, isClient: false } });
console.log(r.leaks[0].via.join('>') === 'c.client.ts>db.ts');

// 无 client 模块
console.log(detectLeak({ x: { deps: [], isClient: false } }).clientClosure.length === 0);
```

**评分点**：
- client 闭包传播正确（deps 正向、环去重）；泄漏判定含 hasSecret/serverOnly 两类
- BFS 最短传播路径可读（via 数组），修复时一眼看到引用链
- server 模块 import client 合法（方向语义正确）；无 client 边界安全
- 能说清「泄漏是安全事故必须构建失败，运行时兜底只在执行路径命中才触发」属于加分
