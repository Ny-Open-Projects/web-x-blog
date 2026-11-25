---
title: [SCN-1141] IoT 设备控制台的界面响应优化（大数据量表格）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1141：IoT 设备控制台的界面响应优化（大数据量表格）

**答**：
- 表格：万级设备表格——虚拟滚动 + 列固定 + 状态列 patch 更新。
- 排序筛选：服务端执行（前端传参），避免全量拉取。
- 导出：可见列导出（筛选条件同步）。

```javascript
// 大表格
function deviceTableQuery({ page, size, sort, filters }) {
  return api('/device/table', { page, size, sort, filters });   // 服务端排序分页
}
// 虚拟滚动：行高 48px 固定，窗口 ±10 行（314 统一抽象）
```
