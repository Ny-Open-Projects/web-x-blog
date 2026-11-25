---
title: [AGT-529] AI 对话页的「首答时间」（用户发出第一个问题到看到答案）怎么优化？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-529：AI 对话页的「首答时间」（用户发出第一个问题到看到答案）怎么优化

**答**：
- 首答时间 = 页面加载 + 输入耗时 + 网络排队 + 模型首 token。前端能优化的三段：页面预加载（路由预取时拉起 SDK 与模型列表）、连接预热（进入页面即建立 SSE/WS 连接与鉴权）、输入期预请求（用户开始输入就预检配额/预建会话）。
- 首答感知优化：骨架先给出"正在理解问题"的中间状态，加轮次级状态（检索中→思考中→生成中），用户等待焦虑显著下降。
- 服务端配合：首轮路由到低延迟模型、常用问题预热缓存。

```javascript
// 输入期预热：开始输入 300ms 后预建会话+预检配额
inputEl.addEventListener('input', debounce(() => {
  if (!prewarmed) {
    prewarmed = Promise.all([api.preflightQuota(), sse.connect(),
      api.precreateSession()]);
  }
}, 300));
async function sendFirst(msg) {
  await prewarmed;                    // 预热完成，省 300~800ms
  return sse.send(msg, { stream: true, firstTokenHint: 'understanding' });
}
```

