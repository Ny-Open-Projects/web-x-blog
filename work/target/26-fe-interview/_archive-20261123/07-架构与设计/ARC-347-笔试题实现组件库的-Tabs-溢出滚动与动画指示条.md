---
title: [ARC-347] 笔试题：实现组件库的 Tabs 溢出滚动与动画指示条？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-347：笔试题：实现组件库的 Tabs 溢出滚动与动画指示条？
**题目**：实现 Tabs：1) 指示条动画（transform 跟随激活 tab 位置与宽度）；2) 超出容器宽度出现左右滚动按钮；3) 激活项自动滚入可视区；4) 键盘左右切换。
**评分点**：
- 指示条定位用 offsetLeft/offsetWidth + transform 动画（不用 layout 属性动画）。
- 溢出检测（scrollWidth > clientWidth）与按钮出现逻辑。
- scrollIntoView 用 scrollLeft 计算（容器内滚动，不用全局 API 防页面滚动）。
- 键盘切换与受控 activeKey。
```tsx
function Tabs({ items, activeKey, onChange }) {
  const listRef = useRef<HTMLDivElement>(null);
  const [bar, setBar] = useState({ x: 0, w: 0 });
  const [overflow, setOverflow] = useState(false);
  const syncBar = useCallback(() => {
    const el = listRef.current!.querySelector(`[data-key="${activeKey}"]`) as HTMLElement;
    if (!el) return;
    setBar({ x: el.offsetLeft, w: el.offsetWidth });                // 1) transform 动画数据
    const box = listRef.current!;
    const l = el.offsetLeft, r = el.offsetLeft + el.offsetWidth;
    if (l < box.scrollLeft) box.scrollTo({ left: l - 16, behavior: 'smooth' });          // 3) 滚入
    if (r > box.scrollLeft + box.clientWidth) box.scrollTo({ left: r - box.clientWidth + 16, behavior: 'smooth' });
  }, [activeKey]);
  useEffect(syncBar, [syncBar]);
  useEffect(() => {
    const box = listRef.current!;
    const check = () => setOverflow(box.scrollWidth > box.clientWidth);
    check();
    const ro = new ResizeObserver(check); ro.observe(box);
    return () => ro.disconnect();
  }, []);
  const onKey = (e: React.KeyboardEvent) => {                       // 4)
    if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
    const idx = items.findIndex(t => t.key === activeKey);
    const next = items[(idx + (e.key === 'ArrowRight' ? 1 : -1) + items.length) % items.length];
    onChange(next.key);
  };
  return <div className="tabs">
    {overflow && <button className="arrow" onClick={() => listRef.current!.scrollBy({ left: -120, behavior: 'smooth' })}>‹</button>} {/* 2) */}
    <div ref={listRef} className="tab-list" role="tablist" tabIndex={0} onKeyDown={onKey}>
      {items.map(t => <div key={t.key} data-key={t.key} role="tab" aria-selected={t.key === activeKey}
        className={t.key === activeKey ? 'tab active' : 'tab'}
        onClick={() => onChange(t.key)}>{t.label}</div>)}
      <span className="tab-bar" style={{ transform: `translateX(${bar.x}px)`, width: bar.w }}/>
    </div>
    {overflow && <button className="arrow" onClick={() => listRef.current!.scrollBy({ left: 120, behavior: 'smooth' })}>›</button>}
  </div>;
}
```
