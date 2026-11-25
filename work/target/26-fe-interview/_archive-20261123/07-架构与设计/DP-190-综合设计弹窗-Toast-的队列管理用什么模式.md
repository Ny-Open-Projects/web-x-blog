---
title: [DP-190] 综合设计：弹窗/Toast 的队列管理用什么模式？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-190：综合设计：弹窗/Toast 的队列管理用什么模式？（高频）
**答**：
- 组合：单例（全局唯一 ModalManager）、策略（入队策略：串行排队/替换/合并同类）、命令（open/close 命令化，可编程取消）、观察者（弹窗生命周期事件给埋点/焦点管理）、享元（同类型弹窗复用容器实例）。
- 核心问题：并发弹窗的层叠灾难——必须由唯一管理者裁决顺序与互斥，而不是各组件自己 v-if。
- 细节：优先级队列（错误 > 确认 > 提示）、z-index 自增、焦点圈（focus trap）与 ESC 处理集中实现。

```javascript
class ModalManager {                                          // 单例
  static #inst; static get inst() { return (this.#inst ??= new ModalManager()); }
  #queue = []; #current = null; #z = 1000; #listeners = new Set(); #types = new Map();
  register(type, Component) { this.#types.set(type, Component); }    // 工厂：弹窗类型目录
  on(fn) { this.#listeners.add(fn); return () => this.#listeners.delete(fn); }
  open(request) {                                              // 命令：open 请求对象
    const merged = { priority: 1, mode: 'queue', ...request };
    const same = this.#queue.find((r) => r.key === merged.key);
    if (same) return same.promise;                             // 合并同类：相同 key 不重复弹
    merged.priority === 0 ? this.#queue.unshift(merged) : this.#queue.push(merged);   // 优先级入队
    this.#queue.sort((a, b) => b.priority - a.priority);
    this.#next();
    return merged.promise;                                     // Promise 化结果：await 用户选择
  }
  #next() {
    if (this.#current || !this.#queue.length) return;          // 策略：串行排队
    const req = this.#queue.shift();
    const Comp = this.#types.get(req.type);                    // 工厂产出
    this.#current = req;
    req.zIndex = ++this.#z;
    this.#listeners.forEach((f) => f({ type: 'open', req }));  // 观察者：埋点/焦点锁定
    render(Comp, { req, close: (result) => this.#close(req, result) });
  }
  #close(req, result) {
    req.resolve(result);                                       // 命令完成：把用户选择交回调用方
    this.#current = null;
    this.#listeners.forEach((f) => f({ type: 'close', req }));
    this.#next();
  }
}
export const modal = ModalManager.inst;                        // 单例出口
// 调用方：await 拿结果，先来后到自动排队，错误弹窗插队
async function onDelete() {
  const ok = await modal.open({ type: 'confirm', key: 'delete-order', priority: 1, title: '确认删除？' });
  if (ok) await api.remove(id);
}
modal.open({ type: 'error', key: 'net-error', priority: 0, title: '网络异常' });   // priority 0 插队
```
