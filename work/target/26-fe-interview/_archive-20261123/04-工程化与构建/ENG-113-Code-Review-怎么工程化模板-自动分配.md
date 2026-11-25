---
title: [ENG-113] Code Review 怎么工程化？模板、自动分配、机器人预审怎么做？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-113：Code Review 怎么工程化？模板、自动分配、机器人预审怎么做？
**答**：
- PR 模板（pull_request_template.md）固化自查清单：变更说明、影响面、测试证据、UI 截图。
- 自动分配：CODEOWNERS 决定必审人，auto-assignment 机器人按目录自动 request review。
- 机器人预审把"人该看的"和"机器该看的"分开：lint/覆盖率/危险操作扫描先跑，结果挂到 PR 上，人只做语义与设计判断。
- 流程纪律：单 PR 控制规模（< 400 行 diff 优先），review 时限进 SLA（如 24h），避免互相积压。

```markdown
<!-- .github/pull_request_template.md -->
## 变更说明
<!-- 一句话说明做什么、为什么做，关联的 issue 编号 -->

## 影响面
<!-- 涉及哪些模块，是否需要数据迁移 / 是否影响线上行为 -->

## 自查清单
- [ ] pnpm lint / test / build 全部通过
- [ ] 新增逻辑附带单测
- [ ] 含 UI 变更时已附截图与设计稿对照
- [ ] 不含明文凭证与调试代码

## 机器人预审结果
<!-- lint 与覆盖率机器人会在评论自动汇报，reviewer 优先看其标红项 -->
```
