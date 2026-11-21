---
title: [AIC-256] AI 门禁如何防止被「糊弄」（写敷衍 commit message、拆小 PR 绕过、在描述里塞提示词）？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-256：AI 门禁如何防止被「糊弄」（写敷衍 commit message、拆小 PR 绕过、在描述里塞提示词）？
**答**：
- 评审对象是 diff 本身而非描述：提示词注入防护——diff 内容中的指令性文本一律视为代码处理。
- 统计特征兜底：PR 频率异常、小 PR 连续高频、diff 内容与描述不匹配时升级人工。
- 绕过检测记录进审计：谁、何时、什么方式绕过，作为治理数据而非惩罚工具。
- 门禁只防低级绕过，核心是让「合规成本 < 绕过成本」：AI 评审快速反馈本身就是激励。

```javascript
const antiBypass = (diff: string) => ({
  promptInjection: /忽略以上|ignore previous|system prompt/i.test(diff)
    ? 'treat-as-code' : 'normal',
  suspicious: prFreq(user) > 10 / day && avgLines < 5 ? 'flag-review' : 'ok',
});
r
```
