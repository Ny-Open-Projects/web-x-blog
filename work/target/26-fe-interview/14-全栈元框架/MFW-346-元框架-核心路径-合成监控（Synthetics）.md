---
title: [MFW-346→MFW-346] 核心路径合成监控（拨测即门禁数据源）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-346：合成监控

**答**:
- 场景集即 SLA 具象化：登录→浏览→下单→支付四条脚本在多 region 每 5 分钟跑——失败分类（DNS/TLS/首字节/断言）直接映射故障域
- 与 RSC 语义对齐的断言：不只 200——断言 RSC 内容标记（关键数据节点存在 + 非 fallback 骨架——「渲染成功但全是兜底数据」这类静默事故只有内容断言能抓）
- 噪音控制：区域网络抖动的重试策略（3 次 2 分钟间隔再判死）+ 维护窗口静默（发布期间停跑不误报）+ 变更感知（路由下线同步停脚本——僵尸拨测也治理 MFW-343 联动）
- 产出双用：值班告警（P0 路径 2 连失败即 page）+ 容量与延迟趋势（拨测数据是唯一不受用户端噪音污染的干净样本）

```javascript
async function probe(site, { regions = ['us','eu','ap'] } = {}) {
  for (const rg of regions) {
    const r = await runInRegion(rg, () => browser.cover(['login', shellHas('[data-testid=price]'), 'checkout']) )
    if (!r.ok && !inMaintenanceWindow()) await escalate({ level: slaOf(s.route), region: rg, kind: r.step })
  }
}
// 断言含内容标记（防骨架假绿）+ 维护窗静默 + 下线路由同步停测
```
