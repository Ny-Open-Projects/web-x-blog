---
title: [MFW-783] 流中 HTML 的合法性校验
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-783：流中 HTML 合法性校验

**答**:
- 流式 HTML 的合法性挑战：1) **chunk 边界切断标签**（`<div` 在 chunk1 末尾、`>content</div>` 在 chunk2——解析器需要缓冲未闭合标签）；2) **Hydration mismatch 的 HTML 源**（SSR 输出的 HTML 不合法 → 水合失败——SSR 的 HTML 验证是水合成功的前提 RBL-914）；3) **校验策略**：流式 HTML 的增量验证（HTML5 解析器的容错——浏览器自动修复不合法 HTML——但水合期望精确匹配）；「容错 vs 精确」：浏览器容错解析（`<div>` 未闭合自动闭合）vs React 水合（DOM 结构精确匹配——容错修复后的 DOM 可能与 React 预期不同 → mismatch）。
- 检测手段：流式 HTML 的「标签平衡检查」（open/close 标签计数——`<div` 与 `</div>` 配对）；「非法嵌套」（p 内套 div——HTML5 规范禁止——浏览器修复但水合错）。
- 追问钩子：为什么「浏览器容错 HTML」反而是水合 mismatch 的来源？——SSR 输出 `<p><div>x</div></p>`（HTML5 禁止 p 内嵌 div）→ 浏览器解析为 `<p></p><div>x</div><p></p>`（自动拆分）→ React 水合期望 `<p><div>x</div></p>` → DOM 结构不匹配 → hydration error；「容错修复」改变了 DOM 结构（React 的 vdom 是 p 含 div 但实际 DOM 是 p 与 div 兄弟——树不匹配）；「HTML 合法性」= 水合的前提：非法 HTML 在浏览器层被修复——修复后的结构与 React 期望不符。

```typescript
// 流式 HTML 标签平衡检查
function createHtmlValidator() {
  const stack: string[] = [];
  const selfClosing = new Set(['img', 'br', 'hr', 'input', 'meta', 'link']);
  const VOID_OK_IN = new Map([['p', ['span', 'a', 'em', 'strong']]]);   // p 内禁止 div/block
  function feed(chunk: string) {
    // 提取标签
    const tags = chunk.match(/<\/?(\w+)[^>]*\/?>/g) ?? [];
    for (const tag of tags) {
      const name = tag.match(/<\/?(\w+)/)?.[1]?.toLowerCase();
      if (!name || selfClosing.has(name)) continue;
      if (tag.startsWith('</')) {
        if (stack.at(-1) === name) stack.pop();
        else stack.push(`UNMATCHED_CLOSE:${name}`);      // 不匹配的关闭标签
      } else if (!tag.endsWith('/>')) {
        // p 内禁止 block 元素
        if (stack.at(-1) === 'p' && !VOID_OK_IN.get('p')?.includes(name))
          stack.push(`INVALID_NEST:${name}-in-p`);
        stack.push(name);
      }
    }
    return { unclosed: [...stack], balanced: stack.every(s => !s.startsWith('INVALID')) };
  }
  return { feed, get unclosed() { return [...stack]; } };
}
// SSR 输出的验证
const validator = createHtmlValidator();
validator.feed('<div><p>');
validator.feed('text<div>');                             // p 内 div → INVALID_NEST
const result = validator.feed('</p></div>');
console.log(result.balanced === false);                  // 非法嵌套
```
