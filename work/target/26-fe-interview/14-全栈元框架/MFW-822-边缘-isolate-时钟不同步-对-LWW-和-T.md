---
title: [MFW-822] 边缘 isolate 时钟不同步，对 LWW 和 TTL 有什么影响
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-822：边缘 isolate 时钟不同步，对 LWW 和 TTL 有什么影响

**答**：
- 结论：LWW 依赖时间戳定胜负、TTL 依赖本地时钟判过期；clock skew 会让「快时钟节点的旧写入」覆盖新值，或让缓存过早/过晚失效。
- 解法：排序用 HLC/逻辑时钟替代物理时钟；TTL 用单调时钟 + 中心下发时间基准；对时间敏感操作容忍 skew 上界。
- 追问钩子：NTP 同步够不够？——跨区 skew 仍可达数十毫秒，金融/库存场景需 HLC + 容忍窗口。

```javascript
// skew 导致 LWW 错判：B 物理时钟快，旧写入反而「更新」
const writeA = { value: 'new', ts: 1000 };           // 真实后写
const writeB = { value: 'stale', ts: 1010 };         // 时钟快 +10ms
function lww(a, b) { return a.ts > b.ts ? a : b; }
console.log(lww(writeA, writeB).value);              // stale —— 错！

// HLC 修正：因果序不依赖物理时钟绝对值
function makeHLC(node) {
  let last = { p: 0, l: 0 };
  return (remote) => {
    const pt = Date.now();
    if (remote) {
      last = { p: Math.max(pt, last.p, remote.p),
               l: pt <= last.p && remote.p <= last.p ? Math.max(last.l, remote.l) + 1 : 0 };
    } else if (pt > last.p) last = { p: pt, l: 0 };
    else last = { p: last.p, l: last.l + 1 };
    return { ...last, node };
  };
}
const a = makeHLC('a'), b = makeHLC('b');
const ta = a(), tb = b(ta);                          // b 看到 a 的写入
console.log(tb.l > ta.l || tb.p > ta.p);             // true：因果序正确
```
