---
title: [MFW-770] 笔试：手写分层 flush 器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-770：笔试：手写分层 flush 器

**答**：实现 `createTieredFlusher(tierConfigs, { flushCallback })`。tierConfigs: `Record<tierName, { chunkKB, flushOnData?, flushMs? }>`。规则：1) `add(tier, content)`：加入 tier 的 buffer；2) flush 条件（RBL-769）：flushOnData=true → 有数据即刷；否则 chunkKB 满 或 flushMs 超时 → 刷；3) flush(tier)：输出合并后的 buffer → flushCallback({ tier, data, bytes })；4) `flushAll()`：所有 tier 强制 flush（完成时调用）；5) **tier 间独立**（lcp 的 flush 不影响 lazy 的 buffer——各自独立计时/计数）。边界：tierConfigs 空（add 不报错——无配置忽略）；add 空 content（不触发 flush）；flush 空 tier（无输出）。

```javascript
function createTieredFlusher(tierConfigs = {}, { flushCallback = () => {} } = {}) {
  const buffers = new Map();
  function getBuf(tier) {
    if (!buffers.has(tier)) buffers.set(tier, { data: [], bytes: 0, lastFlush: Date.now() });
    return buffers.get(tier);
  }
  function flush(tier) {
    const buf = buffers.get(tier);
    if (!buf || !buf.data.length) return null;
    const data = buf.data.join('');
    const bytes = buf.bytes;
    buf.data = []; buf.bytes = 0; buf.lastFlush = Date.now();
    const output = { tier, data, bytes };
    flushCallback(output);
    return output;
  }
  return {
    add(tier, content) {
      const cfg = tierConfigs[tier];
      if (!cfg || !content) return;
      const buf = getBuf(tier);
      buf.data.push(content);
      buf.bytes += content.length;
      const shouldFlush = cfg.flushOnData ||
        buf.bytes >= (cfg.chunkKB ?? 16) * 1024;
      if (shouldFlush) flush(tier);
      else if (cfg.flushMs) {
        // 定时 flush（简化：setTimeout 每次重设）
        clearTimeout(buf.timer);
        buf.timer = setTimeout(() => flush(tier), cfg.flushMs);
      }
    },
    flush(tier) { return flush(tier); },
    flushAll() {
      const outputs = [];
      for (const tier of buffers.keys()) {
        const out = flush(tier);
        if (out) outputs.push(out);
      }
      return outputs;
    },
  };
}

// 自测
const outputs = [];
const flusher = createTieredFlusher({
  lcp: { chunkKB: 1, flushOnData: true },
  lazy: { chunkKB: 2, flushMs: 50 },
}, { flushCallback: (o) => outputs.push(o) });

// LCP：flushOnData → 立即
flusher.add('lcp', '<h1>Title</h1>');
console.log(outputs.length === 1 && outputs[0].tier === 'lcp');

// lazy：不满不刷
flusher.add('lazy', 'a'.repeat(1000));                   // 1KB < 2KB
flusher.add('lazy', 'b'.repeat(500));                    // 累计 1.5KB < 2KB
console.log(outputs.filter(o => o.tier === 'lazy').length === 0);
// 超 chunkKB → 刷
flusher.add('lazy', 'c'.repeat(600));                    // 累计 > 2KB
console.log(outputs.filter(o => o.tier === 'lazy').length === 1);

// flushAll
flusher.add('lazy', 'd'.repeat(500));                    // 未满
flusher.flushAll();
console.log(outputs.filter(o => o.tier === 'lazy').length === 2);

// 空 add
const before = outputs.length;
flusher.add('lcp', '');
console.log(outputs.length === before);                  // 空 content 不触发

// flush 空 tier
console.log(flusher.flush('nonexistent') === null);
```

**评分点**：
- 双 flush 条件：flushOnData 立即 / chunkKB 满 / flushMs 超时（RBL-769 分层策略）
- tier 间独立（lcp 立即不影响 lazy 攒批）；flushAll 强制清空
- 边界（空 content 不触发/空 tier flush null/未知 tier 忽略）
- 能说清「分层 flush 器按内容分级：LCP 立即刷、非关键攒批——延迟与压缩效率的权衡工程化」属于加分
