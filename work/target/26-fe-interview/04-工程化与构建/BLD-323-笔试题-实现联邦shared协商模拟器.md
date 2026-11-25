---
title: [BLD-323] 笔试题——实现联邦 shared 协商模拟器（版本协商 + 双实例检测）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-323：手写联邦协商模拟

**需求与边界**：
- 需求：模拟模块联邦 shared 协商（SCN-BLD-256）——① 宿主与多个 remote 的 shared 清单合并（semver 最高版本优先——singleton 复用）；② requiredVersion 不满足时报错（strictVersion 语义）；③ 双实例检测（同包两个版本被实例化）；④ 协商结果报告（谁用了谁的实例）。
- 边界：① semver 满足判定（^/~ 区间）；② singleton 语义（单实例共享——多 remote 请求同包只实例化一次）；③ 非共享包独立实例（不参与协商）。

**答**：
```javascript
const semver = require('semver');
function negotiateShared(hostShared, remotes) {
  const usage = {};                                    // pkg → { version, provider, instances }
  const errors = [];
  // 合并所有声明：找满足全部 requiredVersion 的最高版本
  const demands = [];
  if (hostShared) demands.push({ from: 'host', spec: hostShared.requiredVersion, singleton: hostShared.singleton });
  for (const r of remotes) for (const [pkg, s] of Object.entries(r.shared ?? {}))
    demands.push({ from: r.name, pkg, spec: s.requiredVersion, singleton: s.singleton, available: s.version });
  for (const pkg of [...new Set(demands.map(d => d.pkg ?? 'react'))]) {
    const ds = demands.filter(d => d.pkg === pkg);
    const available = ds.filter(d => d.available).map(d => d.available);
    const chosen = available.sort(semver.rcompare)[0];  // 最高版本
    const unsatisfied = ds.filter(d => d.spec && !semver.satisfies(chosen, d.spec));
    if (unsatisfied.length)
      errors.push({ pkg, chosen, unsatisfied: unsatisfied.map(d => `${d.from} 要 ${d.spec}`) });   // strictVersion
    const singleton = ds.some(d => d.singleton);
    usage[pkg] = { version: chosen, instances: singleton ? 1 : ds.filter(d => d.available).length,
      providers: ds.map(d => d.from),
      risk: singleton && ds.length > 1 ? 'singleton-shared（单实例）' : 'multi-instance' };
  }
  const doubles = Object.entries(usage).filter(([p, u]) => u.instances > 1 && SINGLETON_RISK.includes(p));
  return { usage, errors, doubles: doubles.map(([p]) => p) };   // 双实例告警（SCN-BLD-256）
}
```

**评分点**:
- 最高版本协商 + semver 满足判定（strictVersion 报错）。
- singleton 语义（单实例复用）。
- 双实例检测（SINGLETON_RISK 包——SCN-BLD-216 hooks 风险）。
- 协商结果报告（谁用谁的实例——运行时可观测）。
