---
title: [NODE-342] Node 服务的 Excel 与 CSV 处理链路如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-342：Node 服务的 Excel 与 CSV 处理链路
**答**:
- 导出（大流量）：流式生成——exceljs stream writer 或 CSV 逐行写（CSV 无样式需求时首选，体积小速度快）；写法上 setHeader + 定量 flush + 背压等待（write 返回 false 等 drain），禁整表驻内存。
- CSV 陷阱：BOM（Excel 中文乱码需 \uFEFF 开头）、注入防护（以 = + - @ 开头的单元格前加 ' 防公式注入）、转义（逗号引号换行）。
- 导入：流式解析（csv-parser/exceljs 读流）逐批校验入库，行级错误收集（行号+原因），大文件走异步任务（ARC-486/490）。
- 类型与格式：日期/金额序列化规则统一（ISO 字符串、整数分），数字防精度（文本格式写长单号防 Excel 科学计数法）。
- 资源控制：导入并发限流、导出任务配额，处理超时与失败重试。
```javascript
// exceljs 流式导出
const wb = new Excel.stream.xlsx.WorkbookWriter({ filename });
const ws = wb.addWorksheet('orders');
ws.columns = [...headers];
for await (const row of db.stream('select ...')) {
  ws.addRow(mapRow(row)).commit();                             // 逐行提交
}
ws.commit(); wb.commit();                                       // 落盘后上传 OSS
// CSV: res.write('\uFEFF') 先写 BOM
```
