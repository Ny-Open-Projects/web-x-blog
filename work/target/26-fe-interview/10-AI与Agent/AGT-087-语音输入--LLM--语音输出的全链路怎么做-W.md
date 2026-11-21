---
title: [AGT-087] 语音输入 → LLM → 语音输出的全链路怎么做（Web Speech API）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-087：语音输入 → LLM → 语音输出的全链路怎么做（Web Speech API）？
**答**：
- 浏览器原生三件套零依赖可用：SpeechRecognition（ASR）→ LLM → speechSynthesis（TTS）。
- 要点：`recognition.lang` 设语言、`interimResults` 控制中间结果实时上屏；TTS 前把 markdown 清洗为纯文本，避免读出符号。
- 回环控制：TTS 播报期间必须停止监听（`onend` 后再开下一轮），否则麦克风听到自己说话陷入自答循环。
- 生产化注意：浏览器方案适合轻量场景，高质量需求走服务端 ASR/TTS（双向流式用 WebSocket）；麦克风权限需用户手势触发，Safari 需 webkit 前缀。

```javascript
// 语音输入 → LLM → 语音输出（浏览器原生）
const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
const synth = window.speechSynthesis;
let listening = false;

function listen(onResult) {
  if (listening) return;                 // 播报期间不监听，防自听自答
  const rec = new SR();
  rec.lang = 'zh-CN';
  rec.interimResults = true;             // 中间结果实时上屏
  rec.onresult = (e) => {
    const text = [...e.results].map((r) => r[0].transcript).join('');
    const isFinal = e.results[e.results.length - 1].isFinal;
    onResult(text, isFinal);
  };
  rec.onend = () => { listening = false; };
  listening = true;
  rec.start();
}

async function voiceTurn(onText) {
  listen(async (text, isFinal) => {
    onText(text);                        // 实时上屏
    if (!isFinal) return;
    const reply = await chat([{ role: 'user', content: text }]);
    const u = new SpeechSynthesisUtterance(reply.replace(/[#*`>\-[\]()]/g, '')); // 清洗 markdown
    u.lang = 'zh-CN';
    u.rate = 1.1;
    u.onend = () => voiceTurn(onText);   // 播报结束后再开下一轮监听
    synth.speak(u);
  });
}
```
