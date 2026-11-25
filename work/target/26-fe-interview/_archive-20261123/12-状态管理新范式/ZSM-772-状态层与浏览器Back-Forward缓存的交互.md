---
title: [ZSM-772] Back/Forward Cache（bfcache）：前进后退时的状态恢复语义
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-772：Back/Forward Cache（bfcache）：前进后退时的状态恢复语义

**答**：
- bfcache 让「后退」瞬间恢复页面（内存快照，不重新加载），对状态层的冲击：**页面冻结时内存 store 完好保留**（无需持久化），但 WS 断了、定时器停了、请求中断了——恢复（pageshow persisted=true）时要做的不是「恢复状态」而是「恢复活性」：重连 WS（带 lastSeq 追平）、补发暂停的任务、刷新 stale 数据。
- 阻断 bfcache 的行为要自查：unload/beforeunload 监听（bfcache 直接禁用）、未及时 close 的 WS（Chrome 会拒缓存的连接类）——「能否进 bfcache」本身是性能优化点（后退速度差 10 倍）。
- pageshow/pagehide 纪律：`pagehide` 时 flush 队列 + 断 WS + 暂停轮询；`pageshow (persisted=true)` 时重连 + 追平 + revalidate stale 查询。注意 bfcache 恢复的 `pageshow` 不触发 `load`——挂载型初始化不会重跑，恢复逻辑必须挂在 pageshow。
- 与多 tab 的交叉：bfcache 恢复后 BroadcastChannel 连接仍在（共享内存），但其他 tab 可能已推进状态——恢复时向 leader 请求快照对齐（ZSM-578 的 welcome 握手复用）。
- 追问钩子：bfcache 与「敏感状态」——登录态/token 在 bfcache 快照中驻留内存，公共电脑的后退可能恢复已登出会话——登出时显式 `location.replace` 打破 bfcache 或在后退恢复时强制 revalidate 会话。

```javascript
// bfcache 生命周期管理
class BfcacheAware {
  setup() {
    window.addEventListener('pagehide', (e) => {
      if (e.persisted) {                    // 进入 bfcache：冻结前清理
        wsClient.close()                    // WS 必须断（否则拒缓存）
        poller.pause()
        offlineQueue.flush().catch(() => {})  // 尽力 flush
      }
    })
    window.addEventListener('pageshow', (e) => {
      if (e.persisted) {                    // 从 bfcache 恢复：恢复活性
        wsClient.connect(url, { lastSeq })  // 重连 + 追平（ZSM-727）
        poller.resume()
        queryClient.invalidateQueries({     // 冻结期间的数据可能过期
          refetchType: 'active',
          predicate: (q) => q.isStaleByTime(q.options.staleTime),
        })
        leaderElector.recheck()             // leader 可能已换人
      }
    })
  }
}

// 不要阻断 bfcache
// ✗ window.addEventListener('unload', cleanup)      —— 禁用 bfcache
// ✓ 用 pagehide 替代

// 敏感状态：登出时打破 bfcache
async function logout() {
  await api.revoke()
  store.reset()
  // location.replace 不产生历史条目且退出当前文档（bfcache 快照失效）
  location.replace('/login?reason=logout')
}
// 或：后退恢复时强制会话校验
window.addEventListener('pageshow', async (e) => {
  if (e.persisted) {
    const valid = await api.checkSession().catch(() => false)
    if (!valid) location.replace('/login?reason=session-expired')
  }
})
```
