---
title: [PER-439] DOM 节点的复用与回收：高频列表更新的节点池化与 detached 检查纪律？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-439：高频列表更新的 DOM 节点池化与回收纪律？

**答**:
- 问题：滚动/筛选驱动的列表高频重建——每次 remove + create 数百节点，GC 与布局压力双高。节点池化：卸载的节点存池，挂载时取池节点改内容（比 createElement 快 3~5 倍且无 GC 新分配）。
- 池纪律：① 取出时全字段重置（textContent/classList/dataset 清干净——旧状态残留是最常见 bug）；② 池上限（防病态页面池泄漏）；③ 事件绑定复用——池节点的事件 handler 在创建时绑定一次（委托更好，PER-022），绝不取池后再 addEventListener（重复绑定累积监听器）。
- 回收纪律：remove 后的节点若仍被 JS 引用（数组/Map）→ detached 节点滞留（PER-266 检测）；池本身就是"受控的 detached 集合"——上限 + 定期清空（页面 hidden 时）双保险。
- 验证：Allocation timeline 对比（节点池化后 createNode 分配消失）；DOM 节点计数曲线（Nodes 应稳定不阶梯涨）。

```javascript
class NodePool {
  #free = [];
  constructor(create, reset, { max = 300 } = {}) { Object.assign(this, { create, reset, max }); }
  acquire(data) {
    const el = this.#free.pop() ?? this.#createOnce();
    this.reset(el, data);                               // 全字段重置：防旧状态残留
    return el;
  }
  release(el) { el.remove(); if (this.#free.length < this.max) this.#free.push(el); }
  #createOnce() {
    const el = this.create();
    el.addEventListener('click', (e) => el.__onClick?.(e));   // 事件只绑一次（委托数据在 __onClick）
    return el;
  }
  purge() { this.#free.length = 0; }                    // 页面 hidden 时清池（防受控 detached 堆积）
}
// reset(el, data) 必须重置：textContent/classList/dataset/__onClick —— 旧状态残留是池化头号 bug
// 事件绑定在 createOnce（一次），数据回调走 el.__onClick 动态指向 —— 取池后再绑定 = 监听器累积泄漏
```
