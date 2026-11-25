---
title: [AIC-666] 「AI 采纳率」怎么量才不被虚荣数据骗了？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-666：「AI 采纳率」怎么量才不被虚荣数据骗了？

**答**：
- 结论先行：**采纳率要分三层量——「安装/开通」≠「使用」≠「有效使用」**，只有第三层才有业务意义。把「装了 Copilot 的人数」当采纳率是典型的虚荣指标。
- 三层指标：1) **覆盖层**：开通/安装人数——只说明推广到位，与价值无关；2) **活跃层**：DAU/周活、补全请求数——说明在用，但可能是「开着不用」或「用了又删」；3) **有效层**：补全接受率、生成代码 7 天存活率、AI 辅助 PR 的有效交付——这才是真采纳（AIC-074 存活率 / AIC-516 接受率）。
- 反作弊：光看接受率也会被「无脑 Tab 接受然后不改」骗——要结合存活率与返工率；一个人一天接受 500 个补全但全被重写，不是高采纳而是高浪费。
- 分层看人群：采纳率要按「老手/新手」「核心模块/边角」拆——老手可能刻意少用 AI（因为他知道哪些不能信），低采纳不代表失败（AIC-069 Senior 用法）。
- 追问钩子：为什么「接受率」单独看会误导？——因为接受是「当下没删」，不代表「代码是对的」；AI 补全常见「接受后 2 分钟发现不对又改掉」，接受率记了 1 次成功，但实际是负价值；只有加上「7 天存活」才能过滤这种假采纳。

```typescript
type DevUsage = { installed: boolean; activeDays: number; accepted: number; survived: number; rewritten: number };

function effectiveAdoption(users: DevUsage[]) {
  const installed = users.filter(u => u.installed).length;
  const active = users.filter(u => u.activeDays >= 3).length;
  const effective = users.filter(u => u.accepted > 0 && u.survived / Math.max(1, u.accepted) > 0.5).length;
  return {
    coverage: users.length ? installed / users.length : 0,
    activeRate: users.length ? active / users.length : 0,
    effectiveRate: users.length ? effective / users.length : 0,
  };
}

const users = [
  { installed: true, activeDays: 5, accepted: 100, survived: 60, rewritten: 40 }, // 有效
  { installed: true, activeDays: 5, accepted: 200, survived: 20, rewritten: 180 }, // 高接受低存活=假采纳
  { installed: true, activeDays: 0, accepted: 0, survived: 0, rewritten: 0 },      // 装了不用
  { installed: false, activeDays: 0, accepted: 0, survived: 0, rewritten: 0 },
];
const r = effectiveAdoption(users);
console.log(r.coverage === 0.75 && r.effectiveRate === 0.25); // 覆盖75%但有效仅25%
```
