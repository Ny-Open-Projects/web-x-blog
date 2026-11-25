---
title: [AGT-878] 多环境配置（dev/staging/prod 的 API 地址/开关）AI 辅助生成时的安全边界？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-878：多环境配置（dev/staging/prod 的 API 地址/开关）AI 辅助生成时的安全边界

**答**：
- 硬边界：密钥类配置 AI 永不接触（从 secret manager 注入，AI 上下文里是占位符）；AI 只生成「非敏感配置的结构与默认值」。schema 校验所有环境配置（缺 key/类型错启动即报）。
- 泄漏防线：AI 工具的上下文采集排除 .env 类文件（glob 黑名单）；git 历史扫描防密钥被 AI 场景连带读走。
- 环境差异可视化：AI 生成配置变更时输出「环境差异表」（哪个环境哪个值变了），评审时一眼看清影响。

```javascript
const CONFIG_SCHEMA = z.object({
  apiUrl: z.string().url(),
  flags: z.record(z.boolean()),
});                                   // 密钥不在schema里
function aiGenConfig(env) {
  return ai.compose(CONFIG_SCHEMA, {
    secrets: 'PLACEHOLDER_FROM_KMS',   // AI 只见占位符
    envDiff: true,                     // 输出环境差异表
  });
}
scanPreCommit({ secrets: true, aiContextExclude: ['.env*'] });
```

