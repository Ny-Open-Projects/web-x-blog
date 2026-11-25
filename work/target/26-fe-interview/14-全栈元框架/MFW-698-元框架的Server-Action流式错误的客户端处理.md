---
title: [MFW-698] Server Action 流式错误的 client 处理
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-698：Action 流式错误的 client 处理

**答**:
- 流式 action 的错误时序：1) **流中途错误**（generator yield 了部分 token → 抛错——client 已渲染部分内容：错误处理策略（部分内容保留 + 错误提示 or 全部回滚 RBL-580 乐观语义）；2) **流开始前错误**（无 token yield 即错——正常 error path）；3) 流的错误传播（AsyncGenerator 的 throw → client 的 for-await 抛出——try/catch 消费）。
- 部分内容的处理策略：1) **保留 + 标注**（部分生成保留 + 「生成中断」提示——用户看到部分结果（多数有用——LLM 的部分输出仍有价值）；2) 全部回滚（清空——适合不可信部分输出（结构化数据：半截 JSON 无用——全清）；3) 「部分内容的价值」决定策略：文本类保留、结构化类清空。
- 流的错误后的重试：新 generator 调用（从头生成——部分内容被替换；「续传」（LLM 的 continue prompt——从断点继续——工程上复杂：stream 状态保存 + prompt 续写）——多数场景全重做（简单可靠）。
- 追问钩子：为什么「LLM 流式中断的部分内容保留」比「全部回滚」更符合用户预期？——部分文本 = 用户已读到的内容（回滚 = 内容消失——阅读上下文丢失）；部分输出仍有价值（LLM 的前半段通常连贯）；保留 + 「生成中断」标注 = 诚实告知（用户自己决定是否重试）；「渐进信息的价值」：文本流式的部分结果优于无结果——与结构化数据的策略相反（半截 JSON 无用）——策略由「部分内容的可用性」决定。

```tsx
// 流式 action 的错误处理
'use server';
export async function* chat(message: string): AsyncGenerator<string> {
  const stream = await llm.create({ prompt: message, stream: true });
  for await (const token of stream) yield token;         // 中途抛错 → client catch
}
// client：部分内容保留
'use client';
function Chat() {
  const [content, setContent] = useState('');
  const [error, setError] = useState<string | null>(null);
  return (
    <div>
      <div>{content}</div>
      {error && <div role="alert">{error} <button onClick={retry}>重试</button></div>}
    </div>
  );
  async function retry() {
    setError(null); setContent('');
    try {
      for await (const token of chat('...')) {
        setContent(prev => prev + token);                // 逐 token
      }
    } catch (e) {
      setError(`生成中断：${e.message}`);                 // 部分内容保留 + 错误提示
    }
  }
}
// 结构化数据的策略（半截 JSON 无用 → 全清）
if (isStructuredOutput) setContent('');                  // 全清
```
