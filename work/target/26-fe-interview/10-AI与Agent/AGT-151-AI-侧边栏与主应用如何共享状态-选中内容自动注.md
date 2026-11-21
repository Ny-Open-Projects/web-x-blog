---
title: [AGT-151] AI 侧边栏与主应用如何共享状态（选中内容自动注入上下文）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-151：AI 侧边栏与主应用如何共享状态（选中内容自动注入上下文）？
**答**：
- 架构：主应用是「唯一事实源」，AI 侧边栏作为消费者订阅选择状态（选中文本/当前路由/打开的文档），通过 store 或事件总线同步，绝不各自持有一份会过期的拷贝。
- 上下文注入设计：选中变化 ≠ 立即发请求——用「附件区」模式，把当前选中作为可编辑的引用卡片挂在输入框上，用户确认后才注入，避免误触大量 token 消耗。
- 会话与上下文分离：同一会话内不同轮次引用的上下文要随消息存档（问答回看时知道当时依据什么），而不是只存最终答案。
- 跨标签页/窗口场景用 BroadcastChannel 保证选择状态一致。

```typescript
// AI 侧边栏的上下文注入（Pinia store + 附件确认模式）
import { defineStore } from 'pinia';

export const useAiPanelStore = defineStore('ai-panel', {
  state: () => ({
    selection: null as { text: string; source: string } | null,   // 主应用写入
    pendingRefs: [] as { text: string; source: string }[],        // 输入框附件区（用户确认后）
    messages: [] as { role: string; content: string; refs: { text: string; source: string }[] }[],
  }),
  actions: {
    onSelectionChange(sel: { text: string; source: string } | null) {  // 主应用调用
      this.selection = sel && sel.text.length > 1 ? sel : null;
    },
    attachSelection() {                                                 // 用户点「+ 引用选中内容」
      if (this.selection) { this.pendingRefs.push(this.selection); this.selection = null; }
    },
    async ask(question: string) {
      const refs = [...this.pendingRefs];
      this.messages.push({ role: 'user', content: question, refs });    // 上下文随消息存档，回看可溯源
      const context = refs.map((r) => `<context source="${r.source}">${r.text}</context>`).join('\n');
      await streamChat([
        { role: 'system', content: '仅基于引用上下文回答，无引用时明确说明。' },
        { role: 'user', content: `${context}\n\n问题：${question}` },
      ], (chunk) => {
        const last = this.messages.at(-1)!;
        if (last.role !== 'assistant') this.messages.push({ role: 'assistant', content: '', refs: [] });
        this.messages.at(-1)!.content += chunk;
      });
      this.pendingRefs = [];
    },
  },
});

async function streamChat(msgs: { role: string; content: string }[], onChunk: (s: string) => void) {
  const res = await fetch('/api/chat/stream', { method: 'POST', body: JSON.stringify({ messages: msgs }) });
  const reader = res.body!.pipeThrough(new TextDecoderStream()).getReader();
  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    for (const line of value.split('\n')) if (line.startsWith('data: ')) onChunk(JSON.parse(line.slice(6)).text ?? '');
  }
}
```
