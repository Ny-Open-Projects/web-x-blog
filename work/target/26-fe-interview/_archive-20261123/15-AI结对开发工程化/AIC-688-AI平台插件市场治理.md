---
title: [AIC-688] AI 平台的「插件市场」怎么治理第三方工具接入？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-688：AI 平台的插件市场怎么治理第三方工具接入？

**答**：
- 结论先行：**第三方插件/工具接入要「准入审核 + 运行沙箱 + 权限最小化 + 持续审计」四道关**——插件能读代码、执行命令，一旦恶意或有漏洞，破坏力比普通 npm 包更大。
- 四道关：1) **准入审核**：审查插件来源、权限声明（要读哪些文件/执行哪些命令）、维护活跃度、已知漏洞——类似应用商店审核；2) **运行沙箱**：插件在隔离环境运行（AIC-095 沙箱），限制文件系统/网络/命令权限；3) **权限最小化**：默认只给完成任务的最小权限，危险权限（写文件/执行命令）需显式授权且限时（AIC-351 渐进授权）；4) **持续审计**：记录插件所有操作（AIC-086 权限审计），异常行为（大量外联/读敏感文件）告警。
- 供应链风险：插件依赖的第三方库可能有漏洞——要做依赖扫描（AIC-434 依赖画像）；插件更新要重新审核，不能自动信任新版本。
- 退出机制：能一键禁用/卸载问题插件，且有回滚——防止「装了容易卸了难」。
- 追问钩子：为什么插件必须「沙箱运行」而不能「信任声明」？——因为插件的权限声明是它自己写的，不可信；且即使善意插件也可能被攻陷（供应链攻击）；沙箱是物理约束——不管插件声称做什么、实际被改成什么，都逃不出限定权限——把「信任」换成「约束」。

```typescript
type Plugin = { name: string; declaredPerms: string[]; source: 'verified'|'community'; hasVuln: boolean };

function admitPlugin(p: Plugin): { admitted: boolean; perms: string[]; reason: string } {
  if (p.hasVuln) return { admitted: false, perms: [], reason: 'known-vulnerability' };
  if (p.source === 'community') {
    // 社区插件默认降权：只给读权限，危险权限需额外人工审批
    return { admitted: true, perms: p.declaredPerms.filter(x => x.startsWith('read:')), reason: 'community-min-perms' };
  }
  return { admitted: true, perms: p.declaredPerms, reason: 'verified' };
}

console.log(admitPlugin({ name: 'x', declaredPerms: ['read:file', 'exec:cmd'], source: 'community', hasVuln: false }).perms);
// ['read:file'] —— 危险 exec 权限被剥离
console.log(admitPlugin({ name: 'y', declaredPerms: ['read:file'], source: 'verified', hasVuln: true }).admitted === false);
```
