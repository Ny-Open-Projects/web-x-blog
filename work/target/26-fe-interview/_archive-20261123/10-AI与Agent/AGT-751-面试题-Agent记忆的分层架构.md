---
title: [AGT-751] Agent 记忆系统分几层（工作/情景/语义/画像），各层的存储与生命周期怎么设计？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-751：Agent 记忆系统分几层（工作/情景/语义/画像），各层的存储与生命周期怎么设计

**答**：
- 四层：工作记忆（当前会话上下文窗口内，易变）、情景记忆（episodic：会话历史/任务记录，按时间检索）、语义记忆（从历史中蒸馏出的知识事实，可长期）、用户画像（偏好/习惯的结构化 profile）。生命周期递增：分钟→天→月→永久（可被用户删除）。
- 蒸馏是核心机制：情景记忆不直接全量进上下文（贵且噪声大），由后台任务蒸馏成语义记忆（"用户是 React 技术栈、偏好函数式写法"），检索时用语义记忆。
- 每层写入都有「准入门槛」：语义记忆写入需多次佐证（避免一次偶然事件变成永久画像），画像字段带置信度随证据更新。

```javascript
const MEMORY_TIERS = {
  working: { ttl: 'session', store: 'context-window' },
  episodic: { ttl: '90d', store: 'vector+time', retrievable: true },
  semantic: { ttl: 'permanent', store: 'vector', admit: 'evidence>=3' },
  profile: { ttl: 'permanent', store: 'kv', fields: 'conf-scored' },
};
async function distill(session) {
  const facts = await llm.extract(session.transcript, EXTRACT_FACTS);
  for (const f of facts) {
    const evidence = await countEvidence(f.statement);
    if (evidence >= 3) await semantic.upsert(f);  // 多次佐证才入语义层
    else await candidate.add(f);                  // 候选池攒证据
  }
}
```

