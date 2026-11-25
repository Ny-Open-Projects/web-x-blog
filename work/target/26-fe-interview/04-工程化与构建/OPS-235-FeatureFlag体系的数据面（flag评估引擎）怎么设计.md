---
title: [OPS-235] Flag 评估引擎（决策的数据面）怎么设计？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## OPS-235：Flag 评估引擎怎么设计？
**答**：
- 评估模型：规则集（用户属性/百分比/白名单/时间窗）按序求值——规则顺序即优先级，规则集版本化（变更可审计可回滚）。
- 性能路径：评估在客户端 SDK 本地完成（规则集快照下发，本地求值零网络）——评估引擎必须 O(flag数×规则数) 且微秒级（渲染路径上）。
- 一致性：同会话评估结果稳定（用户属性快照固化），跨刷新不一致会造成功能闪烁——会话内属性快照是关键。
- 调试能力：决策日志（哪个 flag/命中哪条规则/为什么）可查询——「为什么用户没进灰度」是运营最常问的问题。
- 追问钩子：为什么评估引擎要「会话内属性快照」——用户属性（VIP 等级/地域）会实时变化；每次评估用实时属性会让用户中途「跳出」实验组（体验闪烁+实验数据污染）；会话开始时固化属性快照，保证实验期内分组稳定——这是实验科学的基本要求。

```javascript
class EvalEngine {
  constructor(rulesSnapshot, userSnapshot) {           // 双快照：规则 + 用户属性
    this.rules = rulesSnapshot; this.user = userSnapshot;
  }
  evaluate(flagKey) {
    for (const rule of this.rules[flagKey] ?? []) {
      if (rule.match(this.user))                       // 本地求值，零网络
        return { value: rule.value, matched: rule.id };
    }
    return { value: this.defaults[flagKey], matched: 'default' };
  }
  debug(flagKey) { return this.decisionLog(flagKey); } // 决策可查询
}
```
