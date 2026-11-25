---
title: [DP-530] 笔试：手写 DOM 节点池
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 笔试题, 设计模式]
type: 笔试题
---

## DP-530：笔试：手写 DOM 池

**题目**：实现高频 DOM 创建的节点池 `DomPool`：① acquire(template)：池中取（无则按 template 创建）——如弹幕/粒子/卡片节点；② release(node)：归还（清空内容+复位样式——脏节点清理）；③ 池上限与溢出：池满直接销毁（超出复用价值的节点不占内存）；④ 复用的正确性：节点的事件监听器必须清理（innerHTML 清空不清监听器——removeEventListener 清单）；⑤ 统计：created/reused/destroyed（复用率——优化效果）。写出实现。

```javascript
class DomPool {
  #pool = new Map();      // templateKey -> nodes[]
  #stats = { created: 0, reused: 0, destroyed: 0 };
  constructor({ maxPerTemplate = 50 } = {}) { this.max = maxPerTemplate; }

  acquire(templateKey, createFn) {
    const pool = this.#pool.get(templateKey);
    if (pool?.length) {
      this.#stats.reused++;
      const node = pool.pop();
      node.style.display = '';
      return node;                                     // 复用: 零创建成本
    }
    this.#stats.created++;
    const node = createFn();
    node.__listeners = new Map();                      // 监听器登记 (清理用)
    return node;
  }
  release(templateKey, node) {
    const pool = this.#pool.get(templateKey) ?? this.#pool.set(templateKey, []).get(templateKey);
    if (pool.length >= this.max) { node.remove(); this.#stats.destroyed++; return; }   // 溢出销毁
    node.style.display = 'none';
    // 清理: 内容+监听器
    node.querySelectorAll('*').forEach((c) => c.replaceWith(c.cloneNode(false)));   // 粗暴清监听
    for (const [ev, fn] of node.__listeners ?? []) node.removeEventListener(ev, fn);
    node.textContent = '';
    pool.push(node);
  }
}
// 复用率: reused/(created+reused) — 优化效果可观测
```

**评分点**：
- acquire/release 的池语义（复用零创建成本）
- 脏节点清理（内容+监听器——复用的正确性前提）
- 池上限（超出销毁——内存恒定）
- 复用率统计（优化效果可观测）
