---
title: [WCN-942] 编译式模板运行时报错怎么还原到模板源码位置：generated→template span 映射表
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-942：编译式模板运行时报错怎么还原到模板源码位置：generated→template span 映射表

**答**：
- 结论先行：编译式模板（如把 `<div>{user.name}</div>` 编译成 JS）运行时错误栈指向生成 JS，要让开发者看到「模板第几行的 user.name 出错」，需要维护「生成代码位置 → 模板源码 span（起止行列）」的映射表。
- 做法：编译器在每个生成表达式处记录对应模板节点的位置区间，产出 `templateMap`（类似 source map 但粒度到模板片段）；运行时错误拦截器拿生成行列查表回填模板片段。
- 与普通 source map 的区别：普通 map 映射到「源文件」，这里映射到「模板里的片段」，因为模板往往是字符串/内联，不是真实文件。
- 开源实践：Solid/Vue 编译器生成代码时带 `/*#__PURE__*/` 与位置注释，dev 模式保留映射，prod 模式剥离以省体积。
- 追问钩子：面试官问「内联模板字符串没有文件名怎么办」——答：给模板起虚拟文件名（组件名 + hash），映射表里带上，错误面板显示虚拟名 + 片段高亮。

```javascript
// 编译器产出模板 span 映射（生成位置 -> 模板片段）
const templateMap = [
  { genLine: 12, tpl: { file: 'Card.tmpl', start: [3, 8], end: [3, 20], text: 'user.name' } },
];
function locate(genLine, genCol) {
  const seg = templateMap.find(m => m.genLine === genLine);
  return seg ? `模板 ${seg.tpl.file}:${seg.tpl.start[0]}:${seg.tpl.start[1]} → ${seg.tpl.text}`
             : '未知模板位置';
}
// 运行时错误拦截：把生成栈行号还原为模板片段
try { user.name.first; } catch (e) { console.log(locate(12, 4)); }
// 模板 Card.tmpl:3:8 → user.name
```
