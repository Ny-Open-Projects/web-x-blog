---
title: [ENG-141] 已发布的坏版本怎么回滚？publish 不可变性与撤回策略怎么设计？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-141：已发布的坏版本怎么回滚？publish 不可变性与撤回策略怎么设计？
**答**：
- npm publish 后版本号永久占用不可重发，unpublish 仅 72 小时内且受限；回滚本质是"向前修复"。
- 三档策略：紧急 bugfix patch（分钟级）、deprecate 临时禁用（带原因）、重大事故 unpublish 或镜像层下架。
- 标准动作：revert 出问题的 commit → 发 x.y.z+1 → 刚发完时先 dist-tag rm 摘掉 latest 让新安装回到上一稳定版。
- 消费方配合：应用 lockfile 锁版本 + 内部镜像加坏版本熔断，把坏版本在组织内强制排除。

```bash
# 回滚三板斧：先摘 tag 再发修复版 组织内熔断坏版本
# 1. 刚发完发现炸了 摘掉 latest 让新安装回到上一稳定版
npm dist-tag rm @corp/http-client latest

# 2. revert 代码并发布正向修复版
git revert --no-edit <bad-commit>
npm version patch && npm publish --tag latest

# 3. 组织内镜像层熔断坏版本
curl -X PUT https://verdaccio.corp.internal/-/package/@corp/http-client/bad-versions \
  -H "Content-Type: application/json" \
  -d '{ "blocked": ["2.1.1"], "reason": "安全漏洞 禁止使用 升级到 2.1.2" }'
```
