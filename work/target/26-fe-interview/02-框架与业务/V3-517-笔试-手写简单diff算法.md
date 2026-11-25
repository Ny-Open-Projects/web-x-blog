---
title: [V3-517] 笔试：手写简化版 diff（key 对齐 + 最小移动）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 编译器]
type: 笔试题
---

## V3-517：笔试：手写简化版 diff

**答**：实现 `diffChildren(oldV, newV, container)`：① 同头部/尾部预处理（头头相同/尾尾相同直接 patch）；② 中间乱序段：以新列表为基准建 key→index 映射；③ 旧列表中存在的新 key 复用（patch），不存在的新建，旧列表多余的卸载；④ 最长递增子序列（LIS）求「不需要移动」的节点，其余移动到正确位置；⑤ 无 key 列表退化为 index 对齐 patch。写出核心实现（LIS 可用简化 O(n²) 版）。

```javascript
function diffChildren(oldCh, newCh, container) {
  let s = 0, e1 = oldCh.length - 1, e2 = newCh.length - 1;
  // 1) 头头对齐
  while (s <= e1 && s <= e2 && same(oldCh[s], newCh[s])) { patch(oldCh[s], newCh[s]); s++; }
  // 2) 尾尾对齐
  while (s <= e1 && s <= e2 && same(oldCh[e1], newCh[e2])) { patch(oldCh[e1], newCh[e2]); e1--; e2--; }
  // 3) 旧遍历完 → 新增
  if (s > e1) { for (let i = s; i <= e2; i++) mount(newCh[i], container); return; }
  // 4) 新遍历完 → 卸载
  if (s > e2) { for (let i = s; i <= e1; i++) unmount(oldCh[i]); return; }
  // 5) 中间乱序: key 映射 + LIS
  const keyToNew = new Map(newCh.slice(s, e2 + 1).map((v, i) => [v.key, s + i]));
  const toMounted = [], source = [];   // source[i]: 新位置 i 对应旧位置(-1=需新建)
  const oldKeyIdx = new Map(oldCh.slice(s, e1 + 1).map((v, i) => [v.key, s + i]));
  for (let i = s; i <= e2; i++) {
    const oi = oldKeyIdx.get(newCh[i].key);
    if (oi == null) toMounted.push(i);
    source[i] = oi ?? -1;
    if (oi != null) patch(oldCh[oi], newCh[i]);
  }
  for (let i = s; i <= e1; i++) if (!keyToNew.has(oldCh[i].key)) unmount(oldCh[i]);
  const lis = lisOf(source.filter(x => x >= 0));        // 不需移动的序列
  const stable = new Set(lis);
  // 从后向前插入保证顺序
  let anchor = e2 + 1 < newCh.length ? newCh[e2 + 1].el : null;
  for (let i = e2; i >= s; i--) {
    if (toMounted.includes(i)) { mount(newCh[i], container, anchor); anchor = newCh[i].el; }
    else if (!stable.has(source[i])) { insert(newCh[i].el, container, anchor); anchor = newCh[i].el; }
    else anchor = newCh[i].el;
  }
}
function lisOf(arr) { /* O(n²) DP 求 LIS 索引 */ }
```

**评分点**：
- 头尾预处理减少乱序段（高频优化点）
- key 映射复用 + 新建/卸载分类
- LIS 判定「不移动集合」，从前向后锚点插入
- 无 key 与边界（空列表/全增/全删）退化处理
