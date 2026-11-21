---
title: [OPS-157] npm 包体积治理的路径与成本收益？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-157：npm 包体积治理的路径与成本收益？
**答**：
- 度量先行：bundle 可视化 + 产物体积 TOP 榜，锁定大头（moment/lodash/重复依赖是常客）。
- 高收益动作排序：未使用依赖删除（depcheck）> 重量级替换（moment→dayjs）> 路由级代码分割 > tree-shaking 校验（sideEffects + ESM）> 重复版本合并（dedupe）。
- CI 体积卡口：gzip 后关键 chunk 阈值，超 5% 阻断并 @ 责任人——治理成果靠卡口守住，否则一个月打回原形。
- 收益不只流量：首屏 JS 减半直接改善 LCP/INP，转化率与 CDN 成本同步受益。
- 与构建时长优化（OPS-154）共用度量习惯：每次动作记录 before/after。

```bash
# npm 包体积治理：度量 → 动作 → 卡口
# 1. 现状度量：产物 TOP 榜与可视化
npx vite-bundle-visualizer
du -sh dist/assets/* | sort -rh | head -20

# 2. 高收益动作（按 ROI 排序）
npx depcheck                                        # 未使用依赖
npm ls lodash | head                                # 多版本共存检查
npm dedupe                                          # 重复依赖合并
#    moment → dayjs（-280KB）、lodash 全量 → lodash-es 按需导入
#    路由级动态 import：首屏只带首屏 chunk

# 3. CI 卡口：关键 chunk gzip 体积阈值，超 5% 阻断
npx bundlesize     # package.json 配置 dist/assets/index.*.js < 180KB gzip

# 4. 收益度量：首屏 JS 620KB → 310KB（gzip），LCP p75 改善约 800ms，CDN 流量同步下降
```
