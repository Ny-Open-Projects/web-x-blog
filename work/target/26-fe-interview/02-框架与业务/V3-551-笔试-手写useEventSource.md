---
title: [V3-551] 笔试：手写 useEventSource（SSE composable）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 网络]
type: 笔试题
---

## V3-551：笔试：手写 useEventSource

**答**：实现 `useEventSource(url, events, { immediate })`：① 返回 { data, event, status, open, close }——EventSource 包装；② 指定监听的事件名列表（自定义 event 类型分发）；③ 状态响应式（CONNECTING/OPEN/CLOSED）；④ 手动 open/close（默认自动连接可关）；⑤ 错误重连控制（EventSource 自动重连 vs 手动关闭后不再连）。写出实现。

```javascript
export function useEventSource(url, events = [], { immediate = true } = {}) {
  const data = ref(null);
  const event = ref(null);
  const status = ref('CLOSED');
  let es = null;
  let manualClose = false;

  function open() {
    if (es) return;
    manualClose = false;
    es = new EventSource(url);
    status.value = es.readyState === 0 ? 'CONNECTING' : 'OPEN';
    es.onopen = () => status.value = 'OPEN';
    es.onerror = () => {
      // EventSource 自动重连; 手动 close 后 onerror 不再触发
      status.value = es.readyState === 2 ? 'CLOSED' : 'CONNECTING';
    };
    es.onmessage = (e) => { event.value = 'message'; data.value = e.data; };
    for (const name of events)                       // 自定义事件分发
      es.addEventListener(name, (e) => { event.value = name; data.value = e.data; });
  }
  function close() {
    manualClose = true;
    es?.close();
    es = null;
    status.value = 'CLOSED';
  }
  if (immediate) onMounted(open);
  onScopeDispose(close);
  return { data, event, status, open, close };
}
// 用法: 通知流
const { data, status } = useEventSource('/api/notify/stream', ['alert', 'update']);
watch(data, (v) => v && toast(JSON.parse(v)));
```

**评分点**：
- 自定义事件名的 addEventListener 分发（SSE event: 字段）
- 状态与 readyState 映射
- 手动 close 后不自动重连的语义
- 卸载清理与 immediate 开关
