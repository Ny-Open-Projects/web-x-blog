---
title: [NODE-432] 告警的下钻体系（从告警到根因的固定路径）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-432：告警下钻体系
**答**:
- 问题：告警只说"5xx 升高"，值班要 10 分钟手工切四个看板才定位到接口。下钻体系 = 每类告警预定义"固定下钻路径"（告警 → 维度拆解 → 根因候选 → 证据链接），平台自动化执行。
- 自动下钻实现：告警触发时平台自动跑维度拆解（按 route/instance/version/region/依赖 分桶对比），输出"嫌疑排序"（哪个维度解释了大部分异常，ARC-358 归因思想服务端版）；每项嫌疑附证据链接（对应 trace/日志查询预构造）。
- 根因候选库：每类告警的常见根因清单（5xx → 新发布/依赖故障/资源耗尽/代码 bug），按历史频率排序呈现。
- 工具集成：下钻结果直连工具（一键打开该 route 的 trace 查询、一键查该版本发布 diff）——减少值班上下文切换。
- 运营：下钻命中率统计（嫌疑排序第 1 的根因命中率），持续调优拆解逻辑。
```javascript
// 自动下钻：维度嫌疑排序
async function drilldown(alert) {
  const dims = ['route', 'instance', 'version', 'region', 'dep'];
  const scores = await Promise.all(dims.map(d => anomalyContribution(alert, d)));
  return scores.sort((a, b) => b.contribution - a.contribution).map(s => ({
    dim: s.dim, value: s.top, contribution: s.contribution,     // "route:/order v2.3 解释了 87% 异常"
    links: { trace: traceLink(s), logs: logLink(s), diff: diffLink(s) }
  }));
}
```
