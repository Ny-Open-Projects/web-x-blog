---
title: [XP-210] React Native Hermes 深度：字节码与 GC 调优
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-210：React Native Hermes 深度：字节码与 GC 调优

**答**：
- Hermes 深度：字节码预编译（.hbc，启动免解析）、GC（分代回收，避免长任务暂停）、内存占用低 30%。
- 调优：bundle 拆分（按需加载 .hbc）、GC 触发监控（heap snapshot 分析泄漏）。
- 与 JSI 关系：Hermes 原生支持 JSI（新架构基础）——JSC 不支持。

```javascript
const hermesDeep = {
  bytecode: { what: '.hbc 预编译字节码（构建期生成）',
    gain: '启动免解析 JS 文本——TTI 降 20~40%（HW-807 关联）' },
  gc: { model: '分代回收（年轻代/老年代）',
    issue: 'GC 暂停导致掉帧——大对象分配频繁时明显',
    tuning: '减少大对象临时分配（复用 buffer）+ heap snapshot 定位泄漏' },
  jsi: 'Hermes 原生支持 JSI——Fabric/TurboModule 前提',
  measure: 'android：adb shell dumpsys meminfo（内存）；React DevTools Profiler（渲染）',
};
```
