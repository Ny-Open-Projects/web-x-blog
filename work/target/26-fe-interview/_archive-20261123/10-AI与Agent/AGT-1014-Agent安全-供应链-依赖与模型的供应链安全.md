---
title: [1014] Agent 系统的供应链安全（依赖、模型、数据）怎么管
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 供应链]
type: 面试题
---

## 1014：Agent 系统的供应链安全（依赖、模型、数据）怎么管

**答**：
- 三条供应链：代码依赖（npm 包投毒——常规 lock + 审计）、模型供应链（第三方模型/LoRA 权重被植入后门——只用签名校验的官方渠道，模型指纹入库）、数据供应链（训练/检索数据被投毒——数据来源白名单 + 异常内容扫描）。
- 模型换版是隐形高危动作：新版本权重可能行为漂移，接入前必须过安全回归集（注入/越狱用例）+ 行为基线对比。
- MCP/插件生态：第三方工具包按「不可信组件」对待——沙箱试跑、权限最小化、描述审查（见工具投毒卡）。
- 追问钩子：怎么发现「数据投毒」已发生？——检索结果的异常监控：某来源文档命中后回答偏离基线的比例突升，即为疑似投毒信号。

```ts
async function adoptModel(version) {
  const sig = await verifySignature(version);       // 签名校验
  if (!sig) return reject('unsigned model');
  const base = await behaviorBaseline(version, evalSet);  // 行为基线
  const sec = await runRedteam(version);            // 安全回归
  if (sec.hardBypass > 0) return reject(sec);
  return register({ version, fingerprint: sig.fp, baseline: base }); // 指纹入库
}
```
