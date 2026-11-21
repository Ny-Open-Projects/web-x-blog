---
title: [ZSM-191] 笔试：手写 useSyncedTabs（BroadcastChannel 跨标签状态同步 Hook）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-191：手写 useSyncedTabs（BroadcastChannel 跨标签状态同步 Hook）
**需求**：实现 `useSyncedTabs(channelName, initial)`：1) 任一标签 setState，其余标签同步收到并更新，发起方自己不重复接收；2) 首次挂载从「已在场的其他标签」拉取当前值（不只拿到 initial）；3) 降级：BroadcastChannel 不可用时用 storage 事件实现；4) 卸载关闭通道不泄漏；5) 返回 [state, setState]。核心考点：握手协议（NEW_PING/STATE）与消息时序。

```javascript
export function useSyncedTabs(channelName, initial) {
  const [state, setState] = useState(initial)
  const peers = useRef([])                    // 在场标签的应答收集
  const ref = useRef(initial); ref.current = state

  useEffect(() => {
    if (typeof BroadcastChannel !== 'undefined') return setupBC()
    return setupStorage()                     // 降级实现

    function setupBC() {
      const bc = new BroadcastChannel(channelName)
      bc.onmessage = ({ data: m }) => {
        if (m.type === 'state' && m.sender !== selfId)
          setState(m.payload)
        if (m.type === 'ping' && m.sender !== selfId) {
          bc.postMessage({ type: 'state', sender: selfId, payload: ref.current })
          peers.current.push(m.sender)
        }
      }
      bc.postMessage({ type: 'ping', sender: selfId })    // 入场握手：拉当前值
      const onStorage = setupStorageFallback(bc)           // storage 事件兜底监听
      return () => { bc.close(); window.removeEventListener('storage', onStorage) }
    }

    function setupStorageFallback(bc) {                    // 降级：storage 事件
      const key = `sync:${channelName}`
      const onStorage = (e) => {
        if (e.key !== key || e.newValue === null) return
        const m = JSON.parse(e.newValue)
        if (m.sender !== selfId && m.type === 'state') setState(m.payload)
      }
      window.addEventListener('storage', onStorage)
      return onStorage
    }
  }, [channelName])

  const set = useCallback((next) => {
    setState(prev => {
      const v = typeof next === 'function' ? next(prev) : next
      bcRef.current?.postMessage({ type: 'state', sender: selfId, payload: v })
      return v
    })
  }, [])
  return [state, set]
}
const selfId = crypto.randomUUID()

// 评分点：
// 1. sender 去重：发起方不回放自己的消息
// 2. 入场握手：ping→state 拉取在场标签当前值
// 3. storage 事件降级路径（BroadcastChannel 兼容旧浏览器/Safari 隐私模式）
// 4. 卸载 close + removeEventListener
// 5. 函数式 setState 在广播前计算，避免闭包旧值
```
