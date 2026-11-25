---
title: [SCN-728] SLA 看板的导出与定时报告怎么做？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-728：导出与定时报告怎么做？
**答**：
- 服务端渲染导出：定时周报/月报由服务端 headless 渲染生成 PDF（图表样式与在线版一致），不依赖有人打开看板。
- 快照存证：每次报告附带数据快照版本与口径版本，事后可复现——SLA 报告常用于对上汇报与客户沟通，必须可追溯。
- 分发配置：报告订阅列表（收件人/频率/范围）可配置，范围受限者只收到其权限内的内容。
- 报告摘要化：正文一页（结论+最差三件事+改进项进度），附录放明细——管理层读摘要，工程师看附录。
- 追问钩子：为什么报告不能直接截图看板——截图分辨率/时间范围/口径可能过时，服务端渲染以「报告生成时刻的数据」为准并固化快照，才可仲裁。

```javascript
schedule('0 9 * * 1', async () => {                  // 每周一 9 点
  const rev = await snapshotData(boardSpec, { range: lastWeek() });   // 固化快照
  const pdf = await renderReport(rev, { template: 'weekly', audience: acl });
  await send({ to: subscribers(boardSpec), attach: pdf,
               meta: { dataRev: rev.id, calVer: rev.calVer } });     // 快照可复现
});
```
