---
title: [1019] RAG 管道里的个人敏感信息（PII）怎么合规处理
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 隐私]
type: 面试题
---

## 1019：RAG 管道里的个人敏感信息（PII）怎么合规处理

**答**：
- 处理时点：入库前脱敏（原始文档含 PII，索引时就打码/假名化，召回层永远见不到明文）比输出过滤更根本——「源头没有，怎么问都没有」。
- 假名化要可逆受控：授权场景（HR 查询员工信息）需要还原，用独立密钥库存储映射，检索层只拿假名；密钥访问走审批。
- 遗忘权落地：用户要求删除时，按「文档 → chunk → 向量 → 缓存」全链路删除并留删除审计；向量也要删（向量本身可被反推部分原文）。
- 追问钩子：模型记忆里的 PII 怎么办？——微调/训练数据入库前同样脱敏；对已部署模型无法「删除记忆」，只能靠输出侧检测兜底 + 数据不进训练集的准入控制。

```ts
async function ingestWithPII(doc) {
  const { safe, mapping } = await pseudonymize(doc.text);  // 假名化
  await keyVault.store(doc.id, encrypt(mapping));          // 映射加密存储
  await index.add(chunkDoc(safe));                          // 索引只有假名
}
async function forget(userId) {
  await index.deleteByUser(userId);        // chunk + 向量
  await cache.purgeByUser(userId);         // 缓存
  await keyVault.destroy(userId);          // 映射销毁
  await audit.log({ type: 'erasure', userId });             // 审计留痕
}
```
