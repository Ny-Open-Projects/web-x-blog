---
title: [ARC-098] 平台工程化如何设计（模板中心/脚手架 CLI）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-098：平台工程化如何设计（模板中心/脚手架 CLI）？
**答**：
- 平台工程化的意义：把"团队最佳实践"固化成可执行物——模板中心沉淀工程模板，CLI 一键创建，模板升级可同步到存量应用。
- CLI 设计：命令面小而清晰（create/add/deploy/check），核心是模板拉取 + 交互式变量注入 + 升级机制。
- 模板版本治理：存量应用记录模板版本，`check` 命令对比差异并给出可自动合并的升级（codemod 化）。

```bash
# @corp/cli 命令面设计
corp create web-shop --template=react-ssr --team=trade   # 从模板中心创建应用（注入团队/仓库名等变量）
corp add module request                                   # 向存量应用添加标准模块（带依赖安装与接线）
corp deploy --env=beta                                    # 统一部署入口（内部转 OPS 流水线）
corp check --upgrade                                      # 模板升级检查：对比 base 版本差异

# 模板中心结构（monorepo 内 packages/templates）
# templates/react-ssr/          模板本体（{{teamName}} 等变量占位）
# templates/react-ssr/meta.json 声明：变量表、最低 CLI 版本、升级脚本 codemods/
corp check --upgrade 输出示例：
#   当前模板版本 2.1.0 → 最新 2.4.0
#   [auto] 2.2.0 eslint9 配置迁移 —— 可自动合并
#   [manual] 2.3.0 路由生成方式变更 —— 需人工确认（附迁移文档）
```
