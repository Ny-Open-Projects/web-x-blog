---
title: [AGT-247] MCP 多 Server 聚合——Client 同时接几十个 Server 怎么管理？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-247：一个 Agent 接入多个 MCP Server，工具冲突与上下文膨胀怎么管理？

**答**:
- 问题清单：工具名冲突（两个 Server 都有 `search`）、工具总量爆炸（几十个 Server 的 schema 塞爆上下文）、重复能力（三个 Server 都能查日程）、故障隔离（一个 Server 挂了拖累全局）。
- 命名空间与路由：工具名带 Server 前缀（`github.search`/`slack.search`）消歧；会话级"工具路由"——按当前任务动态注入相关 Server 的工具子集（先让规划器选域，再加载该域工具）。
- 能力去重与优选：相同能力按质量/延迟/权限优选一个，其余标记备用；Server 健康度监控（失败率/延迟），自动降权与熔断。
- 聚合层设计：企业场景常做"MCP 网关"——统一鉴权/审计/限流/工具目录，Client 只连网关，Server 的注册与治理走平台化流程（AGT-282 市场分发的企业版）。

```javascript
class McpGateway {
  async toolsFor(task) {                    // 动态注入
    const domains = await planner.pickDomains(task);
    return this.servers
      .filter(s => domains.includes(s.domain) && s.healthy)
      .flatMap(s => s.tools.map(t => ({
        ...t, name: `${s.name}.${t.name}` })));  // 命名空间
  }
  async call(fqn, args) {
    const [server] = fqn.split('.');
    try { return await this.servers[server].call(fqn, args); }
    catch (e) { this.markUnhealthy(server); throw e; } // 熔断
  }
}
```
