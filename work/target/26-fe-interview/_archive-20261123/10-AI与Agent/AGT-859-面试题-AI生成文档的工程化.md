---
title: [AGT-859] README/API 文档/变更日志的 AI 生成与维护，如何避免文档过期？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-859：README/API 文档/变更日志的 AI 生成与维护，如何避免文档过期

**答**：
- 文档生成挂在「事实源」上：API 文档从类型定义生成（AI 润色但不发明 API）、changelog 从 commit/PR 生成（约定式提交是前提）、README 的架构图从代码结构生成——生成源是代码本身，文档就不过期。
- 过期检测：文档中的代码示例定期「可运行性巡检」（示例代码跑一遍，跑不过即过期标记），链接巡检同理。
- 人工层保留：决策记录（为什么这样设计）AI 写不了，模板留"人类填空区"；AI 只写"是什么"，不编"为什么"。

```javascript
async function docsPipeline() {
  const api = await genFromTypes('./src/types');   // 事实源生成
  const changelog = await genFromCommits(conventional);
  const stale = await examplesCheck(api);          // 示例可运行巡检
  return { api, changelog,
    flagged: stale.map(s => ({ path: s.path,
      note: '示例不可运行，AI 修复草稿已生成' })),
    humanZone: ['decisions', 'tradeoffs'],         // 人工填空区
  };
}
```

