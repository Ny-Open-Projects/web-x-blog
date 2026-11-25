---
title: [1136] Agent 能力注册表怎么支撑动态编排
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 架构]
type: 面试题
---

## 1136：Agent 能力注册表怎么支撑动态编排

**答**：
- 注册表内容：能力名、输入/输出 schema、历史表现（通过率/耗时/成本分位数）、状态（可用/降级/下线）；编排器按能力查表而不是硬编码 Agent 名——新 Agent 上线注册即接入。
- 动态编排：编排器拿到任务后「查能力表选实现」，同能力多实现时按表现数据选（通过率高者优先、成本敏感时选便宜的）。
- 表现数据闭环：每次执行回写统计（成功/失败/耗时），能力表数据保鲜；长期低表现的能力自动标记降级待优化。
- 追问钩子：动态选实现的风险？——表现数据有滞后性（模型刚升级数据还没更新），所以选型是「数据 + 灰度」：新实现先接 5% 流量，数据达标再提权。

```ts
const registry = {
  find(cap, ctx) {
    const impls = this.byCap[cap].filter(i => i.status === 'ok');
    return impls.sort((a, b) => score(b, ctx) - score(a, ctx))[0]; // 数据驱动
  },
  report(id, r) { this.stats[id].update(r); },     // 执行回写
};
function score(impl, ctx) {
  return impl.stats.passRate * (ctx.costSensitive ? 1 / impl.stats.cost : 1);
}
```

