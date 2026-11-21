---
title: [HW-233] 手写一个 diff 视图渲染器：行级 diff 加行内 word diff 高亮
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-233：手写一个 diff 视图渲染器：行级 diff 加行内 word diff 高亮

**答**：
- 需求：实现 DiffView：diff(oldText, newText) 先做行级 LCS diff（added/removed/unchanged），对修改的行对再做空格分词级 diff 高亮；输出渲染行数组 [{type, oldLine?, newLine?, wordSegs?}]。
- 边界：空行处理；超大文件（> 5000 行）只 diff 可视区（简化：全量 LCS 备选 Myers O(ND)）；无变化输出 unchanged 不做行内 diff。
- 评分点：LCS 行级正确；行内二次 diff；复杂度意识。

```javascript
function lcsDiff(a, b) {                                      // 行级 LCS DP
  const n = a.length, m = b.length;
  const dp = Array.from({ length: n + 1 }, () => new Uint16Array(m + 1));
  for (let i = n - 1; i >= 0; i--)
    for (let j = m - 1; j >= 0; j--)
      dp[i][j] = a[i] === b[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
  const rows = []; let i = 0, j = 0;
  while (i < n && j < m) {
    if (a[i] === b[j]) rows.push({ type: 'unchanged', oldLine: a[i], newLine: b[j] }), i++, j++;
    else if (dp[i + 1][j] >= dp[i][j + 1]) rows.push({ type: 'removed', oldLine: a[i] }), i++;
    else rows.push({ type: 'added', newLine: b[j] }), j++;
  }
  while (i < n) rows.push({ type: 'removed', oldLine: a[i++] });
  while (j < m) rows.push({ type: 'added', newLine: b[j++] });
  return rows;
}
function diffView(oldText, newText) {
  const a = oldText.split('\n'), b = newText.split('\n');
  const rows = lcsDiff(a, b);
  return rows.map(r => {
    if (r.type !== 'unchanged') {
      const pair = rows.find(x => x.type !== r.type && Math.abs(rows.indexOf(x) - rows.indexOf(r)) <= 1);
      if (pair && r.oldLine != null && pair.newLine != null)
        r.wordSegs = wordDiff(r.oldLine, pair.newLine);        // 修改行对：行内 diff
    }
    return r;
  });
}
function wordDiff(s1, s2) {                                    // 空格分词级标记
  const w1 = s1.split(/(\s+)/), w2 = s2.split(/(\s+)/);
  const set = new Set(w2);
  return w1.map(w => ({ w, changed: !set.has(w) }));
}
```
