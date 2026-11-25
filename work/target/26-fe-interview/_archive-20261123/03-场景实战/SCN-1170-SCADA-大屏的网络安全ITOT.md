---
title: [SCN-1170] SCADA 大屏的网络安全（IT/OT 隔离下的前端架构）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1170：SCADA 大屏的网络安全（IT/OT 隔离下的前端架构）

**答**：
- 隔离：OT 网（PLC）与 IT 网隔离——数据经单向网闸/工业网关进 IT，前端只读 IT 侧数据。
- 只读：大屏/前端绝不下发控制（控制走 OT 侧组态），前端只读展示（防攻击面）。
- 审计：前端访问审计（车间大屏专人负责）。

```javascript
// IT/OT 隔离
function scadaSecurity(frontend) {
  return {
    readonly: true,                                    // 前端只读
    source: 'dmz-gateway',                             // 数据经隔离网闸
    noControl: '控制指令走 OT 侧组态，前端不下发',
    audit: frontendAccessLog(),
  };
}
function frontendAccessLog() { return []; }
```
