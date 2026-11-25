---
title: [NODE-067] npm 依赖治理与安全审计怎么做？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-067：npm 依赖治理与安全审计怎么做？
**答**：
- 供应链安全是 Node 服务的重灾区（恶意包、typosquatting、依赖投毒）。措施：`npm audit`/`osv-scanner` CI 卡口、`package-lock.json` 必须提交（可复现安装）、`npm ci` 而非 `npm install` 部署、锁定 registry（内网制品库/镜像源）、`postinstall` 脚本白名单审查。
- 依赖治理：定期 `npm outdated` 升级（小步快跑），`depcheck` 清理僵尸依赖，控制依赖树深度（能用内置模块不引包）；等价 API（如 `axios` vs `node fetch`）优先内置。
- 事故应急：XZ/ua-parser 类投毒事件 → 锁定具体版本（`overrides`/`resolutions`）+ 私有 mirror 白名单。

```bash
# CI 安全卡口脚本
npm ci                          # 严格按 lockfile，防漂移
npm audit --omit=dev --audit-level=high || exit 1   # high 以上漏洞直接挂掉流水线
npx depcheck --ignores=@types/*                      # 僵尸依赖检查
node -e "const l=require('./package-lock.json'); \
  const bad=['event-stream@3.3.6','ua-parser-js@0.7.29']; \
  for (const p of Object.keys(l.packages)) \
    if (bad.some(b => p.includes(b.split('@')[0]))) { console.error('命中投毒黑名单:', p); process.exit(1); }"
```

```json
{
  "overrides": {
    "semver": "^7.5.4",
    "minimist": "^1.2.8"
  },
  "engines": { "node": ">=20 <23" },
  "scripts": {
    "preinstall": "npx only-allow npm",
    "audit": "npm audit --omit=dev --audit-level=high"
  }
}
```

---

## 十、综合实战
