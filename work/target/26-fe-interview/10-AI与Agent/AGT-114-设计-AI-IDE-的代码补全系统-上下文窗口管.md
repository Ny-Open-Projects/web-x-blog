---
title: [AGT-114] 设计 AI IDE 的代码补全系统（上下文窗口管理 + 延迟优化）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-114：设计 AI IDE 的代码补全系统（上下文窗口管理 + 延迟优化）？
**答**：
- 补全与对话的本质区别是毫秒级体验：上下文 = 光标前缀（最近约 2000 token，优先级最高）+ 少量后缀（FIM 语义）+ 相关文件片段，前缀稳定可命中前缀缓存。
- 延迟优化组合：小模型 + 短输出（max_tokens 64）+ 300ms 去抖 + 竞态取消（新请求 abort 旧请求）+ 前缀 hash 复用。
- 交互：灰字 ghost text 渲染，Tab 采纳 / Esc 拒绝 / 光标移动作废（AGT-088）。
- 质量信号：展示数与接受数埋点，接受率（accepted/shown）是北极星指标，用于评测与模型迭代。

```typescript
// IDE 补全客户端：上下文组装 + 竞态控制 + 接受率埋点
export function createCompletionEngine(editor: EditorLike) {
  let ctrl: AbortController | null = null;
  let lastPrefixHash = '';

  async function complete() {
    const prefix = editor.textBeforeCursor(8000);   // 前缀最重要，给足
    const suffix = editor.textAfterCursor(1200);    // 后缀少量，FIM 语义
    const h = String(stableHash(prefix));
    if (h === lastPrefixHash) return;               // 前缀未变，直接复用上次补全
    lastPrefixHash = h;
    ctrl?.abort();                                  // 竞态：新请求取消旧请求
    ctrl = new AbortController();
    const t0 = performance.now();
    const res = await fetch('/api/complete', {
      method: 'POST', signal: ctrl.signal,
      body: JSON.stringify({
        messages: [{ role: 'user', content: `<prefix>${prefix}</prefix><suffix>${suffix}</suffix>` }],
        model: 'code-small', max_tokens: 64, temperature: 0.1,
      }),
    });
    const { text } = await res.json();
    telemetry('completion_shown', { ms: performance.now() - t0, prefixHash: h }); // 展示埋点（分母）
    editor.showGhost(text);
    editor.onAcceptOnce(() => telemetry('completion_accepted', { prefixHash: h })); // 接受埋点（分子）
  }

  return {
    onType: debounce(complete, 300),
    onCursorMove: () => { editor.hideGhost(); lastPrefixHash = ''; },
  };
}
```
