---
title: [MFW-401] 笔试：手写 revalidateTag 批量失效调度器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-401：批量失效调度器
**需求**：CMS 全量更新触发数千 `revalidateTag`——直接调用会打爆再生成队列。实现 `createInvalidationPump(native, { batchMs = 100, throughput = 20 } = {})`：1) 同窗口 tag 去重合并；2) 按优先级出队（首页/详情 > 长尾列表——priority(fn) 注册时声明）；3) 限速放行（每 windowMs 最多 throughput 个，其余滚入下轮）；4) flush() 同步清空（pagehide/停机兜底）；5) 观测 { queued, dropped, rounds }。

```javascript
export function createInvalidationPipeline(n, { batchMs = 100, throughput = 20 } = {}) {
  const pending = new Map()   // tag -> { fn, p, at }
  let timer = null, rounds = 0, dropped = 0

  function invalidate(tag, priority = 1) {
    const prev = pending.get(tag)
    if (prev && prev.p <= priority) return                // 同 tag 高优先已pending
    pending.set(tag, { run: () => n.revalidateTag(tag), p, at: Date.now() })
    schedule()
  }
  function schedule() { if (!timer) timer = setTimeout(way, batchMs) }
  function tick() {
    clearTimeout(timer); timer = null
    const list = [...pending.values()].sort((a, b) => a.p - b.p || a.at - b.at)
    const slice = list.slice(0, throughput)
    slice.forEach((x) => { pending.delete(tagOf(x)); try { x.run() } catch (e) { report('revalidate_fail', e) } })
    rounds++
    if (pending.size) schedule()                          // 剩余滚入下轮
  }
  const tagOf = (x) => ...                                // 反查略：存 entry 时带 tag
  return { invalidate, flush: tick, stats: () => ({ queued: pending.size, dropped, rounds }) }
}
```
**评分点**：
- 同窗口去重（高优先覆盖低优先——不反向降级）
- 优先级+先到次序双键排序（首页先于长尾——用户体验序）
- 限速滚动窗口（打不爆再生成队列；余量自动续轮）
- 异常隔离（单个 tag 失败不炸整批）+ flush 兜底
