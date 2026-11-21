---
title: [DP-244] 源码识别：Babel 插件源码中的访问者与作用域分析？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-244：源码识别：Babel 插件源码中的访问者与作用域分析？
**答**:
- 访问者（核心）：babel 插件返回 { visitor: { Identifier(path) {...} } }，遍历 AST 每类节点调用对应 visitor；path 是带操作上下文的封装（替换/删除/作用域查询）。
- 状态管理：program 钩子做初始化（跨节点收集信息），exit 时统一改写——两次遍历的模板方法。
- 命令：path.replaceWith/remove/skip 是 AST 变更命令，变更后 scope 自动重算（依赖分析重跑）。
- 识别要点：能写一个真实插件（如替换 import 源/删除 console），并解释 traverse 的"重新入队"（修改后再次访问）。

```javascript
// Babel 插件：移除 console + 收集作用域
module.exports = ({ types: t }) => ({
  name: 'remove-console',
  visitor: {
    Program(path, state) { path.scope.crawl(); },         // 初始化：重建作用域
    CallExpression(path) {                                 // 访问者
      if (isConsoleCall(path)) path.remove();              // 命令：删除节点
    },
    Identifier(path) {
      if (path.node.name === 'DEBUG' && path.parentPath.isMemberExpression?.() === false) {
        path.replaceWith(t.booleanLiteral(false));         // 命令：替换
        path.skip();                                       // 防重复访问
      }
    },
  },
});
// path.scope.getBinding('x') —— 作用域查询：识别变量来源（局部/导入/全局），做死代码分析的基础
```
