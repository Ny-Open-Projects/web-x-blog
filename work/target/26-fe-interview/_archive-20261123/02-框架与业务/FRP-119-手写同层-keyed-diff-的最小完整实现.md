---
title: [FRP-119] 手写同层 keyed diff 的最小完整实现？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-119：手写同层 keyed diff 的最小完整实现？

**答**：
- 算法（Vue3/React 同源）：①处理**前置/后置相同**节点（key 相同直接 patch，缩小中间乱序区）；②中间区：新 children 建 `keyToNewIndexMap`；遍历旧中间节点——key 命中则 patch 并记录 newIndex，未命中 unmount；③新 children 中没被任何旧节点匹配的是**新增**，mount 并插入；④对匹配上的旧节点计算**最长递增子序列（LIS）**，LIS 内的节点 DOM 顺序不动，其余按新顺序**移动**（insertBefore）。
- 最小实现为控制篇幅可省 LIS，退化为"从后往前遍历 + insertBefore 锚点"（仍保证正确，只是移动次数非最优）；面试写完整时 LIS 是加分项。
- 核心不变量：**同层比较 + key 复用**——key 相同即同一节点（状态/DOM 都保留），绝不跨层比较（呼应 FRP-088 四种情况）。

```javascript
// 简化实现，帮助理解：同层 keyed diff（含 LIS 简化锚点版）
function diff(children1, children2, container) {
  let s1 = 0, s2 = 0;
  const e1 = children1.length - 1, e2 = children2.length - 1;
  // 1. 前置相同：直接 patch
  while (s1 <= e1 && s2 <= e2 && children1[s1].key === children2[s2].key) {
    children2[s2].el = children1[s1].el; s1++; s2++;
  }
  // 2. 后置相同：直接 patch
  while (s1 <= e1 && s2 <= e2 && children1[e1].key === children2[e2].key) {
    children2[e2].el = children1[e1].el; e1--; e2--;
  }
  // 3. 旧耗尽新有剩 -> 批量插入
  if (s1 > e1 && s2 <= e2) {
    for (let i = s2; i <= e2; i++) container.insertBefore(mount(children2[i]), container.firstChild);
    return;
  }
  // 4. 新耗尽旧有剩 -> 批量删除
  if (s2 > e2 && s1 <= e1) {
    for (let i = s1; i <= e1; i++) children1[i].el.remove();
    return;
  }
  // 5. 中间乱序：key -> 新 index
  const keyToNew = new Map();
  for (let i = s2; i <= e2; i++) keyToNew.set(children2[i].key, i);
  const matched = new Map(); // oldIndex -> newIndex
  for (let i = s1; i <= e1; i++) {
    const j = keyToNew.get(children1[i].key);
    if (j === undefined) children1[i].el.remove();      // 旧节点不再存在：删除
    else { children2[j].el = children1[i].el; matched.set(i, j); }
  }
  // 6. 新增 + 移动：从后往前，以"已就位"的下一个节点为锚 insertBefore
  let anchor = null;
  for (let j = e2; j >= s2; j--) {
    const hasOld = [...matched.values()].includes(j);
    if (!hasOld) {
      container.insertBefore(mount(children2[j]), anchor); // 新增
    } else {
      const el = children2[j].el;
      if (el.previousElementSibling !== (anchor ? anchor.previousElementSibling : null) && el !== anchor) {
        // 简化移动判定：不在锚前则移动（LIS 版在此用最长递增子序列跳过稳定节点）
        if (anchor) container.insertBefore(el, anchor);
      }
      anchor = el;
    }
  }
}
function mount(vnode) {
  const el = document.createElement(vnode.type);
  el.textContent = vnode.text ?? '';
  el.__key = vnode.key;
  return el;
}

// 验证：abc -> eabc（前插） -> ebd（删 a、改 c 为 d 的组合操作）
const container = document.createElement('div');
const mk = (key, text) => ({ key, type: 'li', text: text ?? key });
const v1 = [mk('a'), mk('b'), mk('c')];
v1.forEach((v) => container.appendChild(mount(v)));
diff(v1, [mk('e'), mk('a'), mk('b'), mk('c')], container);   // 前插 e
console.log([...container.children].map((el) => el.__key).join('')); // eabc
diff([mk('e'), mk('a'), mk('b'), mk('c')], [mk('e'), mk('b'), mk('d')], container);
console.log([...container.children].map((el) => el.__key).join('')); // ebd：a 删除、d 新增、b 保留
```
