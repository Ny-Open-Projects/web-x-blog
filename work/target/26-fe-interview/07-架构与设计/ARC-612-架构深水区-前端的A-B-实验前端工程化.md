---
title: [ARC-612] AB 实验的前端工程化（实验接入的成本降到最低）如何做？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-612：AB 实验前端工程化
**答**:
- 接入成本问题：每个实验手写分桶判断/埋点标注/开关清理——实验多时混乱。工程化：实验 SDK 统一（分桶/缓存/上报 ARC-423）+ 代码级实验原语（实验分支组件化）。
- 代码原语：条件组件（<Experiment id="x" variants={{ a: <A/>, b: <B/> }} fallback={<A/>}/>——分桶/兜底/曝光埋点内置）、参数注入（useExperiment(id) 返回配置参数——文案/阈值类实验不改代码只改配置）。
- 生命周期自动化：实验创建（平台申请 → 生成接入代码片段）、运行中（曝光/转化自动埋点 ARC-390）、结束（平台推送结论 → 转正流程 ARC-555；未接清理提醒——实验代码遗留检测：lint 扫 Experiment 组件存量）。
- 质量保障：实验分流正确性测试（同用户稳定/流量比例正确——SDK 单测）、实验与性能预算（实验代码也占体积——下线实验代码及时清理，ARC-288 治理）。
- 组织：实验评审（前端侧：可行性/性能影响/埋点完整性评估）。
```tsx
// 实验原语
<Experiment id="pay-btn-color" variants={{
  control: <Btn color="red" />, t1: <Btn color="green" />
}} fallback={<Btn color="red" />} />                              // 曝光/分桶/埋点内置
const { copy } = useExperiment('pay-copy');                       // 参数型实验（配置）
```
