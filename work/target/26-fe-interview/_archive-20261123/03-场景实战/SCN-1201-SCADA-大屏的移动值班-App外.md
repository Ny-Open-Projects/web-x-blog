---
title: [SCN-1201] SCADA 大屏的移动值班 App（外勤巡检联动）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1201：SCADA 大屏的移动值班 App（外勤巡检联动）

**答**：
- 巡检：巡检任务（路线/点位/标准）App 执行，扫码+拍照+读数录入。
- 联动：巡检发现异常一键生成缺陷单（联动 1120 维保）。
- 防伪：巡检到位校验（NFC/定位+时间窗）。

```javascript
// 移动巡检
async function inspectionRun(route) {
  const points = route.points.map(p => ({
    ...p, check: async (reading, photo) => {
      const at = await nfcVerify(p.tagId);             // 到位校验
      if (!at) return { ok: false, reason: '未检测到到位' };
      const r = await api('/inspection/record', { point: p.id, reading, photo });
      if (p.abnormal(reading)) return createDefect(p, reading);   // 异常转缺陷单
      return r;
    } }));
  return { points };
}
async function nfcVerify(id) { return true; }
function createDefect(p, v) { return { ticket: 'D-1' }; }
```
