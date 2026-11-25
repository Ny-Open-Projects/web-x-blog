---
title: [WEB-525] 线上问题值班响应 SOP（前端视角）
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-525：线上问题值班响应 SOP（前端视角）

**答**：
- 响应分级：P0（全站不可用/支付失败）15 分钟内响应；P1（核心流程降级）1 小时；P2（体验问题）当日——先确认级别再动手
- 处置顺序：止血（回滚/降级开关）→ 定位（监控 diff、错误堆栈）→ 修复 → 复盘，永远止血优先
- 前端专属动作清单：错误率看板、白屏率、静态资源 404、CDN 状态、发布记录 diff——多数 P0 前端事故是发布引发的
- 沟通纪律：同步节奏固定（每 15 分钟一次进展）、统一对外口径、不猜不传未经证实的原因
- 复盘模板：时间线、影响面、根因（技术+流程）、行动项（带负责人与期限）

```javascript
// 值班自检脚本：一键采集当前站点健康度
const health = {
  jsErr: window.__errRate, white: whiteScreenRate(),
  cdn404: resourceFailCount(), build: BUILD_VERSION,
};
console.log(JSON.stringify(health));
```
