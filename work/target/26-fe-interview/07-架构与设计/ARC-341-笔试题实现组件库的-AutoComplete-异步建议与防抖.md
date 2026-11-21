---
title: [ARC-341] 笔试题：实现组件库的 AutoComplete 异步建议与防抖？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-341：笔试题：实现组件库的 AutoComplete 异步建议与防抖？
**题目**：实现 AutoComplete：1) 输入防抖 300ms 后请求建议；2) 竞态处理（慢请求不覆盖新结果，AbortController）；3) 空值不发请求并清空建议；4) 键盘选择（上下+回车）；5) loading 态展示。
**评分点**：
- 防抖实现正确（定时器清理）。
- 竞态：每个请求带 AbortController，新请求 abort 旧请求；或用请求序号过滤过期响应。
- 空输入清理建议列表并 abort 在途请求。
- 键盘选择与 loading 态正确。
```tsx
function AutoComplete({ fetcher, onSelect }) {
  const [kw, setKw] = useState('');
  const [opts, setOpts] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [active, setActive] = useState(-1);
  const timer = useRef<ReturnType<typeof setTimeout>>();
  const ctrl = useRef<AbortController>();
  const search = (q: string) => {
    clearTimeout(timer.current);
    ctrl.current?.abort();                                       // 2) 取消旧请求
    if (!q.trim()) { setOpts([]); return; }                      // 3) 空值清理
    setLoading(true);
    timer.current = setTimeout(async () => {
      ctrl.current = new AbortController();
      try {
        const list = await fetcher(q, { signal: ctrl.current.signal });
        setOpts(list); setActive(-1); setLoading(false);
      } catch (e) { if (!String(e).includes('abort')) setLoading(false); }
    }, 300);                                                     // 1) 防抖
  };
  const onKey = (e: React.KeyboardEvent) => {                    // 4)
    if (e.key === 'ArrowDown') { e.preventDefault(); setActive(a => Math.min(a + 1, opts.length - 1)); }
    if (e.key === 'ArrowUp')   { e.preventDefault(); setActive(a => Math.max(a - 1, 0)); }
    if (e.key === 'Enter' && active >= 0) { onSelect(opts[active]); setOpts([]); }
    if (e.key === 'Escape') setOpts([]);
  };
  return <div className="ac">
    <input value={kw} onChange={e => { setKw(e.target.value); search(e.target.value); }} onKeyDown={onKey}/>
    {loading && <Spinner/>}
    {opts.length > 0 && <ul role="listbox">{opts.map((o, i) =>
      <li key={o} aria-selected={i === active} onMouseDown={() => { onSelect(o); setOpts([]); }}>{o}</li>)}</ul>}
  </div>;
}
```
