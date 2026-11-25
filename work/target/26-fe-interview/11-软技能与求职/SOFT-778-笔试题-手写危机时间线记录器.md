---
title: [SOFT-778] 手写 crisisTimeline：故障事件与动作的时间线记录、复盘报告组装、预案缺口提取？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-778：手写 crisisTimeline：故障事件与动作的时间线记录、复盘报告组装、预案缺口提取

**需求与边界**：
- 实现 CrisisTimeline：record(t, event, actor)/report()。
- 边界要求：① record 事件有序（时间倒序插入自动排序）；② report 组装复盘报告：时间线表+关键节点（发现/止损/恢复）耗时+MTTR 计算；③ 预案缺口提取：事件类型在预案库无对应预案则标 GAP；④ 输出 markdown。

**答**：
```javascript
class CrisisTimeline {
  constructor(incident) {
    this.incident = incident; this.events = []; this.startedAt = null;
  }
  record(t, event, actor) {
    this.events.push({ t, event, actor });
    if (event.includes('发现') && !this.startedAt) this.startedAt = t;
    this.events.sort((a, b) => a.t - b.t);          // 自动排序
  }
  report() {
    const first = this.events[0];
    const detected = this.events.find(e => e.event.includes('发现'));
    const mitigated = this.events.find(e => e.event.includes('止损'));
    const recovered = this.events.find(e => e.event.includes('恢复'));
    const mttr = recovered && detected
      ? Math.round((recovered.t - detected.t) / 60000) : null;
    const detectGap = detected && first
      ? Math.round((detected.t - first.t) / 60000) : null; // 发现延迟
    const gap = PLAYBOOKS[this.incident.type] ? null
      : `GAP：${this.incident.type} 无对应预案——本次暴露`;
    const lines = this.events.map(e =>
      `| ${new Date(e.t).toLocaleTimeString()} | ${e.event} | ${e.actor} |`);
    return `## 复盘：${this.incident.type}\n\n` +
      `MTTR：${mttr ?? '未恢复'}分钟｜发现延迟：${detectGap ?? '-'}分钟\n\n` +
      `| 时间 | 事件 | 执行人 |\n|---|---|---|\n${lines.join('\n')}\n\n` +
      (gap ? `**${gap}**（改进项：补预案）` : '预案覆盖 ✓');
  }
}
```

**评分点**:
- 关键节点耗时自动计算（MTTR+发现延迟——复盘的核心数字）。
- 预案缺口提取（危机的产出=更强的预案体系 SOFT-729）。
- 事件自动排序（乱序记录容错）。

