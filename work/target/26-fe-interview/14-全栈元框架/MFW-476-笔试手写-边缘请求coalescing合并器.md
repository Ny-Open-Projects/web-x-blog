---
title: [MFW-476] 笔试：手写边缘请求 coalescing 合并器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-476：边缘请求 coalescing 合并器
**需求**：实现 `coalesce(key, fetcher, { windowMs = 10 })`：1) 10ms 窗口内同 key 的并发调用合并为一次真实 fetch（热门商品页数百并发同 key 是常态）；2) 首个调用立刻发车（不等待窗口攒满——首响优先），窗口内的后来者直接搭车；3) 失败传播：fetch reject 时所有搭车者一起 reject（同 key 同命运）；4) 跨 isolate 不保证（说明注释）——需要全局去重用共享缓存（如 Data Cache），本函数只做请求级合并。

```javascript
const inflight = new Map() // key -> Promise（请求级，isolate 生命周期）

export function coalesce(key, fetcher, { windowMs = 10 } = {}) {
  if (inflight.has(key)) return inflight.get(key) // 搭车
  const p = new Promise((resolve, reject) => {
    // 首个调用即刻执行，不 delay——窗口只对"晚到的同 key"生效
    const deadline = Date.now() + windowMs
    fetcher().then(resolve, reject)
    // 窗口期内到达的调用会命中 inflight；窗口结束清理，允许下一次真实请求
    setTimeout(() => inflight.delete(key), deadline)
  })
  inflight.set(key, p)
  // 失败后立即清理：后来者重新发车，而不是搭上一趟失败车
  p.catch(() => inflight.delete(key) === undefined && inflight.get(key) === undefined)
  return p
}
```

**评分点**：
- 首个即发车不攒批（等待窗口 = 首响延迟，方向反了）
- 同 key Promise 复用（搭车者零成本共享结果）
- 失败即清 inflight（后来者重试而非陪葬——但同批搭车者同命运）
- 明确 isolate 边界（请求级合并与 Data Cache 的分层不混淆）
