---
title: [ZSM-194] 笔试：手写 useDebouncedQuery（防抖 + 请求竞态守卫 + 缓存命中的搜索 Hook）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-194：手写 useDebouncedQuery（防抖 + 请求竞态守卫 + 缓存命中的搜索 Hook）
**需求**：实现 `useDebouncedQuery(keyword, { fetcher, delay = 300 })`：1) keyword 输入防抖 delay 后才请求；2) 请求竞态守卫：只有最后一次防抖结果的响应被采纳；3) 命中缓存（相同 keyword 已有结果且未失效）立即返回不发请求；4) 清空 keyword（空串）不发请求并清结果；5) 卸载取消在途请求。返回 { data, loading, error }。

```javascript
export function useDebouncedQuery(keyword, { fetcher, delay = 300, ttl = 30000 }) {
  const [st, setSt] = useState({ data: null, loading: false, error: null })
  const cache = useRef(new Map())       // keyword -> { data, ts }
  const ctrl = useRef(), timer = useRef(), alive = useRef(true)
  useEffect(() => () => { alive.current = false }, [])

  useEffect(() => {
    const kw = keyword.trim()
    if (!kw) {                                   // 空串：清结果不发请求
      clearTimeout(timer.current); ctrl.current?.abort()
      setSt({ data: null, loading: false, error: null })
      return
    }
    const hit = cache.current.get(kw)
    if (hit && Date.now() - hit.ts < ttl) {      // 缓存命中：立即返回
      setSt({ data: hit.data, loading: false, error: null })
      return
    }
    timer.current = setTimeout(async () => {     // 防抖后请求
      ctrl.current?.abort()
      ctrl.current = new AbortController()
      setSt(s => ({ ...s, loading: true }))
      try {
        const data = await fetcher(kw, ctrl.current.signal)
        cache.current.set(kw, { data, ts: Date.now() })
        if (alive.current) setSt({ data, loading: false, error: null })
      } catch (e) {
        if (alive.current && e.name !== 'AbortError')
          setSt(s => ({ ...s, loading: false, error: e }))
      }
    }, delay)
    return () => clearTimeout(timer.current)     // 关键词再变：重置防抖
  }, [keyword, delay, ttl])

  return st
}

// 评分点：
// 1. 防抖 timer 在依赖变化时清理（连续输入只发最后一次）
// 2. AbortController + alive 双守卫
// 3. TTL 缓存命中零请求立即返回（等价 dedupingInterval+staleTime）
// 4. 空关键词清场语义
// 5. AbortError 不污染 error 状态
```
