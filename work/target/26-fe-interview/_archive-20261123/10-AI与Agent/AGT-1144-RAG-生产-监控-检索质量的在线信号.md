---
title: [1144] 没有人工标注，怎么从线上信号推断检索质量
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 监控]
type: 面试题
---

## 1144：没有人工标注，怎么从线上信号推断检索质量

**答**：
- 五个免费在线信号：检索分数分布漂移（top1 分数分布突变 = 索引/模型异常）、用户行为（点击引用 / 复述问题 / 点踩）、拒答率、答案-来源相似度（生成是否真的用了检索内容）、会话中断率（检索差导致用户流失）。
- 信号组合成「检索健康分」：各信号标准化加权，低于阈值告警——单信号噪声大，组合才稳。
- 定期校准：每季度用人工标注的抽样验证「健康分」与真实质量的相关性，防止信号衰减。
- 追问钩子：哪个信号最早发现检索退化？——实践中「复述问题率」（用户换说法重问）最敏感，早于点踩与拒答率，因为用户先自救再抱怨。

```ts
const health = weighted({
  scoreDrift: z(top1ScoreDist, baseline),        // 分布漂移
  rephraseRate: rate(rephrased),                 // 复述重问（最敏感）
  rejectRate: rate(rejected),
  citeClick: rate(citationClicked),
  genUse: sim(answer, sources),                  // 生成是否用了材料
}, { rephraseRate: 2 });                          // 敏感信号加权
alert.if(health < 0.7);
```
