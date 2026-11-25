---
title: [MFW-714] 流式 patch 的应用顺序
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-714：流式 patch 的应用顺序

**答**:
- 流式 patch 的应用顺序协议：1) **到达序 = 应用序**（Flight chunk 按 HTTP 流到达顺序应用——每个 chunk 到达即渲染（不等后续）；2) **乱序的风险**：HTTP/2 多路复用可能乱序？——Flight 是单一 TCP 流（单响应内有序——HTTP/1.1 和 HTTP/2 的单 response 内 chunk 有序）；3) **重复 chunk**（网络重传——chunk id 去重（已应用的 chunk 忽略 RBL-501 引用解析的幂等）；4) chunk 的依赖序：chunk A 引用 chunk B 的数据——B 未到时 A 挂起（$L 引用 RBL-503 的延迟绑定——到达序≠依赖序：B 后到时 A resolve）。
- 应用序的错误恢复：chunk 解析失败（部分 chunk 损坏——跳过该 chunk（后续 chunk 继续——流式容错）；「跳过的 chunk 的影响」（缺失的 UI 区域——error boundary 兜底 RBL-536）。
- 追问钩子：为什么「Flight 流内 chunk 有序」是协议的重要保证？——有序 = 解析器可以线性处理（到达即解析——无需排序缓冲）；若乱序 = 需要排序缓冲（等待所有 chunk——流式优势消失）；「单响应内有序」是 HTTP 协议层保证（TCP 字节流有序）——Flight 利用 HTTP 有序性设计协议（行式 + 线性解析），避免排序复杂度——协议设计对传输层特性的利用。

```javascript
// 流式 chunk 的有序应用与去重
function createFlightStreamProcessor() {
  const applied = new Set();                             // 已应用的 chunk id
  const pending = new Map();                             // id -> chunks waiting for deps
  function processChunk(id, data) {
    if (applied.has(id)) return;                         // 重复：忽略（幂等）
    applied.add(id);
    try {
      applyToDOM(id, data);                              // 渲染该 chunk
      // 检查是否有等待此 chunk 的依赖
      const waiting = pending.get(id);
      if (waiting) { waiting.forEach(w => processChunk(w.id, w.data)); pending.delete(id); }
    } catch (e) {
      console.warn(`chunk ${id} 解析失败——跳过`, e);      // 容错：跳过不中断流
    }
  }
  return {
    push(chunk) {
      // 检查依赖：chunk 引用了未到达的 id → 挂起
      const deps = extractRefs(chunk.data);
      const missing = deps.filter(d => !applied.has(d));
      if (missing.length) {
        for (const dep of missing) {
          (pending.get(dep) || pending.set(dep, []).get(dep)).push(chunk);
        }
        return;                                          // 等待依赖
      }
      processChunk(chunk.id, chunk.data);
    },
  };
}
```
