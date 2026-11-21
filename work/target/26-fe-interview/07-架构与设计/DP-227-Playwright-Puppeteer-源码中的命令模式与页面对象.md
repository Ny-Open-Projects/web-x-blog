---
title: [DP-227] 源码识别：Playwright 源码中的命令模式与自动等待？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-227：源码识别：Playwright 源码中的命令模式与自动等待？
**答**:
- 命令模式：page.click('btn') 是命令封装（协议消息 → 浏览器执行 → 结果回传），超时/重试配置是命令参数；trace 记录的就是命令序列（可回放）。
- 责任链（自动等待）：click 执行前依次检查（元素存在 → 可见 → stable → enabled → receives events），任一不满足等待重试——隐式前置条件的链式校验。
- 模板方法：expect(locator).toHaveText 断言骨架固定（轮询 + 比较 + 超时），比较逻辑策略注入。
- 识别要点：能解释 Playwright 为何比 Selenium 稳——"等待"内建在命令执行链里，而不是用户 sleep。

```javascript
// Playwright 自动等待链（源码级简化）
async function click(page, selector, { timeout = 30000 } = {}) {
  const deadline = now() + timeout;
  while (now() < deadline) {                     // 模板方法：轮询重试
    const el = await query(page, selector);
    if (!el) { await raf(page); continue; }      // 链条 1：存在
    if (!await isVisible(el)) { await raf(page); continue; }    // 2：可见
    if (await isAnimating(el)) { await raf(page); continue; }   // 3：stable（无动画）
    if (!await isEnabled(el)) throw new Error('element disabled');     // 4：可交互（立即失败）
    if (!await receivesEvents(el, page)) { await raf(page); continue; } // 5：未被遮挡
    return sendCommand('Input.dispatchMouseEvent', el.center());       // 命令下发
  }
  throw new TimeoutError(`click ${selector}`);
}
// expect：poll(deadline, () => compare(actual(), expected)) —— 断言也是"等待+比较"模板
```
