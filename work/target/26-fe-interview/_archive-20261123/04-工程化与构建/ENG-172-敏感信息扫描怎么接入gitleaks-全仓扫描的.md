---
title: [ENG-172] 敏感信息扫描怎么接入？gitleaks 全仓扫描的完整工程？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-172：敏感信息扫描怎么接入？gitleaks 全仓扫描的完整工程？
**答**：
- 三层接入：pre-commit 本地扫暂存区、CI 全量（含历史 commit）、定时任务兜底防绕过。
- .gitleaks.toml 自定义内部凭证规则（AK 前缀 内部 token 格式），补通用规则的漏报。
- 历史泄露处置顺序：先吊销凭证（比删代码更急）→ filter-repo 清洗历史 → force push 与团队协调。
- 报告归档进安全平台；豁免必须带 issue 单号与过期时间，防止白名单变后门。

```toml
# .gitleaks.toml —— 内部凭证自定义规则
title = "corp-gitleaks-rules"

[[rules]]
id = "corp-access-key"
description = "公司内部 AK"
regex = '''corp_ak_[a-zA-Z0-9]{32}'''
keywords = ["corp_ak_"]
tags = ["secret", "corp"]

[[rules]]
id = "corp-jwt-hardcoded"
description = "代码中硬编码 JWT"
regex = '''eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{5,}'''
tags = ["secret", "jwt"]

[allowlist]
description = "测试样例豁免 必须带 issue 号"
regexes = ['''corp_ak_test_[a-z0-9]{32}exempt[0-9]+''']
```

```yaml
# .github/workflows/gitleaks.yml —— CI 与定时兜底
name: gitleaks
on:
  pull_request:
  schedule: [{ cron: '0 19 * * *' }]
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - uses: gitleaks/gitleaks-action@v2
        env: { GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }} }
```
