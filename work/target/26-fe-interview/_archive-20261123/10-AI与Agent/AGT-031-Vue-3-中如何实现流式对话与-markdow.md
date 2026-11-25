---
title: [AGT-031] Vue 3 中如何实现流式对话与 markdown 渲染？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-031：Vue 3 中如何实现流式对话与 markdown 渲染？
**答**：
- 用 `ref` 数组管理消息，流式期间直接对最后一条的 `content` 追加，Vue 的响应式自动触发更新。
- assistant 消息用 `v-html` 渲染 markdown，渲染前必须 sanitize，模型输出可能包含注入脚本。
- `streaming` 状态控制输入框禁用与 loading 指示。
- SSE 解析逻辑同 AGT-002，可在 composable 中复用。

```vue
<!-- Vue 3 流式对话：ref 响应式追加 + sanitize 后的 markdown 渲染 -->
<script setup lang="ts">
import { ref } from 'vue';
import { marked } from 'marked';
import DOMPurify from 'dompurify';

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

const messages = ref<Message[]>([]);
const input = ref('');
const streaming = ref(false);

async function send() {
  const text = input.value.trim();
  if (!text || streaming.value) return;
  input.value = '';
  messages.value.push({ role: 'user', content: text }, { role: 'assistant', content: '' });
  streaming.value = true;

  const res = await fetch('/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ messages: messages.value.slice(0, -1) }),
  });
  const reader = res.body!.getReader();
  const decoder = new TextDecoder();
  const last = messages.value[messages.value.length - 1];

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    for (const line of decoder.decode(value, { stream: true }).split('\n')) {
      if (!line.startsWith('data:')) continue;
      const payload = line.slice(5).trim();
      if (payload === '[DONE]') continue;
      last.content += JSON.parse(payload).choices[0]?.delta?.content ?? '';
    }
  }
  streaming.value = false;
}

function render(md: string): string {
  const html = marked.parse(md, { async: false }) as string;
  return DOMPurify.sanitize(html); // v-html 前必须消毒
}
</script>

<template>
  <div class="chat">
    <div v-for="(m, i) in messages" :key="i" :class="m.role">
      <div v-if="m.role === 'assistant'" class="md" v-html="render(m.content)" />
      <span v-else>{{ m.content }}</span>
    </div>
    <input v-model="input" :disabled="streaming" placeholder="输入消息" @keyup.enter="send" />
  </div>
</template>
```
