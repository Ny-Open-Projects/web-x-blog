---
title: [ENG-244] 构建工具迁移（webpack → Rspack/Vite）怎么做才不翻车？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-244：构建工具迁移怎么做？
**答**：
- 迁移前提盘点：插件清单（每个 webpack 插件找对应或放弃）、loader 特殊逻辑、env 依赖、产物 diff 基线——迁移最大风险是「产物悄悄变了」。
- 产物一致性验证：迁移前建立产物基线（chunk 清单/hash），迁移后逐项对比；hash 变化正常（工具差异），模块集合变化必须解释。
- 分阶段切换：dev 先切（收益最快、风险最低）→ CI 构建并行跑（新旧产物对比）→ prod 切换（灰度：部分项目先迁）。
- 回退预案：迁移分支保留 webpack 配置，配置开关可切回——迁移期不给团队「没有退路」的压力。
- 追问钩子：为什么「dev 先切」风险最低——dev 阶段问题（HMR/速度/报错体验）在开发期就暴露且不影响产物；prod 产物差异是最后验证的，前面阶段已经消化大部分兼容问题。

```bash
# 迁移编排
pnpm build --config webpack   # 基线: manifest.json
pnpm build --config rspack    # 对比
compare-manifest manifest.json manifest-rspack.json
# 新增/消失的模块必须逐个解释，hash 漂移放行
```
