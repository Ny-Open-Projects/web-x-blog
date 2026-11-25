---
title: [OPS-043] 容器内 Nginx 如何在启动时注入环境变量（运行时配置）？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-043：容器内 Nginx 如何在启动时注入环境变量（运行时配置）？
**答**：
- 问题：前端代码在浏览器运行，镜像里的 window.__CONFIG__ 是构建时固化的，一套镜像无法多环境使用。
- 方案：镜像里放配置模板 config.template.js（占位符如 __API_BASE__），容器启动时 ENTRYPOINT 脚本用 envsubst 替换成 config.js，Nginx 再按普通文件下发。
- 效果：构建一次（一次镜像审计/一次安全扫描），任意环境通过注入 env 部署，这是"一次构建多环境部署"的标准做法。
- config.js 必须在 index.html 里以同步 script 引入且不被缓存，保证运行时读到当前环境配置。

```bash
#!/usr/bin/env bash
# docker-entrypoint.sh：启动时用环境变量渲染运行时配置
set -euo pipefail

CONF_DIR="/usr/share/nginx/html"
TEMPLATE="$CONF_DIR/config.template.js"

# 模板内容：window.__CONFIG__ = { apiBase: "__API_BASE__", cdnHost: "__CDN_HOST__" }
# 1. 渲染配置：环境变量 -> 实际值（只替换白名单变量，避免 env 泄露）
envsubst '${API_BASE} ${CDN_HOST} ${SENTRY_DSN} ${APP_ENV}' \
  < "$TEMPLATE" > "$CONF_DIR/config.js"

# 2. 校验关键配置已注入，缺了直接让容器启动失败（fail fast）
grep -q "window.__CONFIG__" "$CONF_DIR/config.js" \
  || { echo "config render failed"; exit 1; }
if echo "$(cat $CONF_DIR/config.js)" | grep -q "__API_BASE__"; then
  echo "ERROR: API_BASE not injected"; exit 1
fi

# 3. Nginx 配置里对 config.js 禁缓存（防浏览器拿到别的环境的值）
#    location = /config.js { add_header Cache-Control "no-cache"; }

echo "runtime config rendered:"
cat "$CONF_DIR/config.js"

# 前台启动 nginx（PID 1，保证收到信号正常退出）
exec nginx -g 'daemon off;'
```
