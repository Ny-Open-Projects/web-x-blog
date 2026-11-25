---
title: [SCN-1148] IoT 设备控制台的设备搜索快捷入口（资产标签）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1148：IoT 设备控制台的设备搜索快捷入口（资产标签）

**答**：
- 标签：设备贴二维码（资产标签），扫码直达设备详情+操作（移动运维）。
- 打印：批量打印资产标签（设备 SN+二维码）。
- 盘点：扫码盘点（设备在场核验，盘亏报表）。

```javascript
// 资产标签盘点
async function assetInventory(scanned) {
  const all = await api('/device/ids');
  const missing = all.filter(id => !scanned.includes(id));   // 盘亏
  const unknown = scanned.filter(s => !all.includes(s));     // 盘盈
  return { missing, unknown,
    report: () => api('/device/inventory-report', { missing, unknown }) };
}
```
