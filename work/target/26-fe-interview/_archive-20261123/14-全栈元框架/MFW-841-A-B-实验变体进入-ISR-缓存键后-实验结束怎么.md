---
title: [MFW-841] A/B 实验变体进入 ISR 缓存键后，实验结束怎么回收缓存
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-841：A/B 实验变体进入 ISR 缓存键后，实验结束怎么回收缓存

**答**：
- 结论：变体必须进入缓存键（否则两变体互相污染），但会成倍增加键基数；实验结束后必须及时清理旧变体缓存，否则成为永久僵尸。
- 落地：键格式 path@version#exp:variant；实验结束事件触发按变体批量清理，设实验 TTL 兜底自动过期。
- 追问钩子：实验期改流量比例会不会导致缓存抖动？——不会，比例只影响新请求分桶，键不变。

```javascript
function expKey(path, version, exp, variant) {
  return `${path}@${version}#${exp}:${variant}`;     // 变体进键，隔离
}
const CACHE = new Map();
function getOrSet(key, render) {
  if (!CACHE.has(key)) CACHE.set(key, render());
  return CACHE.get(key);
}
// 实验结束：按前缀批量失效该实验所有变体
function retireExperiment(exp) {
  for (const k of CACHE.keys()) {
    if (k.includes('#' + exp + ':')) CACHE.delete(k);
  }
}
getOrSet(expKey('/home', 3, 'btn', 'A'), () => '<A>');
getOrSet(expKey('/home', 3, 'btn', 'B'), () => '<B>');
retireExperiment('btn');                             // 两种变体缓存都清理
console.log(CACHE.size);                              // 0
```
