---
title: [MFW-832] 笔试：手写 ISR 回填的版本竞态守卫（CAS 写入）
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-832：笔试：手写 ISR 回填的版本竞态守卫（CAS 写入）

**答**：
- 结论：仅当待写版本 >= 当前缓存版本才允许写入，旧版本回填直接丢弃；这是解决「陈旧回填覆盖」的核心 CAS 语义。
- 关键：版本相等且内容相同视为幂等（防重复写）；版本号必须来自数据版本而非请求时间。
- 追问钩子：为什么不能用 Date.now() 当版本？——慢请求开始早但完成晚，其时间戳可能误导；数据版本才反映内容新鲜度。

```javascript
function createVersionedCache() {
  const store = new Map();
  return {
    writeIfNewer(key, version, html) {
      const cur = store.get(key);
      if (cur && cur.version > version) return false;              // 旧版本丢弃
      if (cur && cur.version === version && cur.html === html) return false; // 幂等
      store.set(key, { version, html });
      return true;
    },
    read(key) { return store.get(key); }
  };
}

// 自测：并发回填竞态
const c = createVersionedCache();
c.writeIfNewer('/p', 10, '<new>');      // true
c.writeIfNewer('/p', 9, '<stale>');     // false：旧版本不覆盖
console.log(c.read('/p').html === '<new>');      // true
c.writeIfNewer('/p', 10, '<new>');      // false：幂等
console.log(c.read('/p').version === 10);        // true
c.writeIfNewer('/p', 11, '<newer>');    // true：更新版本覆盖
console.log(c.read('/p').html === '<newer>');    // true
```

**评分点**：
- CAS 写入：仅当版本 >= 当前才写，旧版本回填丢弃
- 版本相等且内容相同视为幂等，避免重复写
- 版本号来自数据版本而非请求时间（需在点评中点明）
- 边界：首次写入（无当前值）允许、更高版本覆盖
