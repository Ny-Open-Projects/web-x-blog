---
title: [1278] 笔试手写：实现 多模型输出 diff 比对器
date: 2026-11-22
categories: [AI与Agent]
tags: [前端面试, 笔试题, 路由]
type: 笔试题
---

## 1278：笔试手写：实现 多模型输出 diff 比对器

**需求**：实现 diffOutputs(a, b)：两个模型对同一 prompt 的输出文本。按行 diff：输出 { same, aOnly, bOnly, both } 行集合（去除首尾空白后比较）；相似度 = same / max(lenA, lenB)；并标出首个分歧行号。返回 { similarity, firstDiverge, stats }。

```js
function diffOutputs(a, b) {
  const la = a.split('\n').map(s => s.trim()).filter(Boolean);
  const lb = b.split('\n').map(s => s.trim()).filter(Boolean);
  const sa = new Set(la), sb = new Set(lb);
  const same = la.filter(l => sb.has(l));
  const aOnly = la.filter(l => !sb.has(l));
  const bOnly = lb.filter(l => !sa.has(l));
  let firstDiverge = null;
  for (let i = 0; i < Math.max(la.length, lb.length); i++) {
    if ((la[i] ?? null) !== (lb[i] ?? null)) { firstDiverge = i + 1; break; }
  }
  const similarity = +(same.length / Math.max(la.length, lb.length, 1)).toFixed(3);
  return { similarity, firstDiverge, stats: { same: same.length, aOnly: aOnly.length, bOnly: bOnly.length } };
}
```

**评分点**：
- 行级集合 diff（Set 交集/差集）+ 逐行首分歧定位
- trim 后比较（空白噪声容忍）
- 相似度分母取 max 防长度不对称失真
- 能讨论：集合 diff 忽略行序——顺序敏感场景需 LCS 对齐（进阶）
