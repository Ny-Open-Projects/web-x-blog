---
title: [PER-631] npm audit 报告几十条怎么处理？手写一个漏洞分诊器：按可达性分诊而不是按等级盲修
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-631：npm audit 报告几十条怎么处理？手写一个漏洞分诊器：按可达性分诊而不是按等级盲修

**答**：
- 盲按等级修的问题是：critical 但漏洞路径在 devDependency 里（构建工具漏洞，不进产物）实际不可达；间接依赖的升级又可能破坏构建。正确姿势是**可达性分诊**：漏洞包是否出现在产物依赖树（bundledDependencies/import 链）里。
- 分诊规则：direct 依赖且可无破坏升级 -> 直接升；间接依赖 -> `npm ls` 看谁引入，用 overrides/resolutions 强制版本；dev-only -> 排期不紧急；无可修复版本 -> 替代包或缓解措施（CSP 收敛其外联）。
- 要点：分诊结果要落成处置表"（包、等级、可达性、动作、owner、期限），进周会跟踪；CI 对新增 high 可达漏洞阻断。
- 评分点：devDependency 与产物依赖树区分。

```javascript

const { execSync } = require('child_process');
function triageAudit(auditJson, bundleDeps) {
  const { vulnerabilities } = JSON.parse(auditJson);
  return Object.entries(vulnerabilities).map(([pkg, v]) => {
    const inBundle = bundleDeps.has(pkg) || v.direct;     // 是否可达产物
    const devOnly = v.dev;
    let action;
    if (inBundle && v.fixAvailable) action = `立即升级: npm update ${pkg}`;
    else if (inBundle && !v.fixAvailable) action = '无修复版 -> 找替代包或 CSP 收敛外联';
    else if (devOnly) action = 'dev-only 不可达 -> 排期处理，不阻塞';
    else action = `间接依赖 -> overrides 强制: ${v.fixAvailable?.version ?? '人工评估'}`;
    return { pkg, severity: v.severity, reachable: inBundle || devOnly ? 'no-bundle' : 'yes',
      via: (v.via ?? []).map(x => typeof x === 'string' ? x : x.title).slice(0, 2), action };
  }).sort((a, b) => (a.reachable === 'yes') - (b.reachable === 'yes'));
}
// bundleDeps 来自构建统计（webpack stats modules 里出现过的 node_modules 包）
```
