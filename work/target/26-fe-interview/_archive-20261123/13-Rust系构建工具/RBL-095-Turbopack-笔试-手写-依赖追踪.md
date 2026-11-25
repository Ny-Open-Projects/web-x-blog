---
title: [RBL-095] 笔试：手写简化增量计算引擎（依赖追踪 + 失效重算）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-095：笔试：手写简化增量计算引擎（依赖追踪 + 失效重算）
**题目**：实现一个 mini turbo-tasks：1) task(name, fn) 注册计算任务，fn 内通过 read(key) 读文件内容（模拟输入）；2) 执行时自动追踪 fn 读过的所有输入 key，形成依赖边；3) setFile(key, content) 更新输入后，依赖该 key 的任务标记失效；4) get(name) 惰性取值：未失效直接返回缓存，失效则重算；5) 环形依赖检测报错。

```javascript
function createEngine(files) {
  const cache = new Map();    // name -> { value, deps:Set<string> }
  const dirty = new Set();    // 失效任务名
  const running = new Set();  // 环检测

  const engine = {
    // 任务定义：fn(read) 内部所有 read 都被追踪
    task(name, fn) {
      cache.set(name, { fn, deps: new Set(), value: undefined, fresh: false });
      return name;
    },
    read(key) {
      if (engine.__current) engine.__current.deps.add(key); // 自动追踪
      return files.get(key);
    },
    setFile(key, content) {
      files.set(key, content);
      for (const [name, t] of cache)
        if (t.deps.has(key)) { t.fresh = false; dirty.add(name); }
    },
    async get(name) {
      const t = cache.get(name);
      if (!t) throw new Error(`unknown task ${name}`);
      if (t.fresh) return t.value;
      if (running.has(name)) throw new Error(`循环依赖: ${name}`);
      running.add(name);
      const prev = engine.__current;
      engine.__current = t;
      t.deps = new Set();            // 重算时重建依赖边
      t.value = await t.fn(engine.read.bind(engine));
      engine.__current = prev;
      running.delete(name);
      t.fresh = true; dirty.delete(name);
      return t.value;
    },
    __current: null,
    isDirty: (n) => dirty.has(n),
  };
  return engine;
}
module.exports = { createEngine };

// 用法
// const e = createEngine(new Map([['a.ts', 'x']]));
// e.task('parseA', (read) => 'parsed:' + read('a.ts'));
// await e.get('parseA');          // 首算
// e.setFile('a.ts', 'y');         // 失效
// e.isDirty('parseA') === true    // 惰性：get 时才重算
```
**评分点**：
- 执行期自动追踪 read 输入（依赖边动态构建，非静态声明）。
- 失效标记惰性重算（不是立即重算，lazy 是关键语义）。
- 环检测（running 集合 + 报错）。
- 重算时重建 deps（避免残留旧边导致漏失效）。
- 能类比 turbo-tasks：Vc 值、惰性、依赖图失效，正是此模型的工业级实现。
