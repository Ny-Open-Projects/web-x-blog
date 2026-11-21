---
title: [HW-043] 手写 diff（同层简单 diff）
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-043：手写 diff（同层简单 diff）

**答**：
- 评分点：虚拟 DOM 节点约定 `{ type, props, children }`；同层比较策略（React 经典策略）：只对比同一层级的节点，不跨层移动（跨层视为删除 + 新建）；节点 type 不同 → 直接 **REPLACE** 整棵子树（不再深入比较）；type 相同 → diff props（新增 / 删除 / 修改三类变化）+ 递归 diff children；children 用 **key** 匹配复用（说清无 key 按索引、有 key 按 key 对齐两种模式）；输出补丁对象 `{ type, patches }` 或直接返回操作列表，能说出 patch 应用顺序（先 props 后 children）。

```javascript
// ===== 5 分钟速写版 =====
// 节点：{ type, props, children }，children 为节点数组
function diff(oldNode, newNode) {
  const patches = [];
  if (!oldNode) { patches.push({ op: 'CREATE', node: newNode }); return patches; }
  if (!newNode) { patches.push({ op: 'REMOVE' }); return patches; }
  if (oldNode.type !== newNode.type) {                 // 类型不同：整棵替换，不再深入
    patches.push({ op: 'REPLACE', node: newNode });
    return patches;
  }
  // props diff
  const propsPatch = {};
  for (const k of Object.keys(newNode.props)) {
    if (oldNode.props[k] !== newNode.props[k]) propsPatch[k] = newNode.props[k];
  }
  for (const k of Object.keys(oldNode.props)) {
    if (!(k in newNode.props)) propsPatch[k] = undefined; // 删除的 prop
  }
  if (Object.keys(propsPatch).length) patches.push({ op: 'PROPS', value: propsPatch });
  // children diff（同层按索引对齐，简版无 key）
  const max = Math.max(oldNode.children.length, newNode.children.length);
  for (let i = 0; i < max; i++) {
    const childPatches = diff(oldNode.children[i], newNode.children[i]);
    patches.push(...childPatches.map(p => ({ ...p, index: i })));
  }
  return patches;
}

// ===== 标准完整版（含边界处理：children 按 key 匹配）=====
function diffPro(oldNode, newNode, path = '') {
  const patches = [];
  const at = p => (path ? `${path}.${p}` : String(p)); // 补丁路径：便于定位 DOM
  if (!oldNode) return [{ op: 'CREATE', node: newNode, path }];
  if (!newNode) return [{ op: 'REMOVE', path }];
  if (oldNode.type !== newNode.type) {
    return [{ op: 'REPLACE', node: newNode, path }];
  }
  if (oldNode.type === 'TEXT') { // 文本节点直接比内容
    if (oldNode.props.text !== newNode.props.text) {
      patches.push({ op: 'TEXT', value: newNode.props.text, path });
    }
    return patches;
  }
  const propsPatch = {};
  [...Object.keys(oldNode.props), ...Object.keys(newNode.props)].forEach(k => {
    if (oldNode.props[k] !== newNode.props[k]) propsPatch[k] = newNode.props[k];
  });
  if (Object.keys(propsPatch).length) patches.push({ op: 'PROPS', value: propsPatch, path });
  // children：有 key 时按 key 建索引匹配复用；无 key 退化为索引对齐
  const oldChildren = oldNode.children, newChildren = newNode.children;
  const oldKeyed = new Map(oldChildren.map((c, i) => [c.props.key ?? `idx-${i}`, { node: c, i }]));
  newChildren.forEach((nc, ni) => {
    const key = nc.props.key ?? `idx-${ni}`;
    const match = oldKeyed.get(key);
    if (match) {
      patches.push(...diffPro(match.node, nc, at(ni)));
      oldKeyed.delete(key); // 已复用
    } else {
      patches.push({ op: 'CREATE', node: nc, path: at(ni) }); // 新增
    }
  });
  // 剩下未被复用的旧节点全部删除
  oldKeyed.forEach(({ node, i }) => {
    patches.push({ op: 'REMOVE', path: at(i) });
  });
  return patches;
}
// 追问：
// 1. 为什么同层比较 —— 跨层移动在真实业务极少，O(n^3) 全树比较不可接受，React 用 O(n) 策略
// 2. key 的作用 —— children 对齐从索引变 key，避免相邻同类型节点状态错乱（列表插入场景）
// 3. 简版没有 MOVE 补丁，进阶可提 React 的双向遍历 / Vue3 最长递增子序列
```

---
