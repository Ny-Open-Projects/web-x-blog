---
title: [AGT-866] 性能报告（Lighthouse 等）的 AI 解读：如何从一堆建议变成可执行工单？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-866：性能报告（Lighthouse 等）的 AI 解读：如何从一堆建议变成可执行工单

**答**：
- 三步加工：① 去噪（规则过滤：已知的误报/低影响项，别让 AI 复读 Lighthouse 建议清单）；② 归因（结合构建产物分析/网络瀑布/代码结构定位根因——"图片未优化"要定位到具体哪批图片谁上传的）；③ 工单化（产出带负责人/预期收益/验证方式的任务单，进项目管理流）。
- 收益量化：每条建议预估收益（LCP 可减 X ms，基于当前瓶颈计算），按收益排序——团队只做性价比高的。
- 验证闭环：工单完成后自动复测指标对比（优化前后同环境），验证失败回退工单。

```javascript
async function perfTickets(report) {
  const filtered = denoise(report, KNOWN_FALSE_POSITIVES);
  const attributed = await Promise.all(filtered.map(item =>
    attribute(item, { bundle: bundleAnalysis(), waterfall: report.net })));
  return attributed
    .sort((a, b) => b.gainMs - a.gainMs)
    .slice(0, 5)                                   // 只取性价比top5
    .map(a => ticket({ owner: a.suspectOwner,
      gain: a.gainMs, verify: `复测 ${a.metric}` }));
}
```

