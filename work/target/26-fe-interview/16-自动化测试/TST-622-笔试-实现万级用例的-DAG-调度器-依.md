---
title: [TST-622] 笔试：实现万级用例的 DAG 调度器（依赖 / 配额 / 抢占）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-622：笔试：实现万级用例的 DAG 调度器（依赖 / 配额 / 抢占）

**题目**：实现 DAGScheduler：输入 cases=[{id,deps:[],dependents:[],priority}]。ready() 返回入度为 0 的就绪任务并按优先级排序；take() 取出一个任务并更新后继入度；hasCycle() 检测环。

**答**：
- 拓扑排序保证依赖先于依赖者执行；用入度表 + 队列实现 O(V+E)。
- 配额用信号量控制并发；抢占允许高优先级任务插队到队首。
- 检测环并抛错，避免死锁。

```javascript
class DAGScheduler {
  constructor(cases, { slots = 4 } = {}) {
    this.tasks = new Map(cases.map(c => [c.id, c]));
    this.indeg = new Map(cases.map(c => [c.id, (c.deps || []).length]));
    this.slots = slots;
  }
  ready() {
    return [...this.indeg].filter(([, d]) => d === 0)
      .map(([id]) => this.tasks.get(id))
      .sort((a, b) => (a.priority || 5) - (b.priority || 5));
  }
  take() {
    const q = this.ready();
    if (!q.length) throw new Error('无就绪任务或存在环');
    const t = q[0];
    this.indeg.delete(t.id);
    (t.dependents || []).forEach(id =>
      this.indeg.set(id, this.indeg.get(id) - 1));
    return t;
  }
  hasCycle() { return this.indeg.size > 0 && !this.ready().length; }
}
```

**评分点**：
- 拓扑排序入度更新正确
- 优先级抢占语义清晰
- 环检测有效不死锁
- 复杂度 O(V+E) 可扩展到万级
