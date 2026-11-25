---
title: [WCN-937] 手写 token 版本对比工具：输出 added / removed / changed 与语义兼容性判定
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-937：手写 token 版本对比工具：输出 added / removed / changed 与语义兼容性判定

**题目**：实现 `diffTokens(oldTokens, newTokens)`，返回 `{ added:[], removed:[], changed:[{key,from,to}], breaking:[] }`。要求：① added 为新有旧无的 key，removed 为旧有新无的 key（均排序）；② changed 为两边都有但值不同的 key（含 from/to，排序）；③ breaking 判定：removed 的 key 或 changed 中「从语义 token（key 含语义段如 color/spacing）变成字面量」视为 breaking（简化：removed 全算 breaking，changed 中旧值以 `{` 开头且新值不是引用也算 breaking）；④ 输入非对象按空对象处理；⑤ 不修改输入。请自足实现并给出可运行示例。

**答**：

```javascript
function diffTokens(oldTokens, newTokens) {
  const o = (oldTokens && typeof oldTokens === 'object') ? oldTokens : {};
  const n = (newTokens && typeof newTokens === 'object') ? newTokens : {};
  const ok = Object.keys(o), nk = Object.keys(n);
  const added = nk.filter(k => !(k in o)).sort();
  const removed = ok.filter(k => !(k in n)).sort();
  const changed = ok.filter(k => k in n && JSON.stringify(o[k]) !== JSON.stringify(n[k]))
    .map(k => ({ key: k, from: o[k], to: n[k] })).sort((a, b) => a.key.localeCompare(b.key));
  const breaking = [
    ...removed.map(k => `removed: ${k}`),
    ...changed.filter(c => String(c.from).startsWith('{') && !String(c.to).startsWith('{'))
              .map(c => `de-aliased: ${c.key}`),
  ];
  return { added, removed, changed, breaking };
}
console.log(diffTokens(
  { 'color.link': '{blue}', gap: '8px', old: 'x' },
  { 'color.link': '#1677ff', gap: '8px', fresh: 'y' }
));
// added:['fresh'] removed:['old'] changed:[{key:'color.link',from:'{blue}',to:'#1677ff'}]
// breaking:['removed: old', 'de-aliased: color.link']
```

**评分点**：
- added/removed/changed 三类计算正确且排序。
- changed 保留 from/to，比较用深比较（避免引用误判）。
- breaking 判定逻辑正确（removed + 语义去别名）。
- 非对象输入健壮、不修改输入对象。
- 示例输出结构与 breaking 结果正确可运行。
