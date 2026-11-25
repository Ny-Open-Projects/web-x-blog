---
title: [ENG-025] Babel 的编译流程分哪三步？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-025：Babel 的编译流程分哪三步？
**答**：
- parse：把源码字符串解析成 AST（抽象语法树），使用 @babel/parser。
- transform：遍历 AST，visitor 在节点上做增删改，这是插件工作的阶段。
- generate：把修改后的 AST 生成回代码字符串并产出 sourcemap。
- 理解这条链路就能写出代码变换插件，也是理解所有转译工具的基础。

```javascript
// babel-plugin-dev-flag.js —— 演示 transform 阶段的 visitor
module.exports = function ({ types: t }) {
  return {
    visitor: {
      CallExpression(path) {
        // 把 __DEV__() 调用替换为布尔字面量
        if (path.node.callee.name === '__DEV__') {
          path.replaceWith(
            t.booleanLiteral(process.env.NODE_ENV !== 'production')
          );
        }
      },
    },
  };
};

// 配置：plugins: ['./babel-plugin-dev-flag.js']
```
