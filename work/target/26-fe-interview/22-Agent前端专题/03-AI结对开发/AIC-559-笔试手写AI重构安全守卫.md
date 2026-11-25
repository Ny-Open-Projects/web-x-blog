---
title: [AIC-559] 笔试：手写 AI 重构安全守卫
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-559：笔试：手写 AI 重构守卫

**答**：实现 `createRefactorGuard(runTests)`。方法：`guard(refactorFn, tests)`。规则：1) 前置验证：runTests 必须通过（不通过 → throw 'pre-test-fail'）；2) 执行 refactorFn；3) 后置验证：runTests 仍须通过（失败 → 调用 rollback——RBL-558 安全流程）；4) rollback：调用 rollbackFn 恢复；5) 返回 `{ ok, diff?, rolledBack?, preResult, postResult }`。边界：refactorFn 抛错（不跑后置测试——直接返回错误）；前置测试已失败（阻止重构——不执行 refactorFn）；rollbackFn 也抛错（记录——原始错误仍优先）。

```javascript
function createRefactorGuard(runTests) {
  return {
    async guard(refactorFn, tests, rollbackFn) {
      // 1) 前置测试
      const pre = await runTests(tests);
      if (!pre.ok) throw new Error(`pre-test-fail: ${pre.detail ?? 'tests failing'}`);
      // 2) 执行重构
      let diff;
      try { diff = await refactorFn(); }
      catch (e) { return { ok: false, error: e.message, preResult: pre }; }
      // 3) 后置测试
      const post = await runTests(tests);
      if (!post.ok) {
        if (rollbackFn) {
          try { await rollbackFn(); } catch (re) { console.error('rollback failed:', re); }
        }
        return { ok: false, rolledBack: true, postResult: post,
          error: 'post-test-fail——已回滚' };
      }
      return { ok: true, diff, preResult: pre, postResult: post };
    },
  };
}

// 自测
let testResult = { ok: true, detail: 'all pass' };
let refactored = false; let rolledBack = false;
const guard = createRefactorGuard(async () => testResult);
// 正常重构
let r = await guard.guard(async () => { refactored = true; return 'diff-v1'; }, 'tests', async () => { rolledBack = true; });
console.log(r.ok === true && refactored === true && !r.rolledBack);
// 重构后测试失败 → 回滚
refactored = false;
testResult = { ok: false, detail: 'test broke' };       // 先过，重构后 fail
// 修改：前置过 → 重构 → 后置不过
let firstCall = true;
const guard2 = createRefactorGuard(async () => {
  if (firstCall) { firstCall = false; return { ok: true }; }
  return { ok: false, detail: 'broke' };
});
r = await guard2.guard(async () => 'refactored', 'tests', async () => { rolledBack = true; });
console.log(r.ok === false && r.rolledBack === true && rolledBack === true);
// 前置测试失败
testResult = { ok: false };
r = await guard.guard(async () => 'x', 'tests');
console.log(r === undefined || r.error?.includes('pre-test-fail'));
// 重构本身抛错
testResult = { ok: true };
r = await guard.guard(async () => { throw new Error('refactor error'); }, 'tests');
console.log(r.ok === false && r.error === 'refactor error');
```

**评分点**：
- 前置验证（重构前测试必须通过——不做前置 = 重构结果无法判断是"改坏了"还是"本来就坏"）
- 后置失败回滚（重构后测试失败 → revert——AI 重构的行为变更被自动捕获）
- 边界（refactorFn 抛错不跑后置/前置失败阻止重构/回滚失败记录）；安全流程的完整闭环
- 能说清「AI 重构的安全守卫 = 前置测试 + 重构 + 后置测试 + 回滚——测试是重构的安全网（RBL-558）」属于加分
