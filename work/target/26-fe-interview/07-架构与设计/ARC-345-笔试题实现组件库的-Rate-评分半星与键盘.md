---
title: [ARC-345] 笔试题：实现组件库的 Rate 评分半星与键盘？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-345：笔试题：实现组件库的 Rate 评分半星与键盘？
**答**：实现 Rate 评分：1) 鼠标移动位置决定半星（x 相对星宽 < 50% 为半星）；2) 点击提交（区分半星/整星）；3) hover 预览不提交、移出恢复当前值；4) 键盘操作（左右半星步进、上下整星步进）；5) allowClear（再次点击同值清零）。
**评分点**：
- 半星判定正确（clientX - rect.left 与 width/2 比较）。
- hover 预览态与提交值分离（displayValue vs value）。
- 键盘步进 0.5/1 两档正确。
- allowClear 逻辑正确（同值再点 → 0）。
```tsx
function Rate({ value, allowHalf = true, allowClear = false, onChange, count = 5 }) {
  const [hover, setHover] = useState<number | null>(null);
  const display = hover ?? value;                                     // 3) 预览与提交分离
  const onMove = (i: number, e: React.MouseEvent) => {
    if (!allowHalf) return setHover(i + 1);
    const rect = (e.currentTarget as HTMLElement).getBoundingClientRect();
    setHover(i + (e.clientX - rect.left < rect.width / 2 ? 0.5 : 1)); // 1) 半星
  };
  const onPick = (i: number, half: boolean) => {
    const v = i + (allowHalf && half ? 0.5 : 1);
    if (allowClear && v === value) return onChange(0);                // 5) 清零
    onChange(v);
  };
  const onKey = (e: React.KeyboardEvent) => {
    const stepV = { ArrowRight: 0.5, ArrowLeft: -0.5, ArrowUp: 1, ArrowDown: -1 }[e.key];
    if (stepV) { e.preventDefault();
      onChange(Math.min(count, Math.max(0, value + stepV))); }        // 4) 半星/整星两档
  };
  return <div role="radiogroup" tabIndex={0} onKeyDown={onKey} onMouseLeave={() => setHover(null)}>
    {Array.from({ length: count }, (_, i) => {
      const fill = display >= i + 1 ? 'full' : display >= i + 0.5 ? 'half' : 'empty';
      return <span key={i} role="radio" aria-checked={value === i + 1}
        onMouseMove={e => onMove(i, e)}
        onClick={e => onPick(i, (e.clientX - (e.currentTarget as HTMLElement).getBoundingClientRect().left) < ((e.currentTarget as HTMLElement).clientWidth / 2))}>
        <Star fill={fill}/>
      </span>;
    })}
  </div>;
}
```
