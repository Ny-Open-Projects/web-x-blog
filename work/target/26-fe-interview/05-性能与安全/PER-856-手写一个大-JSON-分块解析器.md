---
title: [PER-856] 手写一个大 JSON 分块解析器：按块解析避免主线程长任务且可中断
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-856：手写一个大 JSON 分块解析器：按块解析避免主线程长任务且可中断

**答**：
- 需求：实现 parseInChunks(jsonStr, { chunkKB, onProgress })：按字节切块（块边界对齐到逗号，避免切断 token），逐块 JSON.parse 并合并；每块之间用 setTimeout(0) 让出主线程；返回 {promise, cancel}——cancel 后停止解析，返回已解析部分；onProgress 上报进度（0~1）。
- 边界：对齐函数不得切在字符串字面量内（简化处理：跳过引号内的逗号）；最后一块不足一块大小也提交；cancel 后 onProgress 不再调用。
- 评分点：块边界对齐；让出主线程；可中断且结果完整。

```javascript
function parseInChunks(jsonStr, { chunkKB = 64, onProgress } = {}) {
  let cancelled = false, results = [], pos = 0;
  const align = s => {                         // 块尾对齐：不在引号内的逗号
    let inStr = false, esc = false;
    for (let i = s.length - 1; i >= 0; i--) {
      const ch = s[i];
      if (esc) { esc = false; continue; }
      if (ch === '\\') { esc = true; continue; }
      if (ch === '"') inStr = !inStr;
      if (ch === ',' && !inStr) return i;
    }
    return -1;
  };
  const step = () => new Promise(r => setTimeout(r));
  async function run() {
    const chunkBytes = chunkKB * 1024;
    while (pos < jsonStr.length && !cancelled) {
      let end = Math.min(pos + chunkBytes, jsonStr.length);
      if (end < jsonStr.length) {              // 对齐块边界
        const c = align(jsonStr.slice(pos, end));
        if (c > 0) end = pos + c;
      }
      const part = jsonStr.slice(pos, end);
      const items = JSON.parse('[' + part.replace(/^\[|\]$/g, '') + ']');   // 假定顶层数组
      results = results.concat(items);
      pos = end + 1;
      onProgress && !cancelled && onProgress(pos / jsonStr.length);
      await step();                            // 让出主线程
    }
    return cancelled ? results : results;
  }
  return { promise: run(), cancel: () => { cancelled = true; } };
}
```
