---
title: [MFW-625] 笔试：手写 GraphQL 批量收集器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-625：笔试：手写 GraphQL 批量收集器

**答**：实现 `createBatchedGraphQL({ endpoint, fetchFn, flushMs })`。`query(query, variables)`：1) 加入 batch 队列（同 flush 窗口内的合并为一个 `[Operation]` 数组——Apollo batching 格式：JSON 数组）；2) flushMs 后发送（Promise 共享——同窗口的调用者共享同一响应）；3) 响应按序分发给各调用者（响应数组 index 对应）；4) 单个查询错误：响应含 errors → 对应调用者 reject，其他成功者正常。返回包装。边界：单查询也走 batch（窗口 flush——数组单元素）；flush 期间新查询（下一窗口）；fetchFn 抛错 → 所有等待者 reject。

```javascript
function createBatchedGraphQL({ endpoint, fetchFn = fetch, flushMs = 10 } = {}) {
  let queue = []; let timer = null;
  function flush() {
    const current = queue; queue = []; timer = null;
    const bodies = current.map(c => ({ query: c.query, variables: c.variables }));
    fetchFn(endpoint, { method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify(bodies) })
      .then((res) => res.json())
      .then((responses) => {
        responses.forEach((resp, i) => {
          const c = current[i];
          if (!c) return;
          if (resp.errors) c.reject(new Error(resp.errors[0].message));
          else c.resolve(resp.data);
        });
      })
      .catch((e) => current.forEach(c => c.reject(e)));
  }
  return {
    query(query, variables = {}) {
      return new Promise((resolve, reject) => {
        queue.push({ query, variables, resolve, reject });
        if (!timer) timer = setTimeout(flush, flushMs);    // 窗口合并
      });
    },
  };
}

// 自测
const requests = [];
const gq = createBatchedGraphQL({
  endpoint: '/graphql',
  fetchFn: async (url, opts) => {
    requests.push(JSON.parse(opts.body));
    const bodies = requests.at(-1);
    return new Response(JSON.stringify(bodies.map((b, i) =>
      b.query.includes('Bad') ? { errors: [{ message: 'bad query' }] }
        : { data: { result: `r-${i}-${b.variables.id}` } })));
  },
  flushMs: 5,
});
// 同窗口 3 个查询 → 1 个请求
const [a, b, bad] = await Promise.all([
  gq.query('query A($id: ID)', { id: 1 }),
  gq.query('query B($id: ID)', { id: 2 }),
  gq.query('query Bad($id: ID)', { id: 3 }),
]);
console.log(requests.length === 1 && requests[0].length === 3);   // 合并为 1 请求
console.log(a.result === 'r-0-1' && b.result === 'r-1-2');
// 单查询错误不影响其他
console.log(bad.message === 'bad query' && a.result === 'r-0-1');

// 新窗口
const c = await gq.query('query C($id: ID)', { id: 4 });
console.log(requests.length === 2 && requests[1].length === 1);
```

**评分点**：
- 窗口合并（flushMs 微批次——N+1 的 RSC 组件查询缓解 RBL-930）
- 响应按序分发 + 单查询错误隔离（一个 errors 不影响其他——批量的错误语义）
- Promise 共享（同窗口调用者等同一 flush）；新查询走新窗口
- 能说清「RSC 组件级 GraphQL 查询的 N+1 用 micro-batching 缓解——窗口合并把 N 请求压成 1」属于加分
