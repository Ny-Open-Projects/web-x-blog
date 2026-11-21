---
title: [JS-285] 笔试：手写 camelCase 转 kebab-case
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 正则]
type: 笔试题
---

## JS-285：笔试：camelCase 转 kebab-case

**题目**：实现 `camelToKebab(s)`：camelCase/PascalCase → kebab-case；处理连续大写（HTTPServer → http-server）、前导大写；`kebabToCamel` 反向。

**答**：
```javascript
function camelToKebab(s) {
  return s
    .replace(/([A-Z]+)([A-Z][a-z])/g, '$1-$2')   // 连续大写分界：HTTPServer → HTTP-Server
    .replace(/([a-z\d])([A-Z])/g, '$1-$2')        // 小写/数字 → 大写分界
    .toLowerCase();
}

function kebabToCamel(s) {
  return s.replace(/-([a-z])/g, (_, c) => c.toUpperCase());
}

camelToKebab('backgroundColor');   // 'background-color'
camelToKebab('HTTPServer');        // 'http-server'
camelToKebab('PascalCase');        // 'pascal-case'
camelToKebab('mp4Player');         // 'mp4-player'
kebabToCamel('background-color');  // 'backgroundColor'
```

**评分点**：
- 两步替换：先切连续大写（避免 HTTPServer 变 h-t-t-p…），再切普通边界——顺序是核心
- 数字与字母的边界处理（[a-z\d]）
- toLowerCase 的收尾位置
- 反向 kebabToCamel 的简单性对比
