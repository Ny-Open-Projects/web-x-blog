---
title: [ARC-322] 笔试题：实现组件库的 Portal 与弹层定位？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-322：笔试题：实现组件库的 Portal 与弹层定位？
**题目**：实现 `Popover` 组件：1) 内容通过 Portal 渲染到 body；2) 根据触发元素自动定位（bottom 首选，空间不足自动翻转 top）；3) 点击外部关闭；4) Esc 关闭并归还焦点。
**评分点**：
- Portal 正确创建/复用容器节点（不要每次渲染新建 div）。
- 定位计算正确（getBoundingClientRect + 翻转逻辑 + 边界 8px 预留）。
- 外部点击监听正确（pointerdown 捕获阶段 + Portal 内容不算外部）。
- 焦点管理（打开时焦点进弹层，Esc 归还触发元素）与监听器清理完整。
```tsx
function Popover({ trigger, children }) {
  const [open, setOpen] = useState(false);
  const anchorRef = useRef<HTMLButtonElement>(null);
  const popRef = useRef<HTMLDivElement>(null);
  const [pos, setPos] = useState({ top: 0, left: 0, place: 'bottom' });
  useEffect(() => {
    if (!open) return;
    const a = anchorRef.current!.getBoundingClientRect();
    const space = window.innerHeight - a.bottom;
    const place = space > 100 ? 'bottom' : 'top';                        // 2) 自动翻转
    const p = popRef.current!;
    setPos({
      top: place === 'bottom' ? a.bottom + window.scrollY + 8
                              : a.top + window.scrollY - p.offsetHeight - 8,
      left: a.left + window.scrollX,
      place,
    });
    const onDown = (e: PointerEvent) => {                                // 3) 外部点击
      if (!popRef.current?.contains(e.target as Node) && !anchorRef.current?.contains(e.target as Node))
        setOpen(false);
    };
    const onKey = (e: KeyboardEvent) => { if (e.key === 'Escape') { setOpen(false); anchorRef.current?.focus(); } };
    document.addEventListener('pointerdown', onDown, true);
    document.addEventListener('keydown', onKey);
    return () => { document.removeEventListener('pointerdown', onDown, true); document.removeEventListener('keydown', onKey); };
  }, [open]);
  return (<>
    <button ref={anchorRef} onClick={() => setOpen(o => !o)}>{trigger}</button>
    {open && createPortal(
      <div ref={popRef} role="dialog" style={{ position: 'absolute', ...pos }}>{children}</div>,
      getPortalRoot()   // 复用容器：document.getElementById('portal-root') ?? create once
    )}
  </>);
}
```
