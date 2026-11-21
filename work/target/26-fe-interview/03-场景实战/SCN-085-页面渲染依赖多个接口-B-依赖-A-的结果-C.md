---
title: [SCN-085] 页面渲染依赖多个接口，B 依赖 A 的结果、C 独立、D 依赖 B 和 C，如何编排最优？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-085：页面渲染依赖多个接口，B 依赖 A 的结果、C 独立、D 依赖 B 和 C，如何编排最优？
**答**：
- 先画依赖图（DAG），用 Promise 表达并行与依赖关系，坚决杜绝全串行 await：A、C 并行发出，B 等 A，D 等 B 和 C。
- 失败策略分层：关键接口失败整体报错，次要接口失败降级默认值不阻塞页面。
- 整体加超时兜底（Promise.race），避免单个慢接口拖死整页。

```javascript
// 依赖编排：A、C 并行 -> B 等 A -> D 等 B 和 C
async function loadPage() {
  // 第一层：A 与 C 同时发出（不要串行 await）
  const pA = api.getUser().catch(() => null);
  const pC = api.getRecommend().catch(() => DEFAULT_RECOMMEND);   // C 次要，失败给默认值

  const user = await pA;
  if (!user) throw new FatalError('core-api-down');   // A 是关键接口，失败整体报错

  // 第二层：B 依赖 A 的结果
  const pB = api.getOrders(user.id);

  // 第三层：D 依赖 B 与 C，整体 5 秒超时兜底
  let timer;
  const timeout = new Promise((_, rej) => {
    timer = setTimeout(() => rej(new Error('page-timeout')), 5000);
  });
  const [orders, recommend] = await Promise.race([
    Promise.all([pB, pC]),
    timeout,
  ]).finally(() => clearTimeout(timer)); // 成功后清掉定时器，避免 unhandled rejection
  return { user, orders, recommend };
}
```
