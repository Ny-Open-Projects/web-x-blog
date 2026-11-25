---
title: [ZSM-572] React StrictMode 对状态调试的影响：探针为什么触发两次
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-572：React StrictMode 对状态调试的影响：探针为什么触发两次

**答**：
- StrictMode 在 dev 下刻意 double-invoke：渲染函数执行两次、effect 挂载-卸载-再挂载、useState/useMemo 回调双跑。目的：暴露副作用不纯的代码。这对状态探针的影响是**每个事件可能被记录两次**，日志/回放数据污染。
- 三类影响点：1) setState 探针——如果 setState 在渲染期间被调用（反模式），探针记录翻倍；2) effect 里的 subscribe——挂载两次，探针里的订阅计数虚高；3) 手写 store 的初始化函数被调用两次（Zustand 的 initializer 是纯的没关系，带副作用初始化的会出 bug——这正是 StrictMode 要暴露的）。
- 正确姿势：探针按「事件内容指纹」去重（同 seq 内容 diff 相同则合并）；订阅清理函数必须正确（StrictMode 的卸载重挂就是测试清理函数的）；初始化保持纯函数，副作用放 action。
- 判别技巧：探针里打 `console.count` 看倍数——2 倍 = StrictMode（dev only），不稳定倍数 = 并发渲染中断重放，要按 seq 去重。
- 追问钩子：StrictMode 下的「双跑」不是 bug，是工具——写状态层时应该先在 StrictMode 下跑通，否则并发特性开启后（transition/offscreen）问题会以更隐蔽的方式出现。

```javascript
// 探针去重：内容指纹合并
function dedupeProbe(onEvent) {
  let last = null
  return (event) => {
    const fp = `${event.action}|${event.keys.join(',')}|${JSON.stringify(event.next)}`
    if (last?.fp === fp && event.seq === last.seq) return   // StrictMode 双跑：合并
    last = { fp, seq: event.seq }
    onEvent(event)
  }
}

// StrictMode 安全的初始化（纯）vs 不安全（副作用）
const useCounter = create(() => {
  // 不好：副作用初始化，StrictMode 下跑两次 → 双订阅
  // window.addEventListener('resize', onResize)
  return { count: 0 }
})

// 好的模式：订阅放 action/effect，初始化纯
function useCountListener() {
  useEffect(() => {
    const onResize = () => useCounter.setState({ vw: innerWidth })
    window.addEventListener('resize', onResize)
    return () => window.removeEventListener('resize', onResize)  // 清理函数：StrictMode 必须正确
  }, [])
}

import { StrictMode } from 'react'
createRoot(document.getElementById('root')).render(
  <StrictMode><App /></StrictMode>   // 状态层先在它下面跑通
)
```
