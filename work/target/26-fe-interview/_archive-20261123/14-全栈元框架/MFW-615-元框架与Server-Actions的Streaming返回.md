---
title: [MFW-615] Server Actions 的 Streaming 返回：action 中的流式 UI 更新
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-615：Server Actions 的 Streaming 返回

**答**:
- Action 的流式返回（AI 生成场景）：action 返回 generator/AsyncIterable → Flight 流式输出（LLM token 逐个推 client）——「action 内 LLM 调用 + 流式返回」——不用独立 SSE 端点（RBL-570 的 Action 版）。
- 实现：action 内 `yield` 值 → client 的 useActionState/use 收流（React 的 action streaming——每 yield 一个 UI 更新）；「serverless 的时长限制」内完成（10-60s——LLM 生成通常满足）；超长任务仍需队列 RBL-569。
- 与 RSC 流式的差异：RSC 流式 = 页面渲染的 Suspense；Action 流式 = 变更操作的渐进反馈（生成过程可见）——两者可叠加（生成完成后 revalidate 列表）。
- 追问钩子：为什么「Action 流式」改变了 AI 应用的架构（无需独立 SSE 服务）？——传统：LLM 流 = 独立 SSE 端点（CORS/鉴权/连接管理 RBL-573）；Action 流 = 同源同鉴权（action 的 session 上下文直接用）+ Flight 协议复用（client 的 use 消费）——「流式 UI 的原生化」：React 19 的 action streaming 让「生成型 UI」回归组件模型（不再需要「实时层」的独立架构——RBL-573 的 WS/SSE 层被压缩到「真需要推送」（非请求触发的推送）场景）。

```typescript
// Action 流式返回（LLM 场景）
'use server';
export async function* chat(message: string): AsyncGenerator<string> {
  const stream = await llm.create({ prompt: message, stream: true });
  for await (const token of stream) {
    yield token;                                         // Flight 流式推 client
  }
  await saveConversation(message);                      // 完成后落库
  revalidateTag('conversations');
}
// client 消费
'use client';
function Chat() {
  const [messages, setMessages] = useState<string[]>([]);
  return (
    <form action={async (fd) => {
      const gen = chat(fd.get('msg'));
      for await (const token of gen) {
        setMessages(prev => [...prev.slice(0, -1), (prev.at(-1) ?? '') + token]);   // 逐 token 更新
      }
    }}>
      <input name="msg" />
    </form>
  );
}
```
