---
title: [BLD-303] 笔试题——实现 buildinfo 与产物的一致性校验？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-303：手写 buildinfo 校验

**需求与边界**：
- 需求：验证 buildinfo（SCN-ENG-309）与产物实际状态一致——① commit 匹配（当前工作区 HEAD = buildinfo.commit）；② manifest hash 匹配（buildinfo.outputs vs 实际产物 hash）；③ sourcemap 对齐（每个 chunk 有 map 且 sourcesContent 存在）；④ dirty 工作区告警（未提交变更进产物——可复现性破坏，SCN-ENG-222）。
- 边界：① hash 全量校验（不是抽样——正确性零容忍）；② 失败输出逐项差异（哪几个文件 hash 不符）；③ sourcemap 内容完整性（sourcesContent 缺失 = 排障降级警告非阻断）。

**答**：
```javascript
async function verifyBuildinfo(buildinfo, dist, git) {
  const issues = [];
  const head = await git.head();
  if (head !== buildinfo.commit)
    issues.push({ type: 'COMMIT_MISMATCH', buildinfo: buildinfo.commit, head });
  if (await git.isDirty())
    issues.push({ type: 'DIRTY_WORKTREE', note: '未提交变更进了产物——可复现性破坏' });
  for (const [file, expected] of Object.entries(buildinfo.outputs)) {
    const actual = sha256(fs.readFileSync(path.join(dist, file)));
    if (actual !== expected)
      issues.push({ type: 'HASH_MISMATCH', file, expected, actual });   // 全量零容忍
  }
  const mapIssues = manifest.chunks().filter(c => {
    const map = loadMap(dist, c.file);
    return !map || !map.sourcesContent?.length;
  }).map(c => ({ type: 'SOURCemap_DEGRADED', chunk: c.file, level: 'warn' }));   // 非阻断
  return { ok: issues.every(i => i.type !== 'COMMIT_MISMATCH' && i.type !== 'HASH_MISMATCH' && i.type !== 'DIRTY_WORKTREE'),
    issues: [...issues, ...mapIssues] };
}
```

**评分点**:
- 三层校验（commit/dirty/hash 全量）+ sourcemap 降级警告。
- hash 全量零容忍（SCN-OPS-246 签名链延伸）。
- dirty 工作区检测（可复现性红线——SCN-ENG-222）。
- 阻断与非阻断区分（sourcemap 缺失是排障降级非安全风险）。
