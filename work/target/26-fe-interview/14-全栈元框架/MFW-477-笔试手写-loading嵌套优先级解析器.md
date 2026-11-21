---
title: [MFW-477] 笔试：手写 loading 嵌套优先级解析器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-477：loading.js 嵌套优先级解析器
**需求**：实现 `pickLoadingFallback(route, segments)`：1) segments 为路径各层是否定义 loading.js：['app', 'app/blog', 'app/blog/[slug]']；2) 导航到 route 时选**最浅**的已定义 loading 边界显示（父级 loading 包裹整个子树——嵌套流式语义）；3) 若 route 自身层有 loading 则精确显示自身（就近优先）；4) 返回 { slot, depth }；无任何 loading 时返回 null（整页等待）——并给出该情况下建议（在中间层补 loading）。

```javascript
export function pickLoadingFallback(route, segments) {
  const defs = new Set(segments) // 定义了 loading.js 的层级路径
  const parts = route.split('/').filter(Boolean)
  // 从最浅层往下找第一个有 loading 的祖先
  for (let i = 0; i <= parts.length; i++) {
    const prefix = '/' + parts.slice(0, i).join('/')
    if (defs.has(prefix)) {
      return { slot: prefix, depth: i, exact: i === parts.length }
    }
  }
  // 全链无 loading：整页阻塞
  return {
    slot: null, depth: -1,
    hint: `no loading.js on chain; add one at '/${parts[Math.floor(parts.length / 2)] ?? ''}' or root`,
  }
}
```

**评分点**：
- 最浅祖先优先（父 loading 包住子树——不是就近优先的常见误区，题设明确先浅后自身）
- exact 标记自身层命中（方便区分"精确边界"与"包裹边界"）
- 无边界返回 null + 补点建议（架构工具应给出修复路径）
- 路径分段循环 O(depth)（嵌套深度有限，无需正则）
