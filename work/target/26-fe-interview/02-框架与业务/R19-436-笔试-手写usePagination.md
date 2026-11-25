---
title: [R19-436] 笔试：手写 usePagination（URL 同步分页 hook）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## R19-436：笔试：手写 usePagination

**答**：实现 `usePagination({ fetchPage, pageSize, initialPage })`：① 返回 { items, page, total, setPage, isLoading, error }；② page 变化自动请求（AbortController 取消旧请求——竞态守卫）；③ 预取下一页（当前页加载完成后 idle 预取 page+1）；④ 页码回退语义（请求失败保持当前页数据）；⑤ 与 URL 的 page 参数同步（history state）。写出实现。

```javascript
export function usePagination({ fetchPage, pageSize = 20, initialPage = 1 }) {
  const [items, setItems] = useState([]);
  const [page, setPageState] = useState(initialPage);
  const [total, setTotal] = useState(0);
  const [isLoading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const ctrlRef = useRef(null);

  const load = useCallback(async (p, { silent = false } = {}) => {
    ctrlRef.current?.abort();                         // 取消旧请求
    const ctrl = ctrlRef.current = new AbortController();
    if (!silent) setLoading(true);
    try {
      const r = await fetchPage(p, pageSize, ctrl.signal);
      setItems(r.items); setTotal(r.total); setPageState(p);
      history.replaceState({ page: p }, '', `?page=${p}`);   // URL 同步
      // 预取下一页(idle 时, 不抢主线程)
      requestIdleCallback?.(() => fetchPage(p + 1, pageSize, new AbortController().signal).catch(() => {}));
    } catch (e) {
      if (e.name !== 'AbortError') setError(e);      // 失败保持当前页数据
    } finally { setLoading(false); }
  }, [fetchPage, pageSize]);

  useEffect(() => { load(initialPage); }, []);        // 首次
  const setPage = useCallback((p) => { setError(null); load(p); }, [load]);
  return { items, page, total, setPage, isLoading, error };
}
```

**评分点**：
- AbortController 竞态守卫（翻页连点）
- idle 预取下一页（不抢主线程，独立 signal）
- 失败保持当前页（回退语义）+ URL replaceState 同步
- silent 预取不闪 loading
