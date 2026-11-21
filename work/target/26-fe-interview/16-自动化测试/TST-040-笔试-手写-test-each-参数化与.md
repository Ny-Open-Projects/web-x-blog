---
title: [TST-040] 笔试：手写 test.each 参数化与 only / skip 支持
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-040：笔试：手写 test.each 参数化与 only / skip 支持
**答**：
- 需求：给迷你 runner 加 `it.each(cases)(title, fn)`：cases 为数组，title 支持 %s/%d 占位符替换，每行数据展开为独立用例；同时实现 `it.only/it.skip`。
- 核心：each 先做「数据行 → 用例列表」的展开（占位符格式化 + 参数透传给 fn），only/skip 用标记字段过滤执行阶段。
- 边界：有 only 时只跑 only 用例；skip 用例计入 skipped 并在报告标注；数据行里的对象/数组参数原样传递不展开。

```javascript
const cases = []; // { name, fn, mode }  mode: 'normal'|'only'|'skip'

function formatTitle(title, row) {
  let i = 0;
  return title.replace(/%[sdj%]/g, (m) => (m === '%%' ? '%' : row[i++]));
}

function it(name, fn, mode = 'normal') { cases.push({ name, fn, mode }); }
it.only = (name, fn) => it(name, fn, 'only');
it.skip = (name, fn) => it(name, fn, 'skip');
it.each = (rows) => (title, fn) => {
  rows.forEach((row) => {
    const args = Array.isArray(row) ? row : [row];
    it(formatTitle(title, args), () => fn(...args));
  });
};

async function run() {
  let passed = 0, failed = 0, skipped = 0;
  const only = cases.filter((c) => c.mode === 'only');
  const list = only.length ? only : cases;           // 有 only 只跑 only
  for (const c of list) {
    if (c.mode === 'skip') { skipped++; console.log(`○ ${c.name}`); continue; }
    try { await c.fn(); passed++; console.log(`✔ ${c.name}`); }
    catch (e) { failed++; console.error(`✘ ${c.name}: ${e.message}`); }
  }
  console.log(`${passed} passed / ${failed} failed / ${skipped} skipped`);
  process.exitCode = failed ? 1 : 0;
}

// ---- 用法 ----
it.each([
  [0, '¥0.00'],
  [1234.5, '¥1,234.50'],
  [-20, '-¥20.00'],
])('formatMoney(%d) -> %s', (input, expected) => {
  if (formatMoney(input) !== expected) throw new Error(`${input} != ${expected}`);
});
it.skip('优惠券叠加（规则待定）', () => {});
run();
```
**评分点**：
- each 展开：占位符替换 + 参数透传，错误报告能定位到具体数据行。
- only 存在时短路全量列表。
- skipped 计数并展示（不留盲区）。
- 知道真实框架 each 还支持模板字符串表格与 concurrent 组合。
