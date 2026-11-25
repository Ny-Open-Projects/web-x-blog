---
title: [XP-200] Electron 收束：桌面端能力清单与选型决策
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-200：Electron 收束：桌面端能力清单与选型决策

**答**：
- XP-181~200 收束——安全（contextIsolation/CSP/路径校验）、性能（启动/内存/窗口池）、集成（托盘/通知/深链/菜单）、数据（SQLite/离线同步）、工程（打包/更新/测试/监控）。
- 选型决策：文件系统深度操作/系统托盘/多窗口/原生模块 → Electron；Web 增强 → PWA；轻量跨平台 → Tauri（Rust，体积小）。
- 主线：安全是底线（渲染进程不信任）→ 性能围绕进程管理 → 工程围绕打包分发。

```javascript
const electronCapabilityMap = {
  security: ['XP-181 IPC', 'XP-182 contextIsolation/CSP', 'XP-185 路径校验'],
  performance: ['XP-184 启动/内存', 'XP-193 MessagePort/Utility', 'XP-196 监控', 'XP-198 崩溃恢复'],
  integration: ['XP-188 托盘/通知/快捷键', 'XP-190 菜单', 'XP-195 深链', 'XP-187 Native addon'],
  data: ['XP-189 SQLite/LevelDB', 'XP-192 离线优先', 'XP-194 生命周期'],
  engineering: ['XP-183 自动更新', 'XP-191 打包', 'XP-197 测试', 'XP-199 独占锁'],
  decision: {
    electron: 'IDE/重桌面/深度系统集成',
    pwa: 'Web 增强/轻量跨平台',
    tauri: '轻量桌面（Rust 后端，~10MB）——新项目可考虑',
  },
};
```
