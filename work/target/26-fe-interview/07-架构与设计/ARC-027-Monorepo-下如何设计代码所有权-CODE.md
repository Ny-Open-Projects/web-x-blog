---
title: [ARC-027] Monorepo 下如何设计代码所有权（CODEOWNERS）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-027：Monorepo 下如何设计代码所有权（CODEOWNERS）？
**答**：
- CODEOWNERS 把"谁能改哪些目录"变成可执行规则：改到对应路径 PR 自动指派 reviewer，owner 未 approve 不能合并。
- 它是模块边界清单的权限配套：`apps/*` 归业务团队、`packages/ui` 归平台组、根配置归架构组。
- 注意粒度：过细会造成评审瓶颈，共享基建建议"组 ownership + 个人 backup"。

```text
# .github/CODEOWNERS —— 越靠后的规则优先级越高
*                          @frontend/arch-team        # 默认兜底：根配置、未知路径

/apps/web-shop/            @frontend/trade-team
/apps/admin/               @frontend/platform-biz
/packages/ui/              @frontend/design-system    # 组件库必须 DS 组评审
/packages/design-tokens/   @frontend/design-system @design-lead
/tooling/eslint-config/    @frontend/arch-team
/.github/CODEOWNERS        @frontend/arch-team        # 权限文件本身只能架构组改
# 规则：改 /packages/ui 的 PR 会同时要求 design-system 组 approve，
# 业务团队无法绕过平台组直接修改共享组件
```

---

## 四、组件库与设计系统（ARC-028 ~ ARC-038）
