---
title: [ENG-120] Copilot/Cursor 的团队规范要约定什么？使用边界、代码主权与安全审查？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-120：Copilot/Cursor 的团队规范要约定什么？使用边界、代码主权与安全审查？
**答**：
- 使用边界：白名单场景（样板代码、类型、单测、遗留代码理解）放开；涉密模块（支付、风控）禁用外部 AI。
- 代码主权：AI 产出以提交者名义提交、责任归提交者；PR 描述标注 ai-assisted，review 关注度不低于人工代码。
- 安全审查：生成代码过 secret 扫描与依赖审计才能合入；对话中禁贴真实凭证与生产数据。
- 配套动作：项目内规则文件（copilot-instructions/.cursor/rules，见 ENG-059）+ 定期回收团队的 AI 事故案例更新规范。

```yaml
# ai-coding-policy.yml：团队 AI 编码政策（节选）
allowed:
  - 样板代码与类型定义生成
  - 单测用例与 mock 数据生成
  - 遗留代码阅读理解与迁移建议
restricted:
  - 支付、风控等涉密模块禁止使用外部 AI 服务
  - 禁止在对话中粘贴真实凭证、内网地址、用户数据
code_ownership:
  - AI 产出以提交者名义提交，责任归属提交者
  - PR 描述标注 ai-assisted，reviewer 重点关注边界条件
security:
  - 合入前必须通过 secret 扫描与依赖审计
  - AI 生成代码与人工代码适用同一套门禁
```
