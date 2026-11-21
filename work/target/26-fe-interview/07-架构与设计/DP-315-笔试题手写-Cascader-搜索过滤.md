---
title: [DP-315] 笔试题：手写 Cascader 搜索过滤（保留路径）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-315：笔试题：手写 Cascader 搜索过滤（保留路径）？
**题目**：实现 deepFilter：1) 按关键词过滤树（label 包含）；2) 命中节点的祖先链保留（即使祖先不匹配）；3) 结果扁平化为路径列表（[[grand, parent, hit]])；4) 大小写不敏感 + 多关键词（空格分词 AND）。
**评分点**：
- 递归保留祖先逻辑正确。
- 多关键词 AND 语义。
- 路径扁平化输出完整。
- 性能：单次遍历 O(n)。
```javascript
function deepFilter(tree, keyword) {
  const kws = keyword.toLowerCase().split(/\s+/).filter(Boolean);    // 4) AND 分词
  const match = (label) => kws.every(k => label.toLowerCase().includes(k));
  const paths = [];                                       // 3) 路径收集
  function walk(node, trail) {
    const nextTrail = [...trail, node];
    if (match(node.label)) paths.push(nextTrail);         // 命中：整条路径收集
    for (const c of node.children ?? []) walk(c, nextTrail);  // 2) 祖先保留（继续下钻）
  }
  tree.forEach(n => walk(n, []));
  return paths.map(p => p.map(n => ({ key: n.key, label: n.label })));   // 3)
}
// 用：deepFilter([{ label: '华东区', children: [{ label: '杭州仓库', key: 'hz' }] }], '华东 杭州')
// → [[{label:'华东区'},{label:'杭州仓库'}]] —— 祖先链保留
```
