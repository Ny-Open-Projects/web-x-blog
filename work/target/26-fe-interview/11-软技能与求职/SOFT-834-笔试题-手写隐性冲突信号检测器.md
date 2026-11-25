---
title: [SOFT-834] 手写 silentConflictDetect：协作数据（互审频率/回复延迟/信息共享量）的异常检测、破冰建议生成？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-834：手写 silentConflictDetect：协作数据（互审频率/回复延迟/信息共享量）的异常检测、破冰建议生成

**需求与边界**：
- 实现 silentConflictDetect(data)。
- 边界要求：① data 为成员对的协作数据 { pair: [a,b], reviewCount, avgReplyHours, infoShareCount } 与各自历史基线（基线来自前几期均值）；② 异常判定：互审/共享量较基线降 ≥50% 或回复延迟升 ≥3 倍——标记疑似隐性冲突（SOFT-806 信号）；③ 排除正当原因（假期/项目隔离的成员对——白名单）；④ 破冰建议：分别一对一+共赢小任务（SOFT-806）。

**答**：
```javascript
function silentConflictDetect(data, baselines, { exclude = [] } = {}) {
  const flags = [];
  for (const d of data) {
    const key = [...d.pair].sort().join('|');
    if (exclude.some(p => d.pair.includes(p))) continue; // 正当原因
    const base = baselines[key] ?? {};
    const reviewDrop = base.reviewCount &&
      d.reviewCount < base.reviewCount * 0.5;
    const replyUp = base.avgReplyHours &&
      d.avgReplyHours > base.avgReplyHours * 3;
    const shareDrop = base.infoShareCount &&
      d.infoShareCount < base.infoShareCount * 0.5;
    if ((reviewDrop && shareDrop) || replyUp) {     // 双信号或延迟暴增
      flags.push({ pair: d.pair,
        signals: [reviewDrop && '互审降50%+',
          shareDrop && '信息共享降50%+', replyUp && '回复延迟×3']
          .filter(Boolean),
        advice: '分别1:1听各方版本（SOFT-806）→'
          + '共赢小任务修复→不公开点名' });
    }
  }
  return { flagged: flags,
    note: '数据异常=疑似信号，需人工1:1确认（不公开点名）' };
}
```

**评分点**:
- 三信号异常判定（双信号确认或延迟暴增——降低误报）。
- 白名单排除正当原因（假期/隔离不误判）。
- 破冰建议明确且守“不公开点名”纪律。

