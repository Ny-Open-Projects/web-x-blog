---
title: [PER-776] React Native 新架构（Fabric/TurboModule）对前端性能的实际影响：哪些旧优化还有效？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-776：React Native 新架构（Fabric/TurboModule）对前端性能的实际影响：哪些旧优化还有效？

**答**：
- 新架构变化：Fabric 同步渲染（渲染命令可在 JS 同步完成）、TurboModules 按需加载原生模块（启动时不再全量注入）、JSI 直接调用（去 Bridge 序列化）——**桥开销大幅下降**。
- 旧优化的存废：`maxToRenderPerBatch` 等 Batch 参数意义下降（同步渲染）；但**JS 线程仍会阻塞 UI 提交**（Fabric 中 layout 在 JS 线程算完才提交），虚拟列表窗口/轻组件/memo 依然有效；大 JSON 传输用 JSI 直接引用替代 Base64 桥传。
- 迁移注意：旧 AsyncStorage 等桥模块迁移到 TurboModule 后调用变同步化风险（要防长任务）；新架构下 Perf Monitor 的 JS fps 口径变化（含 layout 时间）。
- 度量：桥调用耗时（旧架构瓶颈指标）→ 新架构看 JS 线程总占用与首帧时间；升级前后分桶对比。

```javascript

const rnNewArch = {
  changes: { fabric: '同步渲染，layout 在 JS 线程算完提交', turbo: '原生模块按需加载',
    jsi: '直接调用去 Bridge 序列化' },
  legacyStillValid: ['虚拟列表窗口收窄', '轻组件/memo', '避免 JS 长任务（会阻塞 UI 提交）',
    '大 JSON 用 JSI 引用替代桥传'],
  legacyDeprecated: 'Batch 参数（maxToRenderPerBatch）意义下降：同步渲染后批次概念弱化',
  metrics: '桥耗时指标退役；看 JS 线程总占用与首帧时间，升级前后分桶对比',
};
console.log(rnNewArch.legacyStillValid.join(' / '));
```
