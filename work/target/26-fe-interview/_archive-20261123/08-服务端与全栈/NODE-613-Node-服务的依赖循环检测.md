---
title: [NODE-613] Node 服务的循环依赖（CJS/ESM 语义差异与治理）如何处理？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-613：循环依赖治理
**答**:
- 语义差异：CJS 循环依赖（部分导出——拿到未完成的 exports，隐式 bug 温床 NODE-004）、ESM 循环（hoisting 下函数声明可用/const 不可——TDZ 报错）、行为差异导致"重构后炸了"（CJS→ESM 迁移暴露隐藏环——NODE-420 检查项）。
- 检测工具：madge/dependency-cruiser（CI 循环检测——违规阻断，允许白名单过渡）、运行时检测（加载顺序日志——dev 启动告警环）。
- 治理手法：提取共享（环的两模块共同依赖 → 抽第三个模块——最常用解）、接口反转（依赖方向反转：A 依赖 B 的接口——B 实现接口注入（DI 解环）NODE-515）、事件解耦（同步依赖改事件——弱化耦合 ARC-080，注意时序语义变化）、延迟 require（动态 import 打破加载环——治标，环仍在）。
- 预防：设计期依赖方向（分层/域边界规则——ARC-396 适应度函数）、单例注册中心（服务定位器模式替代互相 import——慎用，隐式依赖）。
- 度量：循环依赖数（趋零目标）、环引入频率（新增环的 MR 归因）。
```javascript
// madge CI 检查
npx madge --circular src/ --extensions ts  || exit 1
// 解环示例：service-a 与 service-b 互调 → 提取 shared/OrderPolicy 或 事件解耦（a.emit → b.on）
```
