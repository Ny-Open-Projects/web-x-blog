---
title: [HW-173] 手写大数据量 Excel 导出——Worker 内分块生成 CSV/流式下载 + 内存峰值控制与进度
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：10 万行导出：主线程一次 JSON.stringify + Blob 会卡死且内存翻倍。Worker 内流式生成 CSV（分块读取数据 + 行级序列化）→ 用 WritableStream/分片 Blob 拼接下载，内存峰值 = 块大小；进度实时上报；CSV 注入防护（公式注入：= 开头的值加前缀转义）。

```javascript
// worker.js
self.onmessage = async ({ data: { url, columns } }) => {
  const res = await fetch(url);                          // 分页数据或流式接口
  const reader = res.body.getReader();
  const decoder = new TextDecoder();
  let buf = '', parts = [], size = 0;
  const header = columns.map(csvCell).join(',') + '\n';
  parts.push(header); size += header.length;
  const flush = () => {
    self.postMessage({ type: 'chunk', chunk: parts.join(''), progress: size });
    parts = [];
  };
  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;
    buf += decoder.decode(value, { stream: true });
    const lines = buf.split('\n'); buf = lines.pop();    // 不完整行留到下块
    for (const line of lines) {
      if (!line.trim()) continue;
      const row = JSON.parse(line);
      parts.push(columns.map((c) => csvCell(row[c])).join(',') + '\n');
      if (parts.length >= 5000) flush();                 // 每 5000 行回传一块（内存峰值受控）
    }
  }
  if (buf.trim()) parts.push(JSON.stringify(JSON.parse(buf)));
  flush();
  self.postMessage({ type: 'done' });
};
function csvCell(v) {                                    // CSV 注入防护 + 转义
  let s = String(v ?? '');
  if (/^[=+\-@]/.test(s)) s = `'` + s;                   // 公式注入防护：= + - @ 开头加 ' 前缀
  return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;   // 引号/逗号/换行转义
}
// 主线程：chunk 收集 → Blob([...chunks]) 下载（a[download]）或 ReadableStream 直接下发
```

**评分点**：
- Worker 流式分块生成（内存峰值 = 块大小，不卡主线程）——本题核心。
- CSV 注入防护（= 开头公式注入是真实安全漏洞）与转义完整（引号/逗号/换行）。
- 分块回传 + 进度（size 累计）。
- 完整行边界处理（split 留尾巴）。
