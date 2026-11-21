---
title: [OPS-175] 故障注入 SDK 怎么设计？与混沌脚本的区别是什么？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-175：故障注入 SDK 怎么设计？与混沌脚本的区别是什么？
**答**：
- 定位区别：OPS-171 的混沌脚本面向开发/预发的日常验证；故障注入 SDK 面向生产环境（灰度/内部账号）验证降级预案真实生效。
- 设计要点：规则从开关平台远程下发（权限可控）、概率控制、TTL 自动过期防忘关、默认关闭。
- 生产注入默认只对内部账号或灰度桶生效，避免真实用户受影响；注入事件打标上报，看板可区分。
- 用途：演练时打开注入，验证降级矩阵每一行真实可触发（OPS-174 的"开关演练"）。
- 安全约束：SDK 本身可远程禁用；注入不写 localStorage 之外的持久状态。

```typescript
// 故障注入 SDK：生产环境受控验证降级预案（默认关闭，值班可远程开启）
interface FaultRule {
  scope: string;             // 模块：api / cdn / feature
  target: RegExp;
  type: 'latency' | 'error' | 'offline';
  probability: number;
  ttlMs: number;             // 自动过期，防忘关
}

class FaultInjector {
  private rules: FaultRule[] = [];
  private expiredAt = 0;

  async syncFromRemote() {
    // 规则从开关平台下发（权限可控）；生产注入默认仅对内部账号 / 灰度桶生效
    const cfg = await fetch('/api/fault-config?env=gray').then((r) => r.json());
    this.rules = cfg.rules;
    this.expiredAt = Date.now() + cfg.ttlMs;
  }

  shouldFail(url: string): FaultRule | null {
    if (Date.now() > this.expiredAt) return null;   // TTL 过期自动失效
    return this.rules.find((r) => r.target.test(url) && Math.random() < r.probability) ?? null;
  }
}

export const injector = new FaultInjector();
// 用法：fetch 拦截器中 injector.shouldFail(url) 命中即返回 503/延迟
// 与 OPS-171 的区别：混沌脚本验证开发态健壮性，本 SDK 在生产验证降级矩阵真实生效（OPS-174）
```

---

## 二十、值班与流程（OPS-176 ~ OPS-200）

技术之外的组织能力：oncall 机制、SOP、降噪、复盘、无责文化、工具化与体系搭建路线图——运维体系最终是"人 + 流程 + 工具"的组合。
