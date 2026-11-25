---
title: [PER-1090] 如何建立前端安全的"威胁模型"（STRIDE 简化应用）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1090：如何建立前端安全的"威胁模型"（STRIDE 简化应用）

**答**：
- 按资产盘点：用户数据、登录态、支付能力、内容发布权——每资产列威胁。
- STRIDE 简化：伪装（会话劫持）、篡改（参数注入）、抵赖（日志缺失）、信息泄露（XSS/日志）、拒绝服务（前端死循环）、提权（越权接口）。
- 输出：威胁清单 × 现有防线 × 缺口，缺口进 roadmap；每次大功能上线走一遍轻量建模。
- 实践：建模不需要重型文档，一个表格 + 评审会即可，关键在"攻击者视角"习惯。

```javascript
// 威胁模型表生成
function threatModel(assets) {
  const STRIDE = ['伪装', '篡改', '抵赖', '泄露', '拒服', '提权'];
  return assets.map(a => ({
    asset: a.name,
    threats: STRIDE.map(t => ({
      type: t,
      vector: a.vectors?.[t] ?? '待分析',
      control: a.controls?.[t] ?? null,       // 已有防线
      gap: !a.controls?.[t],                  // 缺口标记
    })),
  }));
}
// 评审会逐行过 gap，输出修复优先级
```
