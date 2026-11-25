---
title: [NODE-902] 笔试题——实现多实例灰度参数一致性（配置同步校验）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-902：手写灰度参数一致

**需求与边界**：
- 需求：多实例灰度参数一致（SCN-NODE-663/OPS-573）——① 灰度参数的实例同步（配置中心推送——SCN-NODE-663）；② 一致性校验（各实例生效版本——周期上报比对，SCN-NODE-902）；③ 漂移实例的告警（版本落后——配置未生效，SCN-NODE-663）；④ 漂移的处理（重启实例——SCN-NODE-665）。
- 边界：① 一致性上报的开销（30s 心跳携带版本——SCN-OPS-216）；② 漂移期间的分流风险（不同实例不同灰度——用户横跳，SCN-OPS-244 sticky 缓解）；③ 漂移的根因（推送丢失/启动时序——SCN-NODE-663 回退缓存）。

**答**：
```javascript
setInterval(() => {
  heartbeat({ instance, configVer: currentConfigVer(), grayVer: grayRules.version });   // 版本心跳
}, 30_000);
// 聚合比对
const drifts = instances.filter(i => i.grayVer !== expectedVer);   // 漂移实例
if (drifts.length)
  alert({ type: 'GRAY_DRIFT', instances: drifts,
    risk: '灰度参数不一致——用户横跳风险（SCN-OPS-244）',
    fix: drifts.map(d => `重启 ${d.instance}（SCN-NODE-665 滚动）`) });   // 处理建议
```

**评分点**:
- 版本心跳上报（SCN-NODE-663/OPS-216）。
- 漂移实例告警 + 风险声明（用户横跳——SCN-OPS-244）。
- 处理建议（滚动重启——SCN-NODE-665）。
- 根因（推送丢失/回退缓存——SCN-NODE-663）。
