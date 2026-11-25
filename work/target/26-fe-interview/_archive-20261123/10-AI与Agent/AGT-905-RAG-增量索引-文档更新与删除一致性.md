---
title: [905] 知识库文档频繁更新，RAG 索引如何保证增量一致
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 索引]
type: 面试题
---

## 905：知识库文档频繁更新，RAG 索引如何保证增量一致

**答**：
- 以「文档 ID + 版本号」为最小事务单元：重写一个文档时，先写入新版本 chunk，再删除旧版本 chunk，两步放在同一队列任务里串行执行，杜绝新旧并存导致的检索混乱。
- 删除的坑：chunk 表存文档 ID 外键，删文档必须级联删 chunk，否则出现「幽灵段落」被召回但原文已 404，引用溯源直接穿帮。
- 大规模重建用双索引别名切换：新索引建好 → 校验抽样 → 别名原子切换 → 旧索引保留 24h，回滚只需切回别名。
- 追问钩子：更新期间线上查询会丢结果吗？——用「先写后删」顺序把窗口期从「缺」变「重」，重复结果靠去重兜底，缺结果比重复结果危害更大。

```ts
async function upsertDoc(docId: string, newDoc: Doc) {
  const newChunks = chunkDoc(newDoc).map(c => ({ ...c, docId, ver: newDoc.ver }));
  await index.bulk(newChunks);            // 1. 先写新版
  await index.deleteByQuery({             // 2. 再删旧版（同 docId 旧 ver）
    query: { bool: { filter: [
      { term: { docId } }, { range: { ver: { lt: newDoc.ver } } }
    ]}}
  });
}
```

