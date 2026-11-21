---
title: [JS-105] 函子是什么？Maybe 与 Either 如何做错误处理？（简化版）
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-105：函子是什么？Maybe 与 Either 如何做错误处理？（简化版）

**答**：
- 函子：实现了 `map` 且持有值的容器，map 对内部值应用函数后返回新容器，不拆箱。
- Maybe：包装可能为空的值，空值时 map 直接跳过——把判空逻辑集中到容器里。
- Either：Left 表示错误、Right 表示成功，错误发生时 map 自动短路，最后用 fold 统一分支。
- 价值：错误处理从"散落的 if/try"变成"可组合的数据流"。

```javascript
// Maybe：处理 null / undefined
class Maybe {
  static of(x) { return new Maybe(x); }
  constructor(x) { this._value = x; }
  map(fn) { return this._value == null ? this : Maybe.of(fn(this._value)); }
  getOrElse(dv) { return this._value == null ? dv : this._value; }
}

const user = { address: null };
const city = Maybe.of(user.address)          // null
  .map((a) => a.city)                        // 空值自动跳过
  .map((c) => c.toUpperCase())
  .getOrElse('UNKNOWN');
console.log(city); // UNKNOWN — 没有任何 if 判断

// Either：区分错误与成功两条流水线
class Left {
  constructor(v) { this._value = v; }
  map() { return this; }                     // 错误继续传递，跳过计算
  fold(onLeft, _onRight) { return onLeft(this._value); }
}
class Right {
  constructor(v) { this._value = v; }
  map(fn) { return new Right(fn(this._value)); }
  fold(_onLeft, onRight) { return onRight(this._value); }
}
const Either = { of: (x) => new Right(x), left: (x) => new Left(x) };

const parseJSON = (s) => {
  try { return Either.of(JSON.parse(s)); }
  catch (e) { return Either.left(`解析失败: ${e.message}`); }
};
parseJSON('{"a":1}').fold(
  (err) => console.log('失败', err),
  (v) => console.log('成功', v.a)   // 成功 1
);
parseJSON('{bad}').fold(
  (err) => console.log('失败', err), // 失败 解析失败: ...
  (v) => console.log(v)
);
```
