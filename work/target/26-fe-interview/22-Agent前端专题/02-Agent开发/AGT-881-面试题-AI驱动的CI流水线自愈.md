---
title: [AGT-881] CI 流水线挂了（环境问题/偶发失败），AI 自愈的范围与禁區？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-881：CI 流水线挂了（环境问题/偶发失败），AI 自愈的范围与禁區

**答**：
- 可自愈：基础设施类失败（flaky 重试带归因标注/环境超时自动扩容/缓存损坏自动清理重建）——可逆且预案明确；产物类（构建缓存失效）可自动。
- 禁区：测试失败的"自动跳过"（绝对禁止——跳过失败是质量事故）、改测试去让 CI 绿、未知失败的重试超过 1 次（掩盖真问题）。
- 自愈透明：每次自愈动作在流水线日志显著标注（AI 自愈：原因/动作），自愈率与掩盖率月度统计——自愈不能变成"让红变绿的魔法"。

```javascript
const HEAL_POLICY = {
  allowed: ['flaky-retry(标注)', 'env-scale', 'cache-rebuild'],
  forbidden: ['skip-failing-test', 'modify-test', 'retry-unknown>1'],
};
async function ciSelfHeal(failure) {
  const kind = classify(failure);
  if (!HEAL_POLICY.allowed.includes(kind))
    return page(failure.owner);                    // 禁区直接找人
  const r = await heal(kind, failure);
  logPipeline(`AI自愈：${kind}（${r.action}）`);    // 显著标注
  return r;
}
```

