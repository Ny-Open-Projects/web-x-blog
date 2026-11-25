---
title: [AGT-297] Agent 应用的错误呈现——失败时怎么对用户说？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-297：Agent 失败/超时/拒答时，前端怎么呈现与引导？

**答**:
- 错误分类呈现：可重试错误（网络/限流）→ "稍后自动重试"按钮+预计时间；任务失败 → "失败原因（人话）+已完成部分+重新开始/调整任务的入口"；拒答 → "为什么不能答+用户可以怎么补充"（AGT-265 拒答话术的前端呈现）——三类呈现策略完全不同，不能统一一个"出错了"。
- 半成品处理：失败时保留已生成的部分（标记"部分结果"），比整段清空体验好；截断（max_tokens）提示"因长度截断，可展开继续"。
- 引导设计：失败引导到"更可行的任务表述"（失败案例→改写建议），拒答引导补充信息——错误是交互机会；高频失败的入口做产品级优化（前置说明能力边界）。
- 静默失败检测：前端感知"长时间无 delta"（心跳超时）主动提示连接异常并转恢复流程（AGT-294），不等用户干等。

```jsx
function AgentError({ err, partial }) {
  if (err.retryable) return <AutoRetry in={err.retryAfter} />;
  if (err.type === 'refusal')
    return <RefusalCard reason={err.reason} suggest={err.suggest} />;
  return <FailCard reason={humanize(err)}
    partial={partial && <PartialResult data={partial} />}
    actions={['重试', '调整任务', '反馈问题']} />;
}
// 心跳超时 → 主动提示 + 转恢复流程
```
EOF
mv AGT-297-Agent应用的错误呈现与用户引导.md.tmp 2>/dev/null; ls | grep -cE 'AGT-29[1-7]'
