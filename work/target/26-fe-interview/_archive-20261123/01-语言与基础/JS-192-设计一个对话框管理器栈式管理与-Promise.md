---
title: [JS-192] 设计一个对话框管理器？栈式管理与 Promise 化返回值怎么实现？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-192：设计一个对话框管理器？栈式管理与 Promise 化返回值怎么实现？

**答**：
- 每个 open() 返回 Promise，resolve 值即"用户结果"：确认 resolve(true)、表单 resolve(values)、取消 resolve(false)，调用方 await 代替回调嵌套。
- 栈式管理：对话框上再弹对话框时用数组栈维护层级，z-index 随栈深递增；ESC/遮罩/关闭动作只作用于栈顶。
- 统一关闭入口 close(value)：从栈中摘除、卸载 DOM、resolve 一次（Promise 重复 resolve 无害但要防止重复操作 DOM）。
- 管理器持有独立容器，动态挂载/卸载；关闭时同步清理事件监听，避免 detached DOM 泄漏。
- 取消与确认语义分离靠 resolve 值区分，调用方 `if (!ok) return` 一行处理，无需 try-catch。

```javascript
// 1. 对话框管理器：栈式 + Promise 返回值
class DialogManager {
  constructor() {
    this.stack = [];
    this.container = document.createElement('div');
    document.body.appendChild(this.container);
  }
  open({ title = '', content = '', confirmText = '确定', cancelText = '取消' } = {}) {
    return new Promise((resolve) => {
      const mask = document.createElement('div');
      mask.style.cssText =
        'position:fixed;inset:0;background:rgba(0,0,0,.4);display:flex;align-items:center;justify-content:center;z-index:' +
        (1000 + this.stack.length);                // z-index 随栈深递增
      mask.innerHTML = `<div role="dialog" style="background:#fff;padding:20px;border-radius:8px">
        <h3>${title}</h3><div>${content}</div>
        <button data-act="cancel">${cancelText}</button>
        <button data-act="confirm">${confirmText}</button></div>`;
      this.container.appendChild(mask);
      const entry = { mask, close };
      function close(value) {
        const idx = manager.stack.indexOf(entry);
        if (idx === -1) return;                    // 防重复关闭
        manager.stack.splice(idx, 1);
        mask.remove();                             // 卸载 DOM，监听随节点回收
        resolve(value);                            // 确认 true / 取消 false
      }
      mask.addEventListener('click', (e) => {
        const act = e.target.dataset?.act;
        if (act === 'confirm') close(true);
        else if (act === 'cancel' || e.target === mask) close(false); // 遮罩点击视为取消
      });
      const manager = this;
      this.stack.push(entry);
    });
  }
  confirm(title, content) { return this.open({ title, content }); }
  closeTop() {                                     // 供 ESC 快捷键调用：只关栈顶
    const top = this.stack[this.stack.length - 1];
    top && top.close(false);
  }
}

// 2. 使用：await 拿结果，多层嵌套自动叠层级
const dm = new DialogManager();
async function onDelete() {
  const ok = await dm.confirm('删除确认', '删除后不可恢复，确定吗？');
  if (!ok) return console.log('已取消');
  console.log('执行删除');
  await dm.confirm('完成', '删除成功');             // 第二层弹窗，栈式管理层级正确
}
document.addEventListener('keydown', (e) => e.key === 'Escape' && dm.closeTop());
onDelete();
```
