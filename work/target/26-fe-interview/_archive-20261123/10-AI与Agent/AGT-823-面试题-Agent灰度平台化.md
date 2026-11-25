---
title: [AGT-823] 平台给租户提供 Agent 灰度能力（新版本先给 10% 用户），平台化设计？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-823：平台给租户提供 Agent 灰度能力（新版本先给 10% 用户），平台化设计

**答**：
- 灰度作为平台原语：Agent 发布时可配灰度策略（百分比/白名单/按部门），运行时按会话粘性分流；灰度数据（对比指标）平台自动收集，达标一键全量。
- 指标自动对比：全量组 vs 灰度组的完成率/负反馈/成本实时对比+置信判定（Wilson），租户不需要自己搭实验体系。
- 安全兜底：灰度期间自动回滚规则（负反馈率超阈值 2 倍即自动回退），回滚秒级生效且通知发布者。

```javascript
async function publishWithCanary(pkg, policy) {
  const exp = await runtime.startCanary(pkg, {
    ratio: policy.ratio, sticky: 'session',
    autoRollback: { dislikeRate: 'x2', doneRate: '-5pp' },
  });
  const cmp = await watch(exp, ['doneRate', 'dislikeRate', 'cost']);
  return { expId: exp.id,
    promote: () => cmp.verdict === 'pass' && runtime.fullRollout(pkg) };
}
```

