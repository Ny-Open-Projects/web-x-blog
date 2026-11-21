---
title: [OPS-143] 多项目（monorepo/微前端）发布怎么编排依赖顺序？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-143：多项目（monorepo/微前端）发布怎么编排依赖顺序？
**答**：
- 声明项目依赖 DAG（tokens → 组件库 → 壳应用 → 业务应用），编排器拓扑排序后按层发布，禁止并行乱序。
- 上游发版后下游先在集成环境联调再晋级；npm 包发布后探测 registry 生效再触发下游构建，防"发了但拉不到"。
- 发布以"组"为单位（release train）：一个组内各项目版本关联，整体晋级整体回滚视图。
- 失败策略：暂停后续并通知，支持"从失败点续发"，已成功步骤不重复执行。
- 接口/协议变更要向后兼容一版：新旧版本共存期内下游逐个切换，最后下线旧协议（与 OPS-001 的兼容性要求同源）。

```yaml
# 多项目发布编排：依赖 DAG + 拓扑排序 + 失败续发
projects:
  design-tokens:  { order: 1, type: npm_package, depends_on: [] }
  ui-components:  { order: 2, type: npm_package, depends_on: [design-tokens] }
  shared-utils:   { order: 2, type: npm_package, depends_on: [] }
  web-shell:      { order: 3, type: app, depends_on: [ui-components, shared-utils] }
  app-order:      { order: 4, type: app, depends_on: [web-shell] }
  app-payment:    { order: 4, type: app, depends_on: [web-shell] }
rules:
  - 下游锁定上游版本范围，上游发版后下游先集成环境联调再晋级
  - npm 包发布后探测 registry 生效（私服/unpkg 可拉到新版本）再触发下游构建
  - 协议类变更保持向后兼容一版，新旧共存期内逐个切换后下线旧协议
orchestration:
  trigger: manual_group_release
  group: "2026-W44-payments"          # release train 编号，组内版本关联
  strategy: topological               # 按 DAG 拓扑排序执行
  on_failure: pause_and_notify        # 暂停后续并通知
  resume: from_failed_step            # 从失败点续发，不重复已成功步骤
```

---

## 十六、安全运维（OPS-144 ~ OPS-152）

前端安全运维的主战场：依赖供应链、CVE 应急、凭据防泄漏、劫持应对、SRI、防刷、上线安检、隐私合规与第三方治理。
