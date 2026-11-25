---
title: [XP-215] Flutter 热重载 vs 热更新：开发体验与线上能力
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-215：Flutter 热重载 vs 热更新：开发体验与线上能力

**答**：
- Flutter 热重载：开发时快速 UI 刷新（不丢状态）——但仅 debug 模式；线上热更新：Shorebird（Dart patch）有限支持或动态化方案。
- 对比 RN CodePush：RN 热更新成熟（JS bundle 替换）；Flutter 编译型语言热更新受限（Shorebird 只支持 Dart 层小改动）。
- 合规：热更新需遵守应用商店规则（不绕过审核换核心功能）。

```javascript
const flutterHotReload = {
  devHotReload: { what: 'debug 模式亚秒级 UI 刷新（不丢状态）',
    limit: '不支持 main() 变更/全局变量初始化变更' },
  production: { shorebird: 'Dart 代码 patch（有限支持——不改 native/依赖）',
    alternative: 'Hybrid：Flutter + RN 混合（动态化部分用 RN）或自研 DSL 动态化' },
  compliance: 'iOS 禁止下载可执行代码——热更新不能改变核心功能（JSPatch 被拒案例）',
  decision: 'Flutter 线上动态化能力弱——需动态化的模块考虑 RN/自研 DSL',
};
```
