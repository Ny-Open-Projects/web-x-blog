---
title: [MFW-289] 子资源加载失败的降级链（CDN 抖动）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## MFW-289：子资源降级链

**答**:
- 场景：JS/CSS chunk 从 CDN 拉取失败（抖动/区域故障）——白屏是最大代价；需要客户端级降级链
- 降级链设计：script onerror → 换备用源重试（主 CDN→源站→内嵌 manifest 列出的备份域）→ 最终兜底「刷新引导页」（告知用户网络问题非事故）
- 预防性设计：多 CDN 域名写入构建 manifest（发布时产出 fallback 列表随 HTML 下发）；关键 JS 超小内联兜底（路由器骨架——至少能渲染错误页）
- 监控联动：资源错误率按区域上报（RUM）——CDN 区域性故障分钟级发现（用户反馈之前）

```javascript
function loadWithFallback(src, fallbacks) {
  return new Promise((res, rej) => {
    const tryNext = (i) => i >= fallbacks.length ? rej() : loadScript(fallbacks[i], () => res(), () => tryNext(i + 1))
    tryNext(0)
  })
}
// manifest 下发：{ chunks: { main: ['https://cdn-a/...', 'https://cdn-b/...', '/orig/...'] }}
```
