---
title: [MFW-835] ISR 的软失效与硬失效有什么区别，用户会看到旧页多久
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-835：ISR 的软失效与硬失效有什么区别，用户会看到旧页多久

**答**：
- 结论：软失效（stale-while-revalidate）先返回旧页、后台重生成，用户可能连续多次看到旧内容；硬失效（阻塞重生成）用户等新页但 TTFB 升高。
- 取舍：列表/详情页多用软失效（体验优先），价格/库存类需硬失效或短 TTL（正确性优先）。
- 追问钩子：怎么让用户感知「正在更新」？——旧页注入轻量提示，或客户端轮询版本号，新版本就绪后无缝替换。

```javascript
// 软失效：SWR 缓存头
function softHeaders() {
  return { 'Cache-Control': 'public, s-maxage=60, stale-while-revalidate=300' };
}
// 硬失效：阻塞直到新页生成
async function hardRegenerate(key) {
  await revalidateTag(key);                        // 同步失效
  return renderFresh(key);                          // 用户等新页
}

// 用户感知：旧页带版本号，客户端发现新版后替换
async function checkUpdate(currentVersion) {
  const v = await fetch('/api/version').then(r => r.json());
  if (v.version > currentVersion) location.reload(); // 无缝更新
}
```
