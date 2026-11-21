---
title: [RBL-485] 笔试：手写产物 treemap 渲染数据
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-485：手写产物 treemap 渲染数据
**需求**：实现 `buildTreemap(modules)`：1) 输入模块列表（路径/体积）；2) 层级树：按路径段聚合（node_modules/lodash → 节点）；3) squarified treemap 布局算法（面积 ∝ 体积，宽高比优化——简化版 slice-and-dice 也接受但标注）；4) 输出可直接渲染的矩形列表 { x, y, w, h, name, size, depth }；5) 交互数据：点击节点下钻（子矩形查询）；6) 大数据优化：深度限制（>5 层聚合为 other——渲染性能）。

```javascript
export function buildTreemap(modules, { width = 800, height = 600, maxDepth = 5 } = {}) {
  // 1. 层级树
  const root = { name: 'root', children: {}, size: 0 }
  for (const m of modules) {
    const parts = m.name.split('/').slice(0, maxDepth)
    let node = root
    for (const part of parts) {
      node.children[part] ??= { name: part, children: {}, size: 0 }
      node = node.children[part]
    }
    node.size += m.size                                          // 叶子累积
  }
  // 自底向上汇总
  function sumUp(node) {
    const childSum = Object.values(node.children).reduce((s, c) => s + sumUp(c), 0)
    node.size = node.children && Object.keys(node.children).length ? childSum : node.size
    return node.size
  }
  sumUp(root)

  // 2. slice-and-dice 布局（简化——squarified 需按短边排列优化宽高比）
  const rects = []
  function layout(node, x, y, w, h, depth) {
    const isLeaf = !Object.keys(node.children).length
    if (isLeaf) { rects.push({ x, y, w, h, name: node.name, size: node.size, depth }); return }
    let offset = 0
    const total = node.size || 1
    const horizontal = w >= h
    for (const child of Object.values(node.children)) {
      const ratio = child.size / total
      if (horizontal) {
        const cw = w * ratio
        layout(child, x + offset, y, cw, h, depth + 1)
        offset += cw
      } else {
        const ch = h * ratio
        layout(child, x, y + offset, w, ch, depth + 1)
        offset += ch
      }
    }
  }
  layout(root, 0, 0, width, height, 0)
  return { rects, root }
}

// 用途：bundle analyzer 可视化数据——面积 ∝ 体积，点击下钻
```
**评分点**：
- 层级树构建（路径段聚合 + 叶子累积 + 自底向上汇总）
- 布局算法（slice-and-dice 实现；诚实标注简化——squarified 宽高比优化为进阶）
- 面积 ∝ 体积的语义（treemap 的核心正确性）
- 深度限制（渲染性能保护）
