---
title: [SCN-1136] IoT 设备控制台的设备导入（批量建档）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1136：IoT 设备控制台的设备导入（批量建档）

**答**：
- 导入：批量设备建档（Excel/对接产线）——SN/型号/证书绑定，重复 SN 校验。
- 模板：导入模板下载（字段说明），导入报告（成功/失败明细）。
- 校验：SN 格式/型号存在性校验前置。

```javascript
// 批量建档
async function importDevices(file) {
  const rows = await parseCsv(file);
  const dup = rows.filter((r, i) => rows.findIndex(x => x.sn === r.sn) !== i);
  const invalidModel = rows.filter(r => !MODELS.has(r.model));
  if (dup.length || invalidModel.length)
    return { ok: false, dup: dup.map(d => d.sn),
      invalidModel: invalidModel.map(r => r.sn) };
  return api('/device/import', rows);
}
```
