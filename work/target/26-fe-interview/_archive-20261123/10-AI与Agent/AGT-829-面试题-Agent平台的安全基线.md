---
title: [AGT-829] 平台上线前的安全基线检查（注入防御/越权/数据外泄/供应链），清单是什么？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-829：平台上线前的安全基线检查（注入防御/越权/数据外泄/供应链），清单是什么

**答**：
- 五域基线：提示注入（间接注入测试覆盖：工具结果/文档内容里的注入指令，隔离层级+输出过滤双防线）、越权（横向：租户间/用户间数据隔离渗透测试；纵向：Agent 权限提升路径）、数据外泄（出域标记+外发工具检查+DLP 扫描输出）、供应链（工具来源审核/依赖 SBOM/模型供应链验证）、运行安全（沙箱逃逸测试/资源限额/密钥管理 KMS）。
- 红队例行化：上线前一次全面红队+季度例行（攻击手法在演化），红队发现进修复闭环与回归集。
- 基线的可证性：每项检查有自动化证据（扫描报告/测试结果），安全不是口头承诺。

```javascript
const SECURITY_BASELINE = {
  inject: { indirectTests: '>=50cases', isolation: 'data≠instruction' },
  authz: { horizontal: 'cross-tenant-pentest', vertical: 'priv-escalation' },
  exfil: { egressMark: true, dlp: 'output-scan' },
  supply: { sbom: true, toolReview: 'all-3p' },
  runtime: { escapeTest: true, secrets: 'kms' },
};
function securityGoNoGo(evidence) {
  return Object.entries(SECURITY_BASELINE).every(([k, v]) =>
    hasEvidence(evidence, k, v));                  // 每项有证据
}
```

