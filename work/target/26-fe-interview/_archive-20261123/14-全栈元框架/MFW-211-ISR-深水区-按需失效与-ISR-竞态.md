---
title: [MFW-211] ISR 深水区：按需失效的竞态与旧页回填问题
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-211：ISR 按需失效的竞态

**答**:
- 竞态场景：revalidate 触发后，旧静态页仍在 CDN——新请求先命中旧页（触发后台再生成 STW 前提下）→ 用户看到旧内容一次（可接受的最终一致）vs 需要强一致时用 SSR 动态渲染
- 旧页回填保护：再生成失败时 Next 保留旧页继续服务（不回滚为错误页）——ISR 的可用性优先设计，代价是「失败后内容可能长时间陈旧」——监控再生成失败率
- 按需失效风暴：批量 revalidate 一万个 key（CMS 全量更新）→ 再生成队列打爆——治理：失效调度器合并（同 tag 一次）+ 队列限流 + 优先级（首页先于长尾）
- 版本对账：ISR 页面带生成时间戳（__NGL 或 header x-nextjs-prerender）——线上对账「用户看到的页面龄」

```javascript
// 批量失效调度（合并 + 限流）
const pending = new Set()
let timer
function scheduleRevalidate(key) {
  pending.add(key)
  clearTimeout(timer)
  timer = setTimeout(async () => {                  // 100ms 合并
    for (const k of [...pending].slice(0, 20)) {    // 限流
      await revalidateTag(k); pending.delete(k)
    }
    if (pending.size) scheduleFlush()               // 剩余下一轮
  }, 100)
}
```
