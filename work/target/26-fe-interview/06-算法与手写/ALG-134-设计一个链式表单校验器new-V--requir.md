---
title: [ALG-134] 设计一个链式表单校验器：`new V().required().minLen(6).pattern(...)` 每个规则可自由组合，返回第一个错误信息给 UI 展示？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-134：设计一个链式表单校验器：`new V().required().minLen(6).pattern(...)` 每个规则可自由组合，返回第一个错误信息给 UI 展示？
**答**：链式 API 的关键是每个规则方法把校验函数 push 进数组后 `return this`（返回实例自身才能继续点）。validate 时按注册顺序执行，遇第一个错误短路返回（fail-fast），全过返回 null。多字段并发校验用 `Promise.all` 收集各自结果。规则执行 O(规则数)。

```javascript
class Validator {
  constructor() { this.rules = []; }
  required(msg = '必填项') {
    this.rules.push(v => (v != null && v !== '' ? null : msg));
    return this;                       // 返回 this 维持链式
  }
  minLen(n, msg = `至少 ${n} 个字符`) {
    this.rules.push(v => (v && v.length >= n ? null : msg));
    return this;
  }
  pattern(re, msg = '格式不正确') {
    this.rules.push(v => (re.test(v) ? null : msg));
    return this;
  }
  validate(value) {
    for (const rule of this.rules) {
      const err = rule(value);
      if (err) return err;             // fail-fast：返回第一个错误
    }
    return null;
  }
}
// new Validator().required().minLen(6).pattern(/^\w+$/).validate(input)
// 多字段：fields.map(f => f.validator.validate(f.value))
```
