---
title: [TST-453] 笔试：OpenAPI 新旧版本的 breaking diff 分类器。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-453：笔试：OpenAPI 新旧版本的 breaking diff 分类器。
**答**：契约 `[{path, method, responses: {status: schema}}]` 与 body 必填字段集。分类：删接口/删必填响应状态/新增必填请求字段/删响应字段 = breaking；新增可选字段/新增响应字段 = compatible。输出分类清单。

```javascript
function contractDiff(oldC, nextC) {
  const key = c => `${c.method} ${c.path}`;
  const out = [];
  const oldM = new Map(oldC.map(c => [key(c), c]));
  const nextM = new Map(nextC.map(c => [key(c), c]));
  for (const [k, o] of oldM) if (!nextM.has(k)) out.push({ kind: 'breaking', why: `删除接口 ${k}` });
  for (const [k, n] of nextM) if (!oldM.has(k)) out.push({ kind: 'compatible', why: `新增接口 ${k}` });
  for (const [k, n] of nextM) {
    const o = oldM.get(k);
    if (!o) continue;
    for (const f of n.requiredBody || [])
      if (!(o.requiredBody || []).includes(f)) out.push({ kind: 'breaking', why: `${k} 新增必填字段 ${f}` });
    for (const f of Object.keys(o.responses['200'] || {}))
      if (!(n.responses['200'] || {})[f]) out.push({ kind: 'breaking', why: `${k} 删除响应字段 ${f}` });
    for (const f of Object.keys(n.responses['200'] || {}))
      if (!(o.responses['200'] || {})[f]) out.push({ kind: 'compatible', why: `${k} 新增响应字段 ${f}` });
  }
  return out;
}

```

**评分点**：
- 四类 breaking / 两类 compatible 判定齐全。
- 路径+方法联合键（同 path 不同 method 不混）。
- 输出每项带证据（哪个字段/状态码）。
- 新旧并集遍历（增删两侧）。
