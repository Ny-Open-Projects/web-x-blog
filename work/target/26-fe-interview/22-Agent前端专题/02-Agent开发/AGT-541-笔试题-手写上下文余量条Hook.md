---
title: [AGT-541] 手写 useContextBudget：usage 累计、三档分级、压缩事件、危险提示？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-541：手写 useContextBudget：usage 累计、三档分级、压缩事件、危险提示

**需求与边界**：
- 实现 React Hook useContextBudget(ctxLimit)：输入会话消息流事件，输出 { ratio, level, hint }。
- 边界要求：① 以服务端 usage（promptTokens）为准而非本地估算；② level 三档 0.7/0.9 阈值；③ 压缩事件（compact）后 used 重置为压缩后基线；④ 会话切换时状态归零重算。

**答**：
```javascript
function useContextBudget(ctxLimit = 128000) {
  const [used, setUsed] = useState(0);
  const [sessionId, setSessionId] = useState(null);
  useEffect(() => {
    const onResp = ({ sessionId, meta }) => {
      if (sessionId !== sessionIdRef.current) return; // 其他会话的事件忽略
      setUsed(meta.promptTokens);
    };
    const onCompact = ({ sessionId, afterTokens }) => {
      if (sessionId === sessionIdRef.current) setUsed(afterTokens); // 压缩基线
    };
    api.on('response', onResp); api.on('compact', onCompact);
    return () => { api.off('response', onResp); api.off('compact', onCompact); };
  }, []);
  const ratio = Math.min(used / ctxLimit, 1);
  const level = ratio < 0.7 ? 'ok' : ratio < 0.9 ? 'warn' : 'danger';
  return { used, ratio, level,
    hint: level === 'danger' ? '上下文即将用满，建议压缩或新建会话'
        : level === 'warn' ? '上下文余量不足 30%，长对话可能被裁剪' : null };
}
```

**评分点**:
- 以服务端 promptTokens 为真值，不本地猜测。
- 压缩事件重置基线、会话切换隔离（否则余量条串会话）。
- 三档阈值与分级提示文案对应，danger 给可行动建议。

