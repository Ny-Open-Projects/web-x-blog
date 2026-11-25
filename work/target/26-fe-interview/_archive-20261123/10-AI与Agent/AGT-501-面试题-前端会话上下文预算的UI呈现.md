---
title: [AGT-501] AI 对话页如何把「上下文预算」呈现给用户（余量条、压缩提示、裁剪透明化）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-501：AI 对话页如何把「上下文预算」呈现给用户（余量条、压缩提示、裁剪透明化）

**答**：
- 上下文余量是用户可感知的产品信息：剩余 token 越少，模型「忘记前面」的体验越差，把余量条做成类似电量条（绿/黄/红三档）比藏在设置里更好。
- 触发压缩/裁剪时必须透明化：在消息流插入一条系统提示「已对早期对话做摘要压缩」，否则用户会以为模型"变笨了"。
- 余量估算由前端根据服务端返回的 usage 字段累积计算，不要本地用字符数猜（中英文/代码差异大）。

```javascript
// 上下文预算条组件：订阅每次请求后的 usage
function useContextBudget(messages, ctxLimit = 128000) {
  const [used, setUsed] = useState(0);
  useEffect(() => {
    // 服务端在响应 meta 里返回最近一次真实 prompt_tokens
    api.on('response', (r) => setUsed(r.meta.promptTokens));
  }, []);
  const ratio = used / ctxLimit;
  const level = ratio < 0.7 ? 'ok' : ratio < 0.9 ? 'warn' : 'danger';
  // danger 档：主动提示用户开启新会话或压缩
  return { ratio, level, hint: level === 'danger' ? '上下文即将用满，建议压缩或新建会话' : null };
}
```

