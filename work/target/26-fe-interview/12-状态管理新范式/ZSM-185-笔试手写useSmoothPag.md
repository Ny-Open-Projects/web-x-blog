---
title: [ZSM-185] 笔试：手写 useSmoothPagination（keepPreviousData 语义的分页 Hook）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-185：手写 useSmoothPagination（keepPreviousData 语义的分页 Hook）
**答**：实现 `useSmoothPagination({ fetcher, page, pageSize })`：1) page 变化发起请求；2) 新页数据到达前 data 保留上一页内容（isStale 标记）；3) 响应竞态守卫：只有最新 page 的响应被采纳；4) 首次加载 isLoading；5) 返回 { data, isLoading, isStale, refetch }。核心考点：引用保留 + AbortController + effect 清理顺序。

```javascript
export function useSmoothPagination({ fetcher, page, pageSize }) {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const pageRef = useRef(page)
  const ctrl = useRef()

  useEffect(() => {
    pageRef.current = page
    let alive = true
    setLoading(true)
    ctrl.current?.abort()
    ctrl.current = new AbortController()

    fetcher({ page, pageSize, signal: ctrl.current.signal })
      .then(result => {
        if (!alive || pageRef.current !== page) return   // 竞态守卫：旧响应丢弃
        setData(result)
        setLoading(false)
      })
      .catch(e => {
        if (!alive || e.name === 'AbortError') return
        setLoading(false)
        // 错误处理：保留上一页数据 + 暴露 error（此处省略 error state）
      })
    return () => { alive = false; ctrl.current?.abort() }
  }, [page, pageSize])

  return {
    data,                                  // 上一页数据保留，直到新页到达
    isLoading: loading && data === null,   // 首次才真正 loading
    isStale: loading && data !== null,     // 有旧数据且在刷新
    refetch: () => setTick(t => t + 1),
  }
}
// 评分点：
// 1. keepPreviousData 语义：data 只在新页成功时才覆盖
// 2. isLoading 与 isStale 的区分（首次 vs 平滑翻页）
// 3. 双重竞态守卫：alive 标志 + pageRef 比对 + AbortController
// 4. effect 清理先置 alive=false 再 abort，顺序防泄漏
// 5. 保留旧数据时错误不覆盖 data（降级展示）
```
