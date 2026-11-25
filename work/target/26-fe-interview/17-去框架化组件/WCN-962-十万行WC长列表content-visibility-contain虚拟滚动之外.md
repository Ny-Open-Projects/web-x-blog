---
title: [WCN-962] 十万行长列表 WC 渲染：虚拟滚动之外的内容可见性优化
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-962：十万行长列表 WC 渲染：虚拟滚动之外的内容可见性优化

**答**：
- 结论先行：虚拟滚动解决「DOM 节点数」，但 10w 行即使只渲染窗口内几十个，列表容器布局/绘制仍可能昂贵；叠用 `content-visibility:auto` + `contain` 让浏览器跳过屏幕外子树的布局与绘制。
- content-visibility:auto 配合 `contain-intrinsic-size` 给未渲染行一个占位高度，避免滚动条跳动；与虚拟窗口互补而非替代。
- contain:layout paint style 隔离每行的布局影响域，一行变化不触发整列表重排（大促商品列表常见）。
- 内存治理：WC 实例不要对每个数据行都创建——用「节点池 + 数据绑定」复用 DOM 节点，配合 WeakMap 存状态，避免 10w 个实例常驻。
- 追问钩子：面试官问「content-visibility 会影响可访问性/查找吗」——答：屏幕外内容仍在无障碍树但可能被跳过，且 Ctrl+F 找不到；关键内容（如含表单的行）要显式 `content-visibility:visible`。

```javascript
// 行样式：内容可见性 + 布局隔离
const rowCSS = `
.row {
  content-visibility: auto;          /* 屏幕外跳过布局/绘制 */
  contain-intrinsic-size: auto 64px; /* 占位高度，防滚动跳动 */
  contain: layout paint style;       /* 隔离影响域 */
}
.row interactive { content-visibility: visible; } /* 含交互的行强制渲染 */
`;
// 节点池：复用 DOM 而非每行建 WC 实例
const pool = [];
function renderRows(data) {
  data.forEach((d, i) => {
    const el = pool[i] || (pool[i] = document.createElement('div'));
    el.className = 'row'; el.textContent = d.name; // 绑定数据，节点复用
  });
}
```
