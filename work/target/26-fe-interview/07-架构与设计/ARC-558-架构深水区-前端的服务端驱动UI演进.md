---
title: [ARC-558] 服务端驱动 UI（SDUI）的演进架构如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-558：服务端驱动 UI（SDUI）演进架构
**答**:
- SDUI 定位：服务端下发"组件类型 + 配置 + 顺序"（营销位/动态卡片），客户端渲染器按注册表渲染——运营可配 + 客户端免发版更新页面结构（ARC-437 动态化、ARC-503 活动页的通用化）。
- 演进核心问题：客户端组件版本碎片（老版本没有新组件类型）——服务端下发前按客户端能力过滤（ARC-556 能力协商：不支持的类型降级为老组件或不下发）；组件协议版本化（新增属性老版本忽略——前向兼容，ARC-449 字段级）。
- 渲染器架构：组件注册表（客户端声明支持的组件类型 + 版本）、schema 校验（不认识/不合法的配置渲染兜底卡片——永不白屏）、降级链（SDUI 失败 → 内置默认布局）。
- 安全与体验边界：SDUI 不下发任意 HTML/逻辑代码（白名单组件 + 配置数据——防服务端被攻破后变成远程代码注入 ARC-355）；图片/跳转链接域名白名单。
- 治理：组件库存量统计（各版本使用率）、SDUI 配置的预览工具（发布前所见即所得验证）。
```javascript
// 能力协商 + 兜底渲染
const components = registry.supported();                         // ['banner','grid','video']
const cards = serverCards.filter(c => components.includes(c.type) &&
  semver.gte(c.minClient, CLIENT_VERSION));
render(cards.map(c => validate(c) ? rendererOf(c.type)(c) : FallbackCard(c))); // 校验 + 兜底
```
