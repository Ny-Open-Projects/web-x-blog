---
title: [MFW-687] 笔试：手写 client 边界最小化分析器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-687：笔试：手写 client 边界分析器

**答**：实现 `analyzeClientBoundary(tree)`。tree: `{ name, isClient: boolean, hooks?: string[], imports?: string[], children: tree[] }`. 规则：1) **过度 client 化检测**：父级 client 且所有子也 client（整页 client——'use client' 在顶层）→ warn 'over-client'（拆分建议：叶子化）；2) **hooks 检测**：server 组件有 hooks（useState/useEffect）→ error 'hooks-in-server'；3) **最小化评分**：client 节点占比（越低越好——client 叶子占比 = bundle 效率）；4) **children 模式的识别**：client 节点有 children 属性且 children 是 server 子树 → info 'children-pattern'（良好实践）。返回 `{ issues, clientRatio, suggestions }`。边界：全 server 树（ratio 0）；全 client 树（ratio 1 + over-client）；空树。

```javascript
function analyzeClientBoundary(tree = { name: 'root', isClient: false, children: [] }) {
  let total = 0, clientCount = 0;
  const issues = [], suggestions = [];
  function walk(node, parentClient) {
    total++;
    if (node.isClient) clientCount++;
    // hooks in server
    if (!node.isClient && node.hooks?.length)
      issues.push({ node: node.name, severity: 'error',
        issue: 'hooks-in-server', detail: `server 组件含 hooks: ${node.hooks.join(',')}` });
    // over-client：parent client 且当前也是 client 且有子节点
    if (node.isClient && parentClient && node.children?.length)
      issues.push({ node: node.name, severity: 'warn',
        issue: 'over-client', detail: '整页 client 化——下移到叶子' });
    // children 模式：client 节点的 children 是 server
    if (node.isClient && node.children?.some(c => !c.isClient))
      suggestions.push(`${node.name} 使用 children 模式（client 壳 + server 内容）——良好`);
    node.children?.forEach(c => walk(c, node.isClient));
  }
  walk(tree, false);
  const clientRatio = total ? +(clientCount / total).toFixed(2) : 0;
  if (clientRatio > 0.8)
    suggestions.push('client 占比过高——检查是否需要整页交互');
  return { issues, clientRatio, suggestions };
}

// 自测
const overClient = { name: 'page', isClient: true, hooks: ['useState'], children: [
  { name: 'Header', isClient: true, children: [] },
  { name: 'List', isClient: true, hooks: ['useState'], children: [
    { name: 'Item', isClient: true, children: [] } ] } ] };
let r = analyzeClientBoundary(overClient);
console.log(r.clientRatio === 1);                        // 全 client
console.log(r.issues.some(i => i.issue === 'over-client' && i.node === 'page'));
console.log(r.issues.some(i => i.issue === 'hooks-in-server' && i.node === 'page'));

// server 组件 hooks → error
const badServer = { name: 'page', isClient: false, hooks: ['useState'], children: [] };
r = analyzeClientBoundary(badServer);
console.log(r.issues.some(i => i.issue === 'hooks-in-server'));

// 最小边界（children 模式）
const good = { name: 'page', isClient: false, children: [
  { name: 'Modal', isClient: true, children: [
    { name: 'ServerContent', isClient: false, children: [] } ] } ] };
r = analyzeClientBoundary(good);
console.log(r.clientRatio === 0.33);                     // 1/3 client
console.log(r.suggestions.some(s => s.includes('children 模式')));
console.log(r.issues.length === 0);
```

**评分点**：
- over-client 检测（父 client + 子 client——整页 client 化的架构反模式）；server hooks error
- children 模式识别（client 壳 + server 内容——最佳实践提示）；clientRatio 评分
- 边界（全 server/全 client/空树）；建议的可执行性（下移到叶子）
- 能说清「client 边界的最小化 = 交互逻辑 client 化、内容渲染 server 化——children 模式是黄金模式」属于加分
