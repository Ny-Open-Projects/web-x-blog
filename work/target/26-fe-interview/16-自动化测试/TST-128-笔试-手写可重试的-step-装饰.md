---
title: [TST-128] 笔试：手写可重试的 step 包装器（E2E 步骤级重试 + 耗时上报）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-128：笔试：手写可重试的 step 包装器（E2E 步骤级重试 + 耗时上报）
**答**：
- 需求：实现 `step(name, fn, opts)`——E2E 用例里的业务步骤包装：失败自动重试（步骤级比用例级粒度细，重跑成本低）、每次尝试记录耗时与错误、可标记非幂等步骤禁止重试、全部失败抛出聚合错误（含历次错误）。
- 核心：与 TST-042 的通用重试器差异点在「步骤语义」——要接入报告（记录 name/attempt/ms）、要区分可重试错误（超时类）与不可重试错误（断言类 `err.fatal`）。
- 边界：retries=0；重试前执行 `beforeRetry` 钩子（如清空表单重新 fill，恢复幂等前置态）；聚合错误信息要包含步骤名与每次尝试的错误首行，方便报告定位。

```javascript
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function step(name, fn, { retries = 2, backoff = 500, beforeRetry, report = [] } = {}) {
  const attempts = [];
  for (let i = 0; i <= retries; i++) {
    const start = Date.now();
    try {
      const result = await fn();
      const ms = Date.now() - start;
      attempts.push({ i, ms, ok: true });
      report.push({ name, attempts });              // 接入测试报告
      return result;
    } catch (err) {
      const ms = Date.now() - start;
      attempts.push({ i, ms, ok: false, err: String(err.message).split('\n')[0] });
      if (err.fatal || i === retries) {             // 断言错误 / 用尽次数
        const agg = new Error(`step "${name}" failed after ${i + 1} attempts:\n` +
          attempts.map((a) => `  #${a.i} (${a.ms}ms): ${a.err ?? 'ok'}`).join('\n'));
        agg.attempts = attempts;
        throw agg;
      }
      if (beforeRetry) await beforeRetry(i);        // 恢复前置态再重试
      await sleep(backoff * (i + 1));
    }
  }
}

// ---- 用法（Playwright）----
test('下单流程，步骤级重试', async ({ page }) => {
  const report = [];
  await step('打开商品页', () => page.goto('/goods/1'), { report });
  await step('加入购物车', async () => {
    await page.getByRole('button', { name: '加入购物车' }).click();
    await expect(page.getByText('已加入')).toBeVisible({ timeout: 3000 });
  }, {
    report,
    beforeRetry: async () => await page.reload(),   // 重试前恢复状态
  });
  console.log(report); // 上报到测试平台
});
```

**评分点**：
1. 区分 fatal（断言）与可重试错误，不盲目重试。
2. 聚合错误包含历次尝试信息（不是只抛最后一个）。
3. beforeRetry 钩子处理「非幂等步骤」的恢复语义。
4. 耗时与尝试记录可对接报告（工程完整度）。
