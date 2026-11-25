---
title: [VIZ-447] WebGL 上下文丢失（Context Lost）的恢复策略
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-447：WebGL 上下文丢失（Context Lost）的恢复策略

**答**：
- 原因：GPU 重置/资源耗尽（多标签页占用）——webglcontextlost 事件。
- 处理：preventDefault 阻止自动清理 -> 记录场景状态 -> restored 事件后全量重建（几何/纹理/program）。
- 预防：控制显存用量（439 预算）、监听丢失事件上报（平台监控）。

```javascript
// 上下文丢失恢复
canvas.addEventListener('webglcontextlost', e => {
  e.preventDefault();
  report({ type: 'context-lost', ts: Date.now() });
  snapshotScene();                                   // 场景描述序列化
});
canvas.addEventListener('webglcontextrestored', () => {
  recreateAll(gl);                                   // 重建全部 GPU 资源
  report({ type: 'context-restored', rebuildMs: Date.now() - lostAt });
});
```
