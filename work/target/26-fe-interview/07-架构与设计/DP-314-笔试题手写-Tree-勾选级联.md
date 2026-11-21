---
title: [DP-314] 笔试题：手写 Tree 勾选级联（半选状态）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-314：笔试题：手写 Tree 勾选级联（半选状态）？
**题目**：实现树勾选：1) 勾选父级 → 全部子孙勾选；2) 子级部分勾选 → 父级半选（indeterminate）；3) checkedKeys 受控输出；4) 禁用节点不参与级联但参与展示。
**评分点**：
- 向下级联递归正确。
- 向上汇总正确（全选/半选/未选三态）。
- 禁用节点跳过级联。
- 输出仅含"完全勾选"节点。
```javascript
function treeCheck(tree, checked, disabled = new Set()) {
  const checkMap = new Map(checked.map(k => [k, true]));
  const toggle = (node, val) => {
    if (disabled.has(node.key)) return;                     // 4) 禁用不级联
    checkMap.set(node.key, val);
    (node.children ?? []).forEach(c => toggle(c, val));     // 1) 向下
  };
  const statusOf = (node) => {                              // 2) 向上
    if (disabled.has(node.key)) return { checked: checkMap.has(node.key), indeterminate: false };
    if (!node.children?.length) return { checked: checkMap.has(node.key), indeterminate: false };
    let all = true, some = false;
    for (const c of node.children) {
      const s = statusOf(c);
      all = all && (s.checked && !s.indeterminate);
      some = some || s.checked || s.indeterminate;
    }
    if (all) checkMap.set(node.key, true);
    return { checked: all, indeterminate: !all && some };   // 半选
  };
  tree.forEach(statusOf);
  const checkedKeys = [...checkMap.entries()].filter(([, v]) => v).map(([k]) => k);   // 3)
  return { checkedKeys, statusOf };
}
```
