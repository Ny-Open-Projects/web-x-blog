---
title: [AGT-805] 工具执行（代码/脚本）的沙箱怎么设计（隔离等级/资源限额/网络策略）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-805：工具执行（代码/脚本）的沙箱怎么设计（隔离等级/资源限额/网络策略）

**答**：
- 三档沙箱：轻档（进程内+超时，纯计算类工具）、中档（容器，网络白名单+文件系统只读挂载）、重档（独立 VM/微 VM，租户专属资源池，跑不受信代码）。
- 资源限额全维度：CPU/内存/时长/输出大小/网络流量；超限即杀并记审计——Agent 场景最大风险是"死循环烧资源"。
- 网络默认拒绝（deny-all 白名单放行），出网经代理（审计+防数据外泄）；文件产出走对象存储（不落沙箱本地）。

```javascript
const SANDBOX_TIERS = {
  light: { isolation: 'process', timeout: 5e3 },
  container: { isolation: 'docker', net: 'whitelist', fs: 'ro-mount' },
  vm: { isolation: 'firecracker', tenantPooled: true },
};
async function runInSandbox(code, tier = 'container') {
  const s = SANDBOX_TIERS[tier];
  const r = await sandbox.run(code, { ...s,
    limits: { cpuMs: 2000, memMB: 256, outBytes: 1e6 },
    net: proxyAllowlist(tenant),                  // 默认拒绝+白名单
  });
  if (r.killed) audit.log({ type: 'sandbox.kill', reason: r.reason });
  return r;
}
```

