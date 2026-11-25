---
title: [RBL-589] 构建器的 feature flag 发布模型：高风险优化如何安全放量
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-589：构建器 feature flag 发布模型：高风险优化如何安全放量

**答**：
- 构建器不能像 Web 服务一样灰度到「1% 用户」——每个用户只有 0/1 两态，且构建结果是确定性的。所以「灰度」的对象换成了：1) **opt-in 阶段**（experimental 标志，文档明示风险，收集 issue）；2) **内部孵化**（公司内部 monorepo 先吃狗粮，覆盖真实大仓库）；3) **默认开启前的兼容窗口**（新行为开 flag、旧行为 deprecate、一个 minor 版本后翻转默认值）。
- 高风险优化的必备三件套：**逃生门**（flag 可一键关闭回旧行为，且旧行为至少保留两个 minor）；**特征化诊断**（开启后自动产出兼容性检查报告，如 tree-shaking 激进模式列出「可能被误删的副作用模块」）；**行为指纹对比**（新旧两种模式各构建一次，diff 产物语义报告——用户决定是否切换）。
- 版本纪律：experimental 字段无兼容性承诺但**命名要显眼**（experimental. 前缀），stable 化时的迁移成本要在文档里给足（codemod/config diff）；默认值翻转的版本必须在 changelog 顶部加 BREAKING 区块。
- 数据驱动放量：telemetry（opt-in 匿名上报：flag 使用率/失败率/回退率）——回退率高说明逃生门被频繁使用，特性需要回炉；这是构建工具少有的「运行时反馈」渠道。
- 追问钩子：为什么构建器的 bug 常常是「静默错」而不是「崩溃错」？——错误打包往往产出「能跑但语义错」的产物（循环依赖顺序/副作用误删），崩溃反而是好事；所以 feature flag 的验证手段必须是「语义 diff + 行为测试」而不是「跑起来没报错」。

```javascript
// 双模式对比报告（切换决策依据）
async function compareModes(config) {
  const old = await build({ ...config, experimental: { ...config.experimental, aggressiveShake: false } });
  const neu = await build({ ...config, experimental: { ...config.experimental, aggressiveShake: true } });
  return {
    sizeDelta: neu.size - old.size,                 // 预期：变小
    semanticDiff: diffExports(old, neu),            // 语义 diff：不应有导出消失
    riskyModules: neu.diagnostics
      .filter(d => d.code === 'RBL2201'),           // 「可能误删副作用」特征化诊断
  };
}

// telemetry 上报（opt-in）
const telemetry = {
  flags: { aggressiveShake: { enabled: 0.42, fallback: 0.03, buildFailure: 0.001 } },
  report(flag, { enabled, fallback, buildFailure }) {
    if (!this.optIn) return;                        // 用户显式同意
    send('/telemetry', { flag, enabled, fallback, buildFailure, v: VERSION });
  },
};
// 放量决策：fallback 率 > 5% -> 回炉；< 1% 且无 buildFailure 上升 -> 默认开启候选
```
