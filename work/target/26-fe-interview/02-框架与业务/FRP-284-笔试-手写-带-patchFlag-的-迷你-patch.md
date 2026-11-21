---
title: [FRP-284] 笔试：手写带 patchFlag 的迷你 patch（只比动态点）
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-284：笔试：手写带 patchFlag 的迷你 patch
**题**：vnode 结构 `{ tag, props, children, flag, dynamicChildren }`；实现 `patchVnode(n1, n2)`：flag=TEXT 只比文本；flag=CLASS 只比 class；有 dynamicChildren 时只遍历动态点（跳过 children 全量 diff）；无 flag 走全量。

```javascript
const PatchFlags = { TEXT: 1, CLASS: 2, DYNAMIC: 8 }
function patchVnode(n1, n2) {
  const el = (n2.el = n1.el)
  if (n2.flag & PatchFlags.TEXT) {
    if (n1.children !== n2.children) el.textContent = n2.children
    return
  }
  if (n2.flag & PatchFlags.CLASS) {
    if (n1.props?.class !== n2.props?.class) el.className = n2.props.class ?? ''
    return
  }
  if (n2.dynamicChildren) {           // 编译优化：定点更新
    n2.dynamicChildren.forEach((c, i) => patchVnode(n1.dynamicChildren[i], c))
    return
  }
  patchProps(el, n1.props, n2.props)  // 全量兜底
  patchChildren(el, n1.children, n2.children)
}
```
**评分点**：
- flag 位与分流，TEXT/CLASS 快速路径。
- dynamicChildren 定点遍历（对应 block tree）。
- flag 与 dynamicChildren 互斥关系（叶子用 flag、容器用 dynamicChildren）。
- 无信息时全量兜底保证正确。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-fbcf8f8f-b342-4c77-ac0b-fbd56c2b26f3-cwd'; fi
exit "$__zcode_status"
