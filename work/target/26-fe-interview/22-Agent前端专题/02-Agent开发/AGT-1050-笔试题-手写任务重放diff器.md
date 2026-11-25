---
title: [1050] 笔试手写：实现重放结果与原 trace 的 diff 对比
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 多Agent, 调试]
type: 笔试题
---

## 1050：笔试手写：实现重放结果与原 trace 的 diff 对比

**答**：实现 diffTrace(origin, replay)：对比 { steps: [{ agent, action, output }] }。输出 { same: bool, diffs: [{ step, origin, replay }] }。对比规则：agent+action 序列必须一致（行为漂移）；output 用深度相等（对象递归比较，忽略字段 order），字符串输出做精确比较；长度不同直接 first-divergence（记录首个分歧步骤后停止）。

```js
function deepEq(a, b) {
  if (a === b) return true;
  if (typeof a !== typeof b) return false;
  if (Array.isArray(a)) return Array.isArray(b) && a.length === b.length
    && a.every((x, i) => deepEq(x, b[i]));
  if (a && typeof a === 'object') {
    const ka = Object.keys(a), kb = Object.keys(b);
    return ka.length === kb.length && ka.every(k => deepEq(a[k], b[k]));
  }
  return false;
}
function diffTrace(origin, replay) {
  const diffs = [];
  const n = Math.min(origin.steps.length, replay.steps.length);
  for (let i = 0; i < origin.steps.length; i++) {
    const o = origin.steps[i], r = replay.steps[i];
    if (!r || o.agent !== r.agent || o.action !== r.action ||
        !deepEq(o.output, r.output)) {
      diffs.push({ step: i, origin: o, replay: r ?? null });
      break;                                        // 首个分歧即停
    }
  }
  return { same: diffs.length === 0 && origin.steps.length === replay.steps.length,
    diffs };
}
```

**评分点**：
- 行为对比先比 agent+action 再比 output（行为漂移是最重要信号）
- deepEq 递归实现正确（键序无关、数组有序、NaN/undefined 边界可讨论）
- 首个分歧即停（输出根因而不是噪音列表），长度不等时 same 判 false
- 能讨论：字符串输出是否该用语义相似度而非精确比较（模型非确定性），精确比较适合编排逻辑验证、语义比较适合模型行为对比

