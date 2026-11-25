---
title: [ENG-309] 笔试题——实现 buildinfo 生成与注入（多通道：Define/meta/runtime）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-309：手写 buildinfo 生成

**需求与边界**：
- 需求：生成 buildinfo（commit/时间/版本/依赖 hash/环境），注入三通道——① 构建期 Define（代码内引用）；② HTML meta 标签（页面可读）；③ 运行时 JSON（排障接口）；三通道内容一致性校验。
- 边界：① 时间用 SOURCE_DATE_EPOCH（可复现构建，ENG-222）；② 依赖 hash 用 lockfile 摘要（不用全量 SBOM 减体积）；③ 环境敏感字段脱敏（不含内部域名明细）。

**答**：
```javascript
function buildinfo({ commit, pkg, lockfile, env, sourceDateEpoch }) {
  const info = {
    commit, version: pkg.version,
    builtAt: sourceDateEpoch ?? Date.now(),           // 可复现：CI 传固定 epoch
    depsHash: sha256(lockfile).slice(0, 12),
    env,
  };
  return {
    define: { __BUILD__: JSON.stringify(info) },      // 通道 1：Define
    metaTags: Object.entries(info).map(([k, v]) =>
      `<meta name="build:${k}" content="${escapeAttr(v)}">`).join('\n'),   // 通道 2：meta
    runtimeFile: writeJson('dist/build-info.json', info),   // 通道 3：runtime
    validate: (renderedHtml) => {                     // 三通道一致性
      const meta = parseMeta(renderedHtml);
      const drift = Object.entries(info).filter(([k, v]) =>
        meta[`build:${k}`] !== String(v));
      if (drift.length) fail(`buildinfo 三通道不一致: ${drift.map(([k]) => k)}`);
    },
  };
}
```

**评分点**:
- 三通道注入 + 一致性校验（不同步的元信息比没有更误导）。
- SOURCE_DATE_EPOCH 可复现（ENG-222 联动）。
- depsHash 用 lockfile 摘要（体积与信息量平衡）。
- meta 转义防 HTML 注入。
