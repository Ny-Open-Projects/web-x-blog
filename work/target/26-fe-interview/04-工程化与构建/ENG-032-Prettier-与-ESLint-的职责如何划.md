---
title: [ENG-032] Prettier 与 ESLint 的职责如何划分？怎么避免冲突？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-032：Prettier 与 ESLint 的职责如何划分？怎么避免冲突？
**答**：
- ESLint 管代码质量（no-unused-vars、eqeqeq），Prettier 管格式（缩进、引号、换行）。
- 格式规则冲突的解法：eslint-config-prettier 关闭 ESLint 中所有格式类规则。
- 工作流：编辑器保存即 Prettier 格式化，ESLint 管质量并在 CI 中兜底。
- 两者的规则不要重复配置，单一事实来源。

```javascript
// .prettierrc.js
module.exports = {
  printWidth: 100,
  semi: true,
  singleQuote: true,
  trailingComma: 'es5',
};

// package.json 的 devDependencies 中加入
// eslint-config-prettier
// 并在 eslint.config.js 数组末尾引入，关闭所有格式类 ESLint 规则
// import eslintConfigPrettier from 'eslint-config-prettier';
// export default [ ..., eslintConfigPrettier ];
```
