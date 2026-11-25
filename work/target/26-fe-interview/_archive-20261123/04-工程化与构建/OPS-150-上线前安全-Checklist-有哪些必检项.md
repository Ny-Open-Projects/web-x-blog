---
title: [OPS-150] 上线前安全 Checklist 有哪些必检项？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-150：上线前安全 Checklist 有哪些必检项？
**答**：
- 供应链：lockfile 一致、audit 无高危、新依赖过审、包体积变化在阈值内。
- 凭据：gitleaks 通过、bundle 中无私钥/内部 AK（产物关键字扫描）。
- 响应头：HTTPS/HSTS、CSP（enforce 或 report-only 残留量达标）、nosniff/X-Frame-Options。
- 完整性：第三方 script 全部锁版本（无 latest）、关键外链带 SRI。
- 隐私与运行时：新增埋点过隐私评审（无 PII 明文）、sourcemap 未暴露公网、错误上报与回放开关可远程关闭。
- Checklist 工具化：CI 自动检查 + 发布单勾选双通道（OPS-180），纯人肉遵守率必然衰减。

```yaml
# 上线前安全 Checklist（CI 卡口 + 发布单勾选双通道）
release_gate:
  supply_chain:
    - lockfile 已提交且 npm ci 后无 diff（OPS-144）
    - npm audit 无 high / critical
    - 新依赖经评审，bundle 体积变化 < 10%
  secrets:
    - gitleaks 扫描通过（OPS-146）
    - 产物关键字扫描：无私钥/内部 AK 混入 bundle
  headers:
    - HTTPS 与 HSTS 生效
    - CSP 处于 enforce，或 report-only 日残留 < 10 条（OPS-147）
    - X-Content-Type-Options: nosniff 与 X-Frame-Options 配置正确
  integrity:
    - 第三方 script 全部锁死版本（禁止 latest）
    - 关键外链资源带 SRI（OPS-148）
  privacy:
    - 新增埋点字段过隐私评审，无 PII 明文上报（OPS-151）
    - 新增 Cookie 域纳入 Consent 管理
  runtime:
    - sourcemap 未暴露公网（OPS-077）
    - 错误上报 / 会话回放 / 故障注入开关可远程关闭（OPS-175）
```
