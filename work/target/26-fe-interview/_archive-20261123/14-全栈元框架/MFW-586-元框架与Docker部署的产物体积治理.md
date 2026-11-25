---
title: [MFW-586] 元框架与 Docker 部署：产物体积治理
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-586：Docker 产物体积治理

**答**:
- Next standalone 的镜像瘦身链：1) **standalone 输出**（.next/standalone：node_modules 只含运行时必需——非 standalone 的完整 node_modules 500MB+ → standalone 50MB）；2) **多阶段构建**（builder 装 devDeps 构建 → runtime 只拷 standalone+static+public——RBL-681 模板）；3) **CI 镜像体积门禁**（镜像 > 阈值 fail——体积回归防线：新依赖引入 node_modules 爆炸的检出）。
- 体积构成分析：standalone 的 node_modules 构成（ traced 依赖——Next 的 nft 追踪：分析 import 链拷贝必要文件）；「体积意外增长」的归因（新依赖/动态 import 全量包含/trace 误判——next trace 的保守包含：动态 require 无法静态分析）。
- base 镜像的选择：node:20-alpine（musl——原生模块兼容性风险 RBL-563）vs distroless（最小但调试难）vs slim——「镜像大小 vs 调试/兼容性」的权衡。
- 追问钩子：为什么「镜像体积门禁」对 Next 项目特别必要？——Next 的依赖树是「全量 import 分析」：一个动态 require 的包 = 整包进 standalone（trace 无法静态确定用多少）；依赖的小变更可能让镜像翻倍（moment 全 locale/ AWS SDK 全服务）；「镜像体积的漂移」是依赖治理的滞后指标（RBL-906 依赖治理的镜像维度）：门禁让体积回归在 PR 阶段拦截。

```dockerfile
# 多阶段 + 体积门禁
FROM node:20-slim AS builder
WORKDIR /app
COPY . .
RUN pnpm install --frozen-lockfile && pnpm build
# 体积门禁：standalone 目录
RUN du -sh .next/standalone | awk '{ if ($1+0 > 200) { print "镜像超预算: " $1 "M"; exit 1 } }'
FROM node:20-slim
WORKDIR /app
ENV NODE_ENV=production
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static
COPY --from=builder /app/public ./public
EXPOSE 3000
CMD ["node", "server.js"]
# 归因：standalone 内 node_modules 的 top 依赖
# du -sh .next/standalone/node_modules/* | sort -rh | head -5
```
