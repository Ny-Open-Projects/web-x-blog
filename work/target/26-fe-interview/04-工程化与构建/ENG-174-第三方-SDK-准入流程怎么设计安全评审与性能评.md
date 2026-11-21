---
title: [ENG-174] 第三方 SDK 准入流程怎么设计？安全评审与性能评估怎么做？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-174：第三方 SDK 准入流程怎么设计？安全评审与性能评估怎么做？
**答**：
- 五步准入：申请（用途 数据类型 替代方案）→ 安全评审（隐私协议 数据流向 证书指纹）→ 性能评估（体积 首屏影响 请求数）→ 沙箱试运行 → 入库登记版本与责任人。
- 静态评估自动化：下载包分析体积 依赖树 install 脚本 对外域名清单，输出评审报告。
- 运行时评估：接入后用性能平台对比接入前后 LCP/INP 与请求瀑布，超预期回滚接入。
- 准入非终身制：SDK 升级同样过评审，长期未使用的 SDK 定期清退。

```javascript
// scripts/sdk-admission-audit.mjs —— 第三方 SDK 准入静态评估
import { execSync } from 'node:child_process'
import { mkdtempSync, rmSync } from 'node:fs'

const pkg = process.argv[2]                       // 用法 node sdk-admission-audit.mjs some-sdk
const dir = mkdtempSync('/tmp/sdk-audit-')

// 1. 下载并解包
execSync(`npm pack ${pkg} --pack-destination ${dir}`, { stdio: 'inherit', cwd: dir })
const tgz = execSync(`ls ${dir}/*.tgz`).toString().trim()
execSync(`tar -xzf ${tgz} -C ${dir}`)

// 2. 体积评估
console.log('体积:', execSync(`du -sh ${dir}/package | cut -f1`).toString())

// 3. 声明依赖与安装期脚本
console.log('依赖:', execSync(`npm view ${pkg} dependencies peerDependencies --json`).toString())
console.log('脚本钩子:', execSync(`npm view ${pkg} scripts --json`).toString())

// 4. 对外域名清单 供安全评审判断数据流向
const domains = execSync(
  `grep -rhoE 'https?://[a-zA-Z0-9.-]+' ${dir}/package --include='*.js' | sort -u | head -50`,
).toString()
console.log('对外域名:', domains)
rmSync(dir, { recursive: true, force: true })
```

## 第三十四章 AI 深度工程化（ENG-175 ~ ENG-182）
