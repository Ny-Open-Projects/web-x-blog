---
title: [MP-146] 构建产物分析（体积/依赖）怎么做进 CI？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-146：构建产物分析（体积/依赖）怎么做进 CI？
**答**：
- 编译产物解包分析：按目录/类型（js/wxml/wxss/图片）统计大小与 gzip 后大小，输出 JSON 报告 + PR 评论。
- 依赖分析：`miniprogram-ci` 的 analyzeCodeQuality 或自写脚本扫 `usingComponents` 与 require 链，找出**未被引用的组件/死代码**、重复引入。
- 增量归因：与上版报告 diff，体积增量落到"哪个页面/组件/依赖"，PR 作者定位一目了然。
- 门禁：主包/单分包超阈值阻塞合并；npm 依赖新增需审批（体积与安全双审）。

```bash
#!/bin/bash
# scripts/analyze-dist.sh —— 产物体积分析 + 与基线 diff
OUT=dist-report.json
node scripts/scan-dist.js dist > "$OUT"    # 输出 { main: 1240, pkgTrade: 800, gzipMain: 620 ... }
node scripts/diff-dist.js "$OUT" baseline/dist-report.json > dist-diff.md
cat dist-diff.md   # PR 评论：每个分包增量归因到组件
node -e "
const r = require('./$OUT');
if (r.main > 1900) { console.error('BLOCK 主包超 1900KB'); process.exit(1) }
if (r.deltaMain > 50) { console.error('WARN 主包增量超 50KB，需说明'); }
"
```
