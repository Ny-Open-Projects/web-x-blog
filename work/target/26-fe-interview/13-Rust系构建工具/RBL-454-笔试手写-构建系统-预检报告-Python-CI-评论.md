---
title: [RBL-454] 笔试：手写 PR 构建报告评论生成器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-454：手写 PR 构建报告评论生成器
**答**：实现 `generatePrComment(results)`：1) results：`{ build: { ok, timeMs }, sizeDiff: { summary, md }, tests: { pass, fail, skipped }, checklist: { md } }`；2) 单一评论聚合（不刷屏：bot 只维护一条 sticky 评论——每次更新替换）；3) 分区折叠（<details> 折叠次要信息——CI 噪音治理）；4) 状态徽章（✅/⚠️/❌ 顶部摘要行——reviewer 3 秒判断）；5) 超长截断（评论 > 64KB 平台限制——截断提示 + artifact 链接）；6) 指纹防覆盖：评论带构建 sha 标识（并发构建更新不互踩）。

```javascript
const STATUS = { ok: '✅', warn: '⚠️', fail: '❌' }
const MAX_LEN = 64 * 1024

export function generatePrComment(results, { sha, artifactUrl } = {}) {
  const buildStatus = results.build.ok ? 'ok' : 'fail'
  const testStatus = results.tests.fail > 0 ? 'fail' : results.tests.skipped > 0 ? 'warn' : 'ok'
  const overall = [buildStatus, testStatus].includes('fail') ? 'fail' : 'warn'

  const md = [
    `<!-- build-report:${sha} -->`,                              // 防覆盖指纹
    `## ${STATUS[overall]} 构建报告`,
    `${STATUS[buildStatus]} 构建 ${results.build.ok ? '通过' : '失败'}（${(results.build.timeMs / 1000).toFixed(1)}s）`,
    `${STATUS[testStatus]} 测试：${results.tests.pass} 过 / ${results.tests.fail} 败 / ${results.tests.skipped} 跳过`,
    '',
    '<details><summary>体积 diff</summary>',
    '',
    results.sizeDiff.md,
    '</details>',
    '',
    '<details><summary>检查清单</summary>',
    '',
    results.checklist.md,
    '</details>',
  ].join('\n')

  if (md.length > MAX_LEN)
    return md.slice(0, MAX_LEN - 200) + `\n\n…内容过长，完整报告见 artifact: ${artifactUrl}`
  return md
}

// sticky 更新逻辑：查找历史评论中含 <!-- build-report:${sha} --> 标记的 → patch 更新而非新建
export function findStickyComment(comments, sha) {
  return comments.find((c) => c.body.includes(`build-report:${sha}`))
}
```
**评分点**：
- sticky 评论模式（指纹标记查找替换——不刷屏）
- 状态徽章摘要行（reviewer 3 秒判断——DX 核心）
- details 折叠（次要信息收纳）；超长截断 + artifact 链接兜底
- 并发构建防互踩（sha 指纹——两个 CI job 同时评论的竞态处理）
