---
title: [WCN-905] computed 之间循环依赖导致死循环，怎么检测并给出可读报错
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-905：computed 之间循环依赖导致死循环，怎么检测并给出可读报错

**答**：
- 结论先行：在依赖图里做环检测——计算 computed 时维护「当前求值栈」，若发现要算的节点已在栈中，就是循环依赖，立即抛错而不是无限递归。
- 原理：每个 computed 有状态（干净/计算中/脏），进入计算标记为「计算中」，退出标记「干净」；读取依赖时若对方处于「计算中」即成环。
- 区分「真循环」与「合理重入」：同步读取成环才是死循环；异步（如 setTimeout 后回写）不构成即时环，不应误报。
- 报错要可读：打印完整依赖链（A → B → C → A）而非笼统 stack overflow，便于定位（设计系统 token 派生链常出这种错）。
- 追问钩子：面试官问「动态依赖会不会形成偶发环」——答：依赖是运行时动态的，某分支才形成的环只有走到该分支才暴露，需保留运行时检测而非仅编译期分析。

```javascript
// 环检测：求值栈 + 状态标记
const STATE = { CLEAN: 0, RUNNING: 1, DIRTY: 2 };
function makeComputed(fn, deps) {
  let value, state = STATE.DIRTY;
  const stack = [];
  return { get value() {
    if (state === STATE.RUNNING) {
      throw new Error('循环依赖: ' + [...stack, this.name].join(' -> '));
    }
    if (state === STATE.CLEAN) return value;
    state = STATE.RUNNING; stack.push(this.name || 'computed');
    try { value = fn(); state = STATE.CLEAN; }
    finally { stack.pop(); }
    return value;
  }, name: '' };
}
const a = makeComputed(() => b.value, []); a.name = 'A';
const b = makeComputed(() => c.value, []); b.name = 'B';
const c = makeComputed(() => a.value, []); c.name = 'C';
try { a.value; } catch (e) { console.log(e.message); } // 循环依赖: A -> B -> C -> A
```
