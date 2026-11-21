---
title: [NODE-152] API 网关与 BFF 的分工边界在哪？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-152：API 网关与 BFF 的分工边界在哪？
**答**：
- 网关 = **南北向 + 技术域**：路由转发、JWT 校验、IP 黑白名单、全局限流、TLS 终结、WAF、灰度分流、链路头注入——所有流量都要做且与业务无关的能力。
- BFF = **东西向 + 业务域**：按端聚合裁剪、协议转换（GraphQL/protobuf）、业务缓存、场景级降级、业务埋点。
- 判断口诀：所有流量都要做且与业务无关 → 网关；只有某些端/场景要 → BFF；与领域数据强相关 → 微服务本身。
- 典型反模式：鉴权在网关和 BFF 各做一遍（口径不一）、BFF 直连数据库穿透微服务边界、网关里写业务规则。

```yaml
# 网关路由配置：只认 BFF，不直连微服务；通用能力下沉网关
server:
  routes:
    - id: bff-web
      uri: http://bff-web.internal:3000
      predicates:
        - Path=/api/**
      filters:
        - JwtAuth                     # 鉴权：网关统一做，BFF 不重复
        - RateLimit=1000,1s           # 全局限流
        - AddRequestHeader=X-Trace-Id,generated   # 链路头注入
    - id: open-api                    # 开放平台独立泳道
      uri: http://open-bff.internal:3000
      predicates:
        - Path=/open/v1/**
      filters:
        - ApiKeyAuth
        - RateLimitKeyedByApiKey=100,1m
# BFF 只做业务编排：聚合、裁剪、业务缓存、场景降级（NODE-147/048）
```

---

## 十九、TypeScript Node 工程
