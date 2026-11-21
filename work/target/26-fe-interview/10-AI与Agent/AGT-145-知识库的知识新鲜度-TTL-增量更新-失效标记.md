---
title: [AGT-145] 知识库的知识新鲜度（TTL/增量更新/失效标记）怎么管理？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-145：知识库的知识新鲜度（TTL/增量更新/失效标记）怎么管理？
**答**：
- 三种失效模式要区分：内容变更（重新嵌入替换）、内容过期（带 TTL 的 metadata，检索时过滤或降权）、逻辑失效（政策废止/价格变更，需要显式打失效标记而非等待重爬）。
- 增量管线：源系统发变更事件（webhook/轮询 diff）→ 定位受影响 chunk（父子分块时父块变更要级联重嵌子块）→ 原子替换（先写新版本再切别名，避免检索到半新半旧）。
- 检索侧兜底：结果组装时校验 `validUntil`/`supersededBy`，过期内容不进 prompt 或标注「截至日期」让模型声明时效。
- 高频考点：价格/库存类强时效数据不应该进向量库，应该走 API 工具实时查询——「RAG 管知识，工具管事实」。

```typescript
// 知识新鲜度管理：版本原子替换 + TTL 过滤 + 失效级联
interface KbChunk { id: string; docId: string; text: string; version: number;
  validFrom: number; validUntil: number | null; supersededBy: string | null; }

export class FreshnessManager {
  constructor(private store: { upsert: (c: KbChunk) => Promise<void>; delete: (id: string) => Promise<void>;
                              listByDoc: (docId: string) => Promise<KbChunk[]> }) {}

  // 增量更新：原子版本替换，读方永远看到完整版本
  async applyChange(docId: string, newChunks: { text: string }[]) {
    const old = await this.store.listByDoc(docId);
    const version = Math.max(0, ...old.map((o) => o.version)) + 1;
    const created = newChunks.map((c, i) => ({ id: `${docId}-v${version}-${i}`, docId, text: c.text,
      version, validFrom: Date.now(), validUntil: null, supersededBy: null }));
    for (const c of created) await this.store.upsert(c);          // 先写新版本
    for (const o of old) await this.store.delete(o.id);           // 再删旧版本
  }

  // 逻辑失效：政策废止时显式标记并级联
  async invalidate(docId: string, replacementDocId?: string) {
    for (const c of await this.store.listByDoc(docId)) {
      await this.store.upsert({ ...c, supersededBy: replacementDocId ?? null });
    }
  }

  // 检索侧过滤：过期/失效内容不进 prompt
  filterFresh(hits: KbChunk[], now = Date.now()): { fresh: KbChunk[]; stale: KbChunk[] } {
    const fresh = hits.filter((h) => !h.supersededBy && (h.validUntil === null || h.validUntil > now));
    return { fresh, stale: hits.filter((h) => !fresh.includes(h)) }; // stale 仅供日志分析
  }
}
```
