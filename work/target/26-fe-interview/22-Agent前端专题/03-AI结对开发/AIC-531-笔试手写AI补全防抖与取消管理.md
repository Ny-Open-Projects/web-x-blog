---
title: [AIC-531] 笔试：手写 AI 补全防抖与取消
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-531：笔试：手写 AI 补全防抖与取消

**答**：实现 `createCompletionManager(aiCall, { debounceMs, minChars })`。aiCall: `(context) => Promise<{ text }>`。方法：`onType(position, char)`、`getResult()`。规则：1) **防抖**：onType 后 debounceMs 内无新输入才触发 AI 调用（打字中取消）；2) **取消传播**：新 AI 调用 → 取消上一个进行中的调用（AbortController RBL-640）；3) **最小字符**：position < minChars → 不触发 AI（太短无意义）；4) **结果缓存**：同 position 同 prefix → 缓存命中（重复输入不重调）；5) 返回 `{ current: { text } | null, isPending }`。边界：debounceMs=0（每次输入都调——不防抖）；aiCall 抛错（current=null + error 事件）；连续快速输入（前面的全取消——只有最后一次的结果）。

```javascript
function createCompletionManager(aiCall, { debounceMs = 200, minChars = 3 } = {}) {
  let timer = null; let controller = null;
  let current = null; let isPending = false;
  let lastKey = ''; const cache = new Map();
  function onType(position, char, prefix) {
    const key = `${position}:${prefix}`;
    // 缓存命中
    if (cache.has(key)) { current = cache.get(key); isPending = false; return; }
    // 取消上一个
    if (controller) controller.abort();
    clearTimeout(timer);
    if (position < minChars) { current = null; isPending = false; return; }
    isPending = true; current = null;
    timer = setTimeout(async () => {
      controller = new AbortController();
      try {
        const result = await aiCall({ position, prefix, signal: controller.signal });
        if (controller.signal.aborted) return;           // 已取消
        current = result;
        cache.set(key, result);                          // 缓存
        isPending = false;
      } catch (e) {
        if (!controller.signal.aborted) { current = null; isPending = false; }
      }
    }, debounceMs);
  }
  return { onType,
    getResult: () => ({ current, isPending }),
  };
}

// 自测
let callCount = 0;
const manager = createCompletionManager(
  async ({ prefix }) => { callCount++; await sleep(20); return { text: `AI: ${prefix}` }; },
  { debounceMs: 10, minChars: 3 },
);
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

// 连续快速输入（防抖：只有最后一次触发）
manager.onType(1, 'a', 'a');
manager.onType(2, 'b', 'ab');
manager.onType(3, 'c', 'abc');                           // 最终状态
await sleep(5);
console.log(callCount === 1);                            // 防抖只调了一次
console.log(manager.getResult().isPending === true);     // AI 调用中
await sleep(30);
console.log(manager.getResult().current?.text === 'AI: abc');
console.log(manager.getResult().isPending === false);

// 缓存命中（同 position 同 prefix）
manager.onType(3, 'c', 'abc');
console.log(callCount === 1);                            // 缓存命中不重调

// minChars 限制
manager.onType(1, 'a', 'a');
console.log(manager.getResult().current === null);       // < 3 字符不触发

// 空输入
manager.onType(0, '', '');
console.log(manager.getResult().current === null);
```

**评分点**：
- 防抖正确（连续输入只有最后一次触发 AI 调用——RBL-874 的补全版）；取消传播（新调用取消旧的）
- 缓存命中（同 position+prefix 不重调——成本节省 RBL-524）；minChars 门槛（太短无意义）
- 边界（debounceMs=0/minChars 限制/连续快速输入）；isPending 状态
- 能说清「AI 补全的防抖与取消：用户 200ms 停止打字才触发 + 新请求取消旧请求——避免浪费 tokens」属于加分
