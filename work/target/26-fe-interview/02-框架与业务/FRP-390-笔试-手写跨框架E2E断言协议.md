---
title: [FRP-390] 笔试：手写跨框架 E2E 断言协议（行为一致性验证）
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, 测试]
type: 笔试题
---

## FRP-390：笔试：手写跨框架 E2E 协议

**答**：实现跨框架行为一致性测试协议：① `BehaviorSpec`：声明式定义交互行为（action → expected state/event）——框架无关；② `runSpec(spec, page, mount)`：Playwright 按 spec 驱动（选择器用 data-testid 协议）；③ 断言分两类：内核状态断言（window.__kernel_dump__ 比对）与 UI 断言（DOM 文本/角色）；④ 跨框架跑法：同一 spec 分别在 React 应用与 Vue 应用执行——输出「一致性报告」（两框架结果 diff）；⑤ 失败归因：内核状态一致但 UI 不同 → 壳层绑定 bug。写出实现。

```javascript
export function defineSpec(name, steps) { return { name, steps }; }
// spec 示例:
// defineSpec('add-to-cart', [
//   { action: 'click', target: 'add-btn-sku1' },
//   { assertKernel: (k) => k.cart.items.length === 1 },
//   { assertUi: { testid: 'cart-count', text: '1' } },
// ]);

export async function runSpec(spec, page, { appName }) {
  const results = [];
  await page.goto(`/${appName}/spec-harness`);
  for (const step of spec.steps) {
    if (step.action) await page.getByTestId(step.target).click();
    if (step.assertKernel) {
      const k = await page.evaluate(() => window.__panel__.dump());
      results.push({ type: 'kernel', pass: !!step.assertKernel(k.stores) });
    }
    if (step.assertUi) {
      const text = await page.getByTestId(step.assertUi.testid).textContent();
      results.push({ type: 'ui', pass: text === step.assertUi.text });
    }
  }
  return { spec: spec.name, app: appName, results, allPass: results.every((r) => r.pass) };
}
export function compareRuns(runA, runB) {
  return {
    consistent: runA.allPass === runB.allPass &&
      JSON.stringify(runA.results.map((r) => r.pass)) === JSON.stringify(runB.results.map((r) => r.pass)),
    // 归因: kernel 都 pass 但 ui 不同 → 壳层绑定 bug
    diagnosis: runA.results.every((r) => r.type !== 'kernel' || r.pass) &&
      runA.results.some((r) => r.type === 'ui' && !r.pass) ? 'shell-binding-bug' : 'kernel-or-spec',
  };
}
```

**评分点**：
- spec 的声明式协议（action/双类断言）
- 内核状态断言与 UI 断言分离（归因依据）
- 双框架跑同一 spec 的一致性报告
- 失败归因规则（kernel pass + ui fail = 壳层绑定 bug）

## 变体与延伸（补充）

**变体与延伸**：

1. 内核 dump 要满足什么约束才能跨框架直接比对？ → 必须是纯数据、无函数与类实例，键序稳定（序列化前排序），时间戳与随机值要剔除或注入固定 seed，否则 diff 永远不空。
2. UI 断言为什么优先 role 与文本，而不是 class？ → class 是壳层实现细节，两框架必然不同；role 与可见文本属于可访问性契约，跨框架稳定，顺带把无障碍回归也覆盖了。
3. 一致性报告怎么接 CI 才不误报？ → 按"spec × 框架"参数化跑，结果 JSON 落盘做 diff，只对同一步骤 pass 状态变化报警，环境类错误单独标记 flaky 并重跑，不与一致性混在一起。
