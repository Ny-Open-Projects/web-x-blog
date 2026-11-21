---
title: [AGT-306] 写作助手 Agent——风格一致与事实正确的双约束？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-306：企业写作助手（营销文案/公告/报告）怎么保证风格一致且事实正确？

**答**:
- 风格控制：风格规范结构化（tone/术语表/禁用词/句式偏好入配置，注入 prompt 而非"模仿这个例子"）、少样本用品牌语料库精选（示例质量=输出质量上限）、生成后风格 judge 打分（偏离规范触发重写）。
- 事实约束：营销文案中的数字/资质/承诺类内容必须来自审核过的素材库（RAG 引用，AGT-262），不得模型自创——"夸大宣传"是合规事故源，承诺类词表硬拦截。
- 工作流：大纲→分节生成→整合润色（分步可控可改，用户在每步介入）而不是一次成文；版本管理（多版本并列对比选优）+ 修订记录。
- 评测：风格一致率（judge+人工）、事实合规率（引用完整性+违禁词扫描）、采纳率（生成→使用的转化）——写作助手的价值度量是"被采用的比例"。

```javascript
async function writeCopy(brief) {
  const style = loadStyleGuide(brief.brand);   // tone/术语/禁用词
  const facts = await retrieve(brief.topic, { source: 'approved' });
  const draft = await llm({ brief, style, facts,
    rules: ['数字必须来自 facts 并标注',
            '禁用承诺词表外词汇'] });
  const audit = await Promise.all([
    styleJudge(draft, style),                  // 风格分
    bannedScan(draft), factAudit(draft, facts)]);
  return audit.ok ? draft : rewrite(draft, audit.notes);
}
```
