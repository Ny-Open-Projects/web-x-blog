---
title: [NODE-435] Node 服务的多团队平台治理（标准与例外）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-435：多团队平台治理
**答**:
- 治理对象：几十个 Node 服务散在各团队——治理目标是"标准内自治，例外有审批"，而非中心团队管一切（ARC-435 前端治理的服务端版）。
- 标准分层：强制标准（安全基线/可观测三件套/健康检查/优雅关闭——不达标不接流量，平台自动检测）、推荐标准（框架版本/目录结构——提供迁移工具）、自由区（业务实现细节）。
- 例外机制：豁免申请（写明原因与到期时间——豁免必须过期，防永久豁免堆积 ARC-396）、豁免清单公开（透明化压力）。
- 平台自动治理：服务注册时自动扫描标准符合度、非合规项清单化推送给 owner、升级季统一推 codemod（NODE-420/ARC-425）。
- 度量治理效果：标准覆盖率趋势、豁免数量趋势、新服务开箱合规率（模板化的价值证明）。
```javascript
// 服务标准扫描
const standards = {
  mandatory: { healthCheck: has('/healthz'), graceful: hasSigterm(), otel: hasTrace(),
               secrets: noSecretInCode() },                     // 不达标 → 接入阻断
  recommended: { framework: latest(), logging: pinoStructured() } // 不达标 → 迁移建议
};
function auditService(svc) {
  return { svc, passed: Object.values(standards.mandatory).every(Boolean),
    exemptions: svc.exemptions.filter(e => e.until > Date.now()) }; // 过期豁免失效
}
```
