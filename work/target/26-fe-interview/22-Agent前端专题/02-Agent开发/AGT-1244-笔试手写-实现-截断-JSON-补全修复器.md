---
title: [1244] 笔试手写：实现 截断 JSON 补全修复器
date: 2026-11-22
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## 1244：笔试手写：实现 截断 JSON 补全修复器

**答**：流式返回的 JSON 常因中断而截断。实现 repairJson(s)：把不完整的 JSON 字符串尽可能补全为合法 JSON（补齐未闭合的引号、数组 ]、对象 }），无法挽救时返回 null。要求处理字符串内部未闭合引号、尾随逗号两种坑。

```js
function repairJson(s) {
  const stack = [];
  let inStr = false, esc = false, lastSignificant = '';
  for (const ch of s) {
    if (inStr) {
      if (esc) esc = false;
      else if (ch === '\\') esc = true;
      else if (ch === '"') inStr = false;
      continue;
    }
    if (ch === '"') inStr = true;
    else if (ch === '{' || ch === '[') stack.push(ch);
    else if (ch === '}' || ch === ']') stack.pop();
    if (!/\s/.test(ch)) lastSignificant = ch;
  }
  if (lastSignificant === ',') s = s.replace(/,\s*$/, ''); // 尾随逗号
  if (inStr) s += '"'; // 补引号（转义态挂掉则可能产坏串，保守校验兜底）
  while (stack.length) s += stack.pop() === '{' ? '}' : ']';
  try { JSON.parse(s); return s; } catch { return null; }
}
```

**评分点**：
- 单遍扫描维护括号栈与字符串态（转义符处理）
- 尾随逗号先剥离再补全
- 最终必须 JSON.parse 验证，失败返回 null（不假装成功）
- 能讨论：流式场景应边解析边校验而非事后修复
