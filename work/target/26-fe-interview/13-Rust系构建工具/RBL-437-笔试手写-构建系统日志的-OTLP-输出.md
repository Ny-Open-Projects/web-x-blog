---
title: [RBL-437] 笔试：手写构建日志 OTLP 输出适配
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-437：手写构建日志 OTLP 输出适配
**需求**：实现 `createOtlpLogger({ endpoint })`：1) 构建事件 → OTel 语义约定（logs/spans）：build = trace（span 层级：build→phase→task），日志事件带 traceId 关联；2) span 结构：name/startTime/endTime/attributes（task 名/缓存命中）；3) 批量导出（OTLP/JSON over HTTP，batch 50 或 5s flush）；4) 降级：endpoint 不可达时本地写文件（可后补上传）；5) `child(span)` 嵌套层级与 RBL-405 profiler 数据格式兼容转换。

```javascript
import fs from 'node:fs'

export function createOtlpLogger({ endpoint, fallbackFile = '.cache/build-trace.json' } = {}) {
  const spans = [], logs = []
  let timer = null
  const stack = []

  function startSpan(name, attrs = {}) {
    const span = { name, attrs, traceId: currentTrace(), start: Date.now(), parent: stack.at(-1)?.name }
    spans.push(span)
    stack.push(span)
    return { end: () => { span.end = Date.now(); stack.pop() } }
  }
  function currentTrace() { return buildTraceId ??= crypto.randomUUID() }
  let buildTraceId = null
  function log(severity, message, attrs = {}) {
    logs.push({ severityText: severity, body: message, traceId: currentTrace(), at: Date.now(), ...attrs })
  }

  async function exportBatch() {
    const payload = JSON.stringify({
      resourceSpans: spans.filter((s) => s.end).map((s) => ({
        traceId: s.traceId, spanId: s.traceId.slice(0, 8), parentSpanName: s.parent,
        name: s.name, startTimeUnixNano: s.start * 1e6, endTimeUnixNano: s.end * 1e6,
        attributes: Object.entries(s.attrs).map(([k, v]) => ({ key: k, value: { stringValue: String(v) } })),
      })),
      resourceLogs: logs,
    })
    try {
      await fetch(endpoint, { method: 'POST', body: payload, headers: { 'content-type': 'application/json' } })
    } catch {
      fs.appendFileSync(fallbackFile, payload + '\n')            // 降级：本地可后补
    }
    spans.length = 0; logs.length = 0
  }
  timer = setInterval(exportBatch, 5000)

  return { startSpan, log, flush: exportBatch,
    dispose: () => { clearInterval(timer); exportBatch() } }
}
```
**评分点**：
- OTel 语义映射（span 层级 build→phase→task + traceId 关联 logs）
- 批量导出 + 定时 flush + dispose 兜底
- 降级本地文件（endpoint 不可达不丢数据可后补）
- attrs 结构化（OTLP attributes 格式）
