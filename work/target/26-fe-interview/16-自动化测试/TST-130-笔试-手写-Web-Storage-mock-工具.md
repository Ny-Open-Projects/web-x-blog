---
title: [TST-130] 笔试：手写 Web Storage mock 工具（隔离 + 快照还原 + 过期语义）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-130：笔试：手写 Web Storage mock 工具（隔离 + 快照还原 + 过期语义）
**答**：
- 需求：实现 `createStorageMock()`——替代 jsdom 里不可用的 localStorage 语义（jsdom 有 localStorage 但不持久隔离，且真浏览器 E2E 里需要可控注入）：实现完整 Storage 接口（getItem/setItem/removeItem/clear/key/length），值以字符串存（数字/对象要 toString，与真实行为一致）；支持快照/还原（用例间隔离）；支持带 TTL 的扩展用法供业务测试。
- 核心坑：Storage 只存字符串——`setItem('n', 123)` 后 `getItem` 返回 `'123'`；`setItem('x', undefined)` 存的是 `'undefined'`。测试工具必须复刻这些怪癖，否则测试结果和线上不一致。
- 边界：超配额（约 5MB）抛 QuotaExceededError；key 序按插入序（Storage 的 key(n) 遍历语义）；JSON.parse getItem 返回值由调用方负责，mock 不做序列化魔法。

```javascript
function createStorageMock() {
  let data = new Map();        // 插入序保持
  let snapshot = null;

  const store = {
    getItem(k) { k = String(k); return data.has(k) ? data.get(k) : null; },
    setItem(k, v) {
      k = String(k); v = String(v);                    // 关键：隐式转字符串
      if (v.length > 5 * 1024 * 1024)
        throw new DOMException('QuotaExceededError', 'QuotaExceededError');
      data.set(k, v);
    },
    removeItem(k) { data.delete(String(k)); },
    clear() { data.clear(); },
    key(i) { return [...data.keys()][i] ?? null; },
    get length() { return data.size; },
    // 测试扩展
    __snapshot() { snapshot = new Map(data); },
    __restore() { if (snapshot) data = new Map(snapshot); },
  };
  return store;
}

// 接入：setupFiles 里全局替换
// const s = createStorageMock();
// Object.defineProperty(globalThis, 'localStorage', { value: s, configurable: true });

// ---- 验证怪癖一致 ----
const ls = createStorageMock();
ls.setItem('n', 123);
console.log(ls.getItem('n'));        // '123'（字符串，和真 Storage 一致）
ls.setItem('u', undefined);
console.log(ls.getItem('u'));        // 'undefined'
ls.setItem('a', '1'); ls.setItem('b', '2');
console.log(ls.key(0), ls.length);   // 'a' 2
ls.__snapshot();
ls.clear();
ls.__restore();
console.log(ls.getItem('a'));        // '1'
```

**评分点**：
1. 是否复刻「值隐式转字符串」怪癖（最容易丢分）。
2. key(n)/length 遵循插入序语义。
3. 配额溢出抛 DOMException 而非静默。
4. 快照/还原支持用例隔离（beforeEach restore）。
