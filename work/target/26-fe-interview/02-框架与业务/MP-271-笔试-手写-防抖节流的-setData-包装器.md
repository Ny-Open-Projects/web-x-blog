---
title: [MP-271] 笔试：手写 setData 防抖节流包装器（高频更新合并）
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 笔试题, 19]
type: 笔试题
---

## MP-271：笔试：手写 setData 包装器（高频更新合并）
**答**：实现 `createSafeSetData(page)`：返回 safeSetData(data)；16ms 窗口内多次调用合并（深合并对象）；超 256KB 拆分批次发送；组件销毁后不再发送；暴露 flush 立即发送。

```javascript
function createSafeSetData(page) {
  let buffer = {}, timer = null, destroyed = false
  function deepMerge(dst, src) {
    for (const k in src) {
      if (src[k] && typeof src[k] === 'object' && !Array.isArray(src[k]) && typeof dst[k] === 'object' && !Array.isArray(dst[k])) deepMerge(dst[k], src[k])
      else dst[k] = src[k]
    }
    return dst
  }
  function doSet() {
    timer = null
    if (destroyed || !Object.keys(buffer).length) return
    const data = buffer; buffer = {}
    const size = JSON.stringify(data).length
    if (size > 256 * 1024) {
      for (const k in data) page.setData({ [k]: data[k] }) // 按顶层 key 拆批
    } else page.setData(data)
  }
  const safe = (data) => {
    if (destroyed) return
    deepMerge(buffer, data)
    timer ||= setTimeout(doSet, 16)
  }
  safe.flush = doSet
  safe.destroy = () => { destroyed = true; clearTimeout(timer) }
  return safe
}
```
**评分点**：
- 合并窗口（16ms≈一帧）+ 深合并。
- 超限拆批（按顶层 key）。
- destroy 防泄漏（页面卸载后仍 setData 是崩溃源）。
- flush 满足「需要立即渲染」的场景。
