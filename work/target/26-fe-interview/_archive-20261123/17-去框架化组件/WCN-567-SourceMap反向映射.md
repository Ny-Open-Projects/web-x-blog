---
title: [WCN-567] 编译产物的「Source Map 反向映射」：如何在 DevTools 里把 DOM 节点定位回源码模板行？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-567：编译产物的「Source Map 反向映射」：如何在 DevTools 里把 DOM 节点定位回源码模板行？

**答**：
- 结论：编译时给每个生成的 DOM 节点/插入锚点附加源码位置标记（data-s 属性或映射表），DevTools 插件据此反查。
- 映射表结构：产物节点 id → { file, line, column }；锚点也要记录，因为文本节点常被拆成锚点。
- 运行时注入 debug hook，点击元素时读取标记并高亮对应源码位置。
- 追问：压缩后位置偏移怎么办？（答：用 sourcemap 库做二次映射，从压缩位置还原到源码位置）

```javascript
function buildSourceMap(nodes) {
  const map = new Map();
  for (const n of nodes) map.set(n.id, { file: n.src.file, line: n.src.line, col: n.src.col });
  return map;
}
function locate(node, map) {
  const id = node.dataset?.sLoc;
  const pos = map.get(id);
  if (!pos) return null;
  return `${pos.file}:${pos.line}:${pos.col}`;        // DevTools 可点击跳转
}
```
