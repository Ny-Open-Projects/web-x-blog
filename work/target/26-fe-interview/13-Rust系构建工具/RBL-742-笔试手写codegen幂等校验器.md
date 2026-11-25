---
title: [RBL-742] 笔试：手写 codegen 幂等校验器（重新生成 diff + 过期归因）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-742：笔试：手写 codegen 幂等校验器（重新生成 diff + 过期归因）

**答**：实现 `verifyFreshness({ committed, regenerate, schemaHash, outMeta })`。regenerate 为注入的异步函数 `() => Promise<string>`（重新生成产物文本）。outMeta: `{ sourceSchemaHash, generatedAt }`。规则：1) 重新生成与 committed 相等 → fresh；2) 不等 → 判定过期原因：outMeta.sourceSchemaHash !== 当前 schemaHash → 'schema-drift'；schemaHash 相等但内容不同 → 'generator-drift'（生成器版本变了但没重新生成）；3) 返回 `{ fresh, reason?, committedBytes, freshBytes }`；4) regenerate 抛错 → reason 'generator-error' 且 fresh=false（不吞错）。边界：committed 为空文件（首次生成前）→ 'not-generated'。

```javascript
function verifyFreshness({ committed, regenerate, schemaHash, outMeta = {}, currentSchemaHash }) {
  return (async () => {
    if (!committed) return { fresh: false, reason: 'not-generated', committedBytes: 0, freshBytes: null };
    let freshText;
    try { freshText = await regenerate(); }
    catch (e) { return { fresh: false, reason: 'generator-error', detail: e.message,
      committedBytes: committed.length, freshBytes: null }; }
    if (committed === freshText) return { fresh: true, committedBytes: committed.length, freshBytes: freshText.length };
    const reason = (outMeta.sourceSchemaHash && currentSchemaHash &&
                    outMeta.sourceSchemaHash !== currentSchemaHash)
      ? 'schema-drift' : 'generator-drift';
    return { fresh: false, reason, committedBytes: committed.length, freshBytes: freshText.length };
  })();
}

// 自测
// 1) fresh
let r = await verifyFreshness({ committed: 'A', regenerate: async () => 'A',
  schemaHash: 's1', outMeta: { sourceSchemaHash: 's1' }, currentSchemaHash: 's1' });
console.log(r.fresh === true);

// 2) schema drift
r = await verifyFreshness({ committed: 'A', regenerate: async () => 'B',
  schemaHash: 's2', outMeta: { sourceSchemaHash: 's1' }, currentSchemaHash: 's2' });
console.log(r.fresh === false && r.reason === 'schema-drift');

// 3) generator drift（schema 未变）
r = await verifyFreshness({ committed: 'A', regenerate: async () => 'B',
  schemaHash: 's1', outMeta: { sourceSchemaHash: 's1' }, currentSchemaHash: 's1' });
console.log(r.reason === 'generator-drift');

// 4) 生成器错误
r = await verifyFreshness({ committed: 'A', regenerate: async () => { throw new Error('boom'); },
  currentSchemaHash: 's1' });
console.log(r.reason === 'generator-error' && r.detail === 'boom' && r.committedBytes === 1);

// 5) 未生成
r = await verifyFreshness({ committed: '', regenerate: async () => 'A', currentSchemaHash: 's1' });
console.log(r.reason === 'not-generated');
```

**评分点**：
- 幂等校验核心正确（重新生成 diff committed）；异常路径不吞错（generator-error）
- 过期归因两级（schema-drift / generator-drift）判定准确；未生成独立状态
- 返回字节量便于 CI 报告展示 diff 规模
- 能说清「过期类型是静默 bug 源，幂等校验让『忘了重新生成』变成 CI 红」属于加分
