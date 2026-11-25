---
title: [AGT-183] Agent 时代的用户隐私边界怎么设计（数据流与用途限定）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-183：Agent 时代的用户隐私边界怎么设计（数据流与用途限定）？
**答**：
- 隐私边界要落在「数据流」上而不是隐私条款上：每一次 Agent 读取用户数据（检索记忆/调工具/跨 Agent 委托）都是一个「用途明确的访问」，要有最小化、目的绑定、可撤回三个属性。
- 用途限定实现：会话上下文分「本会话可见 / 跨会话记忆 / 可用于改进」三档标签，用户可对每档单独开关；记忆写入时带用途标签，检索时按当前用途过滤（健康咨询会话不召回金融记忆）。
- 敏感操作的知情权：Agent 首次调用某类敏感数据源（通讯录/位置/邮件）要显式授权，授权粒度到「数据类别 + 操作类型」，而不是「同意一切」。
- 技术兜底：端侧脱敏（PII 出设备前替换，AGT-170 思路前移）、跨 Agent 委托时不传原文只传任务所需最小字段。

```typescript
// 隐私边界：用途标签 + 记忆过滤 + 最小化委托
import { z } from 'zod';

const Purpose = z.enum(['current_session', 'cross_session_memory', 'model_training']);
type Purpose = z.infer<typeof Purpose>;

interface MemoryItem { id: string; content: string; purposes: Purpose[]; category: 'health' | 'finance' | 'general'; }

export function recallForPurpose(memories: MemoryItem[], purpose: Purpose, currentTopicCategory: MemoryItem['category']): string[] {
  // 用途过滤：训练用途必须显式授权；跨类别记忆默认不跨主题召回
  return memories
    .filter((m) => m.purposes.includes(purpose))
    .filter((m) => purpose === 'current_session' ? true : m.category === currentTopicCategory || m.category === 'general')
    .map((m) => m.content);
}

export function setUserConsent(memory: MemoryItem[], purpose: Purpose, granted: boolean): MemoryItem[] {
  return memory.map((m) => ({
    ...m,
    purposes: granted ? [...new Set([...m.purposes, purpose])] : m.purposes.filter((p) => p !== purpose),
  })); // 可撤回：撤销后该用途立即不再召回
}

// 跨 Agent 委托的最小化字段：只传完成任务必需的投影
export function minimalProjectionForDelegate<T extends Record<string, unknown>>(
  data: T, neededFields: (keyof T)[]): Pick<T, keyof T & string> {
  const leaked = Object.keys(data).filter((k) => !neededFields.includes(k as keyof T) && /ssn|phone|email|idcard/i.test(k));
  if (leaked.length) audit.warn({ event: 'delegate.projection.blocked', fields: leaked }); // 敏感字段白名单外拦截
  return Object.fromEntries(neededFields.filter((f) => f in data).map((f) => [f, data[f]])) as any;
}
const audit = { warn: (x: unknown) => { void x; } };
```

## 追问（补充）

**追问**：

1. 用户撤回授权后，已经进上下文的数据怎么办？→ 立即移出可召回集合，后续请求重建上下文，历史数据按保留期到期删除。
2. 多 Agent 委托时隐私边界怎么不被打穿？→ 只传最小字段投影，子 Agent 继承父级用途标签且不能自行扩权，委托链路要能追溯到最初的用户授权。
3. 怎么证明不是只写在条款里？→ 每个数据访问点埋审计事件，能按用户导出谁在什么用途下读过哪些字段，审计日志本身也要设访问权限与保留期。
