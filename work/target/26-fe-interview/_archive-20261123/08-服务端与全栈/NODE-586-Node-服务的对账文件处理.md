---
title: [NODE-586] Node 服务的对账文件处理（渠道对账单解析比对）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-586：对账文件处理
**答**:
- 链路：渠道对账单下载（定时拉取/渠道推送——下载重试与完整性校验）→ 解析（各渠道格式 adapter——字段映射到统一流水模型 NODE-552）→ 入库（对账流水表——渠道+日期唯一幂等）→ 比对（vs 本地支付流水——ARC-382 引擎）→ 差异处理（分级告警/自动补偿——NODE-538）。
- 解析健壮性：格式容错（渠道改格式——解析失败告警不静默、列映射配置化——渠道格式变更只改配置）、编码/金额单位（分元转换——按渠道配置）、大文件流式（百万行——流式比对内存安全）。
- 比对细节：时间边界（渠道日切 vs 平台日切——边界容差：跨日交易归属窗口配置）、在途交易（T 日支付 T+1 结算——容差期处理）、部分对账（渠道文件分片——分片比对断点续跑）。
- 差异处理自动化：自动补单（渠道有本地无——可信补单）、人工核查（大额差异——工单），全部差异留痕分类（根因统计 ARC-538）。
- 观测：对账完成时效（T+1 何时完成）、差异率趋势、解析失败率。
```javascript
// 对账文件处理流水线
async function reconcileFile(channel, date) {
  const file = await download(channel, date);                    // 下载重试+校验
  const rows = await parse(channel, file);                       // 格式 adapter 流式
  for (const batch of chunk(rows, 1000)) await upsertChannelFlow(batch, { channel, date }); // 幂等入库
  const diff = await compareWithLocal({ channel, date, tolerance: boundaryCfg(channel) });
  await handleDiff(diff);                                        // 分级处理
}
```
