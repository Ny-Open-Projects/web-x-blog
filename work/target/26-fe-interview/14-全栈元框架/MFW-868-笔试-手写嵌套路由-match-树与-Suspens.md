---
title: [MFW-868] 笔试：手写嵌套路由 match 树与 Suspense 映射器
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-868：笔试：手写嵌套路由 match 树与 Suspense 映射器

**答**：
- 结论：把按嵌套顺序排列的 match 数组递归映射为 Suspense 树；每个 match 一个边界，pending 决定 fallback，子挂起不波及父。
- 关键：递归构造 child，末节点 child=null；空数组返回 null。
- 追问钩子：为什么每个路由单独边界？——实现局部降级，子路由慢不拖累父布局。

```javascript
function toSuspenseTree(matches) {
  const build = (i) => {
    if (i >= matches.length) return null;
    const m = matches[i];
    return {
      boundary: m.id,
      fallback: m.pending ? 'pending:' + m.id : null,
      content: m.component,
      child: build(i + 1)                            // 子路由嵌套
    };
  };
  return build(0);
}

// 自测
const matches = [
  { id: '/__root', component: 'Root', pending: false },
  { id: '/posts', component: 'Posts', pending: true },
  { id: '/posts/$id', component: 'Post', pending: false }
];
const tree = toSuspenseTree(matches);
console.log(tree.boundary === '/__root' && tree.child.boundary === '/posts'); // true
console.log(tree.child.fallback === 'pending:/posts');                        // true
```

**评分点**：
- 按嵌套顺序递归映射为树，child 指向下一层 match
- 每个 match 一个 Suspense 边界，pending 决定 fallback
- 子挂起只降级子区域，父保持；边界：空数组 / 末节点 child=null
- 能解释局部降级与整体降级的差异（加分）
