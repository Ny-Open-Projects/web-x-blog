---
title: [PER-107] 安全测试如何左移到 CI？SAST/DAST/依赖扫描如何组合？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-107：安全测试如何左移到 CI？SAST/DAST/依赖扫描如何组合？

**答**：
- 左移阶梯：**提交时**（lint + SAST 增量扫描，秒级）、**PR 时**（依赖扫描 + secrets 扫描 + 容器基线，分钟级）、**发布前**（DAST 对测试环境爬测 + 渗透用例回归，小时级）。
- 前端仓库重点项：依赖扫描（audit/Socket）、敏感信息扫描（正则匹配 key/token/内网地址）、SAST 查危险 API（innerHTML/eval）、CSP 与安全头配置检查。
- 工具选型：SAST 用 Semgrep（规则可自写）、依赖用 npm audit + OSV-Scanner、secrets 用 gitleaks、DAST 用 OWASP ZAP 基线扫描。
- 卡口策略：高危阻断合并，中危开 issue 跟踪，避免扫描器噪声导致团队关闭整个流水线。

```yaml
# GitHub Actions：前端仓库安全流水线
name: security
on: [pull_request]
jobs:
  secrets:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - name: gitleaks 扫描提交历史中的密钥
        uses: gitleaks/gitleaks-action@v2

  deps:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22 }
      - run: npm ci --ignore-scripts
      - name: 依赖漏洞门禁
        run: npm audit --audit-level=high

  sast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Semgrep 危险 API 规则
        run: |
          docker run --rm -v "$PWD:/src" returntocorp/semgrep semgrep \
            --config=p/javascript --config=p/xss \
            --error --metrics=off \
            --severity=ERROR   # 高危才阻断，中低危输出报告不卡合并
```

```yaml
# Semgrep 自定义规则：前端高危 sink 检查
rules:
  - id: dom-xss-innerhtml
    message: 用户输入直接写入 innerHTML，存在 XSS 风险，请改用 textContent 或先净化
    severity: ERROR
    languages: [javascript, typescript]
    patterns:
      - pattern: $EL.innerHTML = $X
      - pattern-not: $EL.innerHTML = DOMPurify.sanitize(...)   # 净化后放行
  - id: no-eval
    message: 禁止使用 eval，存在代码注入风险
    severity: ERROR
    languages: [javascript, typescript]
    pattern: eval($X)
  - id: no-hardcoded-secret
    message: 疑似硬编码密钥，请改走环境变量
    severity: ERROR
    languages: [javascript]
    pattern-regex: '(api[_-]?key|secret|token)\s*[:=]\s*["''][A-Za-z0-9_\-]{16,}["'']'
```
