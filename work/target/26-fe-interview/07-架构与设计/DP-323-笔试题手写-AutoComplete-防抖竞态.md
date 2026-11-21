---
title: [DP-323] 笔试题：手写 AutoComplete（防抖+竞态+键盘）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-323：笔试题：手写 AutoComplete（防抖+竞态+键盘）？
**题目**：实现 AutoComplete：1) 输入 300ms 防抖后请求；2) 新请求 abort 旧请求；3) 键盘上下选择 + Enter 提交；4) 空输入清空建议。
**评分点**：
- AbortController 竞态处理正确。
- 防抖清理（timer ref）。
- 键盘选择循环+边界。
- Enter 提交后关闭列表。
```tsx
function AutoComplete({ fetcher, onSelect }) {
  const [q, setQ] = useState(''); const [opts, setOpts] = useState([]);
  const [active, setActive] = useState(-1);
  const timer = useRef(); const ctrl = useRef();
  const search = (v) => {
    clearTimeout(timer.current);
    ctrl.current?.abort();
    if (!v.trim()) { setOpts([]); return; }                  // 4)
    timer.current = setTimeout(async () => {
      ctrl.current = new AbortController();
      try { setOpts(await fetcher(v, { signal: ctrl.current.signal })); setActive(-1); }
      catch (e) { if (!(e instanceof DOMException && e.name === 'AbortError')) throw e; }  // 2) 吞 abort
    }, 300);
  };
  const onKey = (e) => {                                     // 3)
    if (e.key === 'ArrowDown') setActive(a => Math.min(a + 1, opts.length - 1));
    if (e.key === 'ArrowUp') setActive(a => Math.max(a - 1, 0));
    if (e.key === 'Enter' && opts[active]) { onSelect(opts[active]); setOpts([]); }
    if (e.key === 'Escape') setOpts([]);
  };
  return <input value={q} onChange={e => { setQ(e.target.value); search(e.target.value); }}
    onKeyDown={onKey} list="ac-list"/>;
}
```
