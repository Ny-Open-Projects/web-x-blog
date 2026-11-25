---
title: [1005] 越狱（jailbreak）攻击的多层防御怎么搭
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 越狱]
type: 面试题
---

## 1005：越狱（jailbreak）攻击的多层防御怎么搭

**答**：
- 单点防御必破：模型层拒答训练会被新话术绕过，所以防线必须多层——模型层（对齐训练）、应用层（输入分类器识别越狱模式：角色扮演/假设场景/编码混淆）、系统层（权限不因「对话内容」变化，越狱成功也没有权限做坏事）。
- 编码混淆类（Base64/Unicode 变体/多语言切换）靠输入侧归一化检测：解码后再过一遍分类器。
- 会话级累积攻击：单条消息无害，多轮铺垫后越狱——防线要看「会话轨迹」而不是单条消息，会话级风险分累积告警。
- 追问钩子：怎么持续跟新越狱手法？——线上拦截日志回流分析 + 社区攻击情报 + 内部红队定期变异测试，防线是运营出来的不是一次搭建的。

```ts
async function inputGuard(msg, session) {
  const decoded = decodeVariants(msg);            // Base64/Unicode 归一化
  const [jail, sessionRisk] = await Promise.all([
    classifier.jailbreak(decoded),
    sessionRiskScore(session.turns),              // 会话轨迹累积风险
  ]);
  if (jail.score > 0.8 || sessionRisk > 0.8) return refuse('越狱特征');
  return msg;
}
```

