---
title: [AGT-292] 前端状态机——流式对话 UI 的状态与渲染怎么设计？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-292：流式对话的前端状态机怎么设计——delta 渲染与工具状态怎么管理？

**答**:
- 消息状态机：`pending → streaming → tool_running → streaming → done | error | cancelled`——每条 assistant 消息是状态机实例；工具调用在 UI 上呈现为"步骤卡"（调用中/已完成/失败），与文本 delta 分区渲染。
- delta 渲染性能：token 级 setState 会卡——缓冲合帧（rAF 或 50ms tick 批量 flush）、增量渲染只追加不重建（markdown 流式渲染用增量 parser，AGT-153 未闭合代码块处理）、长列表虚拟化（上千轮会话）。
- 顺序与一致性：乱序 delta 重排（按 seq）、error 事件终止流并保留已渲染内容（不整块清除——半截答案也比白屏好，附错误说明与重试按钮）。
- 取消与重试：取消要前端+后端双中止（abort controller + 服务端 cancel），取消后消息状态落库（避免刷新后状态错乱）；重试从 last checkpoint 而不是从零。

```javascript
function useAgentStream(convId) {
  const buf = useRef([]); flush = useRafFlush(delta => {
    appendMessage(delta.seq, delta.payload);     // 合帧追加
  });
  es.onmessage = e => {
    const ev = JSON.parse(e.data);
    if (ev.type === 'delta') buf.current.push(ev);
    if (ev.type === 'tool_start') setToolState(ev.payload, 'running');
    if (ev.type === 'error') { close(); showError(ev); }
  };
  const cancel = () => { es.close();
    fetch(`/api/conv/${convId}/cancel`, { method: 'POST' }); };
  return { cancel };
}
```
