---
title: [ARC-510] 地图选点/POI 交互（打车/外卖场景）的前端架构如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-510：地图选点与 POI 交互架构
**答**:
- 场景特征：高频拖图 + 选点精化（起终点）、POI 列表与地图联动、地址解析链路（ARC-455 地图基础上的业务层）。
- 选点状态机：自由拖动 → 停止（防抖）→ 逆地理编码（坐标 → 地址）→ POI 候选列表 → 用户精化选择 → 确认。逆地理编码防抖 + 竞态取消（ARC-383）；POI 候选按视野请求。
- 联动架构：地图视野变化驱动 POI 列表（ARC-455 moveend 模式）；列表 hover → 地图 marker 高亮（单向联动防循环）。
- 精度与校验：定位权限降级链（精确 → 城市 → 手动输入）；选点纠偏（坐标系转换收口 ARC-455）；服务范围校验（起终点超出服务区提示）。
- 性能与体验：拖动时禁用重计算（松手才算）、POI marker 按视野聚合（万级 POI）、路线绘制懒加载（选好起终点才算路）。
```javascript
// 选点状态机
const picker = machine({
  idle: { dragstart: 'dragging' },
  dragging: { dragend: 'resolving' },
  resolving: async (ctx) => {                                     // 防抖后逆编码
    const { pois, address } = await geocode(ctx.center, { signal: ctx.signal });
    ctx.set({ pois, address }); return 'picking';
  },
  picking: { pick: 'confirmed', dragstart: 'dragging' },
  confirmed: { reselect: 'dragging' }
});
```
