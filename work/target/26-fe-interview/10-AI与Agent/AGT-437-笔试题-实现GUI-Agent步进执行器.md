---
title: [AGT-437] 笔试题——实现 GUI Agent 步进执行器（感知-行动-验证循环+卡住转人）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-437：手写 GUI Agent 执行循环：页面理解、动作执行、状态验证、卡住接管

**需求与边界**：
- 输入：任务目标、页面驱动（dom/screenshot/click）、步数上限；输出：执行结果或转人。
- 边界要求：① 每步执行后验证状态变化（点击无效重试限 1 次）；② 关键操作（支付/删除）强确认；③ 步数熔断与卡住检测（连续 2 次无状态变化）→ 转人并携带上下文；④ 全程截图留痕。

**答**：
```javascript
async function guiAgent({ goal, page, maxSteps = 15, confirm }) {
  const history = []; let stuck = 0;
  for (let s = 0; s < maxSteps; s++) {
    // 1. 感知：DOM 结构 + 截图（混合）
    const state = await page.snapshot();        // {dom, shot, url}
    // 2. 决策：模型给出下一步动作
    const decision = await llm({ goal, state: state.dom,
      history, schema: ACTION_SCHEMA });        // {action, target, value}
    if (decision.action === 'finish')
      return { ok: true, history };
    // 3. 关键操作确认
    if (['pay', 'delete', 'submit_payment'].includes(decision.action)) {
      const d = await confirm(decision);
      if (!d) return { ok: false, reason: 'user_denied', history };
    }
    // 4. 执行
    const before = await page.url();
    await page.act(decision);
    await page.waitForStable();                 // 等渲染稳定
    // 5. 验证：状态变化（URL/DOM 指纹）
    const after = await page.snapshot();
    const changed = after.url !== before ||
      domFingerprint(after.dom) !== domFingerprint(state.dom);
    history.push({ step: s, decision, shot: after.shot,
      changed });
    if (!changed) {
      if (++stuck >= 2)                         // 卡住转人
        return { ok: false, reason: 'stuck', history,
          handoff: { lastUrl: after.url,
            tried: history.slice(-2).map(h => h.decision),
            hint: '请手动处理此步后继续' } };
      await page.act({ ...decision, retry: true });  // 重试一次
    } else stuck = 0;
  }
  return { ok: false, reason: 'max_steps', history };
}
```

**评分点**:
- 感知-行动-验证循环完整（截图+DOM 混合、waitForStable、指纹对比）。
- 关键操作强确认（白名单动作类型）。
- 卡住检测（连续无变化）→ 带上下文转人（lastUrl/tried/hint），不是裸失败。
- 步数熔断与全程截图留痕（可回放）。
