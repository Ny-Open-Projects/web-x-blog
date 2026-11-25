---
title: [WCN-862] 领域特定语言（DSL）编译器设计：以「列表渲染 DSL」为例？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-862：领域特定语言（DSL）编译器设计：以「列表渲染 DSL」为例？

**答**：
- 结论先行：DSL 编译器要先明确「DSL 的表达边界」——列表渲染 DSL 只需描述「遍历什么、每项怎么渲染、key 是什么、空态/加载态」，刻意不做通用计算，换取简单、安全、可静态分析。
- 设计步骤：① 定义语法（ JSON schema 或类模板语句，如 `for item in items key item.id { ... }`）；② 词法/语法分析成 AST；③ 语义分析（作用域、key 唯一性、依赖收集）；④ 降级到 IR（For 节点 + keyed diff 信息）；⑤ 后端生成目标代码（keyed 列表的增删移动最小化更新）。
- 关键编译产物：把列表更新编译成「按 key 的增量 diff」——生成带 key 的 block 树，运行时只做增删移动，不做全量重建；空态/加载态编译成条件块。
- 安全与约束：DSL 限制只能用白名单表达式（不能执行任意 JS），天然防注入；key 必须来自数据字段，编译期校验存在性。
- 取舍：DSL 比通用语言模板简单安全，但表达力有限——复杂逻辑要提供「逃逸舱」（回调/自定义指令），否则开发者会绕开 DSL。
- 追问钩子：面试官会问「DSL 和通用模板引擎怎么选」——答：业务规则固定、需要非程序员可写、强调安全时用 DSL；需要图灵完备灵活性的用通用模板；很多方案是「DSL 为主 + 表达式子集」的混合。

```javascript
// 极简列表 DSL 编译：for 语句 → keyed diff 渲染函数
const dsl = `for item in items key item.id { text item.name }`;
function parse(src) {
  const m = src.match(/for\s+(\w+)\s+in\s+(\w+)\s+key\s+([\w.]+)\s+\{\s*text\s+([\w.]+)\s*\}/);
  if (!m) throw new Error('DSL 语法错误');
  return { item: m[1], list: m[2], key: m[3], text: m[4] };
}
function compile(src) {
  const ast = parse(src);
  // 生成 keyed diff 的渲染函数（示意）
  return `
function render(host, ${ast.list}) {
  const keyOf = (${ast.item}) => ${ast.key};
  return keyedDiff(host, ${ast.list}, keyOf, (${ast.item}, el) => setText(el, ${ast.text}));
}`;
}
console.log(compile(dsl));
```
