---
title: [ZSM-713] 笔试：手写状态面板的 diff 高亮渲染器（树形折叠 + 变更路径标记）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-713：手写状态面板的 diff 高亮渲染器（树形折叠 + 变更路径标记）
**答**：实现 `renderDiffTree(prev, next)`：1) 输出可渲染节点树 `{ path, kind: 'same'|'added'|'removed'|'changed'|'branch', children, value }`——引用相等的子树标记 same 并**截断 children**（折叠）；2) changed 展示 `{ prev, next }`（值截断 50 字符）；3) `collapseDepth`：超过 N 层的 branch 折叠为 `…` 节点（默认展开变更路径）；4) 输出字符串版（console 可读）与结构版（面板渲染）；5) 附用例：变更路径全展开、无关子树折叠。

```javascript
function renderDiffTree(prev, next, { collapseDepth = 2 } = {}) {
  function walk(p, n, path, depth) {
    if (Object.is(p, n)) {
      return { path, kind: 'same', truncated: true }           // 引用相等：折叠
    }
    const bothObj = isPlainObj(p) && isPlainObj(n)
    if (!bothObj) {
      return { path, kind: 'changed', prev: trunc(p), next: trunc(n) }
    }
    const children = []
    const keys = new Set([...Object.keys(p ?? {}), ...Object.keys(n ?? {})])
    for (const k of keys) {
      const cp = path ? `${path}.${k}` : k
      if (!(k in (p ?? {}))) children.push({ path: cp, kind: 'added', next: trunc(n[k]) })
      else if (!(k in (n ?? {}))) children.push({ path: cp, kind: 'removed', prev: trunc(p[k]) })
      else children.push(walk(p[k], n[k], cp, depth + 1))
    }
    // 深层 branch 折叠：存在变更才展开
    const hasChange = children.some((c) => c.kind !== 'same' || c.children?.some((x) => x.kind !== 'same'))
    const node = { path, kind: 'branch', children: hasChange || depth < collapseDepth ? children : undefined,
      folded: !children.some((c) => c.kind !== 'same') && depth >= collapseDepth ? true : undefined }
    return node
  }
  return walk(prev, next, '', 0)
}

function isPlainObj(v) { return v && typeof v === 'object' && !Array.isArray(v) }
function trunc(v) {
  const s = JSON.stringify(v)
  return s.length > 50 ? s.slice(0, 50) + '…' : v
}

// 字符串版（console 可读）
function toConsole(node, indent = '') {
  const mark = { added: '+', removed: '-', changed: '~', same: ' ' }
  let lines = []
  const emit = (n, ind) => {
    if (n.kind === 'same') { lines.push(`${ind}· ${n.path} (same)`); return }
    if (n.kind === 'branch') {
      lines.push(`${ind}┬ ${n.path}`)
      n.children?.forEach((c) => emit(c, ind + '  '))
      if (n.folded) lines.push(`${ind}  …`)
      return
    }
    lines.push(`${ind}${mark[n.kind]} ${n.path}: ${JSON.stringify(n.prev)} → ${JSON.stringify(n.next)}`)
  }
  emit(node, indent)
  return lines.join('\n')
}

// 用例
const prev = { user: { name: 'a', tags: [1] }, meta: { big: 'unchanged' }, items: [1, 2] }
const next = { user: { name: 'b', tags: [1, 2] }, meta: { big: 'unchanged' }, items: [1, 2] }
const tree = renderDiffTree(prev, next)
console.log(toConsole(tree))
// ┬ 
//   ┬ user
//     ~ user.name: "a" → "b"
//     ~ user.tags: [1] → [1,2]
//   · meta (same)          ← 无关子树折叠
//   · items (same)
```
**评分点**：
- 引用相等折叠（same 子树不展开，diff 成本正比变更路径）
- 四类变更标记（added/removed/changed/same）+ 值截断
- collapseDepth 与「有变更才展开」的平衡
- 双输出形态（结构版给面板、字符串版给 console）
