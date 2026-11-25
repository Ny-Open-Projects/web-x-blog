---
title: [SOFT-835] 手写 syncRouter：协作事件按影响度路由同步方式（即时多通道/例行/按需）？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-835：手写 syncRouter：协作事件按影响度路由同步方式（即时多通道/例行/按需）

**需求与边界**：
- 实现 syncRouter(event)。
- 边界要求：① 事件字段 { type, affectsOthers, urgency, audience }；② 路由规则：影响他人排期/接口/依赖 且 urgent→即时+多通道（IM+邮件+看板）；例行进展→固定节奏；细节→文档可查不推送；③ 即时多通道路径生成消息模板（三要素 SOFT-573）；④ 未知类型兜底按需同步（文档——最安全）。

**答**：
```javascript
function syncRouter(e) {
  for (const k of ['type', 'affectsOthers', 'urgency', 'audience'])
    if (e[k] === undefined) throw new Error(`缺字段：${k}`);
  const urgent = e.urgency === 'high' && e.affectsOthers;
  if (urgent) {
    const msg = `【需知悉】${e.type}\n影响：${e.audience}\n`
      + `动作：请${e.action ?? '确认收到'}（截止：${e.deadline ?? '今天'}）\n`
      + `详情：${e.link ?? '（补链接）'}`;          // 三要素模板
    return { mode: '即时+多通道', channels: ['IM群', '邮件', '看板公告'],
      template: msg };
  }
  if (e.type === 'progress')
    return { mode: '例行', channel: '周报/站会' };
  if (e.type === 'detail')
    return { mode: '按需', channel: '文档归档（不推送）' };
  return { mode: '按需', channel: '文档归档（不推送）——兜底最安全' };
}
```

**评分点**:
- 影响度×紧迫度的双维路由（SOFT-824 分级设计落地）。
- 即时通道生成三要素消息模板（纪律内嵌工具）。
- 未知类型兜底按需（不推送=不制造噪音）。

