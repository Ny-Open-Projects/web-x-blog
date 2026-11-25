---
title: [HW-210] 手写能力检测降级矩阵——Permissions-Policy/特性检测驱动的组件降级声明式配置？
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-210：手写能力检测降级矩阵——Permissions-Policy/特性检测驱动的组件降级声明式配置？
**答**：能力驱动组件降级的声明式矩阵：能力清单（摄像头/通知/剪贴板/SharedArrayBuffer 等）→ 每能力三级（支持/受限/不支持）→ 组件声明"需要哪些能力+每级降级渲染"→ 运行时按矩阵渲染。检测一次缓存（能力不频繁变化）+ 变更监听（权限授予后升级）。

```javascript
const CAPABILITIES = {
  camera: async () => !!(navigator.mediaDevices?.getUserMedia)
    && (await navigator.permissions.query({ name: 'camera' })).state !== 'denied',
  clipboardWrite: async () => !!navigator.clipboard?.writeText,
  notifications: () => 'Notification' in window,
  sab: () => typeof SharedArrayBuffer === 'function',     // 需要 COOP/COEP 头
};
const cache = new Map();
async function capability(name) {
  if (!cache.has(name)) cache.set(name, CAPABILITIES[name]?.() ?? Promise.resolve(false));
  return cache.get(name);
}
// 组件声明式降级：
const ScannerComponent = {
  requirements: { camera: 'required' },                   // required: 无能力渲染降级 UI
  levels: { full: FullScanner, basic: QRScanFallback, none: ManualInputForm },
  async resolve() {
    const ok = await capability('camera');
    return ok ? this.levels.full : this.levels.basic;
  },
};
// 降级链：full（实时识别）→ basic（单张拍照识别）→ none（手动输入编号）—— 功能逐级可用
// Permissions-Policy 头（camera=() 禁用）时 capability 检测失败 → 自动走降级——策略与运行时统一
// 权限变更监听：permissions.onchange → 清缓存重查（用户授权后组件升级 full）
```

**评分点**：
- 声明式降级矩阵（能力检测 + levels 三级渲染）——本题核心。
- Permissions-Policy 与运行时检测的统一（头禁用 = 自动降级）。
- 权限变更监听（onchange 清缓存升级）。
- 能力检测缓存 + 每能力的检测函数隔离。
