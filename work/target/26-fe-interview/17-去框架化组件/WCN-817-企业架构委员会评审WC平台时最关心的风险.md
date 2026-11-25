---
title: [WCN-817] 企业架构委员会（EAC）评审 WC 平台时最关心什么风险？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-817：企业架构委员会（EAC）评审 WC 平台时最关心什么风险？

**答**：
- 结论先行：EAC 站在公司全局看风险——他们不关心 WC 的语法细节，只关心「会不会造成技术栈分裂、锁定、合规事故和不可控的成本」。
- 技术栈一致性：WC 会不会与现有框架战略冲突？是否造成两套体系并存、长期维护翻倍？要给出「WC 作为平台层、框架作为应用层」的清晰定位。
- 供应商与锁定：组件依赖的 polyfill/CDN/工具链是否有单点依赖？License 是否合规？退出路径是什么？
- 安全与合规：影子树是否影响安全审计？敏感数据处理、CSP、供应链完整性是否有方案？
- 成本与可持续性：平台团队的长期投入、业务方迁移成本、失败后的退路（回退到框架组件）是否想清楚。
- 追问钩子：面试官会问「怎么回答『为什么不用现成方案』」——答：用决策矩阵与 TCO 对比说明自建的差异化价值与必要性，并明确「什么情况下会采购/开源」，显得理性而非盲目自研。

```javascript
// EAC 风险评审清单：命中高风险项需有缓解方案才能过审
const RISKS = {
  stackSplit:  { level: '高', mitigation: 'WC 定位平台层，框架仍用应用层，边界写入架构规范' },
  lockIn:      { level: '中', mitigation: '多 CDN + 无私有运行时锁定 + 明确退出路径' },
  compliance:  { level: '高', mitigation: '数据不落 attribute、SRI、审计事件可穿透影子树' },
  cost:        { level: '中', mitigation: '3 年 TCO 测算 + 分阶段投入 + 可回退方案' },
};
function reviewEAC(risks) {
  const highs = Object.entries(risks).filter(([, r]) => r.level === '高');
  return highs.every(([, r]) => r.mitigation) ? '通过（高风险均有缓解）' : '打回：高风险缺缓解方案';
}
console.log(reviewEAC(RISKS));
```
