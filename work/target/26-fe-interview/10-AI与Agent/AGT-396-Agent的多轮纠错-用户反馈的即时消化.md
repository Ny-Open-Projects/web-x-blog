---
title: [AGT-396] 多轮纠错——用户说"不对，我指的是…"时怎么处理？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-396：用户纠正 Agent（"不是这个意思"）时，纠错机制怎么设计？

**答**:
- 纠错响应四步：确认理解（复述用户的纠正——"您指的是 X 而不是 Y，对吗"——纠错时复述确认能消除二次误解，AGT-466 收反馈同款）、定位错误源（理解错/检索错/数据错——对应不同修复）、修正输出（基于纠正重新生成，明确引用用户的纠正为最高优先约束）、固化（本次会话内该约束提升为高优先记忆——不再犯同型错误，会话级 AGT-363 保留）。
- 纠错类型分派：意图纠正（"我说的是华东不是华南"→查询重做）、偏好纠正（"不要太正式"→风格调整并记入画像 AGT-329）、事实纠正（"这个数据错了"→数据源核查——用户说数据错不能盲信，核查后确认再改——防恶意纠错污染）。
- 重复纠错检测：同一问题被纠正 ≥2 次→升级策略（换问法澄清/承认理解困难并提供人工通道）——反复纠正的体验损伤远大于一次做对的价值。
- 数据回流：纠错样本是高质量训练数据（AGT-354 数据飞轮）——自动入集与 DPO 数据（授权合规）。

```javascript
async function handleCorrection(u, ctx) {
  const ok = await confirmUnderstanding(u);      // 复述确认
  const kind = classify(u);                      // 意图/偏好/事实
  if (kind === 'fact') await verify(u.claim);    // 不盲信
  ctx.constraints.unshift(u);                    // 最高优先约束
  if (ctx.correctionCount(u.topic) >= 2)
    return escalateOrClarify(u);                 // 重复纠错升级
  return regenerate(ctx, u);
}
```
