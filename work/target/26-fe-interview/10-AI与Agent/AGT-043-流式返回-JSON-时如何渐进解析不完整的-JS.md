---
title: [AGT-043] 流式返回 JSON 时如何渐进解析不完整的 JSON？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-043：流式返回 JSON 时如何渐进解析不完整的 JSON？
**答**：
- 模型流式输出 JSON 时，已收到的前缀是合法 JSON 的前缀：可以「补全闭合」得到可用的部分对象，驱动 UI 渐进渲染。
- 实现思路：扫描字符串维护括号栈（对象/数组开括号进栈），处于字符串内部时忽略括号；未闭合引号补 `"`，栈内括号逆序补 `}` / `]`。
- 边界处理：尾逗号非法要去掉；悬空冒号（键后没值）补 `null` 占位；转义符截断要回退。
- 渐进解析只保证「尽量可读」，严格校验仍要等流结束后用 Zod 做 schema 校验（AGT-048）。

```typescript
// partial JSON 解析：把不完整前缀补全成可 parse 的 JSON
export function parsePartialJson(input: string): unknown | undefined {
  const stack: string[] = [];
  let inString = false, escape = false, lastSignificant = '';
  for (const ch of input) {
    if (escape) { escape = false; continue; }
    if (ch === '\\') { escape = true; continue; }
    if (ch === '"') inString = !inString;
    if (!inString) {
      if (ch === '{') stack.push('}');
      else if (ch === '[') stack.push(']');
      else if (ch === '}' || ch === ']') stack.pop();
      if (!/\s/.test(ch)) lastSignificant = ch;
    }
  }
  let out = input;
  if (escape) out += '\\';                             // 转义符截断
  if (inString) out += '"';                            // 字符串未闭合
  // 尾逗号非法（可能还跟着空白），连同其后空白一起去掉
  if (lastSignificant === ',') out = out.replace(/[\s,]+$/, '');
  if (lastSignificant === ':') out += 'null';          // 键后悬空冒号，补 null 占位
  while (stack.length) out += stack.pop();             // 逆序补齐闭合括号
  try { return JSON.parse(out); } catch { return undefined; }
}

// 流式中渐进渲染：每个 delta 后都能拿到「当前可读」的部分对象
async function progressiveRender(deltas: AsyncIterable<string>, patch: (obj: Record<string, unknown>) => void) {
  let acc = '';
  for await (const d of deltas) {
    acc += d;
    const obj = parsePartialJson(acc);
    if (obj !== undefined) patch(obj as Record<string, unknown>);
  }
}
```
