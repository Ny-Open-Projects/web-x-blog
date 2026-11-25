---
title: [1034] 知识库本身会腐烂，质量巡检怎么自动化
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 质量巡检]
type: 面试题
---

## 1034：知识库本身会腐烂，质量巡检怎么自动化

**答**：
- 巡检四项：覆盖率（评估集证据是否都能召回）、新鲜度（文档最后更新时间分布，过期文档比例）、一致性（同主题多文档的冲突检测——LLM 对比抽查）、可检索性（抽样文档的「自问自答」探针：从文档生成问题再检索，召回不了说明分块或索引有问题）。
- 巡检产物不是报告而是工单：过期文档提醒 owner、冲突文档标注 superseded、召回失败的文档进分块修复队列。
- 节奏：全量巡检月度（低成本探针可周度），事故触发的定向巡检即时。
- 追问钩子：「自问自答」探针为什么有效？——它模拟了真实用户路径（问题→检索→命中），文档「写得好」但「检索不到」的结构性问题会被直接暴露。

```ts
async function patrol(kb) {
  const probes = await sampleDocs(kb, 100).map(async d => {
    const qs = await genQuestions(d, 2);             // 从文档生成探针问题
    return { doc: d.id, hit: (await retrieve(qs[0])).some(h => h.docId === d.id) };
  });
  const rs = await Promise.all(probes);
  return ticket.create(rs.filter(r => !r.hit).map(r =>
    ({ type: 'chunk_fix', doc: r.doc })));          // 直接开工单
}
```
