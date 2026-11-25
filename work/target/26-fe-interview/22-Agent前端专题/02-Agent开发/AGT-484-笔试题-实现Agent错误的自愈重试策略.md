---
title: [AGT-484] 笔试题——实现错误自愈重试（错误分类×策略映射+退避+上限）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-484：手写自愈重试：错误分类、策略映射（换参/换模型/降级）、指数退避

**需求与边界**：
- 输入：执行函数、错误分类器、策略表；输出：最终结果或失败报告。
- 边界要求：① 错误分类决定策略（可重试/换参数/换模型/放弃）；② 指数退避+抖动（防惊群）；③ 总尝试预算（时间+次数双上限）；④ 重试链路记录（每试的错因与策略）。

**答**：
```javascript
async function selfHeal(fn, { classify, policies,
  maxAttempts = 4, maxWallMs = 30e3 }) {
  const trail = []; const start = Date.now();
  let ctx = { args: null, model: 'default' };
  for (let i = 0; i < maxAttempts; i++) {
    try {
      return { ok: true, result: await fn(ctx), trail };
    } catch (e) {
      const cat = await classify(e);          // rate_limit/timeout/
                                              // bad_args/upstream/model_overload
      const policy = policies[cat];
      trail.push({ attempt: i + 1, error: e.message, cat,
        action: policy?.action });
      if (!policy || policy.action === 'abort' ||
          Date.now() - start > maxWallMs)
        return { ok: false, trail, finalError: e.message };
      // 策略应用
      if (policy.action === 'backoff') {
        const base = Math.min(2 ** i * 500, 8000);
        await sleep(base + Math.random() * base * 0.5); // 抖动防惊群
      }
      if (policy.action === 'fix_args' && policy.fix)
        ctx.args = policy.fix(ctx.args, e);
      if (policy.action === 'switch_model')
        ctx.model = policy.next(ctx.model);
      if (policy.action === 'degrade')
        return { ok: true, result: policy.fallback(ctx),
          degraded: true, trail };
    }
  }
  return { ok: false, trail, finalError: '尝试预算耗尽' };
}
// policies 示例：
// rate_limit: { action: 'backoff' },
// bad_args:   { action: 'fix_args', fix: (a, e) => ({...a, date: e.suggested}) },
// model_overload: { action: 'switch_model', next: m => CHEAPER[m] ?? m },
// permission: { action: 'abort' },            // 不可恢复直接放弃
```

**评分点**:
- 错误分类×策略映射（backoff/fix_args/switch_model/degrade/abort）语义正确。
- 指数退避+抖动防惊群；时间+次数双预算。
- 重试链路 trail 完整（每试错因与动作，可归因）。
- 不可恢复错误（permission）直接放弃不浪费预算。
