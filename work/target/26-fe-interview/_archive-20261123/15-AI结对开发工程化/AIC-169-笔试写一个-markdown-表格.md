---
title: [AIC-169] 笔试：实现一个 Markdown 表格解析器：对齐行识别、单元格转义、宽表容错（AI 常输出不规范表格）？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-169：笔试：实现一个 Markdown 表格解析器：对齐行识别、单元格转义、宽表容错（AI 常输出不规范表格）？
**需求**：实现 `parseMdTable(lines)`：
- 识别表头行 + 分隔行（`---|:--:|--:` 含对齐信息）+ 数据行；
- 单元格支持 `\|` 转义与行内代码中的 `|`（不切分）；
- 容错：数据行列数与表头不一致时补空/丢弃并记录 warning；
- 输出 `{headers, align, rows, warnings}`。

```javascript
function splitRow(line) {
  // 处理 \| 转义与 `|` 行内代码
  const cells = [];
  let cur = '', inCode = false;
  for (let i = 0; i < line.length; i++) {
    const ch = line[i];
    if (ch === '\\' && line[i + 1] === '|') { cur += '|'; i++; continue; }
    if (ch === '`') inCode = !inCode;
    if (ch === '|' && !inCode) { cells.push(cur.trim()); cur = ''; continue; }
    cur += ch;
  }
  cells.push(cur.trim());
  // 去首尾空 cell（行首尾的 |）
  if (cells[0] === '') cells.shift();
  if (cells.at(-1) === '') cells.pop();
  return cells;
}

function isSeparator(line) {
  return /^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$/.test(line);
}
function parseAlign(line) {
  return splitRow(line).map(c =>
    c.startsWith(':') && c.endsWith(':') ? 'center' : c.endsWith(':') ? 'right' : 'left');
}

function parseMdTable(lines) {
  const warnings = [];
  const headerIdx = lines.findIndex((l, i) =>
    i + 1 < lines.length && isSeparator(lines[i + 1]) && l.includes('|'));
  if (headerIdx === -1) return { headers: [], align: [], rows: [], warnings: ['未找到表格'] };
  const headers = splitRow(lines[headerIdx]);
  const align = parseAlign(lines[headerIdx + 1]);
  const rows = [];
  for (let i = headerIdx + 2; i < lines.length && lines[i].includes('|'); i++) {
    const cells = splitRow(lines[i]);
    if (cells.length !== headers.length) {
      warnings.push(`第 ${i + 1} 行列数 ${cells.length} ≠ ${headers.length}`);
      while (cells.length < headers.length) cells.push(''); // 补空
    }
    rows.push(cells.slice(0, headers.length));
  }
  return { headers, align, rows, warnings };
}

// 测试
const md = ['| 名称 | 值 |', '|:---|---:|', '| `a|b` | 1 |', '| 转义\\|管道 | 2 |', '| 缺列 |'];
console.log(parseMdTable(md));
// headers:['名称','值'] align:['left','right'] warnings 含缺列行
```

**评分点**：
1. 分隔行正则识别与对齐解析（:--: center）是表格解析的钥匙；
2. 单元格切分必须处理转义 `\|` 与行内代码——逐字符状态机优于 split('|')；
3. 列数不一致容错（补空 + warning）针对 AI 产出的不规范表格；
4. 表格边界（连续数据行止于无 `|` 的行）；
5. 追问：跨行单元格/HTML 表格不在范围，应显式拒绝而非错解。
