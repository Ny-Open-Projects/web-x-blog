---
title: [AGT-381] 多语言 Agent——跨语言能力与本地化工程？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-381：面向多语言用户的 Agent，跨语言能力怎么工程化？

**答**:
- 跨语言检索：query 语言 ≠ 文档语言（中文问英文库）——多语言 embedding（跨语言对齐的模型）或查询翻译双路（原文检索+翻译后检索取并集）；专有名词保留原文不翻译（翻译专名是检索失败源）。
- 输出本地化：回答语言跟随用户语言（prompt 语言规则+用户偏好优先）、术语本地化词表（产品名/法律术语的官方译法）、格式本地化（日期/数字/货币格式按 locale）。
- 质量不均衡治理：模型在低资源语言质量下降——按语言分桶评测（AGT-259 分桶思想），低资源语言的答案加"语言质量可能打折"的呈现策略或路由到更强的处理链。
- 文化与合规：示例/措辞的文化适配（幽默/称谓/敏感话题按地区）、各地区的合规差异（内容审查标准/数据驻留）——本地化不只是翻译。

```javascript
async function multiLingualQA(q, locale) {
  const lang = detect(q);
  const [r1, r2] = await Promise.all([
    vectorSearch(q),                                  // 原文
    vectorSearch(await translate(q, 'en', { keepNames: true })),
  ]);                                               // 双路
  const out = await llm(`以 ${locale} 回答；术语用官方词表
    ${GLOSSARY[locale]}；数字格式按 locale。`, rrf([r1, r2]));
  return langQualityCheck(out, lang);               // 低资源语言标注
}
```
