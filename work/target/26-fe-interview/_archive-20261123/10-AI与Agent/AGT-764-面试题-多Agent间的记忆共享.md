---
title: [AGT-764] 多个 Agent（编码 Agent/文档 Agent）如何共享用户记忆而不重复采集？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-764：多个 Agent（编码 Agent/文档 Agent）如何共享用户记忆而不重复采集

**答**：
- 记忆中心化：统一记忆服务（按用户分域），各 Agent 读写同一记忆库但带「域标签」（编码 Agent 写的技术事实/文档 Agent 写的偏好），跨域读取需要相关（文档 Agent 不需要代码细节）。
- 写入语义分层：事实类共享（技术栈/偏好全域有效），过程类按域（编码习惯只有编码 Agent 用）。
- 一致性：同一用户同一时刻只有一个蒸馏任务跑（防重复蒸馏冲突），Agent 间通过记忆版本号感知更新。

```javascript
const memoryService = {
  async write(agent, fact) {
    return semantic.upsert({ ...fact, domain: agent.domain,
      shared: fact.kind === 'fact' });             // 事实类全域共享
  },
  async read(agent, query) {
    return vector.search(embed(query), {
      filter: { or: [{ shared: true }, { domain: agent.domain }] },
    });                                            // 只读共享+本域
  },
};
```

