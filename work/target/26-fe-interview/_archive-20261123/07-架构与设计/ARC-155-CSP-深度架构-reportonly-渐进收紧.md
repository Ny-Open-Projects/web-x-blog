---
title: [ARC-155] CSP 深度架构（report-only 渐进收紧）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-155：CSP 深度架构（report-only 渐进收紧）如何设计？
**答**：
- 三阶段推进：① `Content-Security-Policy-Report-Only` 全量观察（收集所有违规上报但不拦截，摸清真实依赖面）→ ② 按违规数据收紧白名单并切强制（保留 report-uri 持续观测）→ ③ 强 nonce/严格 hash 替代 `unsafe-inline`，最终达到无 unsafe-*。
- nonce 方案：模板引擎每请求生成 nonce 注入 script 标签与响应头，框架 SSR 原生支持（React 19/Next 有 nonce 透传）；内联事件（onclick 属性）是收紧的最大阻力，要先存量治理。
- 第三方依赖治理：违规上报的主要来源是三方脚本（营销/客服/统计），逐个评估必要性，必要的走白名单 + SRI 校验。
- 日常运营：report-uri 聚合分析，新增违规告警（可能是 XSS 攻击信号，也可能是新依赖上线漏配），白名单变更走 MR 评审。

```nginx
# CSP 渐进收紧三阶段配置（nginx）
# 阶段 1：全量观察（不拦截，只上报）
add_header Content-Security-Policy-Report-Only "
  default-src 'self';
  script-src 'self' 'nonce-{NONCE}' https://sdk.third.com;
  style-src  'self' 'unsafe-inline';          # 样式先放宽，脚本优先收紧
  img-src    'self' data: https://img.corp.com;
  report-uri /csp-report;" always;

# 阶段 2：强制执行（白名单来自阶段 1 违规数据收敛）
add_header Content-Security-Policy "
  default-src 'self';
  script-src 'self' 'nonce-{NONCE}';
  style-src  'self' 'unsafe-inline';
  img-src    'self' data: https://img.corp.com;
  report-uri /csp-report;" always;

# 阶段 3：nonce + hash 全收紧（无 unsafe-*）
# script-src 'self' 'nonce-{NONCE}' 'sha256-{INLINE_HASH}';

# nonce 生成：proxy 或应用层每请求随机生成，注入 <script nonce="{NONCE}">
# 运营：/csp-report 聚合，同指纹违规 > N 次告警；白名单变更走 MR + 安全评审
```
