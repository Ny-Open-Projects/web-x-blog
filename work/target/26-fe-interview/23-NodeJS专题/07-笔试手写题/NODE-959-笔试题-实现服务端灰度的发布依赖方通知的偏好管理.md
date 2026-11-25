---
title: [NODE-959] 笔试题——实现通知偏好管理（消费方的通知定制）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-959：手写偏好管理

**需求与边界**：
- 需求：通知偏好（SCN-OPS-612/959）——① 偏好模型（渠道/频率/类型——SCN-OPS-612）；② 偏好的约束（关键通知不可关——SCN-OPS-612）；③ 偏好的生效（路由器消费——SCN-OPS-320）；④ 偏好的审计（SCN-OPS-220）。
- 边界：① 关键通知豁免（SCN-OPS-612）；② 偏好的灰度（SCN-OPS-228）；③ 偏好的默认值（SCN-OPS-612）。

**答**：
```javascript
async function setNotifyPrefs(consumer, prefs) {
  const validated = prefs.map(p => ({ ...p,
    overridable: !CRITICAL_EVENTS.includes(p.type) }));   // 关键不可关（SCN-OPS-612）
  await savePrefs(consumer, validated);
  audit({ consumer, prefs: validated });               // 审计（SCN-OPS-220）
}
function route(event, consumer) {
  const pref = prefs(consumer)[event.type] ?? DEFAULT_PREFS;
  if (pref.muted && !event.critical) return skip();    // 免打扰（SCN-OPS-612）
  return notify(pref.channel, event);
}
```

**评分点**:
- 偏好模型（渠道/频率/类型——SCN-OPS-612）。
- 关键通知豁免（SCN-OPS-612）。
- 路由消费 + 审计（SCN-OPS-320/220）。
