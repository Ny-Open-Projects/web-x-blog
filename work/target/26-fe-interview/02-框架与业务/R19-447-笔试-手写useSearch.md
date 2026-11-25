---
title: [R19-447] 笔试：手写 useSearch（搜索框完整方案）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 数据流]
type: 笔试题
---

## R19-447：笔试：手写 useSearch

**答**：实现 `useSearch({ fetcher, debounceMs = 300 })`：① 返回 { query, setQuery, results, status }；② 防抖触发（输入停止后请求）；③ 竞态守卫（seq + AbortController 双保险）；④ IME 兼容（composition 期间不触发请求——中文输入法）；⑤ 空输入直接清结果不请求；⑥ status: idle/typing/loading/success/error。写出实现。

```javascript
export function useSearch({ fetcher, debounceMs = 300 }) {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState(null);
  const [status, setStatus] = useState('idle');
  const seqRef = useRef(0);
  const ctrlRef = useRef(null);
  const composingRef = useRef(false);

  useEffect(() => {
    if (composingRef.current) return;                 // IME 组合中不触发
    if (!query.trim()) { setResults(null); setStatus('idle'); return; }
    setStatus('typing');
    const timer = setTimeout(async () => {
      const mySeq = ++seqRef.current;
      ctrlRef.current?.abort();
      const ctrl = ctrlRef.current = new AbortController();
      setStatus('loading');
      try {
        const r = await fetcher(query, ctrl.signal);
        if (mySeq !== seqRef.current) return;         // 旧响应丢弃
        setResults(r); setStatus('success');
      } catch (e) {
        if (e.name === 'AbortError') return;
        if (mySeq === seqRef.current) setStatus('error');
      }
    }, debounceMs);
    return () => clearTimeout(timer);
  }, [query, fetcher, debounceMs]);

  const onChange = useCallback((e) => setQuery(e.target.value), []);
  const onCompositionStart = () => { composingRef.current = true; };
  const onCompositionEnd = useCallback((e) => {
    composingRef.current = false;
    setQuery(e.target.value);                         // 组合结束触发
  }, []);

  return { query, setQuery, results, status,
    inputProps: { value: query, onChange, onCompositionStart, onCompositionEnd } };
}
```

**评分点**：
- 双保险竞态守卫（seq 令牌 + AbortController）
- IME 兼容（composition 事件门控）
- 空输入短路（不请求直接清）
- 五态状态机与 inputProps 透传设计
