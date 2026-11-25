---
title: [MFW-762] 笔试：手写 RSC 边缘兼容审计
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-762：笔试：手写 RSC 边缘审计

**答**：实现 `auditEdgeCompatibility(components)`。components: `{ name, runtime: 'edge'|'nodejs', imports: string[], usesBrowserAPI?: boolean }[]`. 规则：1) edge 组件的 Node API import（fs/path/child_process/crypto(node)/net → error 'node-api-in-edge'）；2) edge 组件的 browser API（window/document——server 渲染无 DOM RBL-914——error 'browser-api-in-server'；3) nodejs 组件的 browser API（同样 error）；4) Web API 检查：fetch/crypto.subtle/URL → ok（edge 可用）；5) 返回 `{ findings: Array<{ component, api, type, severity }>, ok }`（ok = 无 error）。边界：全 nodejs（无 edge 检查）；空 imports；混合 runtime（分组件检查）。

```javascript
const NODE_ONLY_APIS = ['fs', 'path', 'child_process', 'net', 'cluster', 'node:fs'];
const BROWSER_APIS = ['window.', 'document.', 'localStorage.', 'navigator.'];

function auditEdgeCompatibility(components = []) {
  const findings = [];
  for (const comp of components) {
    for (const imp of comp.imports ?? []) {
      // Node API in edge
      if (comp.runtime === 'edge' &&
          NODE_ONLY_APIS.some(n => imp.includes(n) || imp === n))
        findings.push({ component: comp.name, api: imp, type: 'node-api-in-edge',
          severity: 'error', detail: `edge 运行时不支持 ${imp}` });
    }
    if (comp.usesBrowserAPI) {
      findings.push({ component: comp.name, api: 'browser-global',
        type: comp.runtime === 'edge' ? 'browser-api-in-server' : 'browser-api-in-node',
        severity: 'error', detail: 'server 渲染不可用 browser API' });
    }
  }
  return { findings, ok: !findings.some(f => f.severity === 'error') };
}

// 自测
const components = [
  { name: 'ProductsPage', runtime: 'edge', imports: ['node:fetch', 'crypto.subtle'] },   // OK: Web API
  { name: 'DbPage', runtime: 'edge', imports: ['fs', 'path'] },                          // error
  { name: 'WindowPage', runtime: 'edge', usesBrowserAPI: true },                         // error
  { name: 'AdminPage', runtime: 'nodejs', imports: ['fs', 'prisma'] },                   // OK: node 可以
  { name: 'BadServer', runtime: 'nodejs', usesBrowserAPI: true },                        // error
];
let r = auditEdgeCompatibility(components);
console.log(r.errors = r.findings.filter(f => f.severity === 'error'));
console.log(r.findings.filter(f => f.severity === 'error').length === 3);   // DbPage/WindowPage/BadServer
console.log(!r.findings.some(f => f.component === 'ProductsPage'));   // Web API 不报
console.log(!r.findings.some(f => f.component === 'AdminPage'));      // node + fs 不报
console.log(r.ok === false);

// 全 nodejs
r = auditEdgeCompatibility(components.filter(c => c.runtime === 'nodejs'));
console.log(r.findings.filter(f => f.type === 'node-api-in-edge').length === 0);   // 无 edge
console.log(auditEdgeCompatibility([]).ok === true);
```

**评分点**：
- 双维度审计：edge 的 Node API（NODE_ONLY_APIS 白名单）+ browser API（server 无 DOM）
- nodejs runtime 的 browser API 同样 error（server 渲染无 DOM——RBL-914 的静态版）；Web API 不误报
- 边界（全 nodejs 无 edge 检查/空 imports/混合 runtime 分组件审计）
- 能说清「RSC 的组件级 runtime 约束：per-component 的 edge 兼容性检查——一个组件用 fs = 整路由不可 edge」属于加分
