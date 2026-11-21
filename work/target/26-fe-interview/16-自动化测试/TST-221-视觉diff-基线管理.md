---
title: [TST-221] 视觉回归测试的基线（snapshot）如何管理与评审？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-221：视觉回归测试的基线（snapshot）如何管理与评审？
**答**：
- 基线文件进 git（可评审），变更 PR 必须人工确认 diff 图——「更新基线」是显式决策。
- 基线命名含平台/主题/视口（button.chromium.light.mobile.png）。
- 定期清理孤儿基线（用例删除后残留），CI 校验引用一致性。
- 首次生成基线必须人审（否则垃圾基线永久化）。

```javascript
# 更新基线的标准流程
npx playwright test --update-snapshots  # 本地生成新基线
git add __screenshots__                  # PR 中附带 diff 图说明
# CI 校验：引用完整性（基线必须有对应用例）
r
```
