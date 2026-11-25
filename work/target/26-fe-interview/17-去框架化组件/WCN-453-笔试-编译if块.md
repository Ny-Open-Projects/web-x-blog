---
title: [WCN-453] 笔试：实现条件块的编译产物（anchor 注释节点 + 条件切换）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-453：笔试：实现条件块的编译产物（anchor 注释节点 + 条件切换）。
**答**：输入 `{cond, then: node, else: node}`。产物：anchor 占位（注释节点），effect 切换：真渲染 then 假渲染 else（重建/复用按简化选择，说明取舍）。

```javascript
function compileIf({ cond, then, otherwise }) {
  return `
const anchor = document.createComment('if');
parent.insertBefore(anchor, null);
createEffect(() => {
  const keep = anchor.__keep;
  if (keep) { keep.remove(); anchor.__keep = null; }   // 切走先清理
  anchor.__keep = ${cond} ? renderNode(${JSON.stringify(then)}) : ${otherwise} ? renderNode(${JSON.stringify(otherwise)}) : null;
  if (anchor.__keep) anchor.before(anchor.__keep);
});`;
}
// 简化：每次切换重建（真实编译器会缓存分支并做 unmount 协议）

```

**评分点**：
- anchor 注释节点定位（DOM 插入锚点）。
- 条件 effect：切换渲染分支。
- 销毁清理（切走时调用 unmount）。
- 复用 vs 重建取舍说明（缓存代价）。
