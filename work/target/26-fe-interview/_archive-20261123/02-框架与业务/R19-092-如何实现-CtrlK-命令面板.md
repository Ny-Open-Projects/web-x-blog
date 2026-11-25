---
title: [R19-092] 如何实现 Ctrl+K 命令面板？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-092：如何实现 Ctrl+K 命令面板？
**答**：
- 三层组成：全局快捷键（Ctrl/Cmd+K 唤起）、模糊搜索过滤、键盘上下选择 + Enter 执行。
- 过滤用 useMemo 派生，activeIndex 在查询变化时归零，避免选中项越界。
- 键盘循环用取模实现 ArrowDown/ArrowUp 无边界感；Esc 与点击遮罩关闭。
- 打开时 focus 输入框，关闭时焦点归还触发元素，是无障碍硬指标。

```jsx
// CommandPalette.tsx —— 命令面板：快捷键唤起 + 过滤 + 键盘导航
import { useEffect, useMemo, useRef, useState } from 'react';

function CommandPalette({ open, onClose, commands }) {
  const [query, setQuery] = useState('');
  const [activeIndex, setActiveIndex] = useState(0);
  const inputRef = useRef(null);

  const filtered = useMemo(
    () => commands.filter(c => c.title.toLowerCase().includes(query.toLowerCase())),
    [commands, query],
  );

  useEffect(() => {
    if (!open) return;
    setQuery('');
    setActiveIndex(0);
    inputRef.current?.focus();
    const onKey = (e) => {
      if (e.key === 'Escape') onClose();
      if (e.key === 'ArrowDown') { e.preventDefault(); setActiveIndex(i => (i + 1) % filtered.length); }
      if (e.key === 'ArrowUp') { e.preventDefault(); setActiveIndex(i => (i - 1 + filtered.length) % filtered.length); }
      if (e.key === 'Enter') { filtered[activeIndex]?.run(); onClose(); }
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [open, filtered, activeIndex, onClose]);

  if (!open) return null;
  return (
    <div className="palette-mask" onClick={onClose}>
      <div className="palette" onClick={e => e.stopPropagation()}>
        <input
          ref={inputRef}
          value={query}
          placeholder="搜索命令..."
          onChange={e => { setQuery(e.target.value); setActiveIndex(0); }}
        />
        <ul>
          {filtered.map((c, i) => (
            <li key={c.id} className={i === activeIndex ? 'active' : ''} onClick={() => { c.run(); onClose(); }}>
              {c.title}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
// 全局注册快捷键（配合 R19-073 的 useKeyPress）
// useKeyPress('ctrl.k', e => { e.preventDefault(); setOpen(true); });
```
