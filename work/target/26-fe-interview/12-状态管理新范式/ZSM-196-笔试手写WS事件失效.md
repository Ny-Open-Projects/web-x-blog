---
title: [ZSM-196] 笔试：手写 useInvalidateOnEvent（WS 事件 → 缓存失效映射 Hook）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-196：手写 useInvalidateOnEvent（WS 事件 → 缓存失效映射 Hook）
**需求**：实现 `useInvalidateOnEvent(wsEvent$, mapping, qc)`：1) mapping 是 `事件类型 → 失效 key 前缀（可多个）` 的映射表；2) 收到事件时对映射的 key 批量失效（活跃查询重取，不活跃只标 stale）；3) 短时间同类事件去重（500ms 窗口内重复失效同一 key 只执行一次）；4) 不同事件类型的失效互不合并（保证语义独立）；5) 卸载取消订阅。核心考点：失效去重窗口 + 映射表配置化。

```javascript
export function useInvalidateOnEvent(wsEvent$, mapping, qc) {
  const inflight = useRef(new Map())   // key签名 -> timer
  const mRef = useRef(mapping); mRef.current = mapping

  useEffect(() => {
    const sub = wsEvent$.subscribe(({ type, payload }) => {
      const prefixes = mRef.current[type]
      if (!prefixes) return                       // 未注册事件：忽略
      const now = Date.now()
      prefixes.forEach(prefix => {
        const sig = JSON.stringify(prefix)
        const last = inflight.current.get(sig)
        if (last && now - last.at < 500) return   // 500ms 去重窗口
        inflight.current.set(sig, { at: now })
        qc.invalidateQueries({
          predicate: (q) => matchPrefix(q.queryKey, prefix),
        })
      })
    })
    return () => sub.unsubscribe()                // 卸载断开
  }, [qc])

  return null
}

function matchPrefix(key, prefix) {
  return prefix.every((v, i) =>
    v === '*' || JSON.stringify(v) === JSON.stringify(key[i]))
}

// const mapping = {
//   'order.updated': [['orders'], ['dashboard', 'stats']],
//   'goods.price':   [['goods', '*']],          // * 通配任意值
// }
// useInvalidateOnEvent(ws.messages$, mapping, queryClient)

// 评分点：
// 1. 映射表驱动：事件类型 → 失效域，配置集中可审计
// 2. 500ms 同 key 去重防失效风暴（高频推送场景）
// 3. predicate 前缀匹配（支持 * 通配位）
// 4. 未注册事件静默忽略，不影响其他事件
// 5. 卸载 unsubscribe 无泄漏
```
