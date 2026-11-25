---
title: [MFW-666] Legacy 浏览器降级矩阵：nomodule 双包
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-666：Legacy 降级矩阵与 nomodule 双包

**答**:
- 双包策略：1) **modern 包**（ES2020+：module script——现代浏览器）；2) **legacy 包**（ES5 + polyfill：nomodule script——旧浏览器执行）；3) 分发协议：`<script type="module">`（现代浏览器执行）+ `<script nomodule>`（旧浏览器执行——浏览器自动选择）；「双包的正确性 = 行为一致」（两包的语义等价测试 RBL-655——RBL-622 的元框架版）。
- 构建器产出：browserslist 双目标 → 双 bundle（Next 的 legacyBuildSupport；babel targets）——构建成本 ×2（时间/体积——legacy 包仅给需要的浏览器（分发占比 <5% 时成本考量））。
- 降级的检测：用户浏览器的实际分布（RUM browser 占比——legacy 占比 <1% = 可考虑放弃支持（业务决策）；「放弃的决策依据」= RUM 数据而非假设）。
- 追问钩子：为什么「双包的正确性验证」是双包方案的最大成本？——两包由不同编译器产出（esbuild vs babel——行为可能有差异：polyfill 差异/语法转换语义差异）；「行为等价」的验证：同一测试集在两包上跑（RBL-685 矩阵一致性）；差异 = 静默 bug（legacy 用户的功能缺失——占比小但真实用户）；双包的 ROI：legacy 用户占比 × 行为差异风险 vs 双包构建成本——占比 <1% 时「放弃 legacy」可能是更负责任的决策（数据驱动）。

```typescript
// 双包构建配置
// next.config: { compiler: { browserslist: ... } }
// HTML 分发
// <script type="module" src="/_next/static/modern.js"></script>
// <script nomodule src="/_next/static/legacy.js"></script>
// 浏览器自动选择：现代 → module 跳过 nomodule；旧 → 忽略 module 执行 nomodule
// 行为一致性验证（RBL-685）
async function verifyDualBundle(modernUrl, legacyUrl, testCases) {
  for (const tc of testCases) {
    const modernResult = await runInBrowser(tc, { scriptType: 'module' });
    const legacyResult = await runInBrowser(tc, { scriptType: 'nomodule', legacy: true });
    if (!deepEq(modernResult, legacyResult))
      fail(`双包行为不一致: ${tc.name}——modern=${modernResult} legacy=${legacyResult}`);
  }
}
// RUM 数据驱动的放弃决策
const legacyShare = rum.browserShare({ es5: true });
if (legacyShare < 0.01) {
  console.log(`legacy 占比 ${(legacyShare * 100).toFixed(1)}% < 1%——建议放弃双包（业务决策）`);
}
```
