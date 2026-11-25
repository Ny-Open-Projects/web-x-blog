---
title: [NODE-841] 笔试题——实现服务端降级矩阵执行器（L1-L4 联动熔断）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-841：手写降级矩阵

**需求与边界**：
- 需求：服务端降级矩阵（SCN-OPS-329 服务端版）——① 档位继承（L1-L4 动作累积——SCN-OPS-329）；② 熔断自动触发升档（SCN-NODE-669 联动）；③ 只升不降 + 显式 rollback（SCN-OPS-329）；④ 配置签名校验（SCN-OPS-229）。
- 边界：① 升档时熔断器的联动（自动触发降级——SCN-NODE-669 open 事件）；② 降档恢复（显式 rollback——SCN-OPS-329）；③ 档位与演练绑定（未演练档位告警——SCN-861）。

**答**：
```javascript
function degradeExecutor(matrix) {
  let level = 'L0';
  breaker.on('open', ({ target }) => {                 // 熔断自动升档（SCN-NODE-669 联动）
    const auto = matrix.autoRules[target];
    if (auto) apply(auto.level, { source: 'auto-breaker' });
  });
  function apply(next, { source, signature, rollback = false } = {}) {
    if (!verifySig(signature)) return { rejected: 'BAD_SIGNATURE' };   // 签名（SCN-OPS-229）
    if (rank(next) < rank(level) && !rollback)
      return { rejected: 'ONLY_EXPLICIT_ROLLBACK' };   // 只升不降（SCN-OPS-329）
    const prev = level; level = next;
    for (const action of matrix[next] ?? []) execute(action);   // 档位继承（累积——SCN-OPS-329）
    audit({ next, prev, source });                     // 审计（SCN-OPS-219）
    if (matrix[next]?.notDrilled) warn(`${next} 未演练（SCN-861）`);   // 演练绑定
    return { applied: next, prev };
  }
}
```

**评分点**:
- 熔断自动升档（breaker open 事件联动——SCN-NODE-669）。
- 档位继承累积 + 只升不降 + 显式 rollback（SCN-OPS-329）。
- 签名校验 + 审计（SCN-OPS-229/219）。
- 未演练档位告警（SCN-861 演练绑定）。
