---
title: [FRP-293] 笔试：手写迷你自定义 reconciler host（渲染到终端文本）
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-293：笔试：手写迷你自定义 reconciler host
**答**：不用 react-reconciler，手写最小 host 抽象：实现 `{ createInstance(type, props), appendChild(parent, child), commitUpdate(inst, newProps), removeChild }` 接到「终端输出」——instance 输出 `[type]props` 文本，commit 时重打整行；说明与 DOM host 的接口对应关系。

```javascript
const terminalHost = {
  createInstance(type, props) {
    return { type, props, text: `[${type}]${JSON.stringify(props)}` }
  },
  appendChild(parent, child) {
    parent.children ||= []
    parent.children.push(child)
    child.parent = parent
  },
  commitUpdate(inst, newProps) {
    inst.props = newProps
    inst.text = `[${inst.type}]${JSON.stringify(newProps)}`
  },
  removeChild(parent, child) {
    parent.children = parent.children.filter(c => c !== child)
  },
  render(root) {
    const lines = []
    ;(function walk(node, depth) {
      lines.push('  '.repeat(depth) + node.text)
      node.children?.forEach(c => walk(c, depth + 1))
    })(root, 0)
    console.log(lines.join('\n')) // flush 到终端
  }
}
// 与 DOM host 对应：createElement/appendChild/setAttribute/remove/removeChild
```
**评分点**：
- host 接口与 DOM API 一一对应（核心抽象）。
- commitUpdate 增量更新语义（不重建整树）。
- 树遍历 flush 输出。
- 能举真实案例（ink/react-three-fiber）说明此抽象的复用价值。
