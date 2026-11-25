---
title: [943] 多 Agent 系统里子 Agent 的权限怎么收敛
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 安全]
type: 面试题
---

## 943：多 Agent 系统里子 Agent 的权限怎么收敛

**答**：
- 权限最小化三原则：按任务书授予（只开本任务需要的工具）、按资源限制（文件白名单、网络域名白名单）、按时长限制（任务结束权限回收）。
- 危险工具二次确认：shell 执行、外发请求、删除类操作，子 Agent 只能「申请」，编排器或人工批准后由编排器代执行——子 Agent 拿不到原始凭证。
- 提示注入隔离：子 Agent 处理外部内容（网页、工单）时权限应进一步降到只读，因为它的输入可被注入。
- 追问钩子：为什么不让子 Agent 直接持 API key？——一个被注入的子 Agent 等于泄露全部凭证，代执行模式把「权限」和「执行」分离。

```ts
const sandboxGrant = (brief) => ({
  tools: brief.tools.filter(t => SAFE_TOOLS.has(t)),      // 任务书白名单交集
  fs: { read: brief.inputs, write: brief.outputDir },      // 路径白名单
  net: brief.netDomains ?? [],
  exec: 'request-only',                                    // 只能申请，不能直接执行
});
async function requestExec(agent, cmd) {
  await approval.require({ agent, cmd, risk: classify(cmd) });
  return orchestrator.exec(cmd);                           // 编排器代执行
}
```

