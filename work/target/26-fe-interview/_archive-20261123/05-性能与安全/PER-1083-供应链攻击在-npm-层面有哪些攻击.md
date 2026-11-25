---
title: [PER-1083] 供应链攻击在 npm 层面有哪些攻击面
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1083：供应链攻击在 npm 层面有哪些攻击面

**答**：
- 攻击面：新包 typosquatting（拼错包名）、维护者账号被盗（投毒新版本）、install 脚本执行（postinstall）、传递依赖失控。
- 防御：lockfile 固化 + 私有 registry 白名单 + npm audit/osv 扫描进 CI + 禁止 postinstall 脚本（--ignore-scripts）。
- 流程：新增依赖评审（必要性/维护活跃度/下载量）、重大版本升级双人 review。
- 检测：构建产物 hash 基线，产物 diff 异常（体积突增/新增网络调用）告警。

```javascript
// CI 供应链检查脚本
import { execSync } from 'node:child_process';
function supplyChainCheck() {
  const audit = JSON.parse(execSync('npm audit --json').toString());
  const critical = Object.values(audit.vulnerabilities ?? {})
    .filter(v => v.severity === 'critical' || v.severity === 'high');
  if (critical.length) throw new Error('高危依赖: ' +
    critical.map(c => `${c.name}@${c.range}`).join(', '));
  // 检查新增依赖是否过审（对比批准清单）
  const lock = JSON.parse(require('fs').readFileSync('package-lock.json'));
  for (const name of Object.keys(lock.packages ?? {}))
    if (!APPROVED.has(name.replace('node_modules/', '')) && name.includes('node_modules/'))
      throw new Error(`未评审依赖 ${name}`);
}
```
