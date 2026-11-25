---
title: [OPS-046] ConfigMap 在前端多环境配置里怎么用？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-046：ConfigMap 在前端多环境配置里怎么用？
**答**：
- ConfigMap 存非敏感配置（API 地址、开关、CDN 域名），Secret 存敏感信息，两者都通过挂载或环境变量进容器。
- 前端典型用法：config.template.js 由 ConfigMap 挂载，entrypoint envsubst 渲染（接 OPS-043）；不同环境只是同名 ConfigMap 内容不同。
- 注意：挂载文件的更新有同步延迟（约 1 分钟），改 ConfigMap 不会立即生效，滚动更新更可靠。
- 敏感信息绝不进 ConfigMap，且历史经验是 ConfigMap 会被误 git 化管理，务必走声明式仓库+审计。

```yaml
# 环境 config 由 ConfigMap 下发：dev 与 prod 同 key 不同 value
apiVersion: v1
kind: ConfigMap
metadata:
  name: web-mall-config
data:
  config.template.js: |
    window.__CONFIG__ = {
      env: "__APP_ENV__",
      apiBase: "__API_BASE__",
      cdnHost: "__CDN_HOST__",
      sentryDsn: "__SENTRY_DSN__",
      flagsUrl: "__FLAGS_URL__"
    };
---
# Deployment 挂载 ConfigMap 到配置目录
apiVersion: apps/v1
kind: Deployment
metadata: { name: web-mall }
spec:
  template:
    spec:
      containers:
        - name: nginx
          image: registry.example.com/web-mall:v2026.11.01-abc1234
          env:                        # 渲染用的变量来自同环境 ConfigMap
            - name: API_BASE
              valueFrom: { configMapKeyRef: { name: web-mall-env, key: apiBase } }
            - name: APP_ENV
              valueFrom: { configMapKeyRef: { name: web-mall-env, key: env } }
          volumeMounts:
            - name: config-tpl
              mountPath: /usr/share/nginx/html/config.template.js
              subPath: config.template.js
      volumes:
        - name: config-tpl
          configMap: { name: web-mall-config }
```
