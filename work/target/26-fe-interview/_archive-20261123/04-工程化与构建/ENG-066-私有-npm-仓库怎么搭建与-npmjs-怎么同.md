---
title: [ENG-066] 私有 npm 仓库怎么搭建？与 npmjs 怎么同步？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-066：私有 npm 仓库怎么搭建？与 npmjs 怎么同步？
**答**：
- 轻量自托管选 verdaccio：本地代理缓存 npmjs + 承载私有包，断网也能装；企业级选 Nexus/Artifactory 制品库。
- 同步策略：内网包走私有域（@myorg/*），外部包配置 uplink 代理拉取并缓存，形成读写分离。
- 发布与安装的凭据走 token（NPM_CONFIG_//registry.npmjs.org/:_authToken），CI 用机器人账号最小授权。
- 灾备要点：私有包定期备份/镜像到灾备仓库，外网挂了不影响内部安装历史版本。

```yaml
# verdaccio config.yaml 核心片段
storage: /verdaccio/storage
auth:
  htpasswd:
    file: /verdaccio/auth/htpasswd
uplinks:
  npmjs:
    url: https://registry.npmjs.org/
    cache: true
    maxage: 5m
packages:
  '@myorg/*':
    access: $authenticated
    publish: $authenticated
    unpublish: $authenticated
  '**':
    access: $all
    publish: $authenticated
    proxy: npmjs
logs: { content: stdout, format: pretty, level: http }
```

---

## 第十七章 脚手架与模板（ENG-067 ~ ENG-072）
