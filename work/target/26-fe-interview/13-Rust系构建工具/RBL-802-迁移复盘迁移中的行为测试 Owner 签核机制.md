---
title: [RBL-802] 迁移复盘：Owner 签核机制——为什么机器全绿还不够
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-802：迁移复盘：Owner 签核机制——为什么机器全绿还不够

**答**:
- 迁移验证的盲区：自动化测试（语义 diff/行为测试）覆盖「已知语义」，但业务 owner 才知道「哪些行为是隐含依赖」（老构建器的某个意外行为被业务依赖了——如 chunk 顺序导致的加载时序、资源 URL 的历史形状被统计脚本引用）。Owner 签核 = 人工确认「业务关心的点没变」。
- 签核的最小化设计：不要求 owner 看全部 diff——给 owner 的材料是「用户可见差异摘要」（路由/页面/资源清单的变化点），签名对象是「这些变化我确认 OK」——把审查负担压到人擅长的判断上。
- 签核的时机：不是合并前（那时 diff 抽象），而是**预发环境真实验证后**（owner 在预发点一遍核心流程）——真实环境的验证比 diff 报告可信。
- 签核的防形式化：签名记录「验证了什么」（核心路径清单 + 截图/录屏链接），不是纯按钮——审计时能追溯验证深度；「无差异签核」（diff 为空）也要走流程（形式化最小化但仍留痕）。
- 追问钩子：为什么 owner 签核不能被「自动化测试覆盖率提升」取代？——覆盖率度量的是「已知的代码路径」，owner 验证的是「业务连续性」（数据展示正确/埋点照常上报/与后端的隐式契约）——两者的验证对象不同类，机器验证再强也不能替代「业务判断」；工程答案是「机器全绿 + 人工签核」双门禁。

```javascript
// 签核记录结构
const signoff = {
  repo: 'app-checkout',
  buildId: 'b-2026',
  verifiedPaths: ['/', '/cart', '/checkout', '/order-confirm'],   // 核心路径清单
  evidence: ['https://recorder/clip-1', 'console-clean.png'],      // 录屏/截图
  diffSummary: { routeChanges: 0, assetRenames: 12, chunkMoves: 3 },
  owner: '@checkout-team-lead',
  signedAt: '2026-11-22T10:00:00Z',
};
function requireSignoff(migration) {
  if (migration.semanticDiff.length === 0 && migration.behaviorTests === 'green')
    return;                                              // 零差异 + 行为绿：免签核（留痕即可）
  if (!migration.signoff?.owner)
    fail('迁移需要业务 owner 签核（预发验证后）——机器全绿不覆盖业务连续性');
}
```
