---
title: [DP-286] 笔试题：手写 AI 流式请求管道（SSE 解析+背压）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-286：笔试题：手写 AI 流式请求管道（SSE 解析+背压）？
**题目**：实现 `streamChat(prompt, { onToken, onDone, onError })`：1) fetch + ReadableStream 读取 SSE（data: 前缀解析）；2) 分块边界处理（chunk 可能截断事件）；3) onToken 防抖批量回调（每 16ms 合并）；4) abort 支持。
**评分点**：
- SSE 缓冲解析正确（跨 chunk 事件拼接 buffer，\n\n 切事件）。
- [DONE] 终止处理与 reader.cancel。
- 批量 token 回调（rAF/定时器合并）。
- AbortController 清理（unmount 取消）。
```javascript
async function streamChat(prompt, { onToken, onDone, onError, signal }) {
  const ac = signal ?? new AbortController();
  let buffer = ''; let batch = '';
  let flushTimer;
  const flush = () => { if (batch) { onToken(batch); batch = ''; } };
  try {
    const res = await fetch('/api/chat', { method: 'POST', body: JSON.stringify({ prompt }), signal: ac.signal });
    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      buffer += decoder.decode(value, { stream: true });
      const events = buffer.split('\n\n');            // 2) 事件边界
      buffer = events.pop()!;                         // 最后一段可能不完整，留 buffer
      for (const ev of events) {
        const line = ev.split('\n').find(l => l.startsWith('data: '));
        const payload = line?.slice(6);
        if (payload === '[DONE]') { clearTimeout(flushTimer); flush(); return onDone(); }
        if (payload) {
          batch += JSON.parse(payload).content;       // 3) 批量
          flushTimer ??= setTimeout(flush, 16);
        }
      }
    }
    onDone();
  } catch (e) { ac.signal.aborted ? onDone() : onError(e); }
}
// 用：const ac = new AbortController(); streamChat('hi', { onToken, onDone, signal: ac.signal });
// 卸载：onUnmounted(() => ac.abort())
```
