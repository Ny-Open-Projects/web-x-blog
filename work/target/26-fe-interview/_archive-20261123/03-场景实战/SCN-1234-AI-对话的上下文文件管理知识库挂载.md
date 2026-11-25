---
title: [SCN-1234] AI 对话的上下文文件管理（知识库挂载）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1234：AI 对话的上下文文件管理（知识库挂载）

**答**：
- 挂载：会话挂载知识库文档（检索增强范围限定），挂载状态可见（引用自哪个库）。
- 权限：知识库访问权限（团队库/个人库），引用审计。
- 更新：知识库文档更新后向量重建（检索新鲜度提示）。

```javascript
// 知识库挂载
function knowledgeMount(session, kbId) {
  return {
    mounted: kbId,
    scope: '该会话回答优先引用此知识库',
    permission: checkKbPermission(kbId),
    freshness: kbUpdatedAt(kbId),                      // 向量新鲜度
    citation: (ref) => ref.kbId === kbId ? ref : { ...ref, note: '来自通用检索' },
  };
}
function checkKbPermission(id) { return 'granted'; }
function kbUpdatedAt(id) { return Date.now() - 86400_000; }
```
