---
title: [MP-366] 笔试：手写 setData 合帧优化器
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 笔试题, 性能]
type: 笔试题
---

## MP-366：笔试：手写 setData 合帧优化器

**答**：实现 `optimizePage(page)`：① 包装 page.setData——16ms 窗口内多次调用合并（深合并 patch）；② 紧急通道：`setDataurgent(data)` 立即发送（不进合帧——交互反馈类）；③ 合并后回调链（所有挂起 cb 在合并发送完成后按序执行）；④ 卸载时 flush 挂起数据（onUnload）；⑤ 统计（合帧节省次数）。写出实现。

```javascript
function optimizePage(page) {
  const orig = page.setData.bind(page);
  let pending = {}, pendingCbs = [], timer = null, saved = 0;

  page.setData = function (data, cb) {
    const t0 = Date.now();
    pending = deepMerge(pending, data);              // 深合并 patch
    if (cb) pendingCbs.push(cb);
    if (!timer) {
      timer = setTimeout(() => {
        const d = pending, cbs = pendingCbs;
        pending = {}; pendingCbs = []; timer = null;
        orig(d, () => cbs.forEach((cb) => cb()));
        saved++;
      }, 16);
    }
  };
  page.setDataUrgent = function (data, cb) {
    flushPending();                                  // 先清挂起(保序)
    orig(data, cb);
  };
  function flushPending() {
    if (timer) { clearTimeout(timer); timer = null;
      const d = pending, cbs = pendingCbs; pending = {}; pendingCbs = [];
      orig(d, () => cbs.forEach((cb) => cb()));
    }
  }
  page.onUnload = ((origUnload) => function () {     // 卸载 flush
    flushPending(); origUnload?.call(this);
  })(page.onUnload);
  return () => ({ savedFrames: saved });
}
function deepMerge(a, b) {
  const out = { ...a };
  for (const [k, v] of Object.entries(b))
    out[k] = (typeof v === 'object' && v !== null && !Array.isArray(v) && typeof out[k] === 'object' && !Array.isArray(out[k])) ? deepMerge(out[k], v) : v;
  return out;
}
```

**评分点**：
- 16ms 合帧窗口 + 深合并（路径 patch 保序问题要说明——合帧适用于无序安全的数据）
- urgent 立即通道且先 flush 挂起（保序）
- 卸载 flush 防丢最后状态
- 回调链按序执行
