---
title: [WCN-158] 笔试：手写 WC 组件的埋点适配器（全局监听 composed 事件 + 组件归因）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 选型与工程落地]
type: 笔试题
---

## WCN-158：笔试：手写 WC 组件的埋点适配器

**题目**：实现 `installWcTracker(trackFn, { tags })`：① 在 document 上监听所有组件派发的 `wc-track` 事件（composed），按 tags 白名单过滤；② 归因：从 composedPath 找最近的 WC 宿主，取其 tag 与版本（constructor.__WC_VERSION__）；③ 自动补充页面上下文（path、referrer、uid）；④ 批量上报：500ms 或 10 条合并一次；⑤ `stop()` 清理；⑥ 同一事件 1 秒内去重（防连点刷量）。

**答**：

```javascript
export function installWcTracker(trackFn, { tags = null, flushMs = 500, maxBatch = 10 } = {}) {
  const queue = [];
  const seen = new Map();     // "tag|event" -> lastTs（1 秒去重）
  let timer;

  const handler = (e) => {
    if (e.type !== 'wc-track') return;
    const host = e.composedPath().find((n) => n?.nodeType === 1 && n.tagName?.includes('-') && n.localName !== 'wc-track');
    const tag = host?.tagName.toLowerCase();
    if (!tag || (tags && !tags.includes(tag))) return;
    const key = `${tag}|${e.detail?.name}`;
    const now = Date.now();
    if ((seen.get(key) ?? 0) + 1000 > now) return;   // 去重窗口
    seen.set(key, now);
    queue.push({
      tag, version: host.constructor.__WC_VERSION__ ?? 'unknown',
      name: e.detail?.name, props: e.detail?.props,
      path: location.pathname, ts: now,
    });
    if (queue.length >= maxBatch) flush();
    else { clearTimeout(timer); timer = setTimeout(flush, flushMs); }
  };

  function flush() {
    clearTimeout(timer);
    if (!queue.length) return;
    const batch = queue.splice(0);
    try { trackFn(batch); } catch (err) { console.warn('track fail', err); }
  }

  document.addEventListener('wc-track', handler);
  return {
    flush,
    stop() { document.removeEventListener('wc-track', handler); flush(); },
  };
}
// 组件侧：this.dispatchEvent(new CustomEvent('wc-track', {
//   bubbles: true, composed: true, detail: { name: 'buy-click', props: { sku } } }))
```

**评分点**：
- composedPath 归因取最近 WC 宿主 + 版本号（组件维度聚合）。
- 白名单过滤 + 1 秒去重（防刷量）。
- 批量合并（条数/时间双阈值）与 flush 清理。
- stop 双清理（监听 + 余量上报）。
