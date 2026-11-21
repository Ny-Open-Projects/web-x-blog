---
title: [JS-125] try/catch 的性能开销与使用边界？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-125：try/catch 的性能开销与使用边界？

**答**：
- 现代 V8 里 try/catch 本身近乎零开销；真正贵的是抛出过程——构建 Error 对象要采集堆栈。
- 用异常做控制流（循环里 throw 当 break）比正常判断慢一个数量级以上。
- 热路径（每帧执行/大循环）优先"返回错误值"而不是抛错；边界处（模块入口、API 层）用 try/catch 兜底。
- catch 子句不带绑定（`catch {}`，ES2019）可在确定不需要错误对象时减少噪音。

```javascript
function measure(label, fn) {
  const t = performance.now();
  fn();
  console.log(label, (performance.now() - t).toFixed(2), 'ms');
}

// 正常路径 + try/catch：几乎无开销
measure('正常返回 x1e5（带 try/catch）', () => {
  const f = () => 1;
  for (let i = 0; i < 1e5; i++) { try { f(); } catch {} }
});

// 抛错路径：构建堆栈非常昂贵（跑 1e3 次即可感知量级差异）
measure('抛错 x1e3', () => {
  const f = () => { throw new Error('boom'); };
  for (let i = 0; i < 1e3; i++) { try { f(); } catch {} }
});

// 边界示范：
// 1. ✗ 用异常做控制流
function findBad(list, target) {
  try { list.forEach((v) => { if (v === target) throw 'found'; }); }
  catch { return true; }
  return false;
}
// 2. ✓ 普通判断
const findGood = (list, target) => list.includes(target);

// 3. ✓ 返回错误值风格（热路径）
function parseSafe(s) {
  try { return { ok: true, value: JSON.parse(s) }; }
  catch { return { ok: false }; } // catch 不带绑定
}
console.log(parseSafe('{"a":1}'), parseSafe('{bad}'));
```
