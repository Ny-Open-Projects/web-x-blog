---
title: [AGT-810] 企业内的 Agent 应用商店（各部门发布自己的 Agent），发布与治理怎么设计？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-810：企业内的 Agent 应用商店（各部门发布自己的 Agent），发布与治理怎么设计

**答**：
- 发布流：开发者打包（Agent 定义：提示词/工具引用/权限申请）→ 平台校验（工具引用存在/schema 合法）→ 安全评审（权限申请合理性）→ 发布（可见范围：部门/全员）→ 迭代（版本化，用户可选跟随最新或锁定版本）。
- 权限申请显式化：Agent 申请哪些工具/数据范围在商店页明示（用户安装前知情），运行时按申请授予（不超发）。
- 治理指标：使用量/采纳率/负反馈率排行，劣质 Agent（负反馈高）自动降权展示，弃用 Agent（90 天零使用）提示下架。

```javascript
const AGENT_PKG = {
  manifest: { name, version, tools: ['crm.query'], dataScope: 'dept' },
  prompt: versioned, tests: 'min-eval-suite',    // 发布需带最小评测
};
async function publish(pkg, publisher) {
  validate(pkg.manifest);                         // 工具引用存在
  await securityReview(pkg, publisher);           // 权限合理性
  return store.publish(pkg, { visibility: publisher.dept,
    minEval: runEval(pkg.tests) });               // 评测报告随包发布
}
```

