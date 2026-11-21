---
title: [JS-153] 手写竞态控制 hook 工具？abort 与版本号双方案怎么封装？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-153：手写竞态控制 hook 工具？abort 与版本号双方案怎么封装？

**答**：
- 竞态场景：输入联想连续请求，先发后至的旧响应会覆盖新响应，必须丢弃过期结果。
- 版本号方案：每次调用自增 version，响应回来时 version 已变则视为过期——不中止请求，但结果作废，适合无法取消的场景。
- AbortController 方案：新请求发出前 abort 旧请求，真正中止网络传输，省流量，fetch/XHR 均支持。
- 统一封装后业务层只写 `try/catch StaleError`，两种方案可配置切换，过期一律静默丢弃。

```javascript
class StaleError extends Error {
  constructor() { super('stale response'); this.name = 'StaleError'; }
}

// 方案一：版本号（适用于无法取消的请求通道）
function withVersion(fetcher) {
  let version = 0;
  return async (...args) => {
    const current = ++version;
    const result = await fetcher(...args);
    if (current !== version) throw new StaleError(); // 已有更新的调用 → 本次作废
    return result;
  };
}

// 方案二：AbortController（真正中止请求，省流量）
function withAbort(fetcher) {
  let controller = null;
  return async (...args) => {
    controller?.abort();                              // 新请求前中止旧请求
    controller = new AbortController();
    try {
      return await fetcher(controller.signal, ...args);
    } catch (e) {
      if (e.name === 'AbortError') throw new StaleError(); // 中止统一转成过期错误
      throw e;
    }
  };
}

// 统一使用：输入联想
const searchAPI = (kw) => new Promise((r) => setTimeout(() => r(`结果-${kw}`), 100));
const search = withVersion(searchAPI);                // 换成 withAbort 即可切换方案

async function onInput(kw) {
  try {
    const res = await search(kw);
    console.log('渲染', res);
  } catch (e) {
    if (e instanceof StaleError) console.log('丢弃过期响应', kw); // 竞态结果静默丢弃
    else throw e;
  }
}
onInput('a');
onInput('ab');
onInput('abc');
// 100ms 后：渲染 结果-abc ｜ 丢弃过期响应 a ｜ 丢弃过期响应 ab
```

## 二十二、数据结构与算法思维在 JS
