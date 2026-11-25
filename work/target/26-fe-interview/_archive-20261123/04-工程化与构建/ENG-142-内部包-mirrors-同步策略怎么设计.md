---
title: [ENG-142] 内部包 mirrors 同步策略怎么设计？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-142：内部包 mirrors 同步策略怎么设计？
**答**：
- 内部 verdaccio 本质是按需代理缓存：上游挂了缓存仍在，但首次拉取有冷启动问题，需要主动预热。
- 预热策略：定时任务把高频依赖与各仓库 lockfile 全量 fetch 进镜像，保证 CI 离线也能装。
- 断供预案：上游不可达时镜像 failover 到本地缓存（maxage/failover_timeout），关键依赖可固化为准内部包。
- 同步策略写明滞后容忍：元数据 TTL、上游新版本可见延迟、断供切离线模式的通知机制。

```yaml
# verdaccio config.yaml —— 内部镜像同步与预热策略
uplinks:
  npmjs:
    url: https://registry.npmmirror.com
    timeout: 30s
    maxage: 1h            # 元数据缓存窗口 断网期间用旧元数据兜底
    failover_timeout: 5m  # 上游失败后 5 分钟内直接用本地缓存

packages:
  '@*/*':
    access: $authenticated
    publish: $authenticated
    proxy: npmjs
  '@corp/**':
    access: $authenticated
    publish: $authenticated   # 内部包只进内部 不代理外发

publish:
  allow_offline: true       # 上游不可达时允许本地发布 事后同步

# 预热定时任务 每天凌晨把公共 lockfile 依赖 fetch 进缓存
# 0 3 * * * cd /var/cache/warmup && pnpm fetch
```

## 第二十八章 文档与知识工程（ENG-143 ~ ENG-147）
