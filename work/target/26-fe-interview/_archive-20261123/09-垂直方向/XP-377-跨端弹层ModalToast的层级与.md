---
title: [XP-377] 跨端弹层（Modal/Toast）的层级与性能管理
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-377：跨端弹层（Modal/Toast）的层级与性能管理

**答**：
- 层级：统一 z-index 管理（层级 token），防弹层互相覆盖错乱。
- 性能：弹层动画合成层、弹层内容懒渲染（打开时挂载）、关闭后卸载（或保活按配置）。
- 栈管理：弹层栈（后开先关）、遮罩点击规则统一。

```javascript
// 弹层栈
class ModalStack {
  constructor() { this.stack = []; this.base = 1000; }
  open(modal) {
    this.stack.push(modal);
    modal.zIndex = this.base + this.stack.length * 10;
    return () => this.close(modal);
  }
  close(modal) {
    const i = this.stack.indexOf(modal);
    if (i >= 0) this.stack.splice(i, 1);
    this.stack[this.stack.length - 1]?.focus();        // 焦点回落
  }
}
```
