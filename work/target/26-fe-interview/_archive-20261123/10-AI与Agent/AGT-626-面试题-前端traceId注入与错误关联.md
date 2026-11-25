---
title: [AGT-626] 用户报障只给了截图，如何让客服/开发用 traceId 秒级定位到那次会话？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-626：用户报障只给了截图，如何让客服/开发用 traceId 秒级定位到那次会话

**答**：
- traceId 一直暴露在 UI 可达处：消息菜单"复制诊断信息"（traceId+时间+版本），客服工单贴上即可反查；用户无需理解技术细节。
- 前端错误（渲染崩/流断）上报时必须携带当前 turn 的 traceId，与后端 trace 关联成一条链；用户反馈入口自动附带最近 turn 的诊断包。
- 兜底：用户拿不到 traceId 时按「userId+时间窗」反查（索引设计支持），覆盖截图报障场景。

```javascript
function copyDiagnostics(turn) {
  navigator.clipboard.writeText(JSON.stringify({
    traceId: turn.traceId, at: turn.startedAt,
    modelVer: turn.modelVersion, promptVer: turn.promptVer,
    ua: navigator.userAgent,
  }, null, 2));
}
window.onerror = (msg, src, line, col, err) => {
  report({ msg, err: err?.stack, traceId: currentTurn()?.traceId }); // 错误关联
};
```

