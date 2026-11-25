---
title: [AGT-190] Agent 的版本管理为什么是「prompt + 模型 + 工具」三位一体？怎么实现？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-190：Agent 的版本管理为什么是「prompt + 模型 + 工具」三位一体？怎么实现？
**答**：
- 原因：Agent 行为由三者共同决定，单独版本化任何一个都无法复现历史行为——「6 月 1 日线上为什么那样回答」需要三个维度同时可查，benchmark 结论也只有绑定三元组才有意义。
- 实现方式：每次 Agent 运行记录 bundle 版本（prompt 集合哈希 + 模型快照 id + 工具清单哈希），bundle 本身内容寻址（同 bundle 永远同行为）；发布 = 声明新 bundle，回滚 = 切回旧 bundle 指针。
- 依赖三处的版本策略不同：prompt 用语义化版本（内容 diff 可评审）、模型用快照 id（禁止 latest）、工具用集合哈希（工具行为变了即新 bundle，联动重新评测）。
- 与评测联动：CI 里对每个新 bundle 跑评测集，评测报告与 bundle id 绑定存档，形成「版本-质量」历史曲线。

```typescript
// 三位一体版本 bundle：内容寻址 + 发布回滚
import { createHash } from 'crypto';

interface AgentBundle {
  id: string;                        // 内容寻址 id
  prompts: Record<string, { version: string; content: string }>;
  modelSnapshot: string;             // 快照 id，禁止 latest
  tools: { name: string; version: string }[];
  evalReport?: { suite: string; passRate: number };
}

function bundleId(b: Omit<AgentBundle, 'id'>): string {
  const h = createHash('sha256')
    .update(JSON.stringify([b.prompts, b.modelSnapshot, [...b.tools].sort((x, y) => x.name.localeCompare(y.name))]))
    .digest('hex');
  return `bundle-${h.slice(0, 12)}`;
}

export class BundleRegistry {
  private current = new Map<string, string>();          // agentName -> bundleId 指针

  publish(agentName: string, candidate: Omit<AgentBundle, 'id'>): string {
    const id = bundleId(candidate);
    // 工具集变化必须触发重评测
    const prev = this.get(this.current.get(agentName) ?? '');
    if (prev && JSON.stringify(prev.tools) !== JSON.stringify(candidate.tools) && !candidate.evalReport) {
      throw new Error(`工具集变更必须先跑评测集：${prev.tools.map((t) => t.name).join()} -> ${candidate.tools.map((t) => t.name).join()}`);
    }
    bundles.set(id, { ...candidate, id });
    return id;                                          // 发布 ≠ 上线，上线由 promote 显式操作
  }

  promote(agentName: string, bundleId: string) {        // 配合灰度：promote 到 AGT-141 的路由配置
    if (!bundles.has(bundleId)) throw new Error(`bundle 不存在：${bundleId}`);
    this.current.set(agentName, bundleId);
    audit.info({ event: 'bundle.promote', agentName, bundleId });
    const h = this.histories.get(agentName) ?? [];
    this.histories.set(agentName, [...h, bundleId]); // 记录发布历史，供 rollback 切回
  }

  rollback(agentName: string) {                         // 回滚 = 指针切回上一版本
    const history = this.histories.get(agentName) ?? [];
    const prev = history[history.length - 2];
    if (prev) this.current.set(agentName, prev);
  }
  private histories = new Map<string, string[]>();
  get(id: string) { return bundles.get(id); }
}
const bundles = new Map<string, AgentBundle>();
const audit = { info: (x: unknown) => { void x; } };
```
