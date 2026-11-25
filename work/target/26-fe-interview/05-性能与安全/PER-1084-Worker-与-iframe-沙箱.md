---
title: [PER-1084] Worker 与 iframe 沙箱的安全边界怎么划
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1084：Worker 与 iframe 沙箱的安全边界怎么划

**答**：
- iframe sandbox 属性：无 allow-same-origin 则同源策略隔离（唯一身份），加 allow-scripts 允许脚本——两者同给等于无沙箱（可移除自身 sandbox）。
- Worker 沙箱：无法访问 DOM，跨源 Worker 禁止（脚本需同源或 CORS 导入），适合隔离执行不可信逻辑但要防消息面攻击。
- 通信面：iframe/Worker 的 postMessage 是唯一出口，消息 schema 校验 + 深拷贝（结构化克隆天然隔离引用）。
- 深水：不可信代码用 sandbox iframe（null origin）+ CSP 双保险，敏感数据不进沙箱上下文。

```javascript
<!-- 第三方插件沙箱 -->
<iframe sandbox="allow-scripts" csp="script-src 'self'; connect-src 'none'"
  src="/sandbox/plugin-host.html"></iframe>
<script>
// plugin-host.html：null origin，无法读 cookie/storage
addEventListener('message', e => {
  if (e.origin !== 'https://app.example.com') return;    // 只信任宿主
  const { op, payload } = e.data;
  const result = PLUGIN_API[op]?.(payload);              // 能力受控
  e.source.postMessage({ id: e.data.id, result }, e.origin);
});
</script>
```
