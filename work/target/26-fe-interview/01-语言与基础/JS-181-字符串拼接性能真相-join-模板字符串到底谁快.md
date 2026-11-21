---
title: [JS-181] 字符串拼接性能真相？+=、join、模板字符串到底谁快？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-181：字符串拼接性能真相？+=、join、模板字符串到底谁快？

**答**：
- V8 现代优化下三者差距已很小：+= 使用 cons-string（绳结结构）实现 O(1) 延迟拼接，短拼接通常最快且可读性最好。
- "join 比 += 快"的结论来自老引擎时代每次 += 都整串复制；现在只有大量碎片一次性合并时 join 才有优势。
- 真正的坑不是 API 选型而是：拼接产生的 rope 在后续 indexOf/slice 等操作时才触发展平（flatten，O(n)）；超大字符串长期驻留内存；循环 innerHTML 反复解析。
- 经验法则：HTML 拼接用模板字符串一次成型；超大文本累积（日志/CSV 导出）用数组收集最后 join；热点循环避免对同一长串反复子串操作。
- 一切以实测为准：用 performance.now 在目标环境跑基准，别背过时结论。

```javascript
// 1. 基准测试脚手架：预热触发 JIT 后再计时
function bench(name, fn, times = 1e4) {
  fn(0); // 预热
  const t0 = performance.now();
  for (let i = 0; i < times; i++) fn(i);
  console.log(name, (performance.now() - t0).toFixed(1), 'ms');
}

const parts = Array.from({ length: 1000 }, (_, i) => 'frag-' + i);

// 2. += 循环拼接：V8 cons-string 优化，短拼接近似 O(1)
bench('+= 拼接', () => {
  let s = '';
  for (const p of parts) s += p;
});

// 3. join：攒碎片一次合并，碎片极多时占优
bench('join 拼接', () => parts.join(''));

// 4. 模板字符串：生成 HTML 首选，一次成型
bench('模板字符串', () => {
  let s = '';
  for (const p of parts) s += `<li>${p}</li>`;
});

// 5. 经验结论落地
// 少量拼接（<100 次）：可读性优先，直接模板字符串
// 循环拼 HTML：先拼完整字符串再一次 innerHTML，绝不循环 append
// 超大文本累积：数组收集 + 最后 join('')
// 展平陷阱：cons-string 在执行 search/slice 时才展平为平铺串，
//          拼完立即做这类操作会把 O(1) 拼接退化为 O(n)
```
