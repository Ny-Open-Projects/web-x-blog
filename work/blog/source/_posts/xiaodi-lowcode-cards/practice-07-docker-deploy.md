---
title: Docker/云效部署实战：四镜像、双 Nginx、CI 流水线
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 实战, Docker, CI/CD]
---

## Docker/云效部署实战：四镜像、双 Nginx、CI 流水线

**部署分工**：React 编辑端是 SPA 纯静态 → 不打镜像，直接传 OSS Bucket（静态页面首页 index.html + 读写权限公共读 + 绑域名）；Next.js release 与 NestJS server 需常驻 → 打镜像，前面各架一层 Nginx。

**server.Dockerfile 关键顺序**：node:18 → pnpm install → **先 `pnpm build:share` 再 `build:server`**（后端依赖 share 的 TS 类型，顺序错直接编译失败）→ EXPOSE 3000 → `CMD ["pnpm","start:server"]`。Nginx 镜像：`nginx:1.25.0-alpine` + `ADD ./nginx/server.nginx.conf /etc/nginx/nginx.conf` 覆盖默认配置；conf 里 `upstream backend` + `proxy_pass http://backend`（名字须一致）。

**Docker Compose 四容器**：backend(5001:3000)、backend_nginx(5000:80)、frontend(4001:3000)、frontend_nginx(4000:80)；`restart:always`；image 用 `${xxx_tag}` 变量为云效镜像仓库做映射。

**云效流水线**：构建 monorepo（先 share）→ 前端产物传 OSS → compose 制品归档公共存储 → 并行构建推四个镜像到 ACR → 主机部署下载制品 → 清理脚本（`|| true` 关键——首次部署无容器时命令失败不能中断流水线）→ `docker compose up -d`。

真实 BUG 三连（排错谈资）：①`FROM nginx:` 多写冒号拉镜像失败；②Dockerfile 文件名多了字母 s；③tar 的 `-C`（切换目录）误写 `-c`（创建归档）。

出处「课程25 · 23-1~24-2、25-1~27-4」
