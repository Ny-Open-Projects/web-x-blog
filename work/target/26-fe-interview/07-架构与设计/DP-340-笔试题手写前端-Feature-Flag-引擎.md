---
title: [DP-340] 笔试题：手写 Feature Flag 引擎（规则求值）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-340：笔试题：手写 Feature Flag 引擎（规则求值）？
**题目**：实现 FlagEngine：1) flag 定义（default + rules 数组：条件+值）；2) 规则按序求值，首个匹配生效（条件：用户属性/percentage）；3) 依赖 flag（flag 引用其他 flag 结果）；4) 循环依赖检测。
**评分点**：
- 规则求值顺序正确（短路首个匹配）。
- percentage 用稳定 hash 分桶（不随机）。
- 依赖解析拓扑序 + 查环。
- 条件操作符完备（eq/in/gt）。
```javascript
const OPS = { eq: (a, b) => a === b, in: (a, b) => b.includes(a), gt: (a, b) => a > b };
class FlagEngine {
  constructor(private flags, private ctx) { this.#checkCycle(); }
  #checkCycle() {                                          // 4)
    const visit = (name, stack) => { if (stack.has(name)) throw new Error(`循环依赖: ${name}`);
      for (const r of this.flags[name]?.rules ?? [])
        if (r.if?.type === 'flag') visit(r.if.name, new Set([...stack, name])); };
    Object.keys(this.flags).forEach(n => visit(n, new Set()));
  }
  eval(name, resolved = new Map()) {                       // 3) 依赖解析
    if (resolved.has(name)) return resolved.get(name);
    const flag = this.flags[name];
    let value = flag.default;
    for (const rule of flag.rules ?? []) {
      if (rule.if) {
        const cond = rule.if;
        const actual = cond.type === 'flag' ? this.eval(cond.name, resolved) : this.ctx[cond.attr];
        if (!OPS[cond.op](actual, cond.value)) continue;
      }
      if (rule.percentage != null) {
        if (hash(`${name}:${this.ctx.uid}`) % 100 >= rule.percentage) continue;   // 2) 稳定分桶
      }
      value = rule.value; break;                           // 1) 首个匹配生效
    }
    resolved.set(name, value);
    return value;
  }
}
```
