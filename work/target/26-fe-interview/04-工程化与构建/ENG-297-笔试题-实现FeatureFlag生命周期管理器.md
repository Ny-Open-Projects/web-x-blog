---
title: [ENG-297] 笔试题——实现 Feature Flag 生命周期管理器（到期扫描 + 清理 PR 生成）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-297：手写 Flag 生命周期管理器

**需求与边界**：
- 需求：flag 注册表带元数据（type/owner/expiresAt/default）；每周扫描：过期 flag 生成清理任务（提醒 owner → 生成删除 PR 描述）；无 owner flag 标记孤儿。
- 边界：① release flag 过期即清理，ops flag 过期提醒续期不删；② 清理任务含「代码引用位置」（grep 结果）辅助删除；③ 输出周报（flag 总数趋势/过期清单/孤儿清单）。

**答**：
```javascript
function flagLifecycle(flags, { now = Date.now() } = {}) {
  const report = { expired: [], orphan: [], trend: flags.length };
  for (const f of flags) {
    if (!f.owner) { report.orphan.push(f.key); continue; }
    const expired = new Date(f.expiresAt) < now;
    if (!expired) continue;
    if (f.type === 'ops') {                            // 运维 flag：提醒续期
      notify(f.owner, `${f.key} 已过期，请续期或关闭`);
      report.expired.push({ key: f.key, action: 'RENEW_NOTICE' });
    } else {                                           // release/experiment：清理
      const refs = grepFlagUsage(f.key);               // 代码引用位置
      report.expired.push({ key: f.key, action: 'CLEANUP',
        pr: cleanupPRDesc(f, refs) });                 // 生成删除 PR 描述
    }
  }
  return report;
}
function cleanupPRDesc(f, refs) {
  return {
    title: `chore(flags): 移除过期 flag ${f.key}`,
    body: `类型 ${f.type}，owner @${f.owner}，过期 ${f.expiresAt}。\n引用位置:\n${refs.map(r => `- ${r}`).join('\n')}\n默认值: ${f.default}`,
  };
}
```

**评分点**:
- flag 类型差异化处理（ops 续期 vs release 清理）。
- 孤儿 flag（无 owner）单独标记。
- 清理 PR 描述含代码引用位置（删除可导航）。
- 周报含数量趋势（膨胀监控）。
