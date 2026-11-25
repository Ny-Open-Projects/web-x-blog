---
title: [SCN-848] 笔试题——实现 IME 输入序列模拟器（composition 事件时序测试）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-848：手写 IME 序列模拟器

**需求与边界**：
- 需求：模拟中文输入法的 composition 事件序列（compositionstart → 多次 input(composing) → compositionend），驱动联想引擎验证「composing 期间不请求、上屏后请求」；支持快速连续上屏（验证防抖）。
- 边界：① 事件用真实 DOM 事件派发（合成的 isTrusted=false 但监听器行为一致）；② 时序可控（间隔注入）；③ 断言请求次数与时机。

**答**：
```javascript
function typeChinese(input, text, { perChar = 50 } = {}) {
  const fire = (type, data) => input.dispatchEvent(new InputEvent(type, { data, bubbles: true }));
  return new Promise(async (resolve) => {
    fire('compositionstart', '');
    for (const ch of text) {
      fire('input', ch);                               // composing 中间态
      await sleep(perChar);
    }
    fire('compositionend', text);                      // 上屏
    resolve();
  });
}
test('composing 期间零请求，上屏后恰一次', async () => {
  const calls = [];
  const engine = createSuggestEngine({ get: (url, { params }) => (calls.push(params.q), Promise.resolve({ items: [] })) });
  bindEngine(engine, input);
  await typeChinese(input, '计算器');
  expect(calls).toHaveLength(1);                       // 上屏后一次（防抖合并）
  expect(calls[0]).toBe('计算器');
});
test('快速连续输入合并为一次请求', async () => {
  jest.advanceTimersByTime(150);                       // fake timers 过防抖窗
  await typeChinese(input, 'jsq', { perChar: 10 });
  expect(calls).toHaveLength(1);
});
```

**评分点**:
- compositionstart/input/end 三事件序列正确模拟。
- 断言「请求次数与时机」（不只是结果）。
- fake timers 支持防抖时序验证。
- perChar 间隔参数化（快慢打字两种场景）。
