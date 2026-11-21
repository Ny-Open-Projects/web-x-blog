---
title: [ARC-334] 笔试题：实现组件库的 Dropdown 键盘导航？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-334：笔试题：实现组件库的 Dropdown 键盘导航？
**题目**：实现 Dropdown 菜单键盘交互：1) Enter/ArrowDown 打开；2) 打开后 ArrowUp/Down 在项间移动（跳过 disabled 项，循环）；3) Enter 激活当前项；4) Esc 关闭归还焦点到触发器；5) Home/End 跳首尾。
**评分点**：
- roving tabindex 模式正确（当前项 tabIndex=0 其余 -1），而不是管理 DOM focus 数组。
- disabled 项跳过逻辑正确（防死循环：全部 disabled 时不动）。
- Esc 归还焦点到触发器。
- 循环移动边界处理正确。
```tsx
function DropdownMenu({ items }) {
  const [open, setOpen] = useState(false);
  const [active, setActive] = useState(-1);
  const triggerRef = useRef<HTMLButtonElement>(null);
  const listRef = useRef<HTMLUListElement>(null);
  const focusItem = (i: number) => {
    const els = [...listRef.current!.querySelectorAll('li:not([aria-disabled])')];
    if (!els.length) return;                                   // 全 disabled 不动
    const idx = els.findIndex(el => el.dataset.index === String(i));
    (els[idx < 0 ? 0 : idx] as HTMLElement).focus();
  };
  const onKey = (e: React.KeyboardEvent) => {
    const enabled = items.map((it, i) => it.disabled ? null : i).filter(v => v !== null);
    const cur = enabled.indexOf(active);
    const move = (dir: 1 | -1) => enabled.length &&
      setActive(enabled[(cur + dir + enabled.length) % enabled.length]);  // 2) 循环+跳 disabled
    switch (e.key) {
      case 'ArrowDown': e.preventDefault(); open ? move(1) : (setOpen(true), setActive(enabled[0])); break;
      case 'ArrowUp':   e.preventDefault(); open && move(-1); break;
      case 'Home':      e.preventDefault(); enabled.length && setActive(enabled[0]); break;
      case 'End':       e.preventDefault(); enabled.length && setActive(enabled.at(-1)); break;
      case 'Enter':     e.preventDefault(); active >= 0 && items[active].onSelect?.(); break;
      case 'Escape':    setOpen(false); triggerRef.current?.focus(); break;  // 4) 归还焦点
    }
  };
  return (
    <>
      <button ref={triggerRef} aria-haspopup="menu" aria-expanded={open}
        onKeyDown={e => e.key === 'Enter' && setOpen(true)} onClick={() => setOpen(o => !o)}>Menu</button>
      {open && <ul role="menu" ref={listRef} onKeyDown={onKey}>
        {items.map((it, i) =>
          <li key={i} role="menuitem" data-index={i} aria-disabled={it.disabled || undefined}
            tabIndex={i === active ? 0 : -1}                       {/* 1) roving tabindex */}
            onClick={() => !it.disabled && it.onSelect?.()}>{it.label}</li>)}
      </ul>}
    </>
  );
}
```
