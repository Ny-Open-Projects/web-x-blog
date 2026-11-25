---
title: [1245] 笔试手写：实现 流式 markdown 围栏状态机
date: 2026-11-22
categories: [AI与Agent]
tags: [前端面试, 笔试题, 渲染]
type: 笔试题
---

## 1245：笔试手写：实现 流式 markdown 围栏状态机

**需求**：流式渲染 LLM markdown 时，代码块围栏 ``` 可能尚未闭合，直接渲染会样式错乱。实现 fenceState(chunks)：接收依次到达的文本片段数组，返回每段处理后的文本：未闭合围栏内追加「块未完成」占位行，闭合时移除占位并原样保留代码；返回最终拼接结果。

```js
function fenceState(chunks) {
  let out = '', inFence = false, placeholder = false;
  const OPEN = /(^|\n)```/ , CLOSE = /(^|\n)```\s*$/;
  for (const c of chunks) {
    out += c;
    const fences = (out.match(/```/g) || []).length;
    inFence = fences % 2 === 1; // 奇数个围栏 = 未闭合
    if (inFence && !placeholder) { out += '\n[代码块生成中...]'; placeholder = true; }
    if (!inFence && placeholder) { out = out.replace('\n[代码块生成中...]', ''); placeholder = false; }
  }
  return out;
}
```

**评分点**：
- 用围栏计数奇偶判断开闭（跨 chunk 也要数全局）
- 占位行随状态增删、闭合后恢复原文
- 能指出简化点：围栏出现在行首才有效（完整实现需按行扫描）
- 提到 HTML 块/行内代码干扰时的误判风险
