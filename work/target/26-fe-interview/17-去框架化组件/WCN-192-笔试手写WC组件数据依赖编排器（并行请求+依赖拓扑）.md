---
title: [WCN-192] 笔试：手写 WC 组件的数据依赖编排器（声明式请求拓扑 + 失败降级）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 选型与工程落地]
type: 笔试题
---

## WCN-192：笔试：手写数据依赖编排器

**题目**：实现 `orchestrate(spec, ctx)`：spec 为 `{ user: fetchUser, orders: { dep: ['user'], fetch: (deps) => fetchOrders(deps.user.id) }, summary: { dep: ['orders'], fetch: (d) => ..., optional: true } }`；① 按拓扑并行执行：无依赖的立即并发，有依赖的等上游；② 失败传播：required 上游失败 → 下游跳过并整体 reject；optional 失败 → 该项为 null，下游继续；③ 循环依赖检测；④ 返回结果对象与每项耗时；⑤ 全部完成后 resolve。

**答**：

```javascript
export async function orchestrate(spec) {
  const resolving = new Set();              // 循环检测
  const results = {}; const timings = {};

  function run(name, stack = []) {
    if (name in results) return results[name];
    if (resolving.has(name)) throw new Error(`循环依赖: ${[...stack, name].join(' -> ')}`);
    resolving.add(name);
    const node = spec[name];
    const deps = node.dep ?? [];
    const started = performance.now();
    return Promise.all(deps.map((d) => run(d, [...stack, name])))
      .then(async (depResults) => {
        const depMap = Object.fromEntries(deps.map((d, i) => [d, depResults[i]]));
        try {
          const value = await node.fetch(depMap);
          results[name] = value;
        } catch (e) {
          if (node.optional) results[name] = null;   // optional 降级为 null
          else throw Object.assign(e, { failedNode: name });
        }
        timings[name] = performance.now() - started;
        resolving.delete(name);
        return results[name];
      });
  }

  await Promise.all(Object.keys(spec).map((n) => run(n)));
  return { results, timings };
}

// 口径：
// const { results, timings } = await orchestrate({
//   user: { fetch: () => fetch('/me').then((r) => r.json()) },
//   orders: { dep: ['user'], fetch: ({ user }) => fetch(`/orders?uid=${user.id}`).then((r) => r.json()) },
//   ads: { dep: ['user'], fetch: fetchAds, optional: true },   // 广挂不影响主链
// });
// results.user 与 orders 并行链正确；ads 失败 → null；timings 上报性能
```

**评分点**：
- 拓扑执行正确：Promise.all 聚合上游，同层并行。
- required 失败传播（整体 reject 且带 failedNode 归因）、optional 降级 null 不阻塞下游。
- 循环依赖检测（resolving 栈）。
- 逐项耗时采集（编排性能可观测）。
