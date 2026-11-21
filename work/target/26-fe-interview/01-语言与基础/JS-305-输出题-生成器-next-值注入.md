---
title: [JS-305] 输出题：生成器 next 值注入
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 生成器]
type: 笔试题
---

## JS-305：输出题：生成器 next 值注入

**题目**：判断 yield 表达式接收值与产出值的对应关系；第一次 next 的参数去哪了。

**答**：
```javascript
function* gen() {
  const a = yield 1;
  const b = yield a * 10;
  return b + 1;
}
const g = gen();
g.next();      // { value: 1, done: false } —— 第一次 next 的参数被丢弃
g.next(5);     // a = 5 → { value: 50, done: false }
g.next(2);     // b = 2 → { value: 3, done: true }

// 陷阱：for-of 消费时 next 无参 —— yield 表达式值为 undefined
function* g2() { const x = yield 1; console.log(x); }
for (const v of g2()) { /* v === 1 */ } // x 打印 undefined

// 陷阱：yield 优先级低 —— yield a + 10 是 yield (a+10)？错！
function* g3() {
  const r = yield 3 + 10;   // 解析为 (yield 3) + 10 → TypeError? 
  // 实际：yield 3 + 10 = yield (3+10) = 13 —— 加法优先级高于 yield ✅
  // 但 const r = yield 3, 4; // 逗号在 yield 后是序列 → 只 yield 3
}
```
```
规则总结：
- next(arg) 的 arg 成为「当前暂停的 yield 表达式」的值；首个 next 的 arg 被忽略
- for-of/spread 等自动消费调用无参 next → yield 表达式值为 undefined
- yield 优先级低于 + 但高于赋值右侧；`const a = yield 1, b = 2` 会产生意外解析
```

**评分点**：
- 首个 next 参数被丢弃的规则
- 双向传值的映射关系（a=5 → 产出 50）
- 自动消费（for-of）时 yield 值为 undefined 的陷阱
- yield 优先级与解析边界的辨析（加分）
