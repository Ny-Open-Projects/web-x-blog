---
title: [MFW-459] 笔试：手写 RSC Payload 流分块解析器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-459：RSC Payload 流分块解析器（复水侧）
**需求**：实现 `createFlightParser()`：1) 输入为 TextDecoderStream 逐 chunk 喂 `push(text)`，RSC 流按行分隔：行格式 `ID:["..."]`（新模块/数据行）或续行（不带 ID 前缀，拼到上一行）；2) `push` 返回本轮新增的完整记录 [{ id, body }]，不完整行留在缓冲；3) `flush()` 校验缓冲清空，否则抛 `TruncatedFlightError`（流被截断——网络中断常见）；4) 供客户端 Router Cache 增量合并。

```javascript
export function createFlightParser(onRecord) {
  let buf = ''
  const lines = []
  return {
    push(chunk) {
      buf += chunk
      const parts = buf.split('\n')
      buf = parts.pop() // 最后一段可能不完整，留在缓冲
      for (const line of parts) {
        if (!line.trim()) continue
        const m = line.match(/^([0-9a-f]+):(.*)$/)
        if (m) lines.push({ id: m[1], body: m[2], raw: [line] })
        else if (lines.length) {
          const last = lines[lines.length - 1]
          last.body += '\n' + line // 续行归属上一记录
        }
      }
      lines.forEach(l => onRecord({ id: l.id, body: l.body }))
      const n = lines.length; lines.length = 0
      return n
    },
    flush() {
      if (buf.trim()) throw new Error('TruncatedFlightError: ' + buf.slice(0, 40))
    },
  }
}
```

**评分点**：
- split('\n') 后 pop 缓冲尾段（半行不误解析——流式解析核心）
- 无 ID 续行归属上一记录（Flight 格式关键细节）
- flush 校验残缺缓冲抛截断错误（中断可检测而非静默丢数据）
- 解析与消费分离（onRecord 回调，增量合并入 Router Cache）
