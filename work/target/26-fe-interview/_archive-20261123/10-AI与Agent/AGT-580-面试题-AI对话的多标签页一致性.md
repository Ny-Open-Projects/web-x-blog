---
title: [AGT-580] 同一会话开两个标签页，一边生成中另一边打开，如何保持一致？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-580：同一会话开两个标签页，一边生成中另一边打开，如何保持一致

**答**：
- 快速通道：同源标签页用 BroadcastChannel 广播 delta（本地零延迟同步），服务端 WS 事件作为权威兜底（另一设备/广播丢失场景）。
- 生成中状态同步：发起生成的标签页广播 turn_start，其他标签页渲染"另一窗口正在生成"的只读态（防止双窗口同时发消息制造分叉混乱——分叉合法但要显式）。
- 收敛原则：本地广播只做体验加速，最终内容以服务端 turn 记录对账（哈希比对，不一致触发重拉）。

```javascript
const bc = new BroadcastChannel(`ai-session-${sessionId}`);
bc.onmessage = ({ data }) => {
  if (data.type === 'delta') applyDelta(data);           // 本地即时同步
  if (data.type === 'turn_start') setReadOnlyMode(true);
  if (data.type === 'done') reconcileWithServer(data.turnId); // 对账
};
stream.on('delta', d => { applyDelta(d); bc.postMessage({ type: 'delta', ...d }); });
```

