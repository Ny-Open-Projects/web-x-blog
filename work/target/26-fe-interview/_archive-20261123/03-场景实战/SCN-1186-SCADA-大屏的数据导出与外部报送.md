---
title: [SCN-1186] SCADA 大屏的数据导出与外部报送（政府监管平台）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1186：SCADA 大屏的数据导出与外部报送（政府监管平台）

**答**：
- 报送：排放/能耗数据按监管格式定时报送（接口/文件），报送失败重试告警。
- 校验：报送前数据完整性校验（缺点位阻断）。
- 留痕：报送记录与回执归档。

```javascript
// 监管报送
async function regulatoryReport(period) {
  const data = await collectRegulatoryData(period);
  const missing = data.required.filter(k => data[k] == null);
  if (missing.length) return { ok: false, missing, action: '补齐后报送' };
  const r = await submitToGov(data);
  archiveReport(data, r.receipt);
  return { ok: true, receipt: r.receipt };
}
async function submitToGov(d) { return { receipt: 'R1' }; }
async function collectRegulatoryData(p) { return { required: [] }; }
async function archiveReport(d, r) { return true; }
```
