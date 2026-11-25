---
title: [NODE-579] Node 服务的内部 API 治理平台（服务目录/依赖/权限）如何建设？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-579：内部 API 治理平台
**答**:
- 平台整合：服务目录（NODE-427 画像）、依赖声明（NODE-505）、权限矩阵（NODE-484）、SLA 条目（NODE-506）、契约（NODE-528）——分散数据一个门户统一消费（治理不是建系统而是聚合已有数据）。
- 核心流程线上化：权限申请（自助申请 → owner 审批 → 自动生效——审批流节点记录）、依赖接入（新依赖声明 → 影响面提示 → 容量协商入口）、变更通知（NODE-447 契约 diff 自动触达）。
- 治理视图：全局依赖图（服务间调用全景——环检测/单点识别）、权限矩阵审计（越权风险扫描：宽松授权清单）、僵尸盘点（90 天零调用接口/依赖——清理建议）。
- 与 CI 联动：治理规则可执行（未声明依赖阻断/未登记接口阻断——平台输出规则给 CI 消费）。
- 度量：平台使用率（流程走平台的占比——绕过平台的比例治理）、治理指标趋势（僵尸接口数/宽松授权数下降）。
```yaml
# 治理门户数据聚合
catalog: { source: service-registry }       # 服务画像
deps:    { source: trace-agg + declarations }
perms:   { source: authz-matrix }
flows:   [ 'perm-apply', 'dep-onboard', 'contract-notify' ]
ci_rules: [ no-undeclared-dep, no-unregistered-route ]
```
