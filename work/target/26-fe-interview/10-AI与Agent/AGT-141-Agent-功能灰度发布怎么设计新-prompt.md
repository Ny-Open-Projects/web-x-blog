---
title: [AGT-141] Agent 功能灰度发布怎么设计？新 prompt / 新模型的影子运行如何落地？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-141：Agent 功能灰度发布怎么设计？新 prompt / 新模型的影子运行如何落地？
**答**：
- 灰度对象是「prompt 版本 × 模型版本 × 工具集」的三元组配置，通过配置中心下发，网关按流量规则路由——发版不发代码。
- 影子运行：新版本只对镜像流量执行（同一输入并行调旧版与新版，旧版返回给用户，新版结果落库对比），用户无感、零风险地收集真实分布数据。
- 对比维度：自动评测分（judge）、人工抽检、token 成本、延迟分位、负反馈率；新版在滑动窗口内全面不劣于旧版才逐级放量（1% → 5% → 25% → 100%）。
- 每级放量都要有自动回滚条件（负反馈率/成本超阈值即回退），灰度不是一次性的而是常态能力。

```typescript
// 影子运行 + 灰度路由
import { z } from 'zod';

const VersionConfig = z.object({
  promptId: z.string(), promptVersion: z.string(),
  model: z.string(),
  rollout: z.number().min(0).max(100),        // 放量百分比
  shadow: z.boolean(),                        // 是否影子模式
});
type VersionConfig = z.infer<typeof VersionConfig>;

function pickVariant(cfgs: VersionConfig[], userId: string): { primary: VersionConfig; shadowCfg?: VersionConfig } {
  const hash = [...userId].reduce((h, c) => (h * 31 + c.charCodeAt(0)) >>> 0, 7) % 100; // 稳定分桶
  const active = cfgs.filter((c) => !c.shadow && hash < c.rollout);
  const shadowCfg = cfgs.find((c) => c.shadow);
  return { primary: active.at(-1)!, shadowCfg };
}

export async function handleChat(userId: string, input: string, cfgs: VersionConfig[]) {
  const { primary, shadowCfg } = pickVariant(cfgs, userId);
  const primaryP = callLlm(input, primary);

  if (shadowCfg) {
    // 影子：并行执行但不等它返回给用户，结果落库对比
    callLlm(input, shadowCfg)
      .then((out) => shadowStore.save({ userId, input, primary: null, shadow: out, cfg: shadowCfg }))
      .catch((e) => shadowStore.save({ userId, input, primary: null, shadow: `ERROR ${e}`, cfg: shadowCfg }));
  }
  return primaryP;
}

async function callLlm(input: string, cfg: VersionConfig) {
  const prompt = await promptRegistry.load(cfg.promptId, cfg.promptVersion); // 版本化 prompt
  return gateway.chat({ model: cfg.model, messages: prompt.render({ input }) });
}

const shadowStore = { save: (r: unknown) => { void r; } }; // 落库供离线 diff 与 judge 评分
const promptRegistry = { load: async (id: string, v: string) => ({ render: (vs: any) => [{ role: 'user', content: `${id}@${v}: ${vs.input}` }] }) };
const gateway = { chat: async (b: any) => JSON.stringify(b) };
```

---

## 二十五、检索与知识管理进阶
