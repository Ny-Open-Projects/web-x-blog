---
title: [R19-446] 笔试：手写 useFocusTrap 与 useRovingFocus（a11y hooks）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 交互]
type: 笔试题
---

## R19-446：笔试：手写 useFocusTrap

**答**：实现：① `useFocusTrap(containerRef, active)`：Tab 循环在容器内、打开时聚焦第一个可聚焦元素、关闭时焦点还原到触发者；② `useRovingFocus(itemsRef, { orientation })`：roving tabindex 模式（方向键移动 focus、Home/End 跳边界）；③ 焦点还原的触发者记录（打开时 document.activeElement）；④ 卸载清理；⑤ shadow DOM 兼容说明（getRootNode 查找）。写出实现。

```javascript
const FOCUSABLE = 'a[href],button:not([disabled]),input,select,textarea,[tabindex]:not([tabindex="-1"])';

export function useFocusTrap(containerRef, active) {
  const returnFocusRef = useRef(null);
  useEffect(() => {
    if (!active) return;
    returnFocusRef.current = document.activeElement;    // 记录触发者
    const el = containerRef.current;
    const focusables = () => [...el.querySelectorAll(FOCUSABLE)];
    focusables()[0]?.focus();                           // 打开聚焦第一个
    const trap = (e) => {
      if (e.key !== 'Tab') return;
      const f = focusables();
      const first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { last.focus(); e.preventDefault(); }
      else if (!e.shiftKey && document.activeElement === last) { first.focus(); e.preventDefault(); }
    };
    el.addEventListener('keydown', trap);
    return () => {
      el.removeEventListener('keydown', trap);
      returnFocusRef.current?.focus();                  // 关闭还原焦点
    };
  }, [active]);
}

export function useRovingFocus(itemsRef, { orientation = 'vertical' } = {}) {
  const onKeyDown = useCallback((e) => {
    const items = [...itemsRef.current.querySelectorAll('[role$="item"],button')];
    const i = items.indexOf(document.activeElement);
    const dirs = orientation === 'vertical'
      ? { ArrowDown: 1, ArrowUp: -1 }
      : { ArrowRight: 1, ArrowLeft: -1 };
    if (e.key in dirs) {
      e.preventDefault();
      items[(i + dirs[e.key] + items.length) % items.length].focus();
    }
    if (e.key === 'Home') { e.preventDefault(); items[0].focus(); }
    if (e.key === 'End') { e.preventDefault(); items.at(-1).focus(); }
  }, []);
  return { onKeyDown };
}
```

**评分点**：
- 焦点陷阱的循环边界（首尾 wrap）与触发者还原
- roving tabindex 的方向键循环 + Home/End
- FOCUSABLE 选择器的完备性（disabled 排除）
- 卸载清理与焦点归还时序
