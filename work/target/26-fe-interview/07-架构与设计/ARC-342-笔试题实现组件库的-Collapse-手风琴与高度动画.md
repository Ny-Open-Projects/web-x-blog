---
title: [ARC-342] 笔试题：实现组件库的 Collapse 手风琴与高度动画？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-342：笔试题：实现组件库的 Collapse 手风琴与高度动画？
**答**：实现 Collapse：1) 手风琴模式（accordion：同时只展开一个）；2) 展开收起高度动画（内容高度未知，不写死 max-height）；3) 动画结束才真正卸载内容（或保留 DOM 用 grid 动画）；4) 受控 activeKeys。
**评分点**：
- 高度动画不写死 max-height（scrollHeight 测量或 grid-template-rows 1fr 技巧）。
- 动画状态机正确（opening/open/closing/closed），transitionend 清理。
- 手风琴逻辑正确（单键集合运算）。
- 受控/非受控双模式。
```tsx
function Collapse({ items, activeKeys: ak, defaultActiveKeys = [], accordion = false, onChange }) {
  const [inner, setInner] = useState(new Set(defaultActiveKeys));
  const active = ak ? new Set(ak) : inner;
  const toggle = (key: string) => {
    const next = new Set(active);
    if (next.has(key)) next.delete(key);
    else { if (accordion) next.clear(); next.add(key); }        // 1) 手风琴
    ak ? onChange?.([...next]) : setInner(next);                 // 4) 双模式
  };
  return items.map(it => {
    const open = active.has(it.key);
    return (
      <div key={it.key} className="collapse-item">
        <button aria-expanded={open} onClick={() => toggle(it.key)}>{it.title}</button>
        <div className="collapse-body" style={{
          display: 'grid',
          gridTemplateRows: open ? '1fr' : '0fr',                // 2) grid 高度动画，内容高度未知也可
          transition: 'grid-template-rows .25s',
        }}>
          <div style={{ overflow: 'hidden' }}>{it.content}</div> {/* 3) 收起时内容仍挂载（保留状态），overflow 裁剪 */}
        </div>
      </div>
    );
  });
}
```
