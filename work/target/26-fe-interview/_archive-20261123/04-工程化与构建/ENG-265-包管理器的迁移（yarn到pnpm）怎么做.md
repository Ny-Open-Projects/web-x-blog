---
title: [ENG-265] 包管理器迁移（yarn → pnpm）怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-265：包管理器迁移怎么做？
**答**：
- 迁移风险面：lockfile 重算（版本可能漂移！）、hoisting 差异暴露幽灵依赖、CI 缓存键失效、团队肌肉记忆——最大的坑是「迁移后依赖版本静默变化」。
- 版本漂移防御：迁移前冻结 package.json；迁移后 diff 依赖树（yarn.lock vs pnpm-lock 解析后的实际版本清单），漂移逐项审查——packageManager 字段强制（corepack）防混用。
- 分阶段：影子分支跑通全 CI → 影子验证一周（构建产物一致）→ 主分支切换 + 团队公告（命令映射表）。
- 回退预案：迁移分支保留 yarn.lock，出问题切回（接受幽灵依赖回归）。
- 追问钩子：为什么「依赖树 diff」是迁移验证的核心——lockfile 格式不同没法直接比，但解析后的实际安装版本清单可以比；任何版本漂移都可能引入行为变化，这与构建工具迁移的产物 diff 同等重要。

```bash
# 迁移验证
npx synp --source-file yarn.lock   # 或手动转换
pnpm import && pnpm install --frozen-lockfile
# 依赖树 diff
pnpm list -r --depth 0 --json > pnpm-tree.json
yarn list --json > yarn-tree.json
diff <(normalize yarn-tree.json) <(normalize pnpm-tree.json)
# 防混用
{ "packageManager": "pnpm@9.0.0" }   # corepack 强制
```
