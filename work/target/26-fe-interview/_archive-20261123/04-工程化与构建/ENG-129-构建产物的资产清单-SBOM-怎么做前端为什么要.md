---
title: [ENG-129] 构建产物的资产清单（SBOM）怎么做？前端为什么要它？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-129：构建产物的资产清单（SBOM）怎么做？前端为什么要它？
**答**：
- SBOM（软件物料清单）结构化记录产物里的所有依赖及版本，npm 生态用 CycloneDX 格式一键生成。
- 价值：新 CVE 爆出时按清单秒级定位"哪些线上应用受影响"，不用逐仓 grep；也是企业合规与客户审计的常见要求。
- 落地：CI 构建时生成 sbom.json 作为制品的一部分归档，出安全事件时按清单联动应急。
- 前端特殊性：产物是静态资源，运行时依赖（CDN 脚本、第三方 SDK）也要纳入清单，不能只看 package.json。

```bash
# 1. 构建时生成 CycloneDX 格式 SBOM
npx @cyclonedx/cyclonedx-npm --output-file sbom.json --output-format JSON

# 2. 验证内容：依赖总数与关键组件版本
jq '.components | length' sbom.json
jq -r '.components[] | select(.name == "lodash") | .version' sbom.json

# 3. CI 中把 SBOM 随制品归档
# - uses: actions/upload-artifact@v4
#   with:
#     name: sbom
#     path: sbom.json
```
