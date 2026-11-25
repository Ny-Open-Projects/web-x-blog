---
title: [WCN-562] 笔试：实现「事件处理器 → QRL 字符串」编译器（提取闭包依赖 + 生成懒加载 chunk 引用）。
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-562：笔试：实现「事件处理器 → QRL 字符串」编译器（提取闭包依赖 + 生成懒加载 chunk 引用）。

**答**：
- 结论：解析事件处理函数 AST，提取其引用的外部变量作为捕获状态，生成「chunk 路径#函数名」的 QRL 字符串。
- 捕获状态序列化到 q:obj；不可序列化的引用（如 DOM 节点）降级为选择器字符串。
- 生成懒加载 chunk 占位，实际代码按需分割。
- 追问：多个处理器共享依赖如何去重？（答：抽取公共状态到共享 q:obj，处理器引用其 key）

```javascript
function compileQRL(fnAst, chunkPath) {
  const captured = new Map();
  walk(fnAst, n => {
    if (n.type === 'Identifier' && !n.local && isExternal(n.name))
      captured.set(n.name, serializeCapture(n.name));
  });
  const qrl = `${chunkPath}#${fnAst.id.name}`;
  return { qrl, state: Object.fromEntries(captured), code: emitChunk(fnAst) };
}
function serializeCapture(name) {
  return name === 'this' ? { __ref: '$el' } : { __get: name };   // DOM 降级为选择器
}
function emitChunk(ast) { return `export function ${ast.id.name}(ctx){ /* restore & run */ }`; }
```

**评分点**：
- 闭包依赖提取与序列化
- chunk#函数 QRL 生成
- DOM 引用降级选择器
- 共享状态去重
