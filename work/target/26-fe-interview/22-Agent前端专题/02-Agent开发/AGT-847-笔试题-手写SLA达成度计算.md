---
title: [AGT-847] 手写 slaReport：月度可用性/完成率/延迟三指标、豁免条款、credit计算、租户视角输出？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-847：手写 slaReport：月度可用性/完成率/延迟三指标、豁免条款、credit计算、租户视角输出

**需求与边界**：
- 实现 slaReport(tenant, month)。
- 边界要求：① 三指标：availability（分钟级）、taskDone（排除豁免：供应商故障已切换/用户取消）、ttftP95；② 豁免事件带证据链接；③ credit 阶梯：低于目标 0.1% 内 5%、0.1~1% 10%、>1% 30%；④ 输出租户可读格式（不含内部字段）。

**答**：
```javascript
const CREDIT = [[0.001, 0.05], [0.01, 0.10], [Infinity, 0.30]];
function slaReport(tenant, month) {
  const avail = uptimeMinutes(month) / totalMinutes(month);
  const exempt = incidents(month, { tenant,
    type: ['vendor-failover', 'user-cancel'] });   // 豁免事件
  const done = (completed(tenant, month) - exempt.count)
    / attempts(tenant, month);
  const p95 = latencyP95(tenant, month);
  const miss = Math.max(0, 0.999 - avail);
  const credit = CREDIT.find(([t]) => miss <= t)?.[1] ?? 0.3;
  return {
    availability: pct(avail), taskDone: pct(done), ttftP95: p95,
    exempted: exempt.map(e => ({ id: e.id, evidence: e.rca })),
    credit: miss > 0 ? credit : 0,
    readable: `本月可用性 ${pct(avail)}（目标 99.9%），`
      + (miss > 0 ? `SLA 抵扣 ${credit * 100}%` : '达标'),
  };                                               // 租户可读
}
```

**评分点**:
- 三指标齐全且豁免条款带证据（RCA 链接）；豁免先扣再算达成。
- credit 阶梯计算；输出租户可读文案（不含内部口径字段）。

