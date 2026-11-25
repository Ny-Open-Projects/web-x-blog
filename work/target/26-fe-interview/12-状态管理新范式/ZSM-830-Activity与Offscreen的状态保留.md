---
title: [ZSM-830] React 的 Offscreen/Activity：组件隐藏时的状态保留语义
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-830：React 的 Offscreen/Activity：组件隐藏时的状态保留语义

**答**：
- `<Activity mode="hidden">`（原 Offscreen）：组件隐藏但**状态保留**——卸载语义变了：hidden 模式下组件不渲染但 state/订阅保留，切回 visible 时恢复。「页签切换不丢状态」从「手写 keep-alive（ZSM-585 可见性暂停）」变成框架能力。
- 对状态层的影响：1) **effect 生命周期**——hidden 时 effect 清理照常执行（订阅要退订！），visible 时重新挂载——「隐藏≠免清理」，探针照常工作；2) 内存语义——hidden 组件树占内存，长列表 hidden 会驻留大缓存，配合 ZSM-609 的泄漏面要评估「hidden 保留多少值得」；3) 订阅策略——hidden 期间 store 变更是否通知该组件（React 会延迟到恢复时统一 flush），状态库无需特殊处理但要防「恢复时积压变更一次性应用」的渲染风暴（批处理天然覆盖）。
- 与路由缓存的关系：keep-alive 式路由（tab 型后台系统）之前用「路由不卸载 + display:none」的 hack，Activity 提供原生语义——状态层的路由缓存策略从「自建缓存 store」变为「声明 Activity mode」。
- 边界：hidden 组件的 timer/WS 订阅该不该跑？——语义上「隐藏=降级」：UI 更新暂停但数据订阅可保留（恢复时快速对齐），这正是 ZSM-585 可见性分级的状态版本。
- 追问钩子：Activity 与 bfcache（ZSM-772）的区别——Activity 是应用内组件级保留（跨 tab 切换），bfcache 是浏览器级页面保留（跨导航）；两者恢复纪律不同但都遵循「冻结→恢复→对齐」三步。

```javascript
import { Activity, useState } from 'react'

function AppTabs({ activeTab }) {
  return (
    <>
      <Activity mode={activeTab === 'feed' ? 'visible' : 'hidden'}>
        <FeedPage />        {/* hidden 时 state 保留，effect 清理/重挂 */}
      </Activity>
      <Activity mode={activeTab === 'chat' ? 'visible' : 'hidden'}>
        <ChatPage />        {/* 切回时消息状态还在，需恢复对齐 */}
      </Activity>
    </>
  )
}

function FeedPage() {
  // hidden 期间：effect 清理照常执行 → 订阅退订、WS 可降频
  useEffect(() => {
    const unsub = wsClient.subscribe('feed', handler)   // visible 重挂时重新订阅
    return unsub                                        // hidden 时退订（纪律不变）
  }, [])

  // 恢复时的状态对齐：hidden 期间积压的 store 变更会在此一次性 flush
  // （React 延迟通知 + 批处理天然覆盖，无需手写）
  const items = useFeed((s) => s.items)
  return <List items={items} />
}

// keep-alive 路由的旧 hack（Activity 出现前）
// <div style={{ display: active ? 'block' : 'none' }}><Page /></div>
// ← 不卸载组件：状态保留但 effect 不清理（泄漏温床）——Activity 修复了这个语义
```
