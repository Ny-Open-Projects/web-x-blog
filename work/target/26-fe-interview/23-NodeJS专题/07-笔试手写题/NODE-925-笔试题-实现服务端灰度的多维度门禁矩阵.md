---
title: [NODE-925] 笔试题——实现灰度发布数据面板的完整性校验（可复核）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-925：手写数据可复核

**需求与边界**：
- 需求：灰度数据可复核（SCN-OPS-284）——① 灰度面板的预注册（判定口径锁定——SCN-OPS-284）；② 数据完整性校验（样本占比 100%——SCN-OPS-850）；③ 可复核包（配置快照+数据引用——SCN-OPS-284）；④ 探索性发现标注（SCN-OPS-284）。
- 边界：① 预注册的时机（灰度开始前——SCN-OPS-284）；② 探索性发现的分级（SCN-OPS-284）；③ 可复核包的消费（第三方重算——SCN-OPS-284）。

**答**：
```javascript
async function grayPanelIntegrity(release, prereg) {
  const share = await versionTrafficShare();           // SCN-OPS-850 占比
  const srm = chiSquareSF(share.counts, prereg.expectedPcts);   // SRM（SCN-OPS-293）
  const coverage = sampleCoverage(release);            // 采集覆盖（SCN-OPS-850）
  return {
    integrity: srm.ok && coverage === 1,
    prereg: { metrics: prereg.metrics, hash: prereg.hash },   // 预注册（SCN-OPS-284）
    replicationPack: { config: prereg.config, dataRef: release.dataRef, code: ANALYSIS_VER },   // 可复核包
    exploratory: exploratoryFindings(release).map(f => ({ ...f, note: '未预注册，仅假设' })),   // 分级
  };
}
```

**评分点**:
- 预注册 + 可复核包（SCN-OPS-284）。
- SRM + 覆盖完整性（SCN-OPS-293/850）。
- 探索性分级（SCN-OPS-284）。
