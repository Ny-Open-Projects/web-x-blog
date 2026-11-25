---
title: [NODE-904] 笔试题——实现滚动重启验证（逐实例排空验证）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-904：手写滚动验证

**需求与边界**：
- 需求：滚动重启验证（SCN-NODE-665/722）——① 逐实例重启编排（PDB 约束——SCN-NODE-665）；② 每实例的验证（重启后探针通过 + 无请求失败——SCN-NODE-743）；③ 失败中止（某实例重启后异常 → 停止滚动——SCN-OPS-237 降档）；④ 全量完成的验证（SCN-OPS-248）。
- 边界：① 重启的并发控制（maxUnavailable=0——SCN-NODE-665）；② 验证的指标（错误率/延迟——窗口内零失败）；③ 重启风暴防御（SCN-NODE-648）。

**答**：
```javascript
async function rollingVerify(deployment) {
  for (const pod of podsOf(deployment)) {              // 逐实例（SCN-NODE-665 PDB）
    const errBefore = windowErrorRate();
    await restartPod(pod);                             // 触发优雅关闭（SCN-NODE-722）
    await waitForReady(pod);                           // readiness 通过（SCN-NODE-743）
    const errAfter = await windowErrorRate({ excludePod: pod });
    const failed = windowRequestFailures({ during: restartWindow });
    if (errAfter > errBefore * 1.2 || failed > 0) {    // 重启引发失败
      alert({ type: 'ROLLING_FAIL', pod });
      break;                                           // 中止滚动（SCN-OPS-237 降档）
    }
  }
  return { allReady: podsOf(deployment).every(podReady) };   // SCN-OPS-248
}
```

**评分点**:
- 逐实例验证（PDB 约束——SCN-NODE-665）。
- 重启窗口零失败断言（SCN-NODE-743 联动）。
- 失败中止（SCN-OPS-237 降档语义）。
- 全量完成验证（SCN-OPS-248）。
