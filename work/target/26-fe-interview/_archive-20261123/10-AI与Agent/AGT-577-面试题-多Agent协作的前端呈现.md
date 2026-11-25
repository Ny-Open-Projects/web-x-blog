---
title: [AGT-577] 多个子 Agent 协作（主 Agent 派发给检索/写作/审核子 Agent），前端怎么呈现多线程任务？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-577：多个子 Agent 协作（主 Agent 派发给检索/写作/审核子 Agent），前端怎么呈现多线程任务

**答**：
- 用「泳道」组织：每个子 Agent 一条泳道（名字/职责/状态），主 Agent 的分派与汇总作为连接事件；默认只展示主泳道，子泳道折叠。
- 子 Agent 的事件流独立但共享同一 traceId 树（主 span→子 span），折叠视图的进度 = 子任务聚合状态。
- 冲突呈现：两个子 Agent 结论不一致时，UI 并排展示分歧点让用户裁决，而不是静默取其一。

```javascript
function MultiAgentView({ trace }) {
  const main = trace.spans.filter(s => !s.parent);
  const subs = trace.spans.filter(s => s.parent);
  return <>
    <Lane span={main[0]} />                       {/* 主泳道常显 */}
    <Expandable label={`${subs.length} 个子任务`}>
      {subs.map(s => <Lane key={s.id} span={s} />)}
    </Expandable>
    {trace.conflicts?.map(c => <DisagreementCard key={c.id} {...c}
      onPick={pick => resolveConflict(c.id, pick)} />)}
  </>;
}
```

