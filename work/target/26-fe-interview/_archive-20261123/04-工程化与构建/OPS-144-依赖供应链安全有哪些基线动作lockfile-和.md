---
title: [OPS-144] 依赖供应链安全有哪些基线动作？lockfile 和 integrity 起什么作用？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-144：依赖供应链安全有哪些基线动作？lockfile 和 integrity 起什么作用？
**答**：
- lockfile 提交 + npm ci 严格按锁安装：杜绝"同一 commit 不同机器装到不同版本"的供应链注入面。
- lock 中的 integrity 字段是每个包 tarball 的哈希：registry 或代理被篡改时安装直接失败，是 npm 侧的"subresource integrity"。
- install 脚本是投毒主要通道：CI 用 --ignore-scripts，确需脚本的白名单豁免。
- 门禁三件套：npm audit 高危阻断、新依赖 PR 评审（展示体积与依赖树变化）、license 合规检查。
- registry 锁定私服/可信镜像，publish 凭证不落代码仓库（OPS-146）。

```bash
# 依赖供应链安全基线
# 1. 严格按 lock 安装，且安装过程不得改动 lock
npm ci --ignore-scripts
git diff --exit-code package-lock.json \
  || { echo "lockfile changed during install, block merge"; exit 1; }

# 2. integrity 校验确保 tarball 未被篡改（registry/代理被劫持时安装失败）
grep '"node_modules/semver"' -A3 package-lock.json | grep integrity

# 3. 门禁：高危漏洞阻断 + license 合规
npm audit --audit-level=high || exit 1
npx license-checker --production --onlyAllow "MIT;Apache-2.0;BSD-3-Clause;ISC;0BSD"

# 4. registry 与版本策略（.npmrc 入库）
cat .npmrc
#   registry=https://registry.npmmirror.com/
#   save-exact=true        # 依赖固定精确版本，不写 ^ ~

# 5. 新增依赖走 PR：CI 输出 bundle 体积与依赖树 diff，评审后才能合入
```
