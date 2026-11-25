---
title: [RBL-405] 笔试：手写构建耗时 Profile 收集器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-405：手写构建耗时 Profile 收集器
**答**：实现 `createProfiler()`：1) `span(name)` 返回 end()——记录嵌套 span（父子关系由调用栈推断）；2) `mark(event)` 时间点标记；3) 输出 chrome tracing 格式（{ name, cat, ts, dur, ph: 'X' }）与汇总表（各 span 自身耗时/含子耗时）；4) 异步 span 支持（end 可在 promise 后调用）；5) 输出按开始时间排序；6) 嵌套聚合正确（父 span 含子 span 时间）。

```javascript
export function createProfiler() {
  const spans = []
  const marks = []
  const stack = []

  function span(name, cat = 'default') {
    const start = performance.now()
    const parent = stack[stack.length - 1] ?? null
    const rec = { name, cat, start, end: null, parent, children: [] }
    spans.push(rec)
    if (parent) parent.children.push(rec)
    stack.push(rec)
    return {
      end() {
        rec.end = performance.now()
        stack.pop()                                          // 栈顶必须是自己
        return rec.end - rec.start
      },
    }
  }

  function mark(event) { marks.push({ event, at: performance.now() }) }

  function report() {
    const completed = spans.filter((s) => s.end !== null).sort((a, b) => a.start - b.start)
    const trace = completed.map((s) => ({ name: s.name, cat: s.cat, ts: s.start, dur: s.end - s.start, ph: 'X' }))
    const selfTime = (s) => (s.end - s.start) - s.children.reduce((a, c) => a + (c.end - c.start), 0)
    const summary = completed.map((s) => ({
      name: s.name, total: +(s.end - s.start).toFixed(2), self: +selfTime(s).toFixed(2),
      depth: depthOf(s),
    })).sort((a, b) => b.self - a.self)
    return { trace, summary, marks }
  }

  function depthOf(s) { let d = 0, p = s.parent; while (p) { d++; p = p.parent } return d }
  return { span, mark, report }
}

// 用法
const p = createProfiler()
const b = p.span('build'); const c = p.span('convert'); await work(); c.end(); b.end()
// summary: convert self 时间排序 → 优化优先级
```
**评分点**：
- 嵌套 span 由栈推断父子（push/pop 配对；end 后 pop 正确）
- self time 计算（总时长减子时长）——优化排序的正确口径
- chrome tracing 格式兼容（ts/dur/ph: 'X'）
- 异步 span 支持（end 时机由调用方控制）
