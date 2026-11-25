---
title: [FRP-195] 手写 Portal 弹窗管理器：多弹窗的 z-index 栈如何管理？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-195：手写 Portal 弹窗管理器：多弹窗的 z-index 栈如何管理？

**答**：
- 需求：多个弹窗层叠时，**后打开的永远盖住先打开的**，关闭中间某层不影响其他层——用栈结构 + 单调递增的 z-index 种子。
- 实现：全局 manager 维护 `stack: Map<id, zIndex>`；mount 时 push 拿到当前最大 zIndex+1，unmount 时按 id pop。
- 配套能力：ESC 关闭最顶层、遮罩点击只响应**栈顶**弹窗（下层遮罩不拦截）、body 滚动锁定计数（多层叠加时只有全部关闭才解锁）。
- 渲染载体用 createPortal（ReactDOM）挂到 body 下的专用容器，避免应用内 overflow 裁剪。

```javascript
// 简化实现，帮助理解弹窗栈管理
class ModalManager {
  constructor() {
    this.stack = [];             // [{ id, zIndex }]：栈顶是最后打开的
    this.zIndexSeed = 1000;      // 单调递增种子
    this.scrollLockCount = 0;
  }
  open(id) {
    const zIndex = ++this.zIndexSeed;          // 永远比之前的都大
    this.stack.push({ id, zIndex });
    this.lockScroll();
    return zIndex;
  }
  close(id) {
    const idx = this.stack.findIndex(m => m.id === id);
    if (idx > -1) this.stack.splice(idx, 1);   // 从中间移除也不影响其他层
    this.unlockScroll();
  }
  isTop(id) { return this.stack[this.stack.length - 1]?.id === id; }
  lockScroll() {
    if (++this.scrollLockCount === 1) document.body.style.overflow = 'hidden';
  }
  unlockScroll() {
    if (--this.scrollLockCount === 0) document.body.style.overflow = '';
  }
}
const modalManager = new ModalManager();

function Modal({ id, visible, onClose, children }) {
  const [zIndex] = useState(() => visible ? modalManager.open(id) : 0);
  useEffect(() => {
    if (visible) {
      const z = modalManager.open(id);
      // 实际实现中 zIndex 应为 state；此处简化
      const onKey = (e) => {
        if (e.key === 'Escape' && modalManager.isTop(id)) onClose?.(); // ESC 只关栈顶
      };
      window.addEventListener('keydown', onKey);
      return () => {
        window.removeEventListener('keydown', onKey);
        modalManager.close(id);
      };
    }
  }, [visible, id]);

  if (!visible) return null;

  return createPortal(
    <div className="modal-mask" style={{ zIndex }} onClick={() => {
      if (modalManager.isTop(id)) onClose?.();   // 遮罩点击只响应栈顶
    }}>
      <div className="modal-body" onClick={(e) => e.stopPropagation()}>{children}</div>
    </div>,
    document.getElementById('modal-root')       // 统一挂载容器
  );
}

// z-index 演示：
// open('a') -> 1001；open('b') -> 1002（b 盖住 a）
// close('a') -> 栈中只剩 b，b 仍 1002 —— 无需重排（单调递增的意义）
// 传统方案"关一个就全体重排 zIndex"的问题被彻底规避
```
