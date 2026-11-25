---
title: [R19-346] 笔试：手写「骨架屏最小展示 400ms」的数据包装器
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-346：笔试：手写骨架屏最小展示时间包装器
**答**：实现 `withMinDuration(fetcher, ms = 400)`：数据到达快于 ms 时，等待补足时长再 resolve（骨架不闪烁）；慢于 ms 时数据即到即用；不阻塞真实请求（并行计时）。

```javascript
function withMinDuration(fetcher, ms = 400) {
  return async (...args) => {
    const start = Date.now()
    const [data] = await Promise.all([
      fetcher(...args),
      new Promise(r => setTimeout(r, ms)) // 并行计时：请求慢时 min 不额外等待
    ])
    return data
  }
}
// Suspense 数据层使用：const goods = await withMinDuration(() => fetchGoods(id))
```
**评分点**：
- Promise.all 并行（min 计时不叠加在请求时长上——核心）。
- 与 race 方案的区别（race 是超时降级，min 是防闪烁）。
- 参数透传。
- 说明 400ms 的体验依据（太快闪、太慢拖）。
