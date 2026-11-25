---
title: [MP-286] 笔试：手写 Taro 下 useRequest hook（竞态 + 卸载防护）
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 笔试题, 19]
type: 笔试题
---

## MP-286：笔试：手写 Taro 下 useRequest
**答**：React hook：run(args) 发请求（Taro.request）；seq 防竞态；页面卸载（useDidShow 对应的 unmount）后不写状态；支持 immediate 自动执行与依赖重发；返回 { data, loading, error, run }。

```javascript
import { useState, useRef, useEffect } from 'react'
import Taro from '@tarojs/taro'
function useRequest(fetcher, { deps = [], immediate = false } = {}) {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const seq = useRef(0)
  const mounted = useRef(true)
  useEffect(() => { mounted.current = true; return () => { mounted.current = false } }, [])
  const run = async (...args) => {
    const id = ++seq.current
    setLoading(true); setError(null)
    try {
      const res = await fetcher(...args)
      if (id !== seq.current || !mounted.current) return // 竞态/已卸载
      setData(res)
    } catch (e) {
      if (id === seq.current && mounted.current) setError(e)
    } finally {
      if (id === seq.current) setLoading(false)
    }
  }
  useEffect(() => { if (immediate) run() }, deps)
  return { data, loading, error, run }
}
// 页面卸载：Taro 页面组件 unmount 时 effect cleanup 触发（与浏览器一致）
```
**评分点**：
- seq 竞态防护。
- mounted 引用防卸载后 setState（React 18 不再警告但仍是无谓计算）。
- deps 重发。
- loading 状态归属最后一次请求。
