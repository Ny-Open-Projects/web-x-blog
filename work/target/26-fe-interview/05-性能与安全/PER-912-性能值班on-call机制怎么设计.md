---
title: [PER-912] 性能值班（on-call）机制怎么设计
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-912：性能值班（on-call）机制怎么设计

**答**：
- 值班节奏：性能告警与线上 bug 同池值班或独立性能值班，按周轮换 + 备岗。
- 值班 SOP：收到告警→确认影响面（看板）→判断是否发版引起（关联发版记录）→可回滚则回滚、需修复则开单→复盘归档。
- 工具准备：一键回滚脚本、降级开关清单、性能看板快捷链接、常见劣化 Top10 案例 playbook。
- 健康度：统计告警 MTTR（平均解决时长）与误报率，纳入平台改进。

```javascript
// 值班面板聚合：一屏看清当前健康度
function healthSnapshot(records, slo) {
  const g = k => {
    const arr = records.filter(r => r.page === k).map(r => r.lcp).sort((a,b)=>a-b);
    return arr.length ? arr[Math.floor(arr.length * 0.75)] : null;
  };
  const pages = [...new Set(records.map(r => r.page))];
  return pages.map(p => ({ page: p, p75: g(p),
      status: g(p) <= slo.lcp ? 'ok' : (g(p) <= slo.lcp * 1.2 ? 'warn' : 'page') }));
}
// status: ok / warn（看板） / page（触发值班）
```
