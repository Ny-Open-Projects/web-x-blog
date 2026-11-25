---
title: [ENG-152] 依赖许可证合规怎么落地？license 扫描与传染性协议怎么卡口？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-152：依赖许可证合规怎么落地？license 扫描与传染性协议怎么卡口？
**答**：
- 风险分级：MIT/Apache-2.0/BSD/ISC 可商用；LGPL 谨慎；GPL/AGPL 传染性强，前端产物引用可能被要求开源。
- CI 全量扫描必须覆盖传递依赖，不能只看直接依赖；monorepo 各子包独立扫描。
- 白名单机制：allow 直接通过、review 清单走法务入库、deny 直接阻断；deny 命中时提供替代推荐而不是让人自己换一个等价 GPL 包。
- 扫描结果归档为 SBOM 附件，审计与客户合规检查时直接出具。

```bash
# CI 许可证合规卡口
# 1. 全量扫描含传递依赖 输出 json
npx license-checker --production --json --out licenses.json

# 2. 白名单校验 传染性协议即失败
node scripts/license-gate.mjs licenses.json \
  --allow "MIT,Apache-2.0,BSD-2-Clause,BSD-3-Clause,ISC,0BSD,Unlicense,CC0-1.0" \
  --review "LGPL-3.0,MPL-2.0" \
  --deny "GPL-2.0,GPL-3.0,AGPL-3.0"

# 3. license-gate.mjs 核心逻辑
# 读取 licenses.json 每个依赖的 licenses 字段
# 命中 deny 退出码 1 并打印依赖名与引用路径
# 命中 review 输出待法务清单 不阻断
```
