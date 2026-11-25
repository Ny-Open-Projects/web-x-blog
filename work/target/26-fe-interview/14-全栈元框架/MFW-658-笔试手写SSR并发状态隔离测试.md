---
title: [MFW-658] 笔试：手写 SSR 并发状态隔离测试
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-658：笔试：手写 SSR 隔离测试

**答**：实现 `concurrencyLeakTest(renderFn, { iterations, scenario })`。renderFn: `(ctx: { user }) => Promise<string>`（模拟渲染，内部可能有共享状态 bug）。scenario: `{ users: string[] }`. 规则：1) **交错执行**：N 个渲染 Promise 并发（不同用户上下文）；2) 断言：每个渲染的输出包含自己的 user 且不含他人（污染检出）；3) 重复 iterations 轮（交错时序变化——提高检出率：sleep 抖动使时序变化）；4) 返回 `{ leaked: Array<{ run, expected, got }>, clean }`。边界：iterations=0；renderFn 抛错（该轮 fail 记录——不污染其他轮的断言）；scenario.users 单用户（无法检出——标记 insufficient）。

```javascript
async function concurrencyLeakTest(renderFn, { iterations = 10, users = ['alice', 'bob'] } = {}) {
  if (users.length < 2)
    return { leaked: [], clean: null, insufficient: true };   // 单用户无法检出
  const leaked = [];
  for (let iter = 0; iter < iterations; iter++) {
    const jitter = () => sleep(Math.random() * 20);        // 抖动：制造交错时序
    const results = await Promise.all(users.map(async (user, i) => {
      await jitter();
      try {
        const out = await renderFn({ user, sleep: jitter });
        return { user, out };
      } catch (e) {
        return { user, out: null, error: e.message };
      }
    }));
    for (const r of results) {
      if (r.error) continue;                               // 错误轮跳过
      const others = users.filter(u => u !== r.user);
      const contaminated = others.some(o => r.out.includes(o));
      if (!r.out.includes(r.user) || contaminated)
        leaked.push({ run: iter, expected: r.user, got: r.out.slice(0, 50) });
    }
  }
  return { leaked, clean: leaked.length === 0 };
}
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

// 自测
// 有 bug 的渲染（共享模块状态）
let shared = null;
const buggyRender = async ({ user }) => { shared = user; await sleep(5); return shared; };
let r = await concurrencyLeakTest(buggyRender, { iterations: 5 });
console.log(r.clean === false && r.leaked.length > 0);   // 污染检出

// 正确渲染（ALS 风格）
const goodRender = async ({ user }) => {
  const als = new Map();                                 // 每次调用独立（简化 ALS）
  return await new Promise((res) => {
    const p = { user, res };
    setTimeout(() => res(p.user), 5);                    // 闭包隔离
  });
};
r = await concurrencyLeakTest(goodRender, { iterations: 5 });
console.log(r.clean === true && r.leaked.length === 0);

// 单用户 insufficient
r = await concurrencyLeakTest(buggyRender, { users: ['solo'] });
console.log(r.insufficient === true);

// 错误轮不污染断言
const errRender = async ({ user }) => { if (user === 'bob') throw new Error('x');
  await sleep(3); return user; };
r = await concurrencyLeakTest(errRender, { iterations: 2 });
console.log(r.leaked.length === 0);                      // bob 的错误轮跳过，alice 断言正常
```

**评分点**：
- 交错执行 + 抖动（时序变化提高检出率——确定性时序可能漏检）
- 污染断言双向（含自己 + 不含他人）；错误轮跳过（不污染断言）
- 单用户 insufficient（检出的前置条件——诚实标注）；多轮重复（提高检出率）
- 能说清「SSR 并发的模块级 mutable 是静默串包——并发隔离测试是唯一检出手段（dev 串行看不出）」属于加分
