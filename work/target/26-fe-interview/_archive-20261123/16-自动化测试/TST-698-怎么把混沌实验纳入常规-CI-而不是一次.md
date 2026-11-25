---
title: [TST-698] 怎么把混沌实验纳入常规 CI 而不是一次性演练？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-698：怎么把混沌实验纳入常规 CI 而不是一次性演练？

**答**：
- 结论：分层——PR 阶段跑组件级故障注入（秒级），nightly 跑 E2E 混沌场景，生产混沌按季度手动。
- 混沌用例和普通用例同库管理，标记 @chaos；CI 失败同样阻断。
- 注入器必须可复现（固定随机种子），否则 flaky 会淹没信号。
- 追问钩子：混沌用例本身不稳定，老是在 CI 里红，你怎么治？

```javascript
function chaosInCI(stage) {
  const matrix = {
    pr: { scope: 'component', inject: ['api-error', 'dom-hide'], maxSec: 30 },
    nightly: { scope: 'e2e', inject: ['network-loss', 'clock-jump'], maxSec: 600 },
    quarterly: { scope: 'production', inject: ['bucket-fault'], maxSec: 300 },
  };
  return { ...matrix[stage], reproducible: true, tag: '@chaos' };
}
console.log(chaosInCI('pr').inject.join(','));
```
