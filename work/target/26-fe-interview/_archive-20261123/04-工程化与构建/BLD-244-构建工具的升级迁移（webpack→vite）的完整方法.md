---
title: [BLD-244] 构建工具升级迁移的完整方法？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-244：构建迁移完整方法？
**答**：
- 六步法：① 基线（旧工具产物清单/耗时/行为快照）；② 并行构建（新工具影子跑，产物 diff 逐项解释）；③ dev 先切（HMR/启动速度收益，风险最低）；④ CI 并行（新旧产物 diff 门禁）；⑤ prod 灰度切（部分应用/流量）；⑥ 旧配置退役（保留一版可回退）。
- 产物 diff 的解释标准：hash 漂移可接受（工具差异）、模块集合变化必须逐个解释（新增/消失的 chunk）。
- 语义差异清单：env 变量注入方式、CSS 处理、动态 import 粒度、循环依赖行为——迁移 checklist 按语义差异逐项验证。
- 追问钩子：为什么「dev 先切」能消化大部分迁移风险——dev 阶段每天被全团队使用（大量真实场景验证：HMR/依赖解析/CSS/静态资源），问题暴露在开发期且不影响产物；等 prod 切换时剩余风险集中在产物差异——已通过并行 diff 验证过，迁移风险被两阶段分摊。

```bash
# 迁移编排
pnpm build:old && mv dist dist-old          # 1. 基线
pnpm build:new && compare-manifests dist-old dist   # 2. 产物 diff
# 3. dev 切换 → 4. CI 双跑 → 5. prod 灰度 → 6. 退役
```
