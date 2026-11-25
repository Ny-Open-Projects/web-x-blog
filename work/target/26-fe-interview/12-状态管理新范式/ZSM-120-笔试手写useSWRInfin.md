---
title: [ZSM-120] 笔试：手写 useSWRInfinite 核心（分页游标缓存 + 终止判断 + 加载更多）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-120：手写 useSWRInfinite 核心（分页游标缓存 + 终止判断 + 加载更多）
**答**：实现 `useSWRInfinite(getKey, fetcher)`。getKey(index, previousPageData) 返回页 key 或 null（终止）；`data` 为页数组二维结构；`setSize(n)` 触发加载到第 n 页；`size` 当前页数；每页独立缓存，重复 setSize 不重复请求。边界：previousPageData 为 null（无上游）时 index 0；getKey 返回 null 的页不存在。

```javascript
export function useSWRInfinite(getKey, fetcher) {
  const [size, setSize] = useState(1)
  const [pages, setPages] = useState([])   // 第 i 页数据，undefined 表示未加载

  useEffect(() => {
    let cancelled = false
    async function load() {
      const next = []
      let prev
      for (let i = 0; i < size; i++) {
        const key = getKey(i, prev)                  // 用上游页生成下游 key
        if (key == null) break                       // 终止：没有更多页
        if (pageCache.has(key)) { next[i] = pageCache.get(key) }
        else {
          const page = await fetcher(key)
          pageCache.set(key, page)                   // 每页独立缓存
          next[i] = page
        }
        prev = next[i]
      }
      if (!cancelled) setPages(next)
    }
    load()
    return () => { cancelled = true }                // 防卸载后 setState
  }, [size])

  return {
    data: pages.filter(Boolean),                     // 只暴露已加载页
    size,
    setSize: (n) => setSize(Math.max(1, n)),          // 加载更多/收缩
  }
}
const pageCache = new Map()

// 评分点：
// 1. getKey(index, previousPageData) 依赖上游页生成游标 key
// 2. getKey 返回 null 即终止循环，不再发请求
// 3. 页缓存命中不重复请求（等价 SWR 去重）
// 4. 卸载/重入用 cancelled 标志防竞态 setState
// 5. data 为过滤后的页数组，size/setSize 语义正确
```
