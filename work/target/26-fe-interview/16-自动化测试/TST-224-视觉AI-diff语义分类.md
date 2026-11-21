---
title: [TST-224] AI 如何辅助视觉 diff 判定「是否真回归」？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-224：AI 如何辅助视觉 diff 判定「是否真回归」？
**答**：
- diff 图 + 变更上下文喂给视觉模型，输出分类：真实回归（布局崩/文案错）/可接受差异（抗锯齿/动态内容）/无关紧要。
- 分类结果只是建议：真实回归才阻塞，其余转人工快扫——降低人审疲劳。
- 误判回流：人工纠正的分类样本回流训练/提示词，提升判定准确率。
- 关键是「语义」判定：像素 diff 工具只知道不同，AI 能判断「坏没坏」。

```javascript
async function classifyDiff(diffPng: Buffer, ctx: string) {
  const r = await vlm(`对比截图差异，判断是：real-regression / acceptable / noise。
上下文：${ctx}。输出 JSON {category, confidence, reason}`);
  return r.category === 'real-regression' ? 'block' : 'human-quick-check';
}
r
```
