---
title: [TST-151] 笔试：手写动画结束等待 helper（transitionend / getAnimations 兜底）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-151：笔试：手写动画结束等待 helper（transitionend / getAnimations 兜底）
**答**：
- 需求：实现 `waitForAnimation(el, { timeout })`——等待元素动画/过渡真正结束，替代 `sleep(500)` 这种 flaky 死等。三条判定：① 有 transition/animation 属性 → 监听对应 end 事件；② 支持 Web Animations API → `el.getAnimations()` 全部 finished；③ 无动画 → 立即返回。
- 关键细节：transitionend 在属性被中途移除（display:none）时不触发，必须配 timeout 兜底；多个并行动画要 Promise.all；事件要 once 防泄漏。
- 应用：E2E 里点击展开面板后断言内容，必须等动画结束，否则点击落空或断言闪烁。

```javascript
function waitForAnimation(el, { timeout = 3000 } = {}) {
  const style = getComputedStyle(el);
  const hasTransition = parseFloat(style.transitionDuration) > 0;
  const hasAnimation = parseFloat(style.animationDuration) > 0;

  if (!hasTransition && !hasAnimation) return Promise.resolve(); // 无动画立即返回

  const viaWAAPI = typeof el.getAnimations === 'function'
    ? el.getAnimations().map((a) => a.finished)   // 每条动画的 finished promise
    : [];

  const viaEvent = new Promise((resolve) => {
    const done = () => { el.removeEventListener('transitionend', done);
                         el.removeEventListener('animationend', done); resolve(); };
    el.addEventListener('transitionend', done, { once: true });
    el.addEventListener('animationend', done, { once: true });
  });

  const timeoutP = new Promise((_, reject) =>
    setTimeout(() => reject(new Error(`animation on ${el.tagName} not finished in ${timeout}ms`)), timeout));

  return Promise.race([
    Promise.all([...viaWAAPI, viaEvent]).then(() => undefined),
    timeoutP,                                     // 中途 display:none 等导致事件不触发时兜底
  ]);
}

// ---- 用法（E2E 步骤中）----
// await page.click('#expand');
// const panel = await page.$('#panel');
// await waitForAnimation(panel);                 // 替代 sleep(500)
// await expect(page.getByText('详情内容')).toBeVisible();
```

**评分点**：
1. 三级判定：无动画快速返回 / WAAPI / 事件监听（覆盖面）。
2. timeout race 兜底（transitionend 不触发的经典坑）。
3. 事件 once + 清理（无泄漏）。
4. 能说明 sleep(500) 的 flaky 原因（动画时长变化/机器性能）。
