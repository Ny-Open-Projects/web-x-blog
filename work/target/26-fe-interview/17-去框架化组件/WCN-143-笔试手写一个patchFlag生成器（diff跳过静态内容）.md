---
title: [WCN-143] 笔试：手写 patchFlag 生成器（给动态 vnode 打位标记，diff 只查标记项）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 编译器方向]
type: 笔试题
---

## WCN-143：笔试：手写 patchFlag 生成器

**题目**：对 vnode 做 diff 前置优化：① 常量：TEXT=1, CLASS=2, STYLE=4, PROPS=8, FULL_PROPS=16；② `markFlag(vnode)` 分析 props 哪些是动态引用（`__dynamic: true` 的属性）生成 flag 与 `dynamicProps` 数组；③ `patch(old, new)` 按 flag 只比较对应内容：TEXT 只比 children 字符串、CLASS/STYLE 只比对应 props、PROPS 只比 dynamicProps 列出的键；④ FULL_PROPS 回退全量；⑤ 无 flag 的静态节点直接跳过。

**答**：

```javascript
export const PATCH = { TEXT: 1, CLASS: 2, STYLE: 4, PROPS: 8, FULL_PROPS: 16 };

export function markFlag(vnode) {
  const dynKeys = Object.entries(vnode.props ?? {})
    .filter(([, v]) => v && v.__dynamic).map(([k]) => k);
  if (!dynKeys.length && typeof vnode.children !== 'object' && !vnode.$$text) return vnode; // 静态
  let flag = 0;
  if (vnode.$$text) flag |= PATCH.TEXT;
  if (dynKeys.includes('class')) flag |= PATCH.CLASS;
  if (dynKeys.includes('style')) flag |= PATCH.STYLE;
  if (dynKeys.length) flag |= PATCH.PROPS;
  if (dynKeys.includes('key') || dynKeys.some((k) => !['class', 'style'].includes(k) && k !== 'key'))
    flag |= PATCH.FULL_PROPS;
  return { ...vnode, flag, dynamicProps: dynKeys };
}

export function patch(old, next) {
  if (old === next) return;
  const flag = next.flag ?? 0;
  if (flag === 0) return;                          // 静态：跳过
  if (flag & PATCH.TEXT) { if (old.children !== next.children) setText(old.el, next.children); }
  if (flag & PATCH.CLASS) { if (old.props.class !== next.props.class) setClass(old.el, next.props.class); }
  if (flag & PATCH.STYLE) { if (old.props.style !== next.props.style) setStyle(old.el, next.props.style); }
  if (flag & PATCH.PROPS) {
    const keys = (flag & PATCH.FULL_PROPS) ? Object.keys(next.props) : next.dynamicProps;
    for (const k of keys) if (old.props[k] !== next.props[k]) setProp(old.el, k, next.props[k]);
  }
}
// 口径：flag=TEXT|CLASS(3) → diff 只碰 children/class，其余 props 完全不比较
```

**评分点**：
- flag 位运算组合正确（TEXT/CLASS/STYLE/PROPS/FULL_PROPS）。
- dynamicProps 数组驱动"最小比较集"；FULL_PROPS 语义（包含 key 或未知 props 变化）。
- 静态节点短路（flag=0 return）。
- patch 分支按 flag 逐位检查（& 运算）。
