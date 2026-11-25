---
title: [NODE-861] 笔试题——实现多环境配置漂移检测器（staging vs prod）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-861：手写配置漂移

**需求与边界**：
- 需求：配置漂移检测（SCN-ENG-237）——① 多环境配置收集（staging/prod——SCN-NODE-663 配置中心）；② 语义 diff（允许差异白名单——连接串等预期差异）；③ 漂移告警（未预期差异——SCN-ENG-237 "staging 能跑 prod 挂"防御）；④ 漂移报告进评审（SCN-OPS-261）。
- 边界：① 允许差异白名单（数据源地址/密钥引用——预期差异声明化）；② 漂移的来源追踪（谁改的——SCN-OPS-219 审计）；③ 漂移修复建议（对齐值——SCN-ENG-237）。

**答**：
```javascript
async function configDriftDetect() {
  const [staging, prod] = await Promise.all([
    configCenter.snapshot('staging'), configCenter.snapshot('prod')]);
  const diff = semanticDiff(staging, prod, {
    allow: ['db.url', 'redis.url', 'secret.*'],        // 预期差异白名单（SCN-ENG-237）
  });
  const unexpected = diff.filter(d => !d.allowed);
  if (unexpected.length)
    alert({ type: 'CONFIG_DRIFT', drifts: unexpected,
      fix: unexpected.map(d => `对齐 ${d.path}: staging=${d.staging} prod=${d.prod}`),
      origin: auditOrigin(d.path) });                  // 来源追踪（SCN-OPS-219）
  return { drifts: unexpected, report: forReviewBoard(unexpected) };   // 进评审（SCN-OPS-261）
}
cron('0 * * * *', configDriftDetect);                  // 每小时检测（漂移早发现）
```

**评分点**:
- 语义 diff + 预期差异白名单（SCN-ENG-237）。
- 漂移来源追踪（SCN-OPS-219）。
- 修复建议（对齐值）+ 报告进评审（SCN-OPS-261）。
- 定期检测（每小时——漂移早发现）。
