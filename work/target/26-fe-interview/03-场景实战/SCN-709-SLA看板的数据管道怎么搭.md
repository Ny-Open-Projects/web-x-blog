---
title: [SCN-709] SLA 看板的数据管道（采集→聚合→存储→查询）怎么搭？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-709：SLA 数据管道怎么搭？
**答**：
- 链路：RUM SDK 采样采集 → 上报网关（去重/补齐维度）→ 流式聚合（Flink 按分钟窗口算 P95/达标数）→ 时序库（分钟/小时/天多级物化）→ 看板查询 API。
- 前端职责边界：SDK 保证上报完整性与维度齐全（page/biz/region/版本），聚合与查询在服务端——前端不做统计口径（分位数在流侧算）。
- 口径一致性：SDK 采样与流侧分位数算法（t-digest/CKMS）配合，采样率变化必须在口径版本里记录。
- 数据延迟分层：实时层（分钟延迟，值班用）与离线层（小时级精确重算，周报用），看板标注数据层级。
- 追问钩子：为什么 P95 要用 t-digest 而不是排序——流式无限流数据无法全量排序，近似分位数算法以极小误差换 O(1) 内存。

```javascript
// SDK 侧：保证维度完整
function reportSLI(sli) {
  beacon('/rum/sli', {
    ...sli,                                          // { key, value, ts }
    dims: { page: currentPage(), biz: bizOf(currentPage()),
            region: REGION, release: RELEASE, sampleRate: SAMPLE_RATE },   // 口径必需维度
    clientId: stableClientId(),                      // 去重
  });
}
// 流侧（示意）：分钟窗口 t-digest
const windowDigest = new TDigest(0.01);              // 1% 相对误差
window.on('rum.sli', e => windowDigest.push(e.value));
setInterval(() => tdstore.write(sliKey, windowDigest), 60_000);   // 分钟物化
```
