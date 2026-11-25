---
title: [AGT-176] 第三方工具（MCP server / 插件）上架前，安全评审流程怎么设计？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-176：第三方工具（MCP server / 插件）上架前，安全评审流程怎么设计？
**答**：
- 评审流水线五关：静态扫描（代码依赖漏洞、混淆代码、网络外联域名）、行为沙箱（真实环境跑典型调用，记录读写面与外联行为，与声明权限做 diff）、描述一致性（工具 description 承诺与实际行为比对，防描述注入与挂羊头）、权限最小化审查（申请权限是否超出功能所需）、法律合规（数据处理协议、隐私条款）。
- 沙箱运行是关键证据来源：行为 diff 超出声明的权限（比如「天气查询」工具却请求写文件系统）直接一票否决。
- 上架不是终点：持续监控（运行时行为漂移告警）、版本更新重审（minor 更新走快速通道，major 全量重审）、一键下架与客户端失效机制。
- 评审结论要机器可读：签发的信任等级与权限白名单随工具分发，客户端按 AGT-123 的信任分级执行。

```typescript
// 工具上架安全评审流水线
import { createHash } from 'crypto';

interface ReviewVerdict { toolId: string; version: string; trust: 'builtin' | 'verified' | 'community' | 'rejected'; reasons: string[]; }

export async function reviewPipeline(pkg: { id: string; version: string; code: Buffer; manifest: Manifest }): Promise<ReviewVerdict> {
  const reasons: string[] = [];

  // 第 1 关：静态扫描
  const staticFindings = await staticScan(pkg.code);
  if (staticFindings.obfuscated) reasons.push('存在混淆代码');
  if (staticFindings.criticalDeps.length) reasons.push(`依赖含高危漏洞：${staticFindings.criticalDeps.join()}`);

  // 第 2 关：沙箱行为分析，与声明权限 diff
  const behavior = await sandboxRun(pkg, SAMPLE_INVOCATIONS);
  const undeclared = behavior.effects.filter((e) => !manifest.permissions.includes(e));
  if (undeclared.length) reasons.push(`行为超出声明权限：${undeclared.join()}`);

  // 第 3 关：描述一致性（LLM 比对描述与观测行为）
  const consistent = await descConsistency(manifest.description, behavior.summary);
  if (!consistent) reasons.push('工具描述与实际行为不一致');

  // 第 4 关：权限最小化
  const excessive = manifest.permissions.filter((p) => !behavior.usedPermissions.includes(p));
  if (excessive.length > 2) reasons.push(`申请权限远超实际使用：${excessive.join()}`);

  const trust = reasons.length ? 'rejected' : behavior.readonlyOnly ? 'verified' : 'community';
  const digest = createHash('sha256').update(pkg.code).digest('hex').slice(0, 16);
  await registry.publish({ toolId: pkg.id, version: pkg.version, trust, digest });   // 签发结论随分发
  return { toolId: pkg.id, version: pkg.version, trust, reasons };
}

interface Manifest { description: string; permissions: string[]; }
const SAMPLE_INVOCATIONS = [{ args: { q: 'beijing weather' } }, { args: { q: 'shanghai weather' } }];
async function staticScan(code: Buffer) {
  return { obfuscated: false, criticalDeps: [] as string[], externalDomains: [] as string[] };
}
async function sandboxRun(pkg: any, invocations: any[]) {
  void pkg; void invocations;
  return { effects: ['http:get'], usedPermissions: ['http:get', 'read:cache'], readonlyOnly: true,
           summary: '工具仅发起只读 HTTP 请求获取天气数据' };
}
async function descConsistency(desc: string, behavior: string) { void desc; void behavior; return true; }
const registry = { publish: async (x: unknown) => { void x; } };
```
