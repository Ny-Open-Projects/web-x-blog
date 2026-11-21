---
title: [CSS-190] stylelint 规则怎么定制落地到团队？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-190：stylelint 规则怎么定制落地到团队？

**答**：
- 起步用 stylelint-config-standard 兜底，再叠加团队硬约束：颜色必须走 token、z-index 白名单、BEM 命名正则。
- 高价值规则：`declaration-no-important`（堵 important 战争）、`max-nesting-depth`（防深嵌套）、`no-descending-specificity`（防优先级倒挂）。
- 用 message 字段把“为什么”写进报错，规则才有教育意义；配合 lint-staged 只查增量。
- 与 Prettier 分工：stylelint 管质量规则（写什么），Prettier 管格式（怎么写），互不重叠。

```javascript
// .stylelintrc.js —— 团队定制示例
module.exports = {
  extends: ['stylelint-config-standard'],
  rules: {
    // 颜色一律走 token 变量，禁止裸 hex
    'color-no-hex': [true, { message: '颜色请使用 CSS 变量 token，见 tokens.css' }],
    'alpha-value-notation': 'percentage',

    // z-index 白名单，终结层级战争
    'declaration-property-value-allowed-list': {
      'z-index': ['0', '1', '10', '100', '999'],
    },

    // BEM 命名：block__element--modifier
    'selector-class-pattern':
      '^([a-z][a-z0-9]*(-[a-z0-9]+)*)(__([a-z][a-z0-9]*(-[a-z0-9]+)*))?(--[a-z0-9-]+)?$',

    'max-nesting-depth': 3,             // 防结构深耦合
    'no-descending-specificity': true,  // 防优先级倒挂
    'declaration-no-important': true,   // 堵 important 战争
    'comment-empty-line-before': 'always',
  },
  ignoreFiles: ['dist/**', 'coverage/**', '**/legacy/**'],
};
```

## 三十一、综合与体系
