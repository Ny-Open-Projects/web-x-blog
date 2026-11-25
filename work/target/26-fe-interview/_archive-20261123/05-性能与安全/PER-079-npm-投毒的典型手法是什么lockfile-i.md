---
title: [PER-079] npm 投毒的典型手法是什么？lockfile/integrity/最小依赖如何组合防御？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-079：npm 投毒的典型手法是什么？lockfile/integrity/最小依赖如何组合防御？

**答**：
- 典型手法：抢注弃用包名（typosquatting）、向热门包发带后门的新版本（如 colors/faker 假版本、ua-parser-js 投毒事件）、通过 `postinstall` 脚本在安装时执行恶意代码。
- 组合防御：**lockfile 锁定精确版本与 integrity 哈希**、CI 用 `npm ci`（拒绝 lockfile 之外的版本）、`--ignore-scripts` 禁安装期脚本、`overrides` 强制钉住存在风险的传递依赖。
- 流程防御：新依赖必须过评审（star/维护者/下载量/最近发布时间）、`npm audit` + Socket/OSV 扫描进 CI、锁文件变更在 PR diff 里重点审。
- 最小依赖原则：能自己写 20 行就不引一个包，少一个依赖少一条投毒路径。

```bash
#!/bin/bash
# CI 依赖安全卡口：npm ci + 禁脚本 + 审计门禁
set -euo pipefail

# 1) 严格按 lockfile 安装，integrity 不匹配直接失败
npm ci --ignore-scripts   # 禁止 postinstall 脚本执行，防投毒安装阶段

# 2) 审计门禁：高危漏洞即失败（可按需放宽为 --audit-level=critical）
npm audit --audit-level=high --omit=dev || {
  echo "::error::依赖审计未通过，禁止合并"
  exit 1
}

# 3) lockfile 完整性提示：PR 中 lockfile 变更需评审标记
if git diff --name-only origin/main...HEAD | grep -q 'package-lock.json'; then
  echo "::warning::本 PR 修改了 lockfile，请确认新依赖经过安全评审"
fi

npm run build
```

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "scripts": {
    "preinstall": "npx only-allow npm",
    "prepare": "husky install"
  },
  "overrides": {
    "lodash.template": "npm:@nolyfill/lodash.template@latest",
    "got@<11.8.5": ">=11.8.5",
    "minimist@<1.2.8": ">=1.2.8"
  },
  "engines": { "npm": ">=10" }
}
```
