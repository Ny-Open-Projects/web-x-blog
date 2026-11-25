---
title: [960] 笔试手写：实现稳定分流（同 UID 恒定命中同桶）
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 评测, 分流]
type: 笔试题
---

## 960：笔试手写：实现稳定分流（同 UID 恒定命中同桶）

**答**：实现 bucket(uid, salt, total=100)：对 uid+salt 做稳定哈希映射到 0..total-1；同一 uid 多次调用结果一致；不同 salt 分布均匀（可讨论）。再实现 assign(uid, experiment)：experiment = { salt, groups: [{name, weight}] }（weight 之和不必为 100，按比例），返回组名。

```js
function hash(str) {              // FNV-1a 32bit，稳定无依赖
  let h = 2166136261;
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}
function bucket(uid, salt, total = 100) {
  return hash(uid + '|' + salt) % total;
}
function assign(uid, exp) {
  const total = exp.groups.reduce((s, g) => s + g.weight, 0);
  const b = bucket(uid, exp.salt, total);        // 哈希到 weight 总空间
  let acc = 0;
  for (const g of exp.groups) {
    acc += g.weight;
    if (b < acc) return g.name;
  }
  return exp.groups.at(-1).name;                  // 浮点兜底
}
console.log(assign('u1', { salt: 'exp1',
  groups: [{ name: 'control', weight: 90 }, { name: 'treat', weight: 10 }] }));
```

**评分点**：
- 稳定性：哈希入参包含 salt，同 uid 同 salt 恒定命中（无随机数）
- 按权重比例分流且 weight 不必归一化 100
- FNV/简单哈希实现正确（Math.imul 防 32 位溢出）
- 边界讨论：换 salt 等于重新洗牌全量用户、分组权重变化会导致部分用户换组（可讨论方案：分桶复用）

