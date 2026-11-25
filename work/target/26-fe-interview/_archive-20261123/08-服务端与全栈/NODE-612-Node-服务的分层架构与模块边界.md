---
title: [NODE-612] Node 服务的分层架构（路由/服务/数据层）边界如何守护？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-612：服务端分层边界守护
**答**:
- 分层定义：路由层（协议解析/参数校验/调 service——无业务逻辑）、服务层（业务逻辑/事务编排——不碰 HTTP 细节）、数据层（Repository/外部客户端——NODE-485）、领域模块内聚（按业务域分目录——域内三层一体，跨域走接口）。
- 边界规则：路由不写 SQL、service 不碰 req/res（可测性）、repo 不含业务判断（语义方法而非逻辑）、跨域调用走 service 接口（不直捣别域 repo）。
- 守护手段：依赖检查脚本（dependency-cruiser/自写——ARC-409 分层检查服务端版：CI 违规阻断）、目录约定 lint（import 路径规则）、code review checklist（边界是否破坏——评审项）。
- 演进守护：适应度函数（ARC-396——分层规则自动化是唯一可靠的守护）、例外豁免（重构期临时违规——留痕到期清理）、域间防腐层（跨域调用包装——下游变更隔离 ARC-145）。
- 收益度量：域间违规数（趋零）、域内测试独立性（service 测试不需要起 HTTP——分层有效的证明）。
```javascript
// dependency-cruiser 规则（服务端分层）
forbidden: [
  { from: '^src/routes', to: '^src/repos' },                    // 路由禁直连数据层
  { from: '^src/services', to: '^src/routes' },                 // 服务禁碰路由
  { from: '^src/modules/(A)', to: '^src/modules/(B)/repos' }    // 跨域禁直捣 repo
]
```
