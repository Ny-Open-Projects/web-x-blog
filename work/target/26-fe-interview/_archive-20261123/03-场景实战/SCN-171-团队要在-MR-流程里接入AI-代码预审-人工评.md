---
title: [SCN-171] 团队要在 MR 流程里接入"AI 代码预审"，人工评审只看 AI 拦不住的问题，如何设计架构？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-171：团队要在 MR 流程里接入"AI 代码预审"，人工评审只看 AI 拦不住的问题，如何设计架构？
**答**：
- 定位是"预审"而不是"替代评审"：AI 负责机械性问题（风格、常见 bug 模式、测试缺失、敏感信息），人负责设计与业务正确性。
- 链路：MR webhook → 拉 diff（带上下文文件）→ 按文件分片（超长 diff 截断策略）→ 调 LLM → 结构化结果（行级评论）回写到 MR，总评贴在描述区。
- 结果必须是"建议 + 级别"而不是"阻断"：初期 observe 模式跑两周校准误报率，再按类别逐步升级为 warn/error。
- 成本与安全：diff 不含未授权代码外发（私有化部署或脱敏），缓存相同 blob hash 的评审结果，大 MR 拆片并行。

```javascript
// AI 预审服务：webhook -> diff 分片 -> LLM -> 行级评论回写
export async function reviewMr(req) {
  const { mrId, project } = parseWebhook(req);
  const diff = await gitlab.getMrDiff(project, mrId);
  const findings = [];

  for (const shard of shardDiff(diff, { maxLines: 400 })) { // 超长 diff 分片，带上下文文件
    const cacheKey = hashBlob(shard);
    const cached = await cache.get(cacheKey);
    if (cached) { findings.push(...cached); continue; }      // 相同内容命中缓存省成本

    const res = await llm.chat({
      system: '你是资深前端评审。只输出 JSON：[{line, level: info|warn|error, kind, message, suggestion}]。仅评机械性问题：空指针、异步未捕获、样式副作用、测试缺失、疑似密钥。不确定的不要说。',
      user: renderShardPrompt(shard),
      json: true,
    });
    const parsed = safeParse(res).filter(f => CONFIDENT[kindLevel(f)]); // 过滤低置信
    findings.push(...parsed);
    await cache.set(cacheKey, parsed, { ttl: '7d' });
  }

  // 回写：error 级行内评论，其余汇总进总评
  await gitlab.postMrSummary(project, mrId, summarize(findings));
  for (const f of findings.filter(f => f.level === 'error')) {
    await gitlab.postLineComment(project, mrId, f);
  }
  // observe 模式不阻断；校准后按 kind 配置升级为必须解决
  await metrics.record('ai-review', { mrId, count: findings.length, kinds: tally(findings, 'kind') });
}

function shardDiff(diff, { maxLines }) {
  // 每片附带被改文件全文的关键上下文，单纯 diff 会让 AI 误判
  return groupBy(diff.files, maxLines).map(files => ({ files, context: files.map(f => f.content) }));
}
```
