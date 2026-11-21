---
title: [ENG-088] 运行时配置注入怎么做？window.__CONFIG 与环境变量怎么取舍？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-088：运行时配置注入怎么做？window.__CONFIG 与环境变量怎么取舍？
**答**：
- 构建期环境变量（VITE_*）打进产物：改配置必须重新构建，适合不常变的构建态常量。
- 同一 Docker 镜像要部署到多环境（k8s 多套集群）时，必须运行时注入：容器启动时把配置写进 index.html 的 window.__APP_CONFIG__。
- 读取封装成统一模块，优先级 window.__CONFIG__ > 构建期变量 > 默认值，并做类型定义与校验。
- 安全边界：运行时配置同样可能被用户看到，任何密钥都不该放在这个链路里，只放地址、开关类公开配置。

```html
<!-- index.html：容器启动脚本会替换占位符，实现一次构建多环境部署 -->
<script>
  window.__APP_CONFIG__ = {
    apiBase: "/__API_BASE__",
    sentrySampleRate: 0.2,
  };
</script>
```

```typescript
// src/config.ts：统一读取入口，优先级 window 配置 > 构建期变量 > 默认值
interface AppConfig {
  apiBase: string;
  sentrySampleRate: number;
}

export const config: AppConfig = {
  apiBase:
    window.__APP_CONFIG__?.apiBase ??
    import.meta.env.VITE_API_BASE ??
    '/api',
  sentrySampleRate: window.__APP_CONFIG__?.sentrySampleRate ?? 1,
};
```
