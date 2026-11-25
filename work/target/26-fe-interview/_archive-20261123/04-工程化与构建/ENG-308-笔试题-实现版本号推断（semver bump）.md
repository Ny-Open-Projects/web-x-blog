---
title: [ENG-308] 笔试题——实现版本号推断（API diff → semver bump）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-308：手写 semver bump 推断

**需求与边界**：
- 需求：对比新旧 API 报告（导出符号签名集），推断版本 bump——删除/签名不兼容的导出 = major；新增导出/参数加可选 = minor；其余 = patch；无 API 变化跳过发布。
- 边界：① 函数参数位置变化视为不兼容（major）；② 泛型/类型导出变化计入；③ bump 结果与 changeset 声明交叉校验（不一致告警）。

**答**：
```javascript
function inferBump(oldApi, newApi, declared) {
  const removed = [...oldApi.keys()].filter(k => !newApi.has(k));
  const added = [...newApi.keys()].filter(k => !oldApi.has(k));
  let bump = 'patch';
  const breaking = [];
  for (const k of [...oldApi.keys()].filter(k => newApi.has(k))) {
    const diff = signatureDiff(oldApi.get(k), newApi.get(k));
    if (diff.incompatible) {                          // 参数位置变化/必选参数新增/类型收窄
      bump = 'major'; breaking.push({ symbol: k, ...diff });
    } else if (diff.optionalAdded || added.length) bump = Math.max(bump, 'minor');
  }
  if (removed.length) { bump = 'major'; breaking.push({ removed }); }
  if (!removed.length && !added.length && !breaking.length && !declared)
    return { skip: true };                            // 无 API 变化跳过发布
  if (declared && RANK[declared] < RANK[bump])
    warn(`changeset 声明 ${declared} 低于 API 推断 ${bump}，以 ${bump} 为准`);
  return { bump: RANK[bump] >= 2 ? 'major' : bump, breaking };
}
const RANK = { patch: 0, minor: 1, major: 2 };
function signatureDiff(a, b) {
  return {
    incompatible: a.params.slice(0, b.requiredParams).join() !== b.params.slice(0, a.requiredParams).join()
      || a.requiredParams > b.requiredParams,
    optionalAdded: b.requiredParams < a.requiredParams,
  };
}
```

**评分点**:
- API diff 判定 bump（删除/不兼容签名 → major）。
- 参数位置/必选参数变化 = 不兼容（细节决定正确性）。
- 与 changeset 声明交叉校验（ENG-204 联动）。
- 无变化 skip 发布（噪声发版治理）。
