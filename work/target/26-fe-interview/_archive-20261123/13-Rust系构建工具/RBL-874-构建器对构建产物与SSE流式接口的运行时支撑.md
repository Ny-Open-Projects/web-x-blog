---
title: [RBL-874] 场景题：SSE 流式接口的产物支撑——EventSource 封装的构建期处理
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-874：场景题：SSE 流式接口的产物支撑——EventSource 封装与降级链

**答**:
- SSE（AI 对话/实时推送）的产物层要点：1) **EventSource vs fetch-stream 的选择**（EventSource 只支持 GET/无自定义头；fetch + ReadableStream 支持POST——现代方案 fetch 流式）；2) 降级链（fetch stream → EventSource → 轮询），构建期能力清单（RBL-751）决定启用层级；3) 断线重连语义（Last-Event-ID 头）封装在共享层。
- 构建器的配合：1) 流式工具库独立 chunk（低频页面用——聊天页才加载，RBL-840 上传 SDK 同构策略）；2) polyfill 边界（ReadableStream 的浏览器兼容 vs 目标矩阵——不支持则降级链生效）；3) mock 层（RBL-834 的流式版本：dev 下 SSE 模拟器——mock 也要流式行为一致否则联调假象）。
- 重连的状态管理：SSE 重连的「消息不丢」要求服务端事件带 id + 客户端重放窗口——构建器无关但产物常量（重连参数）要进配置层（可调）不是硬编码。
- 资源清理契约：组件卸载时 abort（AbortController）——泄漏的 SSE 连接是 AI 应用的高频 bug；构建器 lint 规则可检测「组件内建 EventSource/fetch-stream 无 abort 清理」模式（静态启发式诊断）。
- 追问钩子：为什么「mock 层也要流式一致」在 AI 应用联调中特别重要？——SSE 的消费代码按「事件块到达」编写（增量渲染/token 顺序）；mock 若一次性返回全文，前端渲染逻辑（防抖/排序/光标）根本没被测过——联调通过上线即碎；mock 与真实的「行为同构」（分块时序）比「数据同构」更难也更重要——契约测试的流式扩展。

```javascript
// 流式客户端封装（降级链 + 清理契约）
export function createStream(url, { onChunk, signal }) {
  const cap = capability();                              // RBL-751 能力清单
  if (cap.fetchStream) return fetchStream(url, { onChunk, signal });
  if (cap.eventSource) return esFallback(url, { onChunk, signal });
  return pollFallback(url, { onChunk, signal });         // 轮询兜底
}
async function fetchStream(url, { onChunk, signal }) {
  const res = await fetch(url, { signal });
  const reader = res.body.getReader();
  const decoder = new TextDecoder();
  let buf = '';
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    buf += decoder.decode(value, { stream: true });
    for (const event of parseSSE(buf)) onChunk(event);   // 按 SSE 事件边界切分
  }
}
// 组件内使用（清理契约）
// useEffect(() => { const s = createStream(...); return () => s.abort(); }, [deps]);
```
