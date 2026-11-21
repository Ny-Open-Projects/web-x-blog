---
title: [AGT-479] 笔试题——实现流量录制与回放（脱敏录制+确定性回放+对比断言）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-479：手写流量录制回放：请求录制脱敏、mock 回放、响应对比断言

**需求与边界**：
- 输入：生产流量、录制配置；输出：可回放的测试资产。
- 边界要求：① 录制脱敏（请求体 PII 处理后存储）；② 回放确定性：LLM/工具返回用录制 stub 替换（可切换"录制模式"或"回放模式"）；③ 回放断言（结构一致/关键内容一致——不比对全文，LLM 输出有随机性）；④ 采样录制（控存储成本）。

**答**：
```javascript
class TrafficRecorder {
  constructor({ mode = 'record', sample = 0.05, store }) {
    this.mode = mode; this.sample = sample; this.store = store;
  }
  async intercept(req, realCall) {
    if (this.mode === 'record') {
      if (Math.random() > this.sample) return realCall(req);
      const resp = await realCall(req);
      await this.store.save({
        id: uid(), req: redactPII(req),             // 录制脱敏
        resp: redactPII(resp),
        fingerprints: { structure: structOf(resp),
          keywords: extractKeywords(resp) },        // 回放断言依据
      });
      return resp;
    }
    // replay 模式：查 stub
    const hit = await this.store.match(req);
    if (hit) return hit.resp;
    return realCall(req);                           // 未命中降级真调
  }
  async replayAssertions(session) {                  // 回放对比
    const results = [];
    for (const t of session.turns) {
      const cur = await run(t.req);
      const base = this.store.get(t.id);
      results.push({
        turn: t.id,
        structureMatch: structOf(cur) === base.fingerprints.structure,
        keywordCoverage: coverage(base.fingerprints.keywords,
          extractKeywords(cur)),                    // 关键内容覆盖
        // 不比对全文（LLM 输出随机性），比对结构+关键词
      });
    }
    return { pass: results.every(r =>
      r.structureMatch && r.keywordCoverage > 0.8), results };
  }
}
// 用途：压测回放 / 回归对比 / bug 复现（脱敏后可共享）。
```

**评分点**:
- 录制脱敏（PII 处理后存储）+ 采样控制成本。
- 回放 stub 化（LLM/工具确定化）+ 未命中降级真调。
- 断言设计正确：结构+关键词覆盖（不比对全文——LLM 随机性认知）。
- 三用途意识（压测/回归/复现）。
