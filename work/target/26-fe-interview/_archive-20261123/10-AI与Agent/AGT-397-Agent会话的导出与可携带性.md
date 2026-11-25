---
title: [AGT-397] 会话导出与可携带性——用户数据的导出权怎么实现？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-397：用户要求导出自己的会话/记忆数据（可携带权）怎么实现？

**答**:
- 合规背景：数据可携带权（GDPR 等）要求用户能导出与转移自己的数据——Agent 产品的导出面：会话历史/记忆与画像/任务记录/上传文档。
- 导出实现：统一导出接口（按用户聚合全部数据域：会话 JSON/记忆结构化/文档原件——格式通用可转移：JSON/Markdown/PDF 组合包）、异步生成（大数据量导出走队列+完成通知）、导出审计（谁在何时导出了什么——导出本身也是敏感操作 AGT-285）。
- 质量要求：导出内容完整（含被压缩/摘要的原始数据——可携带的是完整数据不是摘要）、结构可解释（schema 文档随包提供）、脱敏选项（导出给第三方时的脱敏建议）。
- 删除联动：导出与删除权配套（AGT-355）——"导出我的所有数据"入口与"删除我的所有数据"入口并列且同标准实现。

```javascript
async function exportUserData(userId) {
  const bundle = await Promise.all([
    sessions.all(userId), memory.profile(userId),
    memory.longTerm(userId), tasks.all(userId),
    docs.originals(userId)]);                   // 完整域覆盖
  const pack = zip(bundle, { schema: SCHEMA_DOC,
    generatedAt: now() });
  await audit.log({ userId, action: 'export' });
  return asyncDownload(pack);                   // 异步+通知
}
// 导出与删除入口并列，同标准实现。
```
