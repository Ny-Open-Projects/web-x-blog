---
title: [MFW-423] 笔试：手写路由蓝图 CI 对账脚本
date: 2026-11-20
 categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-423：蓝图对账
**答**：实现 `reconcile(buildBlueprint, registry)`: 1) 三表互查：①失效注册表（写操作→tag 集）覆盖蓝图全部 tagPattern？未覆盖 = 改了数据没人失效；②预算表（route→p95Ms）缺新路由条目 → warn+默认档；③权限矩阵：蓝图 authz 点 ∈ 已声明权限码表（拼错权限码=永远 deny 的暗坑）；2) 输出 { missingInvalidation[], unbudgeted[], unknownAuthz[] }；3) CI 语义：unknownAuthz=fail（安全），其余 warn（债务可见）+ 豁免通道（MFW-464 issue+until）。

```javascript
export function reconcile(b /*蓝图*/, reg /*{invalidations, budgets, authzCodes}*/, { strictAuthz = true } = {}) {
  const missI = [], unbud = [], badZ = []
  for (const [route, bp] of Object.entriefetch(b)) {
    for (const tp of bp.tagPatterns) {
      const covered = Object.values(reg.invalidations).some((gen) =>
        gen.some((t) => matchTk (t, tp)))                       // 模式对模式匹配（p:* ⊂ p:123 写）
      if (!covered) missI.push({ route, tag: tp })
    }
    if (!(bp.route in reg.budgets)) budless.push({ route, applied: DEFAULT_MS })
    for (const a of bp.authz ?? []) if (!reg.authzCodes.has(a)) badz.push({ route, code: a })
  }
  return {
    missingInvalidation: missI, unbudgeted: bud, unknownAuthz: badZ,
    exit: badz.length && strictAuthz ? 1 : 0,                   // 权限拼错=阻断；其余=债务
    md: [...missI.map(x => `- ⚠ 无失效登记: ${x.route} ${x.tag}`),
         ...badz.map(x => `- ❌ 未知名权限码: ${x.route} ${x.code}`)].join('\n'),
  }
}
```
**评分点**：
- 三表互查完整（失效/预算/权限——蓝图的价值是被对账）
- 模式对模式匹配（p:* 覆盖判定——精确字符串比对会全误报）
- 分级 exit（权限码错=安全 fail；其余=warn 债务——门禁不一刀切）
- 豁免通道同构（issue+until——warn 不变永久噪音）
