---
title: [JS-225] WeakRef 与 FinalizationRegistry：能依赖它清理资源吗
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 内存]
type: 面试题
---

## JS-225：WeakRef 与 FinalizationRegistry：能依赖它清理资源吗

**答**：
- WeakRef：持有对象的弱引用，`deref()` 在对象存活时返回它（已回收返回 undefined）——用于「缓存但不阻止回收」
- FinalizationRegistry：对象被 GC 后收到回调——听起来像析构函数
- 关键警告：两者都**不可靠**——GC 时机不确定，回调可能根本不执行（页面关闭、引擎实现差异）；规范明确「不能用作资源管理的关键机制」
- 正确姿势：资源清理（关闭文件、断开连接、取消定时器）必须显式调用（try/finally、AbortController、Symbol.dispose 提案）
- 用途定位：缓存驱逐提示、内存诊断工具——锦上添花非保命手段

```javascript
const cache = new Map(); // key -> { ref: WeakRef }
function getCached(key) {
  const entry = cache.get(key)?.ref?.deref();
  if (!entry) cache.delete(key); // 死了就清掉空壳
  return entry;
}
// FinalizationRegistry 只做「顺手清理」
const reg = new FinalizationRegistry((held) => console.log('已回收', held.id));
```
