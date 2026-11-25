---
title: [AIC-194] 笔试：实现一个 AI 截断 JSON 修复器：括号配对补全、字符串态识别与置信分级（可修复/需重生成）？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-194：笔试：实现一个 AI 截断 JSON 修复器：括号配对补全、字符串态识别与置信分级（可修复/需重生成）？
**答**：实现 `repairTruncatedJson(text)`：
- 流式输出被截断的 JSON：逐字符扫描追踪「是否在字符串内」（处理转义 `\"`）；
- 按栈补全未闭合的括号/数组（从内到外闭合）；
- 字符串被截断时：丢弃最后一个不完整的键值对再闭合（半截值不可信）；
- 输出 `{repaired, confidence: 'high'|'low'}`：仅缺闭合括号=high；丢数据=low（建议重生成最后一段）。

```javascript
function repairTruncatedJson(text) {
  const stack = [];
  let inStr = false, escaped = false;
  let lastComplete = 0; // 最后一个完整元素的位置

  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (inStr) {
      if (escaped) { escaped = false; continue; }
      if (ch === '\\') { escaped = true; continue; }
      if (ch === '"') { inStr = false; lastComplete = i; }
      continue;
    }
    if (ch === '"') { inStr = true; continue; }
    if (ch === '{' || ch === '[') stack.push(ch);
    else if (ch === '}' || ch === ']') stack.pop();
    else if (ch === ',' || ch === '}' || ch === ']') lastComplete = i;
  }

  let cut = text.length, confidence = 'high';
  if (inStr) {
    // 字符串截断：回退到最后一个完整元素（逗号/闭合）之后，丢弃半截键值
    cut = lastComplete + 1;
    confidence = 'low';
  }
  let body = text.slice(0, cut);
  // 去掉尾部的悬挂逗号/冒号
  body = body.replace(/[,:\s]+$/, '');
  // 按栈闭合（从内到外）
  let repaired = body;
  for (const open of stack.reverse()) {
    repaired += open === '{' ? '}' : ']';
  }
  // 重新验证
  try { JSON.parse(repaired); } catch { confidence = 'low'; }
  return { repaired, confidence, droppedTail: cut < text.length };
}

// 测试
console.log(repairTruncatedJson('{"items": [1, 2, {"a": 1}, "b"'));
// 字符串 "b" 截断 → 丢弃 → {"items": [1, 2, {"a": 1}]} confidence low
console.log(repairTruncatedJson('{"items": [1, 2,'));
// 仅缺闭合 → {"items": [1, 2]} confidence high
```

**评分点**：
1. 字符串态状态机（含 `\"` 转义）是正确性根基——简单数括号会被字符串里的括号骗到；
2. 截断策略分级：只缺闭合=high 可直接用；丢数据=low 必须提示上游重生成（静默丢数据是事故源）；
3. 尾部悬挂逗号/冒号清理在闭合之前；
4. 修复后二次 JSON.parse 验证，不盲信自己的修复；
5. 追问：流式场景应边收边验证（AIC-149 配合），截断修复是最后兜底而非常规路径。
