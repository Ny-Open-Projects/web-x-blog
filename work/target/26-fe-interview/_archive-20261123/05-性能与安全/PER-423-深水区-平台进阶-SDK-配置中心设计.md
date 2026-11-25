---
title: [PER-423] 监控 SDK 的配置中心设计：采样率/插件开关/上报端点的远程配置如何安全下发？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-423：监控 SDK 的配置中心设计：远程配置如何安全下发？

**答**:
- 配置通道（复用 PER-370 模式）：HTML 内联默认配置（兜底）→ SW 缓存的配置接口（分钟级）→ 实时推送（秒级止血）。配置内容：采样率（分页面分层）、插件开关、上报端点、上报体积/频率、PII 脱敏规则版本。
- 安全下发三原则：① 签名校验——配置带签名（防配置接口被劫持注入恶意配置，如把上报端点改成攻击者服务器——数据外泄通道）；② 白名单 schema——配置字段白名单 + 类型校验（畸形配置不让 SDK 崩溃）；③ 灰度配置——配置本身按用户分桶下发（新配置先灰度 1%，防"错误配置全量生效"的二次事故）。
- 失败模式处理：配置接口失败 → 沿用上次缓存配置（永不因配置失败而停止采集）；配置回滚机制——保留最近 N 个配置版本，一键回滚。
- 变更审计：配置变更日志（谁/何时/改了什么/影响面）——采样率改错（全量采集打爆服务端）的追溯依据。

```javascript
// 配置下发：签名 + schema 校验 + 灰度
async function fetchSDKConfig() {
  try {
    const r = await fetch('/api/sdk-config');
    const { payload, sig } = await r.json();
    if (!await verifySig(payload, sig, PUB_KEY)) return lastConfig;      // 签名校验：防劫持
    const cfg = validateSchema(payload);                                  // 白名单 schema
    if (!cfg) return lastConfig;
    localStorage.setItem('sdk-config', JSON.stringify(cfg));              // 缓存回退
    return cfg;
  } catch { return lastConfig; }                                          // 失败沿用旧配置，采集不中断
}
// 灰度配置：服务端按用户分桶下发（1% → 10% → 100%）；配置变更日志留档
// 关键防线：上报端点在白名单域集合内校验——配置即使被篡改也无法把数据导到外部域
```
