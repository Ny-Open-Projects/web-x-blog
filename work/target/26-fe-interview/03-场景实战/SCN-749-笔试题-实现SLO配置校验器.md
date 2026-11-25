---
title: [SCN-749] 笔试题——实现 SLO 配置校验器（阈值联动 + 告警参数合法性）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-749：手写 SLO 配置校验器

**需求与边界**：
- 校验项：① compliance ∈ (0,1) 且窗口合法；② burn rate 阈值关系（fast > slow > 1）；③ 快慢窗时长比合理（fast < slow）；④ 指标存在于注册表且口径版本兼容；⑤ owner 存在。
- 输出全部错误（非首个），错误分级 error/warning。

**答**：
```javascript
function validateSLO(cfg, registry) {
  const errors = [];
  const err = (level, code, msg) => errors.push({ level, code, msg });
  if (!(cfg.compliance > 0 && cfg.compliance < 1)) err('error', 'BAD_COMPLIANCE', '达标率需在 (0,1)');
  if (!['1h', '24h', '7d', '30d'].includes(cfg.window)) err('error', 'BAD_WINDOW', cfg.window);
  const { fast, slow } = cfg.burnRate ?? {};
  if (fast && slow) {
    if (!(fast > slow && slow > 1)) err('error', 'BAD_BURN_RATIO', `需 fast(${fast}) > slow(${slow}) > 1`);
    if (fast / slow > 10) err('warning', 'FAST_TOO_HOT', '快窗过高易抖动告警');
  } else err('error', 'MISSING_BURN', '缺少 burn rate 配置');
  const metric = registry.get(cfg.key);
  if (!metric) err('error', 'UNKNOWN_METRIC', cfg.key);
  else if (metric.calVer !== cfg.calVer) err('error', 'CAL_MISMATCH', `口径 ${metric.calVer} ≠ 配置 ${cfg.calVer}`);
  if (!metric?.owner) err('warning', 'NO_OWNER', '指标无 owner，告警无人认领');
  return { ok: !errors.some(e => e.level === 'error'), errors };
}
```

**评分点**:
- burn rate 数学关系校验（fast > slow > 1）。
- 快窗过高 warning（告警抖动风险）。
- 口径版本一致性校验。
- error/warning 分级（warning 不阻断但提示）。
