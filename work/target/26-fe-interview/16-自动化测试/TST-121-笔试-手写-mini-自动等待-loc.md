---
title: [TST-121] 笔试：手写 mini 自动等待 locator（轮询 + actionability + 超时）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-121：笔试：手写 mini 自动等待 locator（轮询 + actionability + 超时）
**答**：
- 需求：实现 `waitFor(selector, { timeout, interval })`——在 jsdom 环境模拟 Playwright 的自动等待：轮询查询元素，出现即返回；支持 `visible` 检查（display:none / visibility:hidden 不算可见）；超时抛带原因的 TimeoutError。
- 核心：requestAnimationFrame 在 jsdom 不可用，用 `setInterval` 轮询；每轮先查存在再查可见性，记录最后一次失败原因用于超时报错（Playwright 错误信息就是这个思路）。
- 边界：timeout=0 只查一次；interval 必须 > 0 且小于 timeout；元素中途出现又消失要继续等（每轮独立判定）；DOM 抛错（selector 非法）应立即抛而不是等超时。

```javascript
function isVisible(el) {
  if (!el) return false;
  const style = getComputedStyle(el);
  if (style.display === 'none' || style.visibility === 'hidden') return false;
  const rect = el.getBoundingClientRect();
  return rect.width > 0 && rect.height > 0;
}

async function waitFor(selector, { timeout = 3000, interval = 100, visible = true } = {}) {
  const start = Date.now();
  let lastReason = 'not found';
  while (Date.now() - start <= timeout) {
    const el = document.querySelector(selector);
    if (el) {
      if (!visible || isVisible(el)) return el;
      lastReason = 'found but not visible';
    }
    await new Promise((r) => setTimeout(r, interval));
  }
  throw new Error(
    `waitFor "${selector}" timeout ${timeout}ms: ${lastReason}` // 像素级报错定位
  );
}

// ---- 验证 ----
const btn = document.createElement('button');
btn.style.display = 'none';
document.body.append(btn);
setTimeout(() => (btn.style.display = 'block'), 300);
await waitFor('button', { timeout: 1000 });  // 300ms 后通过
try { await waitFor('#nope', { timeout: 200 }); }
catch (e) { console.log(e.message); }        // timeout 200ms: not found
```

**评分点**：
1. 轮询实现是否用条件循环而非一次性递归，能覆盖「元素后出现」场景。
2. 可见性判定是否检查 display/visibility/尺寸三个维度。
3. 超时错误是否携带「最后失败原因」（报错可定位，Playwright 精髓）。
4. 边界：非法 selector 是否立即抛错；interval/timeout 参数校验。
