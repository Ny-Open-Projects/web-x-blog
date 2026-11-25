---
title: [NODE-958] 笔试题——实现发布窗口动态调整（数据驱动窗口）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-958：手写窗口调整

**需求与边界**：
- 需求：窗口动态调整（SCN-OPS-258/948）——① 窗口质量统计（各窗口异常率——SCN-OPS-948 模式）；② 动态禁用（异常率高的窗口自动封禁——SCN-OPS-258）；③ 恢复（窗口质量回升——SCN-OPS-258）；④ 调整的审计（SCN-OPS-273）。
- 边界：① 禁用的阈值（2× 基线——SCN-OPS-948）；② 恢复的条件（连续 N 周正常——SCN-OPS-948）；③ 调整的可见性（发布日历——SCN-OPS-258）。

**答**：
```javascript
cron('0 0 * * 1', async () => {                        // 每周评估（SCN-OPS-948）
  const windows = allReleaseWindows();
  for (const w of windows) {
    const rate = windowIncidentRate(w);
    if (rate > base * 2 && !w.banned) { banWindow(w); audit({ ban: w, rate }); }   // 禁用（SCN-OPS-948）
    else if (w.banned && rate < base) { unbanWindow(w); audit({ unban: w }); }   // 恢复
  }
});
```

**评分点**:
- 窗口质量统计（SCN-OPS-948）。
- 动态禁用/恢复（SCN-OPS-258）。
- 审计（SCN-OPS-273）。
