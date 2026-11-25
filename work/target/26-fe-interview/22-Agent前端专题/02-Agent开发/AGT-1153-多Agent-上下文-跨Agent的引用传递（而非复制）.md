---
title: [1153] Agent 间传「引用」而不是复制全文，工程上怎么做
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 上下文]
type: 面试题
---

## 1153：Agent 间传「引用」而不是复制全文，工程上怎么做

**答**：
- 引用机制：产物写 artifact store 得 URI，消息里传 URI + 摘要 + 哈希；消费方按需拉取，拉取时校验哈希防「引用的内容已变」。
- 收益：消息轻（上下文不膨胀）、可追溯（所有消费方读同一份产物）、权限可管（按 URI 鉴权而不是靠复制控制）。
- 细节：引用要「带版本」（URI 含产物版本），上游更新产物不悄悄影响下游；摘要必须忠实（消费方靠摘要决定要不要拉全文）。
- 追问钩子：引用失效（产物被清理）怎么办？——生命周期对齐：产物 TTL ≥ 所有下游任务的预期完成时间 + 复盘期；清理任务检查引用计数（见产物生命周期卡）。

```ts
async function publishArtifact(content) {
  const ver = 1;
  const id = await store.put(content);
  const uri = `art://${ctx.taskId}/${id}?v=${ver}`;
  const digest = sha256(content);
  return { uri, digest, summary: summarize(content, 100) }; // 引用三件套
}
async function consume(ref) {
  const content = await store.get(ref.uri);
  if (sha256(content) !== ref.digest) throw new Error('artifact drift'); // 防内容漂移
  return content;
}
```
