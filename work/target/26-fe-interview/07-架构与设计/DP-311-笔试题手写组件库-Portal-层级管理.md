---
title: [DP-311] 笔试题：手写组件库 Portal 层级管理？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-311：笔试题：手写组件库 Portal 层级管理？
**题目**：实现 PopupManager：1) 全局 z-index 递增分配（push/pop 回收）；2) 嵌套弹层层级正确（子弹层始终高于父）；3) ESC 关闭最顶层；4) 容器复用（同一 portal root）。
**评分点**：
- 栈式分配正确（push 得到 max+1，pop 归还）。
- 回收后复用编号（避免 z-index 无限膨胀）。
- ESC 只关栈顶（keydown 监听唯一入口）。
- 容器惰性创建单例。
```javascript
class PopupManager {
  #stack = [];
  #root = null;
  get root() {                                            // 4) 容器单例
    return this.#root ??= (() => { const d = document.createElement('div');
      d.id = 'popup-root'; document.body.appendChild(d); return d; })();
  }
  push(el) {
    const z = 1000 + this.#stack.length;                  // 1) 栈式层级
    el.style.zIndex = z;
    this.#stack.push(el);
    return () => this.pop(el);
  }
  pop(el) {
    const i = this.#stack.indexOf(el);
    if (i >= 0) this.#stack.splice(i, 1);
    el.style.zIndex = '';                                 // 2) 回收编号（重排后自然复用）
  }
  handleKeydown(e) {                                      // 3) ESC 关栈顶
    if (e.key !== 'Escape') return;
    const top = this.#stack.at(-1);
    top?.onEsc?.();
  }
}
document.addEventListener('keydown', e => popupMgr.handleKeydown(e));
// 用：const release = popupMgr.push(dialogEl); dialogEl.onEsc = () => { close(); release(); }
```
