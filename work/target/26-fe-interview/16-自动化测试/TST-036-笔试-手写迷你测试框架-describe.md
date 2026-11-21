---
title: [TST-036] 笔试：手写迷你测试框架（一）describe / it / expect 核心 runner
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-036：笔试：手写迷你测试框架（一）describe / it / expect 核心 runner
**答**：
- 需求：实现 `describe/it/expect` 三个函数：it 收集用例不立即执行；describe 嵌套形成用例树；全部注册完统一执行并输出「通过数/失败数/失败详情」，失败用例不中断后续执行。
- 核心：用栈管理当前 describe 上下文（注册时挂到栈顶），执行阶段深度遍历树；expect 返回带断言方法的对象，失败 throw Error 被 runner 捕获记为 failed。
- 边界：用例名要带 describe 路径前缀；计数要区分 passed/failed/total；退出码非 0 表示有失败（CI 依赖）。

```javascript
let stack = [];          // describe 上下文栈
const suite = { name: 'root', cases: [], children: [] };

function describe(name, fn) {
  const node = { name, cases: [], children: [] };
  stack.at(-1).children.push(node);
  stack.push(node);
  fn();
  stack.pop();
}

function it(name, fn) {
  stack.at(-1).cases.push({ name: [...stack.slice(1), { name }].map((n) => n.name).join(' > '), fn });
}

function expect(actual) {
  return {
    toBe(exp) { if (actual !== exp) throw new Error(`expect ${actual} toBe ${exp}`); },
    toEqual(exp) { if (JSON.stringify(actual) !== JSON.stringify(exp)) throw new Error(`${actual} != ${exp}`); },
    toBeTruthy() { if (!actual) throw new Error(`${actual} is not truthy`); },
  };
}

async function run(suite = arguments.length ? undefined : globalSuite) { /* 简化：执行全局注册树 */
  const node = arguments.length ? suite : suiteRoot;
  let passed = 0, failed = 0;
  for (const { name, fn } of node.cases) {
    try { await fn(); passed++; console.log(`✔ ${name}`); }
    catch (e) { failed++; console.error(`✘ ${name}\n  ${e.message}`); }
  }
  for (const child of node.children) { const r = await run(child); passed += r.passed; failed += r.failed; }
  return { passed, failed };
}

// ---- 用法 ----
describe('math', () => {
  it('1+1=2', () => expect(1 + 1).toBe(2));
  it('string', () => expect('a').toEqual('a'));
});
run(rootSuite).then(({ passed, failed }) => { console.log(`${passed} passed, ${failed} failed`); process.exitCode = failed ? 1 : 0; });
```
**评分点**：
- 注册与执行分离（先收集用例树再跑），嵌套 describe 用栈实现。
- 失败隔离：单用例 throw 不影响后续，最终非零退出码。
- 用例名带完整 describe 路径。
- expect 至少实现 toBe（===）与 toEqual（深度），且知道真实框架还支持扩展 matcher/异步。
