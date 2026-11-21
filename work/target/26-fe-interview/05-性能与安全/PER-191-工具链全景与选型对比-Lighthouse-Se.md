---
title: [PER-191] 工具链全景与选型对比（Lighthouse/Sentry/SonarQube/OWASP ZAP 等）？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-191：工具链全景与选型对比（Lighthouse/Sentry/SonarQube/OWASP ZAP 等）？

**答**：
- 选型按**用途三象限**：门禁要快而稳（ESLint/npm audit/Lighthouse CI），诊断要深而慢（DevTools/ZAP），监控要全而省（RUM/Sentry 采样）。
- 关键认知：每个工具都有明确的能力边界——Lighthouse 是实验室口径不代表真实用户，ZAP 有误报需人工确认，Sentry 计费要配采样策略。
- 工具不叠加堆积：同类工具选一个当主力，其他当补充；工具数量翻倍不等于安全感翻倍。
- 工具链要进 CI 与值班 SOP：能在门禁拦的不靠人眼，能在告警里看到的不到线上翻日志。

```json
{
  "toolchain_panorama": [
    { "tool": "Lighthouse", "type": "实验室性能审计", "use": "CI 门禁与单页诊断", "limit": "实验室口径，不代表真实用户分布" },
    { "tool": "web-vitals 加自建 RUM", "type": "真实用户监控", "use": "P75 口径与业务归因", "limit": "采样与上报成本需治理" },
    { "tool": "Sentry", "type": "错误与性能监控", "use": "错误聚合与 sourcemap 还原", "limit": "用量计费，需配采样策略" },
    { "tool": "Chrome DevTools", "type": "深度诊断", "use": "火焰图 内存 网络逐帧分析", "limit": "不可自动化，靠 SOP 沉淀" },
    { "tool": "ESLint 加 Semgrep", "type": "SAST", "use": "危险 API 与安全模式扫描", "limit": "规则需持续维护" },
    { "tool": "OWASP ZAP", "type": "DAST", "use": "黑盒扫描 XSS 与注入", "limit": "误报需人工确认" },
    { "tool": "npm audit 加 Socket", "type": "供应链", "use": "依赖漏洞与新版本行为分析", "limit": "新投毒有滞后窗口" },
    { "tool": "gitleaks", "type": "凭证扫描", "use": "提交与历史全量扫描", "limit": "需配套密钥轮换流程" }
  ],
  "selection_rule": "门禁用快而稳的，诊断用深而慢的，监控用全而省的；同类工具只选一个主力"
}
```
