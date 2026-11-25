---
title: [WCN-151] WCN 组件团队的协作规范：API 评审、命名空间、发布流程如何制度化？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-151：WCN 组件团队的协作规范：API 评审、命名空间、发布流程如何制度化？

**答**：
- 命名空间制度：所有 tag 必须带组织前缀（`acme-*`）且登记在中央 registry（JSON 清单），CI 校验重复/格式——杜绝 define 冲突（WCN-048）。
- API 评审：新组件 RFC（动机/契约草案/对比现有方案）→ 评审通过后实现；attribute/事件命名遵循 `kebab-case` + 组件语义前缀；breaking 变更必须走 deprecate → 双版本窗口 → 移除三步。
- 发布流程：changesets 版本管理 + custom-elements.json diff 报告 + 双宿主冒烟测试（React/Vue demo 页）+ CDN 发布脚本（上传 → 校验 SRI → 更新 importmap staged → 切换）。
- 文档即契约：Storybook 文档页与 manifest 同源生成，禁止文档与实现两处维护；示例代码可直接复制运行。
- 治理指标：组件复用率、API 破坏次数/季度、接入人日、issue 平均解决时长。

```json
// registry.json（中央登记）
{ "acme-button": { "owner": "design-sys", "version": "1.4.2", "status": "stable" },
  "acme-data-table": { "owner": "design-sys", "version": "0.9.0", "status": "beta" } }
```

```yaml
# 发布流水线关键闸口
- lint: tag 前缀与 registry 校验
- test: 双宿主冒烟 + a11y 门禁 + 视觉回归
- check: manifest diff → breaking 需 changelog 标注 + 版本 major
- deploy: CDN staged 上传 → SRI 校验 → importmap 切换 → 看板观察 30 分钟 → 正式
```
