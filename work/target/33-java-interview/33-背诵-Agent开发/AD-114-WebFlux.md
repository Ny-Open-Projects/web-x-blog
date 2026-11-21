---
title: "[AD-114] MCP·WebFlux（部署）"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · WebFlux（部署）

- **事实**：MCP SSE/WebFlux server 部署：标准 Spring Boot 应用部署（多实例+负载均衡），与 stdio 子进程形态运维完全不同
- **原理**：远程 MCP server 是常驻服务（HA/监控/发布 JA-313/314），stdio 是宿主管理（JA-095），两形态运维面不同要分清
- **常见误区**：
  1. 两种形态运维相同（错）
  2. 远程 server 无需 HA（错）
  3. 部署与形态无关（错）
- **工程用法**：MCP 部署形态
- **版本锚点**：实战共识
