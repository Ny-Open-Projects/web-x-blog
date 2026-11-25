---
title: [WCN-773] 笔试：手写编译期的双向绑定宏展开器
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-773：笔试：手写编译期的双向绑定宏展开器

**答**：
- 需求：实现 `expandDefineModel(code)`，输入源码字符串含 `const NAME = defineModel('ARG')`（ARG 可省略，默认 'modelValue'），输出把该行替换为可写 computed 对象的代码：`const NAME = { get value(){ return __props.ARG }, set value(v){ __emit('update:ARG', v) } }`。要求支持多行、多个 defineModel；边界：无参默认、单引号/双引号。
- 要点：用正则匹配声明语句并捕获 NAME/ARG；构造替换字符串；逐行处理或全局 replace；ARG 缺省用 modelValue。

```javascript
function expandDefineModel(code) {
  const RE = /const\s+(\w+)\s*=\s*defineModel\(\s*(['"])([\w-]+)\2\s*\)/g;
  return code.replace(RE, (m, name, _q, arg) => {
    return `const ${name} = { get value(){ return __props.${arg} }, ` +
           `set value(v){ __emit('update:${arg}', v) } }`;
  }).replace(/const\s+(\w+)\s*=\s*defineModel\(\s*\)/g, (m, name) => {
    return `const ${name} = { get value(){ return __props.modelValue }, ` +
           `set value(v){ __emit('update:modelValue', v) } }`;
  });
}
const src = `
const count = defineModel('count');
const title = defineModel();
`;
console.log(expandDefineModel(src));
```

**评分点**：
- 正确匹配带参与无参 defineModel，ARG 默认 modelValue。
- 展开为 get/set 可写对象，读 props、写 emit update。
- 支持多个宏与多行源码（全局 replace）。
- 引号类型（单/双）兼容，正则边界严谨。
