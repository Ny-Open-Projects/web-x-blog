---
title: [DP-231] 源码识别：Vitest/Jest 测试框架源码中的收集器与观察者？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-231：源码识别：Vitest/Jest 测试框架源码中的收集器与观察者？
**答**：
- 收集器+组合：describe/it 递归嵌套构建测试树（组合模式），收集阶段只建结构不执行。
- 观察者+状态机：运行阶段逐用例执行 → 结果事件（onTestCaseResult）→ reporter 订阅渲染输出；TAP/JUnit reporter 是输出策略替换。
- 模板方法：runner 的骨架固定（beforeAll → each test → afterAll），fixture 钩子注入。
- 识别要点：能解释"describe 是纯收集，test 内 expect 失败 throw → runner 捕获记为 fail"——断言失败即异常控制流。

```javascript
// 迷你测试框架
let root = { children: [], type: 'suite', name: 'root' };
let ctx = root;
function describe(name, fn) { const s = { type: 'suite', name, children: [], parent: ctx };
  ctx.children.push(s); const prev = ctx; ctx = s; fn(); ctx = prev; }   // 收集器（组合树）
function it(name, fn) { ctx.children.push({ type: 'test', name, fn }); }
async function run(node, reporters) {
  if (node.type === 'suite') {
    for (const c of node.children) await run(c, reporters);       // 深度遍历
    return;
  }
  const before = now();
  try { await node.fn(); reporters.forEach(r => r.onPass(node, now() - before)); }
  catch (e) { reporters.forEach(r => r.onFail(node, e)); }        // 断言 throw → 捕获归类
}
// expect = 断言描述符：expect(x).toBe(y) → 不等 throw new Error(diff) —— 失败即异常
```
