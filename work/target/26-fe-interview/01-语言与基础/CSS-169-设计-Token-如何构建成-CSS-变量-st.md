---
title: [CSS-169] 设计 Token 如何构建成 CSS 变量（style-dictionary 思想）？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-169：设计 Token 如何构建成 CSS 变量（style-dictionary 思想）？

**答**：
- 单一来源：token 以 JSON/YAML 维护（颜色/字号/间距/圆角/阴影五类），设计工具与代码共用。
- 构建期 transform：命名 camelCase → kebab-case、值校验、别名解析（brand.500 → #009966），再按平台输出 css/scss/js/ios/android。
- 输出契约：CSS 输出 `:root` 变量文件，JS 输出 es6 常量（图表库等消费），两端永不手写颜色。
- 版本治理：token 变更走 code review，语义 token（text-primary）与原始 token（gray-500）分层，组件只允许用语义层。

```javascript
// build-tokens.js —— style-dictionary 的最小工作集
const StyleDictionary = require('style-dictionary');

StyleDictionary.extend({
  source: ['tokens/**/*.json'],   // token 单一来源
  platforms: {
    css: {
      transformGroup: 'css',      // 命名转换与值校验
      buildPath: 'dist/',
      files: [{
        destination: 'tokens.css',
        format: 'css/variables',
        options: { selector: ':root' },
      }],
    },
    js: {
      transformGroup: 'js',       // 供 JS 侧（图表库/Canvas）消费
      buildPath: 'dist/',
      files: [{ destination: 'tokens.js', format: 'javascript/es6' }],
    },
  },
}).buildAllPlatforms();

/* token 源文件结构（tokens/color.json）：
{
  "color": {
    "gray": { "500": { "value": "#6b7280" } },
    "brand": { "500": { "value": "#009966" } },
    "text": { "primary": { "value": "{color.gray.500}" } }  // 别名引用
  }
}
输出 dist/tokens.css：
:root { --color-brand-500: #009966; --color-text-primary: #6b7280; } */
```
