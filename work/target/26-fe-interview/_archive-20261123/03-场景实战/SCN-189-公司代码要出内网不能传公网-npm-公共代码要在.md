---
title: [SCN-189] 公司代码要出内网不能传公网 npm，公共代码要在团队间复用，如何搭 npm 私服？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-189：公司代码要出内网不能传公网 npm，公共代码要在团队间复用，如何搭 npm 私服？
**答**：
- 私服双职责：托管私有包（内网组件库/工具库）+ 上游代理缓存（npmjs 拉取加速与离线可用），Verdaccio/Nexus 二选一，企业级多仓选 Nexus。
- 同步策略是核心矛盾：上游代理自动缓存公有包；私有包发布权限收紧（白名单 + 发布账号），防止内网包名撞上未来公有包（加 @corp scope 天然隔离）。
- 客户端配置：`.npmrc` 把 @corp scope 指向私服，其余走代理；token 走环境变量不入库。
- 配套治理：私有包必须带 CI 发布（禁止本地 publish）、版本 changelog 自动生成、弃用包 deprecate 标记。

```yaml
# Verdaccio 私服配置：scope 隔离 + 上游代理 + 发布权限
storage: /verdaccio/storage
auth:
  htpasswd:
    file: /verdaccio/htpasswd
    max_users: 20                                     # 账号收紧，新增走审批
uplinks:
  npmjs:
    url: https://registry.npmjs.org/                  # 上游代理：公有包缓存加速
    cache: true
    timeout: 10s
packages:
  '@corp/*':                                          # 私有 scope：只进内网，绝不外传
    access: $authenticated
    publish: $authenticated
    unpublish: team-frontend-core                     # 撤包仅核心团队
  '@*/*':                                             # 其他 scope：走上游代理
    access: $all
    publish: $authenticated
    proxy: npmjs
  '**':
    access: $all
    publish: $authenticated
    proxy: npmjs
middlewares:
  audit: { enabled: true }
logs: { content: stdout }
publish:                                              # 私有包发布前置校验（配合 CI）
  allow_publish: true
```

```ini
# 项目 .npmrc：scope 分流（token 从环境变量取，不入库）
@corp:registry=https://npm.example.com/
registry=https://npm.example.com/            # 其余走私服代理缓存
//npm.example.com/:_authToken=${NPM_TOKEN}
always-auth=true
```

```bash
# 发布流水线：CI 内发布（禁止本地 publish），版本与 changelog 自动化
# .gitlab-ci.yml 片段
publish-package:
  stage: release
  only: { refs: [tags] }                              # 只有打 tag 才发布，tag 即版本
  script:
    - npm version "$CI_COMMIT_TAG" --no-git-tag-version
    - npm publish --access restricted                 # @corp scope 默认私有
    - node scripts/gen-changelog.js >> RELEASE.md     # 从 conventional commits 生成变更记录
```
