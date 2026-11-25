---
title: [MFW-738] 笔试：手写 RSC Context 校验
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-738：笔试：手写 RSC Context 校验

**答**：实现 `validateContextUsage(tree)`。tree: `{ name, type: 'server'|'client', uses: { context: boolean, provider: boolean, useContext: boolean }[], children }[]`. 规则：1) server 组件含 provider → error 'provider-in-server'（provider 必须 client）；2) server 组件 useContext → error 'useContext-in-server'；3) server 组件通过 children 模式包裹 client provider → info 'children-pattern'（正确模式——server children 传入 client provider）；4) client 子树的 useContext（正常——不报）；5) server 树的 props 直传（无 context——info 'props-pattern'——另一种正确模式）。返回 `{ findings: Array<{ node, severity, type }>, patterns: { childrenMode: number, propsMode: number } }`。边界：全 client 树（无 server findings）；无 context 使用；空树。

```javascript
function validateContextUsage(tree = { name: 'root', type: 'server', uses: {}, children: [] }) {
  const findings = []; const patterns = { childrenMode: 0, propsMode: 0 };
  function walk(node, parentIsClientProvider) {
    if (node.type === 'server') {
      if (node.uses?.provider)
        findings.push({ node: node.name, severity: 'error', type: 'provider-in-server',
          detail: 'server 组件不能是 Context.Provider——provider 必须 client' });
      if (node.uses?.useContext)
        findings.push({ node: node.name, severity: 'error', type: 'useContext-in-server',
          detail: 'server 组件不能 useContext——server 无 React 状态' });
      if (parentIsClientProvider)
        patterns.childrenMode++;                          // server children 在 client provider 内
      else if (!node.uses?.context)
        patterns.propsMode++;                             // props 直传模式
    }
    const isProvider = node.type === 'client' && node.uses?.provider;
    node.children?.forEach(c => walk(c, isProvider));
  }
  walk(tree, false);
  return { findings, patterns };
}

// 自测
// 错误：server 有 provider
let bad = { name: 'Page', type: 'server', uses: { provider: true }, children: [] };
let r = validateContextUsage(bad);
console.log(r.findings.some(f => f.type === 'provider-in-server' && f.severity === 'error'));

// 错误：server useContext
bad = { name: 'Data', type: 'server', uses: { useContext: true }, children: [] };
r = validateContextUsage(bad);
console.log(r.findings.some(f => f.type === 'useContext-in-server'));

// 正确：children 模式
const good = { name: 'Layout', type: 'server', uses: {}, children: [
  { name: 'ThemeProvider', type: 'client', uses: { provider: true }, children: [
    { name: 'ServerContent', type: 'server', uses: {}, children: [] } ] } ] };
r = validateContextUsage(good);
console.log(r.findings.length === 0);
console.log(r.patterns.childrenMode === 1);              // server children 在 provider 内

// 正常：client 子树 useContext
const clientTree = { name: 'Client', type: 'client', uses: { useContext: true }, children: [] };
r = validateContextUsage(clientTree);
console.log(r.findings.length === 0);                    // client useContext 正常

// props 模式
const propsOnly = { name: 'Page', type: 'server', uses: {}, children: [
  { name: 'ClientComp', type: 'client', uses: {}, children: [] } ] };
r = validateContextUsage(propsOnly);
console.log(r.patterns.propsMode >= 1);                  // props 直传计数
```

**评分点**：
- 双 error 检测（provider-in-server/useContext-in-server——RBL-737 的规则落地）
- children 模式识别（server children 在 client provider 内——正确模式计数）；props 模式计数
- 边界（全 client/无 context/空树）；client 子树的 useContext 正常（不误报）
- 能说清「RSC 的 Context 边界：provider 必须 client + server 用 props/ALS——显式数据流是 server 端的设计哲学」属于加分
