---
title: [AGT-669] 评测也有 flaky（同一用例时过时不过），如何治理评测的随机性？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-669：评测也有 flaky（同一用例时过时不过），如何治理评测的随机性

**答**：
- flaky 三来源：模型采样随机（高温）、外部依赖抖动（检索超时）、judge 随机（打分漂移）。治理先分类：模型随机用温度 0/固定种子；依赖抖动做重试+标记；judge 随机用双评委均值。
- flaky 识别：同一用例近 N 次结果方差超阈值标 flaky，隔离到「观察区」不阻断门禁，但持续监控——flaky 用例让 CI 门禁失去信任。
- 关键用例禁 flaky：安全/门禁类用例必须确定性化（温度 0 + 缓存金标路径），做不到确定性就改判据（宽松化到可确定性判定）。

```javascript
function flakyDetect(history) {
  const rate = variance(history.verdicts);
  return rate > THRESH ? { flaky: true,
    quarantine: 'observation',                    // 隔离观察区
    diagnose: classifyFlaky(history),             // 模型随机/依赖抖动/judge漂移
  } : { flaky: false };
}
function stabilize(critical) {
  return critical.map(c => ({ ...c, temperature: 0,
    judge: 'deterministic-rules',                 // 安全类禁随机
    fallback: 'relaxed-rubric' }));
}
```

