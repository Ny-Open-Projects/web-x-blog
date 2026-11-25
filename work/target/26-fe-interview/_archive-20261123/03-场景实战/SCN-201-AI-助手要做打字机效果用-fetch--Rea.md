---
title: [SCN-201] AI 助手要做打字机效果：用 fetch + ReadableStream 消费 LLM 流式接口，中断与渲染节流怎么设计？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-201：AI 助手要做打字机效果：用 fetch + ReadableStream 消费 LLM 流式接口，中断与渲染节流怎么设计？

**答**：
- 选型先想清楚：`EventSource` 只能 GET、不能带 Authorization 头和自定义 body、不能控制重连——LLM 网关需要 POST + token + 多轮上下文，所以统一用 `fetch` + `ReadableStream`，SSE 协议层解析复用 AGT-041 的状态机（本场景给出面向 UI 的精简版）。
- 解析要点：`res.body` 是字节流，必须 `new TextDecoder()` 配 `{ stream: true }` 跨 chunk 解码（否则中文多字节字符被 chunk 切开时乱码）；SSE 按**空行**分帧，`data:` 字段多行用 `\n` 连接，OpenAI 风格流以 `data: [DONE]` 收尾；每轮末尾留有不完整帧要放回缓冲区。
- 中断设计：一个 `AbortController` 的 `signal` 贯穿整个请求；"停止生成"就是 `abort()`，`fetch` 与 `reader.read()` 都以 `AbortError` 拒绝；React 18 StrictMode 开发期 effect 双执行，cleanup 必须 abort，Vue 在 `onBeforeUnmount` abort，且中断后**已生成的文本要保留**。
- 渲染节流：每个 chunk 都 `setState` 会造成每秒几十次重渲（外加整段 markdown 反复解析），把增量缓冲进 ref，`requestAnimationFrame`（或 30-50ms 定时）每帧批量刷入 state——渲染频率与网络 chunk 频率解耦；流式中的 markdown 渲染配合 AGT-149 处理未闭合代码块。

```javascript
// streamChat.js：fetch 流式消费 SSE（POST + Authorization，EventSource 做不到）
export async function streamChat({ messages, signal, onDelta }) {
  const res = await fetch('/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${getToken()}` },
    body: JSON.stringify({ messages, stream: true }),
    signal,
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);      // 出错时响应不是流，按普通 HTTP 处理
  const reader = res.body.getReader();
  const decoder = new TextDecoder();                       // decode(value, {stream:true}) 才能正确跨 chunk 解中文
  let buf = '';
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    buf += decoder.decode(value, { stream: true });
    const frames = buf.split('\n\n');                      // SSE 以空行分帧
    buf = frames.pop();                                    // 末段可能不完整，留回缓冲区
    for (const frame of frames) {
      const data = frame.split('\n')
        .filter((line) => line.startsWith('data:'))
        .map((line) => line.slice(5).replace(/^ /, ''))
        .join('\n');                                       // 多行 data 用 \n 连接
      if (data === '[DONE]') { await reader.cancel(); return; }
      if (data) onDelta(JSON.parse(data).choices?.[0]?.delta?.content ?? '');
    }
  }
}
```

```jsx
// useChatStream.js：缓冲 + rAF 批量刷新 + AbortController 全链路
export function useChatStream() {
  const [answer, setAnswer] = useState('');
  const [status, setStatus] = useState('idle');            // idle | streaming | done | aborted | error
  const bufRef = useRef('');
  const rafRef = useRef(0);
  const ctrlRef = useRef(null);

  const flush = () => {                                    // 每帧最多渲染一次
    rafRef.current = 0;
    if (bufRef.current) setAnswer((prev) => prev + bufRef.current);
    bufRef.current = '';
  };
  const enqueue = (chunk) => {                             // chunk 只进缓冲，不直接 setState
    bufRef.current += chunk;
    if (!rafRef.current) rafRef.current = requestAnimationFrame(flush);
  };

  useEffect(() => () => {                                  // 卸载兜底：abort + 取消挂起的帧
    ctrlRef.current?.abort();
    cancelAnimationFrame(rafRef.current);
  }, []);

  const send = async (messages) => {
    ctrlRef.current?.abort();                              // 上一轮未结束先掐断
    const ctrl = new AbortController();
    ctrlRef.current = ctrl;                                // 记录本轮 controller，用于区分中断来源
    setAnswer(''); bufRef.current = '';
    setStatus('streaming');
    try {
      await streamChat({ messages, signal: ctrl.signal, onDelta: enqueue });
      if (ctrlRef.current !== ctrl) return;                // 已被新一轮 send 接管，别覆盖状态
      flush();                                             // 流结束补刷最后一段
      setStatus('done');
    } catch (e) {
      if (e.name === 'AbortError') {
        if (ctrlRef.current !== ctrl) return;              // 被"停止生成"或新一轮掐断的旧请求：不覆盖状态
        flush(); setStatus('aborted');                     // 用户停止：保留已生成文本
      } else {
        setStatus('error');
      }
    }
  };
  const stop = () => ctrlRef.current?.abort();             // "停止生成"按钮直接调用
  return { answer, status, send, stop };
}
```

```javascript
// Vue 3 版差异点：shallowRef 避免长文本深响应开销，onBeforeUnmount 接管中断
// （send/AbortController 链路与上方 React 版同构，ctrl 为当轮请求的 AbortController）
const answer = shallowRef('');
const buf = shallowRef('');
let raf = 0;
function enqueue(chunk) {
  buf.value += chunk;
  if (!raf) raf = requestAnimationFrame(() => {            // 与 React 同思路：帧级批量刷
    answer.value += buf.value; buf.value = ''; raf = 0;
  });
}
onBeforeUnmount(() => { ctrlRef.current?.abort(); if (raf) cancelAnimationFrame(raf); });
```
